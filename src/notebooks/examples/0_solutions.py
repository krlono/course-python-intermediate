# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Exercise solutions – Data Processing in Python

# This exercise set covers key concepts from the course.
# Start at the top and work your way down – the exercises increase in difficulty.

# ---

# # 🟢 Level 1 – Basic Python

# ### Exercise 1: Simple function
# Create a function that returns triple the value of a number.

# - Give the function a descriptive name
# - Test it with different numbers

def mult_3(x):
    return x * 3


print(mult_3(5))
x = 9
print(f"{x} * 3 = {mult_3(x)}")

# ---

# ### Exercise 2: Invalid input
# Try passing into the function from the previous exercise:
# - a string ("hi")
# - True and False

mult_3('hi')

mult_3(True), mult_3(False) 

# Extend the function:
# - Add an error message if the input is not a number
#
# **Tip**
#
# Use `isinstance(object, type)`

print(isinstance(5, int))
print(isinstance("5", int))


def mult_3(x):
    if isinstance(x, (int, float)):
        return x * 3
    raise ValueError(f'{x} is not a number')


mult_3('oops')

mult_3(8)

mult_3(4.2)


# ---

# ### Exercise 3: Boolean logic
# Create a function `is_adult(age)` with the following logic:

# - Return `True` if `age` is greater than or equal to 18
# - Return `False` otherwise

def is_adult(age):
    if age >= 18:
        return True
    return False    


is_adult(0)

# ---

# ### Exercise 4: Move function to its own file
# - Create a .py file in `functions/`
# - Move the function from exercise 2 or 3 there
# - Import and use the function
#     - Make sure to restart the kernel before importing so the function is loaded during import and not retained from a previous cell execution

import os
os.getcwd()

# +
import sys
sys.path.append("../../")

from functions.funcs import is_adult
is_adult(12)
# -

# ---

# # 🟡 Level 2 – Lists and structure

# ## Exercise 5: Working with lists

numbers = [1, 2, 3, 4, 5]

# - Create a new list with values that are one less than the numbers in the list (use list comprehension)

numbers_minus_1 = [t - 1 for t in numbers]
numbers_minus_1

# - Use list comprehension to create the following result:
#     - ['The number is 1', 'The number is 2', 'The number is 3', 'The number is 4', 'The number is 5']

[f'The number is {t}' for t in numbers]

# ---

# ## Exercise 6: File names

files = ["data/a.parquet", "data/b.parquet"]

# - Create a list of file names without the path

[f.split('/')[-1] for f in files]

# chained split: first on "/", then on "."
[f.split('/')[-1].split('.')[0] for f in files]

# ---

# ## Exercise 7: Unique values

columns = ["id", "name", "age", "age"]

# - Remove duplicates in the list using a set

set(columns)

# - Convert the result back into an alphabetically sorted list

sorted(list(set(columns)))

# ---

# # 🟠 Level 3 – Files and glob

# ### Exercise 8: Find files
# - Use `glob` to create a list of all .parquet files in a folder in `/buckets/product/`

from glob import glob

# - Count the number of files using `len()`

files = glob("/buckets/product/kurs-python-ii/metstat/input/temp/*.parquet")
for f in files:
    print(f)
len(files)

# ---

# ### Exercise 9: Recursive search
# - Extend the task to also find files in subfolders

files = glob("/buckets/product/kurs-python-ii/metstat/**/*.parquet", recursive=True)
for f in files:
    print(f)
len(files)

# ---

# ### Exercise 10: Get latest file version
# Search for a prepared data file and load the latest version using `get_latest_fileversions`. Try to do as much as possible without looking at production code.
#
# 1) Create a glob pattern using an f-string
# 2) Use the imported function to determine the latest version
# 3) Load the dataset with pandas

import pandas as pd
from glob import glob
from fagfunksjoner import get_latest_fileversions
from config.config import settings

folder = settings.prepared_dir
year = settings.year
print(folder)
print(year)

obs_filename = f"{folder}/temp/observations-imputed_p{year}_v*.parquet"
obs_filename = get_latest_fileversions(glob(obs_filename))

obs = pd.read_parquet(obs_filename)
obs

# ---

# # 🔵 Level 4 – Pandas and data processing

# ### Exercise 11: Read multiple files
# - Read multiple .parquet files using glob and list comprehension
#     - use `/buckets/product/kurs-python-ii/metstat/input/temp/pre-input/frost/`
# - Combine them into one DataFrame

parq_files = glob("/buckets/product/kurs-python-ii/metstat/input/temp/pre-input/frost/*.parquet")
all_df_list = [pd.read_parquet(file) for file in parq_files]
all_df = pd.concat(all_df_list, ignore_index=True)
all_df

# **Challenge**
# - These files follow the SSB naming standard and include a reference time column.
#   Assume the time column does not exist and you want to add a cohort/year variable when merging.
#   Use what you have learned about `split()` to extract the year from the filename and add it to a column called `year`.

years = [p.split('_')[-2][1:] for p in parq_files]  # The year with a leading 'p' is the second-to-last element ([-2]); remove 'p' with [1:]
years

for year, df in zip(years, all_df_list):
    df["year"] = year
all_df = pd.concat(all_df_list, ignore_index=True)
all_df    

# ---

# ## Exercise 12: map vs replace

import pandas as pd

df_map = pd.DataFrame({
    "code": ["A", "B", "C", "A", "B", "C", "D"]
})

mapping = {
    "A": "Squirrel",
    "B": "Deer",
    "C": "Fox"
}

df_map

# - Recode `code` using both `map()` and `replace()` and write the result to new columns in `df_map`.
# - What is the difference between the two methods?

df_map['code_map'] = df_map['code'].map(mapping)
df_map

df_map['code_replace'] = df_map['code'].replace(mapping)
df_map

# ---

# ### Exercise 13 a): Dates
# Given a column `date` with standard string format:

print(df_time['date'].dtype)
df_time['date'] = pd.to_datetime(df_time['date'])
df_time['date'].dtype

# ### Exercise 13b): Special date/time format
# The column "date_time_special" has format "DD-MM-YYYY HH:MM"

print(df_time['date_time_special'].dtype)
df_time['date_time_special'] = pd.to_datetime(df_time['date_time_special'], format="%d-%m-%Y %H:%M")
print(df_time['date_time_special'].dtype)

df_time['year'] = df_time['date_time_special'].dt.year
df_time['month'] = df_time['date_time_special'].dt.month
df_time['time'] = df_time['date_time_special'].dt.time

# ---

# # 🔴 Level 5 – More advanced

# ### Exercise 14: Validate data
#
# It is common to check that a column contains only valid values.

# Example:
# - gender should only be "M" or "F"
# - month should be between 1 and 12
# - status should be "ACTIVE" or "INACTIVE"

valid = ['ACTIVE', 'INACTIVE']
df.loc[df['status'].isin(valid) == False]

# **Challenge**

def is_not_valid(df, col, valid, include_missing=True):
    if include_missing == False:
        unique_values = set(df[col].loc[df[col].notna()].unique())
    else:
        unique_values = set(df[col].unique())
    not_valid = unique_values - set(valid)
    return list(not_valid)

# ---

# ### Exercise 15: Create a file overview

# Create a function that takes a folder path and returns a pandas DataFrame
# with detailed metadata about all files.

# Variables:
# - full file path
# - file name
# - file type
# - file size
# - last modified date

# (Code remains unchanged since it is already in English)
