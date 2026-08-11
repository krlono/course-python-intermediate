# # Impute values and add columns

import pandas as pd
import numpy as np
import os
from glob import glob

# ## Set working folder and import settings

# +
local_user_folder = os.environ["USERPROFILE"] 

project_name = 'course-python-intermediate'
working_folder = f'{local_user_folder}/{project_name}'
working_folder

os.chdir(working_folder)

os.getcwd()
# -

# ## Import settings and define working directories

from config.config import settings
year = settings.year
print(f'Current year is {year}')
data_dir = settings.data_dir
data_dir = f'{local_user_folder}\\{data_dir}'
print(f'Data directory is {data_dir}')
process_dir = f'{data_dir}/processed/'
print(f'Process directory is {process_dir}')
statistics_dir = f'{data_dir}/statistics/'
print(f'Statistics directory is {statistics_dir}')

# ## Read households dataframe

households_file = f'{process_dir}lcs_households_wgt_{year}.parquet'
households = pd.read_parquet(households_file)
print(f'{households.shape[0]} rows and {households.shape[1]} columns read from {households_file}')

# ## Impute missing asset values
# We use a [hot-deck imputation](https://en.wikipedia.org/wiki/Imputation_(statistics)) method in this example

asset_vars = [
    "owns_bicycle",
    "owns_car",
    "owns_freezer",
    "owns_fridge",
    "owns_motorcycle",
    "owns_tv"
]

asset_vars = [x for x in households.columns if x[:3] == 'own']
asset_vars

# +
households_imputed = households.copy()

rng_master = np.random.default_rng(19853127)

for var in asset_vars:

    missing_idx = households_imputed.index[
        households_imputed[var].isna()
    ]

    for idx in missing_idx:

        # -----------------------
        # row-specific deterministic RNG
        # -----------------------
        seed = int(rng_master.integers(0, 2**32 - 1))
        rng = np.random.default_rng(seed)

        row = households_imputed.loc[idx]

        # -----------------------
        # donor hierarchy (deterministic logic)
        # -----------------------
        donors = households_imputed[
            (households_imputed[var].notna()) &
            (households_imputed["state"] == row["state"]) &
            (households_imputed["urbrur"] == row["urbrur"]) &
            (households_imputed["building_type"] == row["building_type"])
        ]

        if len(donors) == 0:
            donors = households_imputed[
                (households_imputed[var].notna()) &
                (households_imputed["state"] == row["state"]) &
                (households_imputed["urbrur"] == row["urbrur"])
            ]

        if len(donors) == 0:
            donors = households_imputed[
                (households_imputed[var].notna()) &
                (households_imputed["state"] == row["state"])
            ]

        # safety fallback (should rarely trigger)
        if len(donors) == 0:
            donors = households_imputed[
                households_imputed[var].notna()
            ]

        # -----------------------
        # deterministic donor selection
        # -----------------------
        donor_idx = rng.integers(0, len(donors))
        donor_value = donors.iloc[donor_idx][var]

        households_imputed.loc[idx, var] = donor_value

households_imputed
# -

households.compare(households_imputed)

# ## Read person dataframe

persons_file = f'{process_dir}lcs_persons_wgt_{year}.parquet'
persons = pd.read_parquet(persons_file)
print(f'{persons.shape[0]} rows and {persons.shape[1]} columns read from {persons_file}')
persons.style

# ## Find outliers
#
# 1. Detect and treat outliers first.
# 2. Impute missing values afterwards.
#
# The reason to treat outliers first is that outliers can distort the models or donor pools used for imputation. If we first impute using data that include implausible incomes, the imputed values may also become implausible.
#
# For income, we detect outliers on the logarithm of positive incomes rather than on the raw values, since income is typically right-skewed. This uses [Interquartile Range method](https://en.wikipedia.org/wiki/Interquartile_range) (IQR).

# +
person_edit = persons.copy()

valid = (
    person_edit["income"].notna() &
    (person_edit["income"] > 0)
)

log_income = np.log(person_edit.loc[valid, "income"])

q1 = log_income.quantile(0.25)
q3 = log_income.quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

person_edit["income_outlier"] = False
person_edit.loc[valid, "income_outlier"] = (
    (np.log(person_edit.loc[valid, "income"]) < lower) |
    (np.log(person_edit.loc[valid, "income"]) > upper)
)
person_edit.loc[person_edit['income_outlier'] == True]

# -

# Set outlier values to missing

person_edit.loc[person_edit['income_outlier'] == True, "income"] = np.nan
person_edit

# ## Hot deck imputation
# Here, we also use a hotdeck imputation

# +
persons_imputed = person_edit.copy()

# deterministic RNG
#rng_master = np.random.default_rng(12345)

# Children rule (deterministic, no randomness involved)
persons_imputed.loc[
    (persons_imputed["age"] < 16) & (persons_imputed["income"].isna()),
    "income"
] = 0


# Adults with missing income
missing = persons_imputed[
    (persons_imputed["age"] >= 16) &
    (persons_imputed["income"].isna())
].index


for idx in missing:

    # -----------------------
    # row-specific RNG (fully reproducible)
    # -----------------------
    seed = 7627187
    rng = np.random.default_rng(seed)

    row = persons_imputed.loc[idx]

    # -----------------------
    # donor pools (fixed logic, no randomness here)
    # -----------------------
    donors = persons_imputed[
        (persons_imputed["income"].notna()) &
        (persons_imputed["age"] >= 16) &
        (persons_imputed["occupation"] == row["occupation"]) &
        (persons_imputed["state"] == row["state"])
    ]

    if len(donors) == 0:
        donors = persons_imputed[
            (persons_imputed["income"].notna()) &
            (persons_imputed["age"] >= 16) &
            (persons_imputed["occupation"] == row["occupation"])
        ]

    if len(donors) == 0:
        donors = persons_imputed[
            (persons_imputed["income"].notna()) &
            (persons_imputed["age"] >= 16) &
            (persons_imputed["state"] == row["state"])
        ]

    if len(donors) == 0:
        donors = persons_imputed[
            (persons_imputed["income"].notna()) &
            (persons_imputed["age"] >= 16)
        ]

    # -----------------------
    # deterministic donor selection
    # -----------------------
    donor = donors.iloc[
        rng.integers(0, len(donors))
    ]

    donor_income = donor["income"]

    # -----------------------
    # controlled perturbation
    # -----------------------
    adjusted_income = max(
        0,
        donor_income * rng.uniform(0.95, 1.05)
    )

    persons_imputed.loc[idx, "income"] = adjusted_income
persons_imputed.style
# -

persons_imputed.isna().sum()

person_edit.compare(persons_imputed)

# ## Drop unneeded columns

persons_imputed = persons_imputed.drop(columns='income_outlier')

# ## Add aggregated household columns to person dataframe
# We can add some aggregated household columns to the persons dataframe, for instance household income and household size

persons_imputed['income_hh'] = persons_imputed.groupby('hh_id')['income'].transform('sum')
persons_imputed['hh_size'] = persons_imputed.groupby('hh_id')['member'].transform('size')
persons_imputed

# ## Export to parquet

persons_file = f'{statistics_dir}lcs_persons_imputed_{year}.parquet'
persons_imputed.to_parquet(persons_file)
print(f'{persons_imputed.shape[0]} rows and {persons_imputed.shape[1]} columns written to {persons_file}')

households_file = f'{statistics_dir}lcs_households_imputed_{year}.parquet'
households_imputed.to_parquet(households_file)
print(f'{households_imputed.shape[0]} rows and {households_imputed.shape[1]} columns written to {households_file}')
