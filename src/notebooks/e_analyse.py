# # Basic analysis

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

# ## Read households and persons parquet files

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
        (persons['age'] >= 10) & (persons['age'] < 20),
        (persons['age'] >= 20) & (persons['age'] < 50),
        (persons['age'] >= 50) & (persons['age'] < 68),
        (persons['age'] >= 68)
    ],
    ['0-9', '10-19', '20-49', '50-67', '68+'],
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
           '5': 'Divorced'},
          'occupation':{
           '1': 'Farmer with non-family employees',
           '2': 'Farmer with only family members',
           '3': 'Unpaid family farm worker',
           '4': 'Non-farm employer with non-family employees',
           '5': 'Non-farm employer with only family employees',
           '6': 'Unpaid assistance in family enterprise',
           '7': 'Self-Employed Independent contractor, technician, professional, etc',
           '8': 'Wage Employee in Private Company (with contract)',
           '9': 'Paid Employee in Private Company (without contract)',
           '10': 'Wage Employee for Government',
           '11': 'Wage Employee in Parastatal (government owned company)',
           '12': 'Casual/Day Laborer',
           '13': 'Intern/free labor/voluntary work',
           '14': 'Home maker',
           '15': 'Was not working, but was looking for work and has worked previously',
           '16': 'Was not working, but was looking for work. Has never worked before',
           '17': 'Was not working, and was not looking for work',
           '18': 'Student',
           '19': 'Retired/pensioner',
           '20': 'Was not working because of disability or chronical illness'},
          'building_type': {
              "1": "Brick",
              "2": "Wood",
              "3": "Concrete",
              "4": "Mud"
          }
         }          

persons_l = persons.replace(labels)
persons_l.style

households_l = households.replace(labels)
households_l.style



# ## Unweighted number of persons by sex

persons_l["sex"].value_counts()

# ## Weighted number of persons by sex

persons_l.groupby("sex")["weight_person"].sum()

# ## Unweighted age group distribution

persons_l["age_group"].value_counts().sort_index()

# ## Weighted age group distribution

persons_l.groupby("age_group")["weight_person"].sum()

# ## Unweighted occupation distribution

persons_l["occupation"].value_counts().sort_index()

# ## Weighted occupation distribution

persons_l.groupby("occupation")["weight_person"].sum()

# ## Building types

households_l["building_type"].value_counts()

# ## Unweighted household size

households_l["no_of_persons"].value_counts().sort_index()

# ## Weighted household size

households_l.groupby("no_of_persons")["weight_household"].sum()

# ## Unweighted average household size

households_l["no_of_persons"].mean()

# ## Weighted average household size

np.average(
    households_l["no_of_persons"],
    weights=households_l["weight_household"]
)

# ## Unweighted mean income by sex

persons_l.groupby("sex")["income"].mean()

# ## Weighted mean income by sex

persons_l.groupby("sex").apply(
    lambda x: np.average(
        x["income"],
        weights=x["weight_person"]
    ),
    include_groups=False
)

# ## Household income per capita

persons_l["income_per_capita"] = (
    persons_l["income_hh"] /
    persons_l["hh_size"]
)
persons_l

# ## Mean income per capita

np.average(
    persons_l["income_per_capita"],
    weights=persons_l["weight_person"]
)

# ## Weighted Income per capita by sex

persons_l.groupby("sex").apply(
    lambda x: np.average(
        x["income_per_capita"],
        weights=x["weight_person"]
    ),
    include_groups=False
)

# ## Asset ownership

# ### Percentage owning TV, Unweighted

households_l["owns_tv"].mean() * 100

# ### Percentage owning TV, weighted

np.average(
    households_l["owns_tv"],
    weights=households_l["weight_household"]
) * 100

asset_vars = [x for x in households_l.columns if x[:3] == 'own']
for var in asset_vars:
    pct = np.average(
        households_l[var],
        weights=households_l["weight_household"]
    ) * 100

    print(var, round(pct,1))

# ## Relationships

# ## Household size by building type

households_l.groupby("building_type")["no_of_persons"].mean()

# ### Mean income by age group

persons_l.groupby("age_group").apply(
    lambda x: np.average(
        x["income"],
        weights=x["weight_person"]
    ),
    include_groups=False
)

