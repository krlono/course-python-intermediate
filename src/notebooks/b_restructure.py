# # Restructure input data
# The input data is checked for duplicates and restructured

import pandas as pd
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
input_dir = f'{data_dir}/input/'
print(f'Input directory is {input_dir}')
process_dir = f'{data_dir}/processed/'
print(f'Process directory is {process_dir}')

survey_data = pd.read_parquet(f'{input_dir}lcs_survey_{year}.parquet')
survey_data

# ## Check for duplicates

survey_data.loc[survey_data.duplicated(subset=['hh_id'], keep=False)]

population_data = pd.read_parquet(f'{input_dir}population_{year}.parquet')
population_data.loc[population_data['state'].isin(['2','5'])]

# ## Errors 
# The last 020003 should be 020013
# The first 050040 should be 050042
#
# We will change this errors and update the population data

survey_data['dups'] = survey_data.groupby('hh_id', as_index=False).cumcount()
survey_data.style

survey_data.loc[
(survey_data['hh_id'] == '020003') & 
(survey_data['dups'] == 1) & 
(survey_data['year'] == 2023),  'hh_id'] = '020013'
survey_data.loc[
(survey_data['hh_id'] == '050040') & 
(survey_data['dups'] == 0) & 
(survey_data['year'] == 2023),  'hh_id'] = '050042'
survey_data.style

# ## Update population

population_data.loc[12, 'sampled'] = True
population_data.loc[41, 'sampled'] = True
population_data.loc[41, 'no_of_persons'] = 6
population_data.style

# ## Check for duplicates again

survey_data.loc[survey_data.duplicated(subset=['hh_id'], keep=False)]

# ## Drop unneded column

survey_data = survey_data.drop(columns='dups')

# ## Restructure data into a persons dataframe

drop_cols = [
    'building_type', 'no_of_persons', 'no_of_rooms', 'owns_bicycle',
    'owns_car', 'owns_freezer', 'owns_fridge', 'owns_motorcycle', 'owns_tv',
    'years_in_community'
]
person_data = survey_data.drop(columns = drop_cols)
persons = pd.wide_to_long(
    person_data, 
    ['relationship_to_head', 'sex', 'marital_status', 'occupation', 'birth_date', 'income'], 
    sep='_', 
    i=['hh_id', 'year', 'state', 'urbrur'], j='member'
    )
persons = persons.dropna(how='all')
persons = persons.reset_index()
persons

# ## Add age

persons['age'] = year - persons['birth_date'].dt.year
persons

# ## Create household dataframe

household_cols = ['hh_id', 'year', 'state', 'urbrur', 'years_in_community',
    'building_type', 'no_of_persons', 'no_of_rooms', 'owns_bicycle',
    'owns_car', 'owns_freezer', 'owns_fridge', 'owns_motorcycle', 'owns_tv'
]
households = survey_data[household_cols]
households

# ## Export to parquet

persons_file = f'{process_dir}lcs_persons_{year}.parquet'
persons.to_parquet(persons_file)
print(f'{persons.shape[0]} rows and {persons.shape[1]} columns written to {persons_file}')

households_file = f'{process_dir}lcs_households_{year}.parquet'
households.to_parquet(households_file)
print(f'{households.shape[0]} rows and {households.shape[1]} columns written to {households_file}')
