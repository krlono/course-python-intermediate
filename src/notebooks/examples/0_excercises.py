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

# # Exercises – Data Processing in Python

# This set of exercises covers key concepts from the course.
# Start at the top and work your way down – the exercises increase in difficulty.

# ---

# # 🟢 Level 1 – Basic Python

# ### Exercise 1: Simple function
# Create a function that returns the triple value of a number.



# - Give the function a descriptive name
# - Test it with different numbers


# ---

# ### Exercise 2: Invalid input
# Try passing the following into the function from the previous exercise:
# - a string ("hi")
# - True and False



# Extend the function:
# - Add an error message if the input is not a number
#
# **Tip**
#
# Use `isinstance(object, type)`

print(isinstance(5, int))
print(isinstance("5", int))


# ---

# ### Exercise 3: Boolean logic
# Create a function `is_adult(age)` with the following logic:

# - Return `True` if `age` is greater than or equal to 18
# - Return `False` otherwise




# ---

# ### Exercise 4: Move function to its own file
# - Create a .py file in `functions/`
# - Move the function from exercise 2 or 3 there
# - Import and use the function
#     - Make sure to restart the kernel before importing so the function is loaded from the file and not retained from a previous cell execution
#  
# You may need to run these commands for Python to find the external folder where the function is stored


import sys
sys.path.append("../../")

# ---

# # 🟡 Level 2 – Lists and structure

# ## Exercise 5: Working with lists

numbers = [1, 2, 3, 4, 5]

# - Create a new list with values that are one less than the numbers in the list (use list comprehension)




# - Use list comprehension to create the following result:
#     - ['The number is 1', 'The number is 2', 'The number is 3', 'The number is 4', 'The number is 5']




# ---

# ## Exercise 6: File names

files = ["data/a.parquet", "data/b.parquet"]

# - Create a list of file names without the path




# ---

# ## Exercise 7: Unique values

columns = ["id", "name", "age", "age"]

# - Remove duplicates in the list using a set




# - Convert the result back into an alphabetically sorted list




# ---

# # 🟠 Level 3 – Files and glob

# ### Exercise 8: Find files
# - Use `glob` to create a list of all .parquet files in a folder under `../../data`




# - Count the number of files using `len()`




# ---

# ### Exercise 9: Recursive search
# - Extend the task to also find files in subfolders




# ---

# ### Exercise 10: File information
# - Find size and last modified date for each file




# ---

# # 🔵 Level 4 – Pandas and data processing

# ### Exercise 11: Read multiple files
# - Read multiple .parquet files using glob and list comprehension
#     - use `/../../data/persons*.csv`
# - Combine them into one DataFrame




# **Challenge**
# - These files follow the SSB naming standard and they include a reference time column.
#   Assume the time column does not exist and you want to add a cohort/year variable during merging.
#   Use what you have learned about `split()` to extract the year from the filename and add it to a column named `cohort`.




# ---

# ## Exercise 12: map vs replace

import pandas as pd

df_map = pd.DataFrame({
    "code": ["A", "B", "C", "A", "B", "C", "D"]
})

mapping = {
    "A": "Fill in your own recoding 1",
    "B": "Fill in your own recoding 2",
    "C": "Fill in your own recoding 3"
}

df_map

# - Recode `code` using both `map()` and `replace()` and write the result to new columns in `df_map`.
# - What is the difference between the two methods?




# ---

# ### Exercise 13 a): Dates
# Given a column `date` with standard date format as a string:

import pandas as pd

df_time = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "date": [
        "2024-01-15",
        "2024-02-10",
        "2024-02-25",
        "2024-03-05",
        "2023-02-20",
        "2024-01-30"
    ],
    "date_time_special": [
        "15-01-2024 08:30",
        "10-02-2024 14:45",
        "25-02-2024 09:15",
        "05-03-2024 16:00",
        "20-02-2023 11:20",
        "30-01-2024 07:50"
    ],
    "value": [100, 200, 150, 300, 250, 180]
})

df_time

# - Convert `date` to `datetime`
# - Create columns for:
#   - year
#   - month
# - Filter by one month




# ### Exercise 13b): Special date/time format
#
# Often the date format can be inferred (by you or pandas), but ambiguity may lead to errors.
#
# The column `"date_time_special"` has the format: `"DD-MM-YYYY HH:MM"`.
#
# 1. Convert to datetime where the format is specified
# 2. Create columns for:
#    - year
#    - month
#    - hour
# 3. Filter by:
#    - February
#    - time before 12:00


# ---



# # 🔴 Level 5 – More advanced

# ### Exercise 14: Validate data
#
# In data processing, it is common to check that a column contains only valid values.
#
# Example:
# - gender should only be `"M"` or `"F"`
# - month should be between 1 and 12
# - status should be `"ACTIVE"` or `"INACTIVE"`
#
# ---
#
# Given the dataset below. You can convert the `status` column to a set to get all unique values (similar to the `.unique()` method).
# - Use this to print values that are not expected in the column.

import pandas as pd

df = pd.DataFrame({
    "status": [
        "ACTIVE",
        "INACTIVE",
        "ACTIVE",
        "ERROR",
        "ACTIVE"
    ]
})

set(df["status"].to_list())

list(df["status"].unique())


# **Challenge**
#
# Create a function that takes a pandas.DataFrame `df`, a column name `col`, and a list of valid values `valid`.
# It should return any values that are not in this list.
#
# You may instead consider using a `pandas.Series` together with the `valid` list as arguments.
#
# How are missing values handled in your function?


# Note: For larger validation needs
#
# In real-world data projects, validation is often more comprehensive than simple checks using `set()`.
#
# Examples:
# - checking data types
# - required columns
# - valid ranges
# - rules between columns
# - handling missing values
#
# For larger validation needs, it may be useful to use a library like `pandera`.
#
# `pandera` allows you to define rules and expectations for datasets.
#
# Examples of what can be validated:
# - that a column is an integer
# - that values are positive
# - that dates are not missing
# - that categories contain only valid values
#
# This makes the code:
# - easier to maintain
# - easier to test
# - more robust in production
#
# In this course, we stick to simple custom validations using standard Python and pandas, but it is useful to know that such tools exist.
#

# ### Exercise 15: Using list comprehensions and glob to create a custom file overview in pandas

# - Use glob to create a pandas.DataFrame overview of files in a folder of your choice.
# - Each row in the dataset should correspond to one file.
# - Variables should be:
#     - full file path
#     - file name without path
#     - file type (parquet, csv, txt)
#     - file size
#     - last modified date
#
# **Tip**
#
# When using list comprehension without filtering, order and count are preserved.
#
# You can define a pandas DataFrame using a combination of dictionary and lists:
# ```
# df = pd.DataFrame(
#     {
#         column_name1: list_of_values,
#         column_name2: list_of_values2
#     }
# )
# ```



# - Print the five largest files



# - Print the five most recently modified files



# - Perform a groupby and find the count of each file type



# ---
