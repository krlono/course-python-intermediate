# %% [markdown]
# # Exercise solutions – Data Processing in Python
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
def mult_3(x):
    return x * 3


# %%
print(mult_3(5))

x = 9
print(f"{x} * 3 = {mult_3(x)}")


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
mult_3("hi")


# %%
mult_3(True), mult_3(False)


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
def mult_3(x):
    if isinstance(x, (int, float)):
        return x * 3

    raise ValueError(f"{x} is not a number")


# %%
mult_3("oops")


# %%
mult_3(8)


# %%
mult_3(4.2)


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
def is_adult(age):
    if age >= 18:
        return True

    return False


# %%
is_adult(0)


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


# %%
import os

os.getcwd()


# %%
import sys

sys.path.append("../../")


# %%
from functions.funcs import is_adult

is_adult(12)


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
numbers_minus_1 = [t - 1 for t in numbers]

numbers_minus_1


# %% [markdown]
# Use list comprehension to create the following result:
#
# `['The number is 1', 'The number is 2', 'The number is 3',
# 'The number is 4', 'The number is 5']`


# %%
[f"The number is {t}" for t in numbers]


# %% [markdown]
# ---
#
# ## Exercise 6: File names


# %%
files = ["data/a.parquet", "data/b.parquet"]


# %% [markdown]
# Create a list of file names without the path.


# %%
[f.split("/")[-1] for f in files]


# %% [markdown]
# Chained split: first on `/`, then on `.`.


# %%
[f.split("/")[-1].split(".")[0] for f in files]


# %% [markdown]
# ---
#
# ## Exercise 7: Unique values


# %%
columns = ["id", "name", "age", "age"]


# %% [markdown]
# Remove duplicates in the list using a set.


# %%
set(columns)


# %% [markdown]
# Convert the result back into an alphabetically sorted list.


# %%
sorted(list(set(columns)))


# %% [markdown]
# ---
#
# # 🟠 Level 3 – Files and glob


# %% [markdown]
# ### Exercise 8: Find files
#
# - Use `glob` to create a list of all `.parquet` files in a folder in
#   `../../../data`
# - Count the number of files using `len()`


# %%
from glob import glob


# %%
files = glob("../../../data/input/*.parquet")

for f in files:
    print(f)

len(files)


# %% [markdown]
# ---
#
# ### Exercise 9: Recursive search
#
# Extend the task to also find files in subfolders.


# %%
files = glob("../../../data/**/*.parquet", recursive=True)

for f in files:
    print(f)

len(files)


# %% [markdown]
# ---
#
# ### Exercise 10: File information
#
# Find size and last modified date for each file.


# %%
import pandas as pd

from pathlib import Path
from datetime import datetime


# %%
folder = Path("../../../data")

files = folder.rglob("*")

records = []

for file in files:
    stat = file.stat()

    records.append(
        {
            "name_full": file.resolve(),
            "path": file.parent,
            "name": file.name,
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime),
        }
    )

file_info = pd.DataFrame(records)

file_info


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
parq_files = glob("../../../data/input/lcs_*.parquet")

all_df_list = [
    pd.read_parquet(file)
    for file in parq_files
]

all_df = pd.concat(
    all_df_list,
    ignore_index=True,
)

all_df


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
years = [
    p.split("_")[-1].split(".")[0]
    for p in parq_files
]

years


# %%
for year, df in zip(years, all_df_list):
    df["year"] = year

all_df = pd.concat(
    all_df_list,
    ignore_index=True,
)

all_df


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
    "A": "Squirrel",
    "B": "Deer",
    "C": "Fox",
}

df_map


# %% [markdown]
# Recode `code` using both `map()` and `replace()` and write the result to
# new columns in `df_map`.
#
# What is the difference between the two methods?


# %%
df_map["code_map"] = df_map["code"].map(mapping)

df_map


# %%
df_map["code_replace"] = df_map["code"].replace(mapping)

df_map


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


# %% [markdown]
# - Convert `date` to `datetime`
# - Create columns for:
#   - year
#   - month
# - Filter by one month


# %%
print(df_time["date"].dtype)

df_time["date"] = pd.to_datetime(df_time["date"])

print(df_time["date"].dtype)


# %% [markdown]
# Create the year and month variables.


# %%
df_time["year"] = df_time["date"].dt.year
df_time["month"] = df_time["date"].dt.month

df_time


# %% [markdown]
# Filter by one month.


# %%
df_time.loc[df_time["month"] == 2]


# %% [markdown]
# ### Exercise 13b: Special date/time format
#
# Often the date format can be inferred by you or Pandas, but ambiguity may
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
print(df_time["date_time_special"].dtype)

df_time["date_time_special"] = pd.to_datetime(
    df_time["date_time_special"],
    format="%d-%m-%Y %H:%M",
)

print(df_time["date_time_special"].dtype)


# %%
df_time["year"] = df_time["date_time_special"].dt.year
df_time["month"] = df_time["date_time_special"].dt.month
df_time["time"] = df_time["date_time_special"].dt.time

