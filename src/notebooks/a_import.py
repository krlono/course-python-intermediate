# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     notebook_metadata_filter: kernelspec
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Import source data
#
# The source data is data in the format delivered to the statisticians.
# This will be converted to input data which is data stored in the agreed
# format for input data.


# %%
import pandas as pd
import os
from glob import glob


# %% [markdown]
# ## Set working folder and import settings


# %%
local_user_folder = os.environ["USERPROFILE"]

project_name = "course-python-intermediate"
working_folder = f"{local_user_folder}/{project_name}"

working_folder


# %%
os.chdir(working_folder)

os.getcwd()


# %% [markdown]
# ## Import settings and define working directories


# %%
from config.config import settings

year = settings.year
print(f"Current year is {year}")

data_dir = settings.data_dir
data_dir = f"{local_user_folder}\\{data_dir}"

print(f"Data directory is {data_dir}")

source_dir = f"{data_dir}/source/"
print(f"Source directory is {source_dir}")

input_dir = f"{data_dir}/input/"
print(f"Input directory is {input_dir}")


# %%
csv_files = glob(f"{source_dir}/*.csv")
csv_files


# %% [markdown]
# ## Create dictionary with data types


# %%
person_string = [
    "relationship_to_head",
    "sex",
    "marital_status",
    "occupation"
]

person_float = [
    "income"
]

person_date = [
    "birth_date"
]

dtype_dict = {}
person_dates = []

for i in range(1, 10):

    for s in person_string:
        dtype_dict[f"{s}_{i}"] = "string"

    for f in person_float:
        dtype_dict[f"{f}_{i}"] = "float"

    for d in person_date:
        person_dates.append(f"{d}_{i}")

print(dtype_dict)
person_dates


# %%
household_string = [
    "hh_id",
    "state",
    "urbrur",
    "building_type"
]

household_float = [
    "no_of_persons",
    "years_in_community",
    "no_of_rooms",
    "owns_car",
    "owns_motorcycle",
    "owns_bicycle",
    "owns_fridge",
    "owns_freezer",
    "owns_tv"
]

for s in household_string:
    dtype_dict[f"{s}"] = "string"

for f in household_float:
    dtype_dict[f"{f}"] = "float64"

dtype_dict


# %% [markdown]
# ## Import survey data
#
# We use the data types defined in the separate dictionary.


# %%
survey_file = f"{source_dir}lcs_survey_{year}.csv"

survey_data = pd.read_csv(
    survey_file,
    na_values={".", " .", ""},
    dtype=dtype_dict,
    parse_dates=person_dates
)

print(
    f"{survey_data.shape[0]} rows and "
    f"{survey_data.shape[1]} columns read from {survey_file}"
)

survey_data["year"] = year

print(survey_data.info())

survey_data


# %%
survey_data.columns


# %% [markdown]
# ## Import population


# %%
pop_file = f"{source_dir}population_{year}.csv"

population_data = pd.read_csv(
    pop_file,
    na_values={".", " .", ""},
    dtype={
        "hh_id": "string",
        "state": "string",
        "urbrur": "string",
        "no_of_persons": "float64",
        "sampled": "bool"
    }
)

print(
    f"{population_data.shape[0]} rows and "
    f"{population_data.shape[1]} columns read from {pop_file}"
)

population_data["year"] = year

print(population_data.info())

population_data.loc[population_data["state"] == "3"]


# %% [markdown]
# ## Export to parquet


# %%
survey_file = f"{input_dir}lcs_survey_{year}.parquet"

survey_data.to_parquet(survey_file)

print(
    f"{survey_data.shape[0]} rows and "
    f"{survey_data.shape[1]} columns written to {survey_file}"
)


# %%
population_file = f"{input_dir}population_{year}.parquet"

population_data.to_parquet(population_file)

print(
    f"{population_data.shape[0]} rows and "
    f"{population_data.shape[1]} columns written to {population_file}"
)


# %% [markdown]
# ## The print as a function


# %%
def print_io(file, df, direction):
    if direction.upper() == "R":
        rw = "read from"

    if direction.upper() == "W":
        rw = "written to"

    print(
        f"INFO: {df.shape[0]} rows and "
        f"{df.shape[1]} columns {rw} to {file}"
    )


# %%
print_io(
    population_file,
    population_data,
    "W"
)


# %% [markdown]
# ## Check missing values


# %%
survey_data.isna().sum()
