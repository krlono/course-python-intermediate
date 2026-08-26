# %% [markdown]
# # Exercises – Data Processing in Python
#
# This set of exercises covers key concepts from the course.
# Start at the top and work your way down – the exercises increase in difficulty.


# %% [markdown]
# ---
#
# # 🟢 Level 1 – Basic Python


# %% [markdown]
# ### Exercise 1: Simple function
#
# Create a function that returns the triple value of a number.
#
# - Give the function a descriptive name
# - Test it with different numbers


# %%
# Write your function here.


# %%
# Test your function with different numbers.


# %% [markdown]
# ---
#
# ### Exercise 2: Invalid input
#
# Try passing the following into the function from the previous exercise:
#
# - a string (`"hi"`)
# - `True` and `False`


# %%
# Test the function with a string.


# %%
# Test the function with True and False.


# %% [markdown]
# Extend the function:
#
# - Add an error message if the input is not a number.
#
# **Tip**
#
# Use `isinstance(object, type)`.


# %%
print(isinstance(5, int))
print(isinstance("5", int))


# %%
# Modify your function here.


# %%
# Test the modified function.


# %% [markdown]
# ---
#
# ### Exercise 3: Boolean logic
#
# Create a function `is_adult(age)` with the following logic:
#
# - Return `True` if `age` is greater than or equal to 18
# - Return `False` otherwise


# %%
# Create the is_adult() function here.


# %%
# Test the function with different ages.


# %% [markdown]
# ---
#
# ### Exercise 4: Move function to its own file
#
# - Create a `.py` file in `functions/`
# - Move the function from exercise 2 or 3 there
# - Import and use the function
# - Make sure to restart the kernel before importing so the function is
#   loaded from the file and not retained from a previous cell execution.
#
# You may need to run these commands for Python to find the external folder
# where the function is stored.


# %%
import sys

sys.path.append("../../")


# %%
# Import your function here.


# %%
# Test your imported function here.


# %% [markdown]
# ---
#
# # 🟡 Level 2 – Lists and structure


# %% [markdown]
# ## Exercise 5: Working with lists


# %%
numbers = [1, 2, 3, 4, 5]


# %% [markdown]
# Create a new list with values that are one less than the numbers in the list
# (use list comprehension).


# %%
# Create the new list here.


# %% [markdown]
# Use list comprehension to create the following result:
#
# `['The number is 1', 'The number is 2', 'The number is 3',
# 'The number is 4', 'The number is 5']`


# %%
# Create the list here.


# %% [markdown]
# ---
#
# ## Exercise 6: File names


# %%
files = ["data/a.parquet", "data/b.parquet"]


# %% [markdown]
# Create a list of file names without the path.


# %%
# Create the list here.


# %% [markdown]
# ---
#
# ## Exercise 7: Unique values


# %%
columns = ["id", "name", "age", "age"]


# %% [markdown]
# Remove duplicates in the list using a set.


# %%
# Remove duplicates here.


# %% [markdown]
# Convert the result back into an alphabetically sorted list.


# %%
# Create the sorted list here.


# %% [markdown]
# ---
#
# # 🟠 Level 3 – Files and glob


# %% [markdown]
# ### Exercise 8: Find files
#
# - Use `glob` to create a list of all `.parquet` files in a folder in
#   `../../../data`


# %%
from glob import glob


# %%
# Find all .parquet files here.


# %% [markdown]
# Count the number of files using `len()`.


# %%
# Count the files here.


# %% [markdown]
# ---
#
# ### Exercise 9: Recursive search
#
# Extend the task to also find files in subfolders.


# %%
# Find .parquet files recursively here.


# %% [markdown]
# ---
#
# ### Exercise 10: File information
#
# Find size and last modified date for each file.
#
# **Tip:** Use `Path` from `pathlib` with `rglob()`.


# %%
from pathlib import Path
from datetime import datetime

import pandas as pd


# %%
# Create a Path object for ../../../data.


# %%
# Use rglob() to find the files.


# %%
# Create a list containing information about each file.


# %%
# Convert the list into a DataFrame.


# %% [markdown]
# ---
#
# # 🔵 Level 4 – Pandas and data processing


# %% [markdown]
# ### Exercise 11: Read multiple files
#
# - Read multiple `.parquet` files using `glob` and list comprehension
# - Use `../../../data/input/lcs_*.parquet`
# - Combine them into one DataFrame


# %%
# Find the parquet files here.


# %%
# Read the files into a list of DataFrames.


# %%
# Combine the DataFrames into one DataFrame.


# %% [markdown]
# **Challenge**
#
# These files include a reference time column.
#
# Assume the time column does not exist and you want to add a cohort/year
# variable during merging.
#
# Use what you have learned about `split()` to extract the year from the
# filename and add it to a column named `cohort`.


# %%
# Extract the year from each filename.


# %%
# Add the year/cohort to each DataFrame.


# %%
# Combine the DataFrames.


# %% [markdown]
# ---
#
# ## Exercise 12: `map` vs `replace`


# %%
df_map = pd.DataFrame(
    {
        "code": ["A", "B", "C", "A", "B", "C", "D"]
    }
)

