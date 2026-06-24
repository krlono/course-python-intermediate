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
# # Missing values in Python and pandas
#
# Missing values are values that are absent or unknown.
#
# This is very common in data processing:
# - missing income
# - unknown date of birth
# - empty text value
# - missing category
#
# It is important to understand the difference between:
# - actual missing value
# - empty string ("")
# - whitespace (" ")
# - zero value (0)

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Different types of missing values

# %% [markdown]
# ### np.nan
#
# Standard missing value for numeric data

# %%
np.nan

# %% [markdown]
# ### None
#
# Python’s general "no value"
#
# Often used in lists, dictionaries,
# and object columns

# %%
None

# %% [markdown]
# ### NaT
#
# "Not a Time"
#
# Missing value for date/time in pandas

# %%
pd.NaT

# %% [markdown]
# ### pd.NA
#
# Newer pandas missing value
#
# Often used with nullable data types
# such as string, Int64, and boolean

# %%
pd.NA

# %% [markdown]
# ## Important
#
# These may look similar,
# but behave slightly differently

# %%
type(np.nan), type(None), type(pd.NaT), type(pd.NA)

# %% [markdown]
# ## Example data

# %%
df = pd.DataFrame(
    {
        "name": ["Anna", "", None, "Per", " \t\n "],
        "birth_date": ["2020-01-01", None, "2021-05-10", "", "2023-02-29"],
        "income": [100, 200, np.nan, 400, pd.NA],
        "group": ["A", pd.NA, None, "B", "A"],
    }
)

df

# %% [markdown]
# ## Convert date

# %%
df["birth_date"] = pd.to_datetime(df["birth_date"], errors="coerce")

df

# %% [markdown]
# `errors="coerce"` means:
#
# invalid values are converted to `NaT`

# %% [markdown]
# ## How missing values are handled by data type

# %%
df.dtypes

# %% [markdown]
# Typical behavior:
#
# - numeric → `NaN`
# - date → `NaT`
# - text → `None` / `NaN` / `pd.NA`
# - category → `NaN`

# %% [markdown]
# ## String: blank, empty string, and missing

# %%
df["name"]

# %% [markdown]
# Difference:
#
# - `""` → empty string (not missing)
# - `" "` → whitespace (not missing)
# - `None` → missing
# - `np.nan` → missing

# %% [markdown]
# `isna()` only detects true missing values

# %%
df["name"].isna()

# %% [markdown]
# This means:
#
# - `""` is NOT considered missing
# - `" "` is NOT considered missing

# %% [markdown]
# ## Convert empty strings to missing

# %%
df["name_clean"] = df["name"].replace("", np.nan)

df["name_clean"].isna()

# %% [markdown]
# ## Also remove whitespace

# %%
df["name_clean2"] = df["name"].str.strip().replace("", np.nan)

df["name_clean2"]

# %% [markdown]
# This captures:
#
# - `""`
# - `" "`
# - `"   "`

# %% [markdown]
# ## Finding missing values

# %% [markdown]
# Entire dataset

# %%
df.isna()

# %% [markdown]
# Non-missing

# %%
df.notna()

# %% [markdown]
# Number of missing per column

# %%
df.isna().sum()

# %% [markdown]
# Share of missing per column

# %%
df.isna().mean()

# %% [markdown]
# ## Filtering on missing values

# %% [markdown]
# Rows with missing income

# %%
df[df["income"].isna()]

# %% [markdown]
# Rows without missing income

# %%
df[df["income"].notna()]

# %% [markdown]
# ## `fillna()`

# %% [markdown]
# Replace missing values with a fixed value

# %%
df["income_fill"] = df["income"].fillna(0.0)
df["name_fill"] = df["name_clean2"].fillna("NN")
df

# %% [markdown]
# Text

# %%
df["name_fill"] = df["name"].fillna("Unknown")

df

# %% [markdown]
# Date

# %%
df["birth_date_fill"] = df["birth_date"].fillna(pd.Timestamp("2000-01-01"))

df

# %% [markdown]
# ## Forward and backward filling

# %%
df["income_ffill"] = df["income"].ffill()
df["income_bfill"] = df["income"].bfill()

df

# %% [markdown]
# - `ffill()` → uses the previous value
# - `bfill()` → uses the next value

# %% [markdown]
# ## `dropna()`

# %% [markdown]
# Remove rows with missing values

# %%
df.dropna()

# %% [markdown]
# Remove only if income is missing

# %%
df.dropna(subset=["income"])

# %% [markdown]
# ## Missing in category

# %%
df["group"] = df["group"].astype("category")

df["group"]

# %% [markdown]
# Missing values still exist

# %%
df["group"].isna()

# %% [markdown]
# ## Missing in lists

# %%
values = [1, 2, None, 4]

values

# %% [markdown]
# Find missing values

# %%
[v is None for v in values]

# %% [markdown]
# `None` is often used in standard Python lists

# %% [markdown]
# ## Missing in dictionaries

# %%
person = {"name": "Anna", "income": None}

person

# %% [markdown]
# Check missing

# %%
person["income"] is None

# %% [markdown]
# Important:
#
# A missing key
# is not the same as `None`

# %%
person.get("age")

# %% [markdown]
# `age` does not exist
#
# `income` exists, but is missing

# %% [markdown]
# ## Important domain question
#
# What does missing mean?
#
# - unknown value?
# - not relevant?
# - actual zero?
#
# This must be evaluated conceptually,
# not just technically

# %% [markdown]
# ## Tips
#
# - Check for missing values early in your analysis
# - Do not use `fillna(0)` automatically
# - Distinguish between blank text and true missing
# - Be especially careful with dates and categories
