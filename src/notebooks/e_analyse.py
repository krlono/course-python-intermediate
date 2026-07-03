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

pd.crosstab(
    persons_l['state'], 
    columns=persons_l['sex'], 
    values=persons_l['weight_person'], 
    aggfunc='sum',
    margins=True
)