mapping = {
    "A": "Fill in your own recoding 1",
    "B": "Fill in your own recoding 2",
    "C": "Fill in your own recoding 3",
}

df_map


# %% [markdown]
# Recode `code` using both `map()` and `replace()` and write the result to
# new columns in `df_map`.
#
# What is the difference between the two methods?


# %%
# Use map() to create a new column.


# %%
# Use replace() to create another new column.


# %%
# Compare the results.


# %% [markdown]
# ---
#
# ### Exercise 13a: Dates
#
# Given a column `date` with standard date format as a string:


# %%
df_time = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6],
        "date": [
            "2024-01-15",
            "2024-02-10",
            "2024-02-25",
            "2024-03-05",
            "2023-02-20",
            "2024-01-30",
        ],
        "date_time_special": [
            "15-01-2024 08:30",
            "10-02-2024 14:45",
            "25-02-2024 09:15",
            "05-03-2024 16:00",
            "20-02-2023 11:20",
            "30-01-2024 07:50",
        ],
        "value": [100, 200, 150, 300, 250, 180],
    }
)

df_time


# %% [markdown]
# - Convert `date` to `datetime`
# - Create columns for:
#   - year
#   - month
# - Filter by one month


# %%
# Convert date to datetime.


# %%
# Create the year column.


# %%
# Create the month column.


# %%
# Filter the data by one month.


# %% [markdown]
# ### Exercise 13b: Special date/time format
#
# Often the date format can be inferred (by you or pandas), but ambiguity may
# lead to errors.
#
# The column `date_time_special` has the format:
# `DD-MM-YYYY HH:MM`.
#
# 1. Convert to datetime where the format is specified
# 2. Create columns for:
#    - year
#    - month
#    - hour
# 3. Filter by:
#    - February
#    - time before 12:00


# %%
# Convert date_time_special to datetime.
# Specify the format explicitly.


# %%
# Create the year column.


# %%
# Create the month column.


# %%
# Create the hour column.


# %%
# Filter by February.


# %%
# Filter by time before 12:00.


# %% [markdown]
# ---
#
# # 🔴 Level 5 – More advanced


# %% [markdown]
# ### Exercise 14: Validate data
#
# In data processing, it is common to check that a column contains only valid
# values.
#
# Example:
#
# - gender should only be `"M"` or `"F"`
# - month should be between 1 and 12
# - status should be `"ACTIVE"` or `"INACTIVE"`
#
# ---
#
# Given the dataset below. Use a list of valid status codes
# (`"ACTIVE"`, `"INACTIVE"`) and check against these to find rows with invalid
# values.
#
# - Use this to print values that are not expected in the column.
#
# You can also check for valid gender and valid months
# (here you can check against a range of values).


# %%
import pandas as pd


# %%
df = pd.DataFrame(
    {
        "status": [
            "ACTIVE",
            "INACTIVE",
            "ACTIVE",
            "ERROR",
            "ACTIVE",
        ],
        "gender": [
            "F",
            "F",
            "M",
            "F",
            "X",
        ],
        "month": [
            1,
            14,
            None,
            4,
            9,
        ],
    }
)

df


# %% [markdown]
# Create a list containing the valid status values.


# %%
# Create valid_status here.


# %% [markdown]
# Find and print the invalid status values.


# %%
# Check for invalid status values here.


# %% [markdown]
# Create a list containing the valid gender values.


# %%
# Create valid_gender here.


# %% [markdown]
# Find and print the invalid gender values.


# %%
# Check for invalid gender values here.


# %% [markdown]
# Check that month contains values between 1 and 12.


# %%
# Check for invalid month values here.


# %% [markdown]
# **Challenge**
#
# Create a function that takes a pandas `DataFrame` `df`, a column name `col`,
# and a list of valid values `valid`.
#
# It should return any values that are not in this list.
#
# You may instead consider using a `pandas.Series` together with the `valid`
# list as arguments.
#
# How are missing values handled in your function?


# %%
# Create your function here.


# %%
# Test your function with the status column.


# %%
# Test your function with the gender column.


# %% [markdown]
# ---
#
# ### Exercise 15: Create a function for file information
#
# Create a function that takes a folder path and returns a pandas DataFrame
# with detailed metadata about all files.
#
# Variables:
#
# - full file path
# - file name
# - file type
# - file size
# - last modified date


# %% [markdown]
# **Tip**
#
# You can use:
#
# - `Path`
# - `rglob()`
# - `stat()`
# - `DataFrame`
#
# You may also want to use `getpass` to identify the file owner.


# %%
# Import the modules you need.


# %%
# Create your get_files_info() function here.


# %% [markdown]
# Test your function using the folder `../../../`.


# %%
folder_path = "../../../"


# %%
# Run your function here.


# %% [markdown]
# Print the five largest files.


# %%
# Sort by file size and display the five largest files.


# %% [markdown]
# Print the five most recently modified files.


# %%
# Sort by modification date and display the five most recently modified files.


# %% [markdown]
# Find the count of each file type.


# %%
# Count the different file extensions.


# %% [markdown]
# ---
# # End of exercises