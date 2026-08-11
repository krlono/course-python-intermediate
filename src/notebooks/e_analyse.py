# # Impute values and add columns

import pandas as pd
import numpy as np
import os
from glob import glob
import plotly.express as px

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
statistics_dir = f'{data_dir}/statistics/'
print(f'Statistics directory is {statistics_dir}')
output_dir = f'{data_dir}/output/'
print(f'Output directory is {output_dir}')

# ## Read households dataframe

households_file = f'{statistics_dir}lcs_households_imputed_{year}.parquet'
households = pd.read_parquet(households_file)
print(f'{households.shape[0]} rows and {households.shape[1]} columns read from {households_file}')

persons_file = f'{statistics_dir}lcs_persons_imputed_{year}.parquet'
persons = pd.read_parquet(persons_file)
print(f'{persons.shape[0]} rows and {persons.shape[1]} columns read from {persons_file}')

# ## Add age group

persons['age_group'] = np.select(
    [
        (persons['age'] >= 0) & (persons['age'] < 10),
        (persons['age'] >= 10) & (persons['age'] < 68),
        (persons['age'] >= 68)
    ],
    ['0-9', '10-67', '68+'],
    default='Missing age'
)
persons['age_group'].value_counts()

pd.crosstab(persons['state'], columns=persons['sex'], margins=True)

pd.crosstab(
    persons['state'], 
    columns=persons['sex'], 
    values=persons['weight_person'], 
    aggfunc='sum',
    margins=True
)

labels = {'state':
          {'1': 'Central west', 
           '2': 'Central east',
           '3': 'North',
           '4': 'East',
           '5': 'South',
           '6': 'West',
           '9': 'Capital' 
           },
          'urbrur':
          {'1': 'Urban',
           '2': 'Rural'},
          'relationship_to_head':
          {'0': 'Head', 
           '1': 'Spouse', 
           '2': 'Daughter/son', 
           '3': 'Spouse of son/daughter',
           '4': 'Grandchild',
           '5': 'Sister/brother',
           '6': 'Sister/brother in-laws',
           '7': 'Parent',
           '8': 'Parent-in-law',
           '9': 'Niece/nephew',
           '10': 'Other relative', 
           '11': 'Non relative'},
          'sex':
          {'1': 'Male', 
           '2': 'Female'},
          'marital_status':
          {'1': 'Never married', 
           '2': 'Married', 
           '3': 'Widowed', 
           '4': 'Separated', 
           '5': 'Divorced'}
         }

persons_l = persons.replace(labels)
persons_l.style

# ## Unweighted number of persons by sex

persons["sex"].value_counts()

# ## Weighted number of persons by sex

persons.groupby("sex")["weight_person"].sum()

# ## Unweighted age group distribution

persons["age_group"].value_counts().sort_index()

# ## Weighted age group distribution

persons.groupby("age_group")["weight_person"].sum()

# ## Unweighted occupation distribution

persons["occupation"].value_counts().sort_index()

# ## Weighted occupation distribution

persons.groupby("occupation")["weight_person"].sum()

# ## Unweighted household size

households["no_of_persons"].value_counts().sort_index()

# ## Weighted household size

households.groupby("no_of_persons")["weight_household"].sum()

# ## Unweighted average household size

households["no_of_persons"].mean()

# ## Weighted average household size

np.average(
    households["no_of_persons"],
    weights=households["weight_household"]
)

# ## Unweighted mean income by sex

persons.groupby("sex")["income"].mean()

# ## Weighted mean income by sex

persons.groupby("sex").apply(
    lambda x: np.average(
        x["income"],
        weights=x["weight_person"]
    ),
    include_groups=False
)

# ## Household income per capita

persons["income_per_capita"] = (
    persons["income_hh"] /
    persons["hh_size"]
)
persons

# ## Mean income per capita

np.average(
    persons["income_per_capita"],
    weights=persons["weight_person"]
)

# ## Weighted Income per capita by state

