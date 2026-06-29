# # Import data

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

from config.config import settings
year = settings.year
print(year)
data_dir = settings.data_dir
data_dir = f'{local_user_folder}\\{data_dir}'
data_dir

csv_files = glob(f"{data_dir}/*.csv") 
csv_files

# ## Import person file

households = pd.read_csv(
    f"{data_dir}/households_{year}.csv",
    dtype={
        "hh": "object",
        "year": "int",
        "years_in_community": "int",
        "building_type": "object",
        "number_of_rooms": "int",
        "owns_car": "bool",
        "owns_motorcycle": "bool",
        "owns_bicycle": "bool",
        "owns_fridge": "bool",
        "owns_freezer": "bool",
        "owns_tv": "bool"
    },
    na_values={".", " ."},
)
print(households.info())
households

persons = pd.read_csv(
    f"{data_dir}/persons_{year}.csv",
    dtype={
        "hh": "object",
        "member": "int",
        "year": "int",
        "state": "object",
        "urbrur": "object",
        "building_type": "object",
        "relationship_to_head": "object",
        "sex": "object",
        "marital_status": "object",
        "income": "float",
        "weight_person": "float",
    },
    parse_dates=["birth_date"],
    na_values={".", " ."},
)
persons.info()

persons.isna().sum()
