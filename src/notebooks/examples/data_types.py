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
# # Data types in Python and pandas
#
# Data types tell Python what kind of value something is.
#
# Examples:
# - numbers
# - text
# - date
# - boolean (True/False)
#
# The correct data type is important because:
# - calculations are correct
# - filtering works properly
# - groupby and merge become safer
# - code becomes faster and more robust

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Common data types in Python

# %% [markdown]
# ### int
#
# Integer

# %%
age = 35
type(age)

# %% [markdown]
# Used for:
# - number of persons
# - year
# - IDs (often, but not always)

# %% [markdown]
# ### float
#
# Decimal number

# %%
income = 523000.50
type(income)

# %% [markdown]
# Used for:
# - income
# - percentages
# - averages
# - calculations with missing values (NaN)

# %% [markdown]
# ### str
#
# Text

# %%
name = "Anna"
type(name)

# %% [markdown]
# Used for:
# - names
# - municipality names
# - categories
# - file paths

# %% [markdown]
# ### bool
#
# True / False

# %%
active = True
type(active)

# %% [markdown]
# Used for:
# - filters
# - rules
# - yes/no variables

# %% [markdown]
# ### NoneType
#
# No value

# %%
type(None)

# %% [markdown]
# Often used as missing in Python

# %% [markdown]
# ## Lists and dictionaries

# %% [markdown]
# ### list
#
# Multiple values in sequence

# %%
columns = ["id", "name", "income"]
type(columns)

# %% [markdown]
# Often used for:
# - column names
# - files
# - values to loop over

# %% [markdown]
# ### tuple
#
# Like a list, but cannot be changed

# %%
pair = ("Oslo", "Bergen")
type(pair)

# %% [markdown]
# ### set
#
# Unique values

# %%
unique = {"A", "B", "A"}
print(unique)
type(unique)

# %% [markdown]
# Used for:
# - removing duplicates
# - comparing columns

# %% [markdown]
# ### dict
#
# Key + value

# %%
mapping = {"A": "Oslo", "B": "Bergen"}

type(mapping)

# %% [markdown]
# Often used for:
# - mapping
# - renaming
# - configuration

# %% [markdown]
# ## Data types in pandas

# %%
df = pd.DataFrame(
    {
        "age": [30, 45, 28],
        "income": [500000, 650000, 420000],
        "name": ["Anna", "Per", "Ola"],
        "active": [True, False, True],
        "date": ["2024-01-01", "2024-02-15", "2024-03-10"],
    }
)

df

# %% [markdown]
# ## View data types

# %%
df.dtypes

# %% [markdown]
# This is one of the first things we should check

# %% [markdown]
# ## Convert data type

# %% [markdown]
# ### Date

# %%
df["date"] = pd.to_datetime(df["date"])

df.dtypes

# %% [markdown]
# Now we can use:
# - `.dt.year`
# - filtering by date
# - time calculations

# %% [markdown]
# ### Category
#
# Useful for groups with few unique values

# %%
df["name"] = df["name"].astype("category")

df.dtypes

# %% [markdown]
# Often used for:
# - gender
# - municipality
# - region
# - status

# %% [markdown]
# ### String

# %%
df["name"] = df["name"].astype("string")

df.dtypes

# %% [markdown]
# Often better than object

# %% [markdown]
# ## Important: object
#
# object often means:
# "pandas is not entirely sure"

# %%
df["mixed"] = [1, "A", None]

df.dtypes

# %% [markdown]
# object often needs further inspection

# %% [markdown]
# ## Common mistakes

# %% [markdown]
# Numbers stored as text

# %%
df2 = pd.DataFrame({"income": ["100", "200", "300"]})

df2.dtypes

# %% [markdown]
# This causes problems when summing

# %%
df2["income"].sum()

# %% [markdown]
# Must convert to numeric first:

# %%
df2["income"] = pd.to_numeric(df2["income"])

df2["income"].sum()

# %% [markdown]
# ## Boolean filtering

# %%
df["income"] > 500000

# %% [markdown]
# The result is a boolean series:
# True / False

# %% [markdown]
# ## Data types and missing values
#
# Missing values affect data types:
#
# int + missing → often becomes float
#
# because NaN is float-based

# %%
s = pd.Series([1, 2, np.nan])

s.dtype

# %% [markdown]
# Alternative:
# nullable integer

# %%
s = pd.Series([1, 2, pd.NA], dtype="Int64")

s.dtype

# %% [markdown]
# ## When to use what?

# %% [markdown]
# - int → integers
# - float → decimals
# - str/string → text
# - bool → yes/no
# - datetime → date/time
# - category → few unique groups
# - dict → mapping
# - list → multiple values

# %% [markdown]
# ## Tips

# %% [markdown]
# - Always check `df.dtypes`
# - Convert dates early
# - Avoid unnecessary object types
# - Use category for grouped data
# - Watch out for numbers stored as text

# %% [markdown]
# ## Checking data types with isinstance()
#
# `type()` tells what data type something has.
#
# `isinstance()` is often used when we want to check:
#
# "Is this value a specific type?"
#
# This is often more practical in functions and validation.

# %% [markdown]
# ### Simple examples

# %%
age = 35
isinstance(age, int)

# %%
name = "Anna"
isinstance(name, str)

# %%
income = 523000.50
isinstance(income, float)

# %%
active = True
isinstance(active, bool)

# %% [markdown]
# ### Multiple types at once
#
# Useful if both int and float should be accepted

# %%
value = 100

isinstance(value, (int, float))

# %% [markdown]
# This means:
#
# Is value either int OR float?

# %% [markdown]
# ### Example in a function

# %%
def double_value(x):
    if isinstance(x, (int, float)):
        return x * 2
    return f"Must be a number, currently {type(x)}"

# %%
double_value(10)

# %%
double_value("10")

# %% [markdown]
# ### Example with lists

# %%
values = [1, "2", None, 4]

[isinstance(v, int) for v in values]

# %% [markdown]
# ### Example with dictionaries

# %%
person = {"name": "Anna", "income": 500000}

isinstance(person, dict)

# %% [markdown]
# ### In pandas
#
# We often check entire columns with `df.dtypes`,
# but sometimes we want to check individual values

# %%
df = pd.DataFrame({
    "income": [100, 200, 300],
    "tax": [33, 87, '131']
})
print(df.dtypes)

df

# %%
first_income = df.loc[0, "income"]
first_tax = df.loc[0, "tax"]
string_tax = df.loc[2, "tax"]

print(type(first_income))
print(isinstance(first_income, (int, float, np.int64)))

print(type(first_tax))
print(isinstance(first_tax, (int, float, np.int64)))

print(type(string_tax))
isinstance(string_tax, (int, float, np.int64))

# %% [markdown]
# Note:
#
# pandas often uses its own types such as:
# - numpy.int64
# - numpy.float64
#
# so results may vary slightly

# %% [markdown]
# ### Robust solution in pandas

# %%
import numpy as np

isinstance(first_income, (int, float, np.integer, np.floating))

# %% [markdown]
# This is often safer in data work

# %% [markdown]
# ## Tips
#
# - Use `type()` to inspect data types
# - Use `isinstance()` for logic and validation
# - `isinstance()` is often better than `type() == ...`