display(df_time)


# %% [markdown]
# Filter by February and time before 12:00.


# %%
df_time.loc[
    (df_time["month"] == 2)
    & (df_time["date_time_special"].dt.hour < 12)
]


# %% [markdown]
# ---
#
# # 🔴 Level 5 – More advanced


# %% [markdown]
# Example:
#
# - gender should only be `"M"` or `"F"`
# - month should be between 1 and 12
# - status should be `"ACTIVE"` or `"INACTIVE"`


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


# %%
valid_status = ["ACTIVE", "INACTIVE"]
valid_gender = ["F", "M"]


# %%
print("Invalid status")

display(
    df.loc[
        df["status"].isin(valid_status) == False
    ]
)


# %%
print("\nInvalid gender")

display(
    df.loc[
        df["gender"].isin(valid_gender) == False
    ]
)


# %%
print("\nInvalid month")

display(
    df.loc[
        df["month"].isin(range(1, 13)) == False
    ]
)


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
def is_not_valid(
    df,
    col,
    valid,
    include_missing=True,
):
    if include_missing == False:
        unique_values = set(
            df[col]
            .loc[df[col].notna()]
            .unique()
        )
    else:
        unique_values = set(
            df[col].unique()
        )

    not_valid = unique_values - set(valid)

    return list(not_valid)


# %%
is_not_valid(
    df,
    col="status",
    valid=valid_status,
)


# %%
is_not_valid(
    df,
    col="gender",
    valid=valid_gender,
)


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


# %%
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional, Union

import getpass
import pandas as pd


# %%
def get_files_info(
    folder_path: Union[str, Path],
    include_subfolders: bool = False,
    extensions: Optional[Union[str, Iterable[str]]] = None,
    min_size: Optional[int] = None,
    max_size: Optional[int] = None,
    name_contains: Optional[str] = None,
) -> pd.DataFrame:
    """
    Collect metadata about files in a directory.

    Parameters
    ----------
    folder_path : str or Path
        Path to the directory to scan.
    include_subfolders : bool, default False
        If True, recursively include files in subdirectories.
    extensions : str or iterable of str, optional
        File extension(s) to filter by (e.g. ".csv", "csv", or
        [".csv", "txt"]).
        Matching is case-insensitive, and a leading "." is added if missing.
    min_size : int, optional
        Minimum file size in bytes.
    max_size : int, optional
        Maximum file size in bytes.
    name_contains : str, optional
        Substring that must be present in the file name.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns:
        ['name_full', 'path', 'name', 'suffix', 'size',
         'created', 'modified', 'owner']

    Examples
    --------
    >>> df = get_files_info("data/")

    >>> df = get_files_info(
    ...     "data/",
    ...     extensions="csv",
    ... )

    >>> df = get_files_info(
    ...     "data/",
    ...     include_subfolders=True,
    ...     extensions=["csv", ".parquet"],
    ...     min_size=10_000,
    ... )

    >>> df = get_files_info(
    ...     "data/",
    ...     name_contains="2024",
    ... )
    """

    folder = Path(folder_path)

    if include_subfolders:
        files = folder.rglob("*")
    else:
        files = folder.glob("*")

    # Normalize extensions input
    def _normalize_ext(ext: str) -> str:
        ext = ext.lower()

        if ext.startswith("."):
            return ext

        return f".{ext}"

    if extensions is not None:
        if isinstance(extensions, str):
            extensions = {
                _normalize_ext(extensions)
            }
        else:
            extensions = {
                _normalize_ext(ext)
                for ext in extensions
            }

    records = []

    for file in files:
        if not file.is_file():
            continue

        # Cheap filters first
        if (
            extensions is not None
            and file.suffix.lower() not in extensions
        ):
            continue

        if (
            name_contains is not None
            and name_contains not in file.name
        ):
            continue

        stat = file.stat()

        if (
            min_size is not None
            and stat.st_size < min_size
        ):
            continue

        if (
            max_size is not None
            and stat.st_size > max_size
        ):
            continue

        try:
            owner = file.owner()
        except Exception:
            owner = getpass.getuser()

        records.append(
            {
                "name_full": file.absolute(),
                "path": file.parent,
                "name": file.name,
                "suffix": file.suffix,
                "size": stat.st_size,
                "created": datetime.fromtimestamp(
                    stat.st_ctime
                ),
                "modified": datetime.fromtimestamp(
                    stat.st_mtime
                ),
                "owner": owner,
            }
        )

    return pd.DataFrame(records)


# %% [markdown]
# Test the function.


# %%
folder_path = "../../../"

files = get_files_info(
    folder_path,
    include_subfolders=True,
    extensions=["py", "parquet"],
)

files


# %% [markdown]
# Print the five largest files.


# %%
files.sort_values(
    "size",
    ascending=False,
).head(5)


# %% [markdown]
# Print the five most recently modified files.


# %%
files.sort_values(
    "modified",
    ascending=False,
).head(5)


# %% [markdown]
# Find the count of each file type.


# %%
files["suffix"].value_counts()