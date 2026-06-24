# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Lists, tuples, and sets
#
# These are three fundamental ways to store multiple values in Python.
#
# They are used all the time in data processing, for example for:
# - column names
# - files
# - values in datasets

# %% [markdown]
# ## List (list)
#
# A list is a collection that:
# - has order
# - can be modified (mutable)
# - can contain duplicates

# %%
columns = ["id", "name", "age", "age"]

# %% [markdown]
# ## Access a value

# %%
first = columns[0]
first

# %% [markdown]
# ## Add a value

# %%
columns.append("income")
columns

# %% [markdown]
# ## Typical use in data processing
#
# - list of files
# - list of columns

# %%
from glob import glob

files = glob("*.py")
files

# %% [markdown]
# ## Tuple
#
# A tuple is:
# - ordered
# - cannot be changed (immutable)
# - can contain duplicates

# %%
column_pair = ("income", "cost")

# %% [markdown]
# Tuples are often used when:
# - values belong together
# - and should not be changed

# %%
# Example: returning multiple values from a function

def get_min_max(df, column):
    return df[column].min(), df[column].max()

# %%
import numpy as np

# Unpacking a tuple
import pandas as pd

df = pd.DataFrame(
    {"id": ["1", "2", "3", "4", "5"], "income": [100, 300, 400, np.nan, 200]}
)
min_value, max_value = get_min_max(df, "income")
min_value, max_value

# %% [markdown]
# ## Set (set)
#
# A set is:
# - unordered
# - contains only unique values
# - used for comparisons

# %%
columns = ["id", "name", "age", "age"]

unique_columns = set(columns)
unique_columns

# %% [markdown]
# ## Typical use in data processing
#
# Remove duplicates:
#
# unique_files = set(files)

# %%
# Find differences between datasets:

columns_df1 = {"id", "name", "age"}
columns_df2 = {"id", "name", "income"}

missing = columns_df1 - columns_df2
missing

# %%
# Common columns:

common = columns_df1 & columns_df2
common

# %% [markdown]
# ## Comparison
#
# - list  → ordered + mutable
# - tuple → ordered + immutable
# - set   → unique values + no order

# %% [markdown]
# ## When to use what?
#
# - list: default choice (most commonly used)
# - tuple: when data should not be modified
# - set: when you need unique values or comparisons

# %% [markdown]
# ## Tips
#
# - Usually use list
# - Convert to set when you need unique values
# - Use tuple for "fixed" groups of values