label_yesno = {
    0: 'No',
    1: 'Yes'
}
for a in asset_vars:
    households_l[a] = households_l[a].map(label_yesno)
households_l

# ## Unweighted building type × Owns car

pd.crosstab(
    households_l["building_type"],
    households_l["owns_car"]
)

# ## Weighted building type × Owns car

pd.crosstab(
    households_l["building_type"],
    columns=households_l["owns_car"],
    values=households_l["weight_household"],
    aggfunc="sum",
    margins=True
)

# ## Weighted building type × Owns car, row percentages

pd.crosstab(
    households_l["building_type"],
    columns=households_l["owns_car"],
    values=households_l["weight_household"],
    aggfunc="sum",
    normalize='index',
    margins=True
).mul(100)

# ## Weighted building type × each asset type, row percentages

for a in asset_vars:
    display(
        pd.crosstab(
            households_l["building_type"],
            columns=households_l[a],
            values=households_l["weight_household"],
            aggfunc="sum",
            normalize='index',
            margins=True
        ).mul(100)        
    )

# ## All assets in one table

household_assets = households[['building_type'] + asset_vars]
household_assets['building_type'] = household_assets['building_type'].map(labels['building_type'])
asset_table = (
    household_assets
    .groupby("building_type")[asset_vars]
    .mean()
    .mul(100)
    .round(1)
)
# Add total
asset_table.loc["Total"] = (
    households[asset_vars]
    .mean()
    .mul(100)
    .round(1)
)
asset_table

# ### Save as parquet file

asset_file = f'{output_dir}lcs_households_assets_by_building_type_{year}.parquet'
asset_table.to_parquet(asset_file)
print(f'{asset_table.shape[0]} rows and {asset_table.shape[1]} columns written to {asset_file}')

# ## Graphs

persons_l["age"].hist(bins=20)

households_l["no_of_persons"].hist()

households_l["building_type"].value_counts().plot.bar()

persons_l.boxplot(
    column="income",
    by="occupation",
    rot=90
)

households_l[asset_vars].mean().mul(100).plot.bar()

# ## Graphs made with plotly

px.histogram(
    persons_l, 
    x='marital_status', 
    color='sex', 
    barmode="group", 
    title='Persons by marital status and sex (unweighted)'
)

px.histogram(
    persons_l, 
    x='marital_status', 
    y='weight_person',
    histfunc='sum',
    color='sex', 
    barmode="group", 
    title='Persons by marital status and sex')

px.histogram(
    persons_l, 
    x='marital_status', 
    y='income',
    histfunc='sum',
    color='sex', 
    barmode="group", 
    title='Persons by marital status and sex')

px.histogram(
    persons_l.assign(
        weighted_income=persons_l["income"] * persons_l["weight_person"]
    ),
    x="marital_status",
    y="weighted_income",
    histfunc="sum",
    color="sex",
    barmode="group",
    title="Weighted income by marital status and sex"
)

px.histogram(
    persons_l.sort_values('sex'),
    x="marital_status",
    y="income",
    histfunc="avg",
    color="sex",
    barmode="group",
    title="Unweighted average income by marital status and sex"
)

# +
weighted_mean = (
    persons_l
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

persons.groupby(["marital_status", "sex"], as_index=False)["income"].mean().sort_values('marital_status')

# ### Save as parquet file

income_file = f'{output_dir}lcs_persons_income_by_marital_status_and_sex_{year}.parquet'
weighted_mean.to_parquet(income_file)
print(f'{weighted_mean.shape[0]} rows and {weighted_mean.shape[1]} columns written to {income_file}')

# ## Poverty
# Suppose the poverty line is 2500

poverty_line = 2500

persons_l["poor"] = (
    persons_l["income_per_capita"] < poverty_line
).astype(int)
persons_l

# ### Unweighted poverty rate

persons_l["poor"].mean() * 100

# ### Weighted poverty rate

np.average(
    persons_l["poor"],
    weights=persons_l["weight_person"]
) * 100

# ### Weighted poverty rate by sex

persons_l.groupby("sex").apply(
    lambda x: np.average(
        x["poor"],
        weights=x["weight_person"]
    ) * 100,
    include_groups=False
)