persons.groupby("state").apply(
    lambda x: np.average(
        x["income_per_capita"],
        weights=x["weight_person"]
    ),
    include_groups=False
)

# ## Asset ownership

# ### Percentage owning TV, Unweighted

households["owns_tv"].mean() * 100

# ### Percentage owning TV, weighted

np.average(
    households["owns_tv"],
    weights=households["weight_household"]
) * 100

asset_vars = [x for x in households.columns if x[:3] == 'own']
for var in asset_vars:
    pct = np.average(
        households[var],
        weights=households["weight_household"]
    ) * 100

    print(var, round(pct,1))

# ## Relationships

# ## Household size by building type

households.groupby("building_type")["no_of_persons"].mean()

# ### Mean income by age group

persons.groupby("age_group").apply(
    lambda x: np.average(
        x["income"],
        weights=x["weight_person"]
    ),
    include_groups=False
)

# ### Mean income by building_type

persons.groupby("sex")['income'].mean()

persons.groupby("sex").apply(
    lambda x: np.average(
        x["income"],
        weights=x["weight_person"]
    ),
    include_groups=False
)

# ## Unweighted building type × Owns car

pd.crosstab(
    households["building_type"],
    households["owns_car"]
)

# ## Weighted building type × Owns car

pd.pivot_table(
    households,
    values="weight_household",
    index="building_type",
    columns="owns_car",
    aggfunc="sum"
)

pd.crosstab(
    households["building_type"],
    columns=households["owns_car"],
    values=households["weight_household"],
    aggfunc="sum",
    normalize='index',
    margins=True
).mul(100)

# ## Graphs

persons["age"].hist(bins=20)

households["no_of_persons"].hist()

households["building_type"].value_counts().plot.bar()

persons.boxplot(
    column="income",
    by="occupation",
    rot=90
)

households[asset_vars].mean().mul(100).plot.bar()

# ## Graphs made with plotly

px.histogram(persons, x='marital_status', color='sex', barmode="group", title='Persons by marital status and sex (unweighted)')

px.histogram(
    persons, 
    x='marital_status', 
    y='weight_person',
    histfunc='sum',
    color='sex', 
    barmode="group", 
    title='Persons by marital status and sex')

px.histogram(
    persons, 
    x='marital_status', 
    y='income',
    histfunc='sum',
    color='sex', 
    barmode="group", 
    title='Persons by marital status and sex')

px.histogram(
    persons.assign(
        weighted_income=persons["income"] * persons["weight_person"]
    ),
    x="marital_status",
    y="weighted_income",
    histfunc="sum",
    color="sex",
    barmode="group",
    title="Weighted income by marital status and sex"
)

px.histogram(
    persons.sort_values('state'),
    x="marital_status",
    y="income",
    histfunc="avg",
    color="sex",
    barmode="group",
    title="Unweighted average income by marital status and sex"
)

# +
weighted_mean = (
    persons
    .groupby(["marital_status", "sex"], as_index=False)
    .apply(
        lambda x: pd.Series(
            {'income_w': np.average(
                x["income"],
                weights=x["weight_person"]
            )
             }
    )
        ,
        include_groups=False
    )
    .sort_values('marital_status')
)

px.histogram(
    weighted_mean,
    x="marital_status",
    y="income_w",
    histfunc="avg",
    color="sex",
    barmode="group",
    title="Weighted average income by marital status and sex"
)
# -

weighted_mean_by_state_sex

# +
weighted_mean = (
    persons
    .groupby(["marital_status", "sex"])
    .apply(
        lambda x: np.average(
            x["income"],
            weights=x["weight_person"]
        ),
        include_groups=False
    )
)

weighted_mean
# -

persons.groupby(["marital_status", "sex"], as_index=False)["income"].mean().sort_values('marital_status')

display(weighted_mean_by_state_sex)

pd.crosstab(
    persons_l['state'], 
    columns=persons_l['sex'], 
    values=persons_l['weight_person'], 
    aggfunc='sum',
    margins=True
)
