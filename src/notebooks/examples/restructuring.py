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
# # Pivoting data in pandas
#
# Pivoting means changing the shape of the data:
#
# - long format → wide format
# - wide format → long format
#
# This is very common in statistics production:
#
# - tables for reporting
# - preparation before analysis
# - data validation
# - production of statistical datasets

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Example data (long format)
#
# This is often the best format for analysis

# %%
df = pd.DataFrame(
    {
        "municipality": ["Oslo", "Oslo", "Oslo", "Oslo", "Oslo", "Oslo", "Bergen", "Bergen"],
        "year": [2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024],
        "gender": ["F", "F", "M", "F", "M", "M", "M", "M"],
        "income": [500000, 520000, 400000, 350000, 700000, 650000, np.nan, 470000],
        "tax": [200000, 200000, 130000, 110000, np.nan, 270000, 150000, 170000],
    }
)

df

# %% [markdown]
# Here we have:
#
# multiple rows per combination of: municipality + year + gender

# %% [markdown]
# ## `.T` (transpose)
#
# Flips rows and columns

# %%
df.T

# %% [markdown]
# Useful together with e.g. `describe`, since it can produce many columns

# %%
df.groupby("municipality").describe()

# %% [markdown]
# After restructuring, the table becomes more readable

# %%
df.groupby("municipality").describe().T

# %% [markdown]
# Often used for:
#
# - quick checks in notebooks
# - small tables
# - debugging
#
# Not commonly used in production code

# %% [markdown]
# ## `pivot()`
#
# Creates wide format
#
# Requires that the combination of values in the columns defined in `index` and `columns` is unique.
# That is not the case here, so we choose to aggregate first.

# %%
df_agg = df.groupby(["municipality", "gender", "year"], as_index=False).agg(
     income=("income", "sum"),
     tax=("tax", "sum")
)
df_agg

# %% [markdown]
# Now we can pivot by municipality and gender

# %%
pivot_df = df_agg.pivot(
    index=["municipality", "gender"], 
    columns="year", 
    values="income"
)

pivot_df

# %% [markdown]
# Result:
#
# - one row per municipality and gender
# - one column per year

# %% [markdown]
# Important:
#
# If multiple rows share the same combination of index + columns, `pivot()` will fail

# %% [markdown]
# We can pivot multiple columns; column names will then get a MultiIndex

# %%
pivot_df = df_agg.pivot(index=["municipality", "gender"], columns="year", values=["income", "tax"])

print(pivot_df.columns)
pivot_df

# %% [markdown]
# ## `pivot_table()`
#
# Like pivot(), but can also aggregate. Now the combination of index and columns does not have to be unique.
# We perform both aggregation and pivoting in one operation.

# %%
pivot_table_df = df.pivot_table(
    index="municipality", columns="year", values=["income", "tax"], aggfunc="sum"
)

pivot_table_df

# %% [markdown]
# Common aggfunc:
#
# - sum
# - mean
# - count
# - min
# - max

# %% [markdown]
# Example with multiple groups

# %%
pivot_table_df = df.pivot_table(
    index=["municipality", "gender"],
    columns="year",
    values=["income", "tax"],
    aggfunc="sum",
)

pivot_table_df

# %% [markdown]
# Here we see we got MultiIndex column names. We can convert them to regular column names.

# %%
print(pivot_table_df.columns)
pivot_table_df.columns = (
    pivot_table_df.columns.get_level_values(0)
    + "_"
    + pivot_table_df.columns.get_level_values(1).astype("str")
)
pivot_table_df.columns

# %% [markdown]
# Now we can convert the index columns back to regular columns

# %%
pivot_table_df = pivot_table_df.reset_index()
pivot_table_df

# %% [markdown]
# We can also have multiple aggregations. Now we get three levels in the column names.

# %%
pivot_table_df2 = df.pivot_table(
    index=["municipality", "gender"],
    columns="year",
    values=["income", "tax"],
    aggfunc=["sum", "mean"],
)

pivot_table_df2

# %%
print(pivot_table_df2.columns)
pivot_table_df2.columns = (
    pivot_table_df2.columns.get_level_values(1)
    + "_"
    + pivot_table_df2.columns.get_level_values(0)
    + "_"
    + pivot_table_df2.columns.get_level_values(2).astype("str")
)
pivot_table_df2.columns

# %% [markdown]
# ## `melt()`
#
# Goes from wide format to long format

# %%
long_df = pivot_table_df.melt(id_vars=["municipality", "gender"], var_name="variable_year", value_name="value")

long_df

# %% [markdown]
# Result:
#
# - fewer columns
# - more rows

# %% [markdown]
# Typical use:
#
# before groupby
# before visualization
# before modeling

# %% [markdown]
# Should split variable_year into two columns

# %%
long_df["variable"] = long_df["variable_year"].str.split("_").str[0]
long_df["year"] = long_df["variable_year"].str.split("_").str[1]
long_df.drop(columns="variable_year", inplace=True)
long_df

# %% [markdown]
# ## `wide_to_long()`
#
# Specialized tool for reshaping from wide to long format

# %%
long_df2 = pd.wide_to_long(
    pivot_table_df, stubnames=["income", "tax"], i=["municipality", "gender"], j="year", sep="_"
).reset_index()

long_df2

# %% [markdown]
# Used when column names follow a clear pattern:
#
# - income_2023
# - income_2024
# - income_2025
# - tax_2023
# - tax_2024
# - tax_2025

# %% [markdown]
# ## `unstack()`
#
# `unstack()` requires a unique index.
#
# If we have duplicates, we must aggregate first.
#
# The combination:
#
# - municipality
# - year
# - gender
#
# is not unique in our test data

# %%
df.groupby(
    ["municipality", "year", "gender"]
).size()

# %% [markdown]
# We see that Oslo + 2023 + M and Oslo + 2024 + F appear twice

# %% [markdown]
# ### This causes `unstack()` to fail

# %%
table = df.set_index(
    ["municipality", "year", "gender"]
)
table.unstack()

# %% [markdown]
# Typical error:
#
# ValueError:
# Index contains duplicate entries, cannot reshape

# %% [markdown]
# Solution: aggregate first.
#
# Here, the grouped columns become indices, which is required to use `stack` and `unstack`

# %%
agg_df = df.groupby(
    ["municipality", "year", "gender"]
).agg(
    income=("income", "sum"),
    tax=("tax", "sum")
)

agg_df

# %% [markdown]
# Now the index is unique

# %%
agg_df.index.is_unique

# %% [markdown]
# ### `unstack()` works when the index is unique

# %%
agg_df.unstack()

# %% [markdown]
# The innermost level (`gender`) moves to columns

# %%
agg_df.unstack().unstack()

# %% [markdown]
# The two innermost levels move to columns

# %% [markdown]
# Can also be written like this for clarity

# %%
agg_df.unstack(level=["gender", "year"])

# %% [markdown]
# The two innermost levels (`gender` and `year`) move to columns

# %% [markdown]
# ### Select level explicitly

# %%
agg_df.unstack(level="year")

# %% [markdown]
# We choose the order of levels in the columns ourselves

# %%
agg_df_ay = agg_df.unstack(level=["year", "gender"])
agg_df_ay

# %% [markdown]
# ### The result gets MultiIndex columns

# %%
wide = agg_df.unstack(level="municipality")
wide

# %%
wide.columns

# %% [markdown]
# Multiple levels in columns are common after unstack

# %% [markdown]
# ## `stack()`
#
# Moves column levels back to the index

# %%
wide.stack(future_stack=True)

# %% [markdown]
# We are back to long format

# %% [markdown]
# ### Get back a DataFrame

# %%
wide.stack(future_stack=True).reset_index()

# %% [markdown]
# Multiple levels in a stack

# %%
agg_df_ay.stack(level=['year', 'gender'], future_stack=True)

# %% [markdown]
# ### Relationship with `pivot_table()`
#
# `pivot_table()` essentially performs:
#
# - groupby()
# - agg()
# - unstack()
#
# in one operation

# %%
pivot_df = df.pivot_table(
    index=["municipality", "gender"],
    columns="year",
    values="income",
    aggfunc="sum"
)

pivot_df

# %% [markdown]
# `pivot_table()` automatically handles duplicates

# %% [markdown]
# ### Missing values

# %%
agg_df.unstack()

# %% [markdown]
# Missing values remain as NaN

# %% [markdown]
# ## Comparison

# %% [markdown]
# `pivot()`
#
# - long → wide
# - no aggregation
# - requires unique combinations

# %% [markdown]
# `pivot_table()`
#
# - long → wide
# - with aggregation
# - allows duplicates

# %% [markdown]
# `melt()`
#
# - wide → long
# - result often needs further processing

# %% [markdown]
# `wide_to_long()`
#
# - wide → long
# - best when names follow a pattern

# %% [markdown]
# `unstack()`
#
# - index → columns
# - makes the table wider

# %% [markdown]
# `stack()`
#
# - columns → index
# - makes the table longer

# %% [markdown]
# `pivot()` and `melt()`
#
# are often simpler for common tasks

# %% [markdown]
# `stack()` and `unstack()`
#
# are especially useful with MultiIndex data

# %% [markdown]
# `.T`
#
# - transpose
# - mainly for inspection

# %% [markdown]
# ## Summary

# %% [markdown]
# - Long format is often best for analysis
# - Wide format is often best for reporting
# - `pivot_table()` is more robust and flexible than `pivot()`
# - `unstack()` requires a unique index
# - use groupby + agg first if duplicates exist
# - `pivot_table()` is often easier
# - `stack()` and `unstack()` are very useful with MultiIndex data
# - `stack()` and `unstack()` are often used after groupby()
# - `reset_index()` is often useful after stack()
# - MultiIndex can be hard to read
# - Check `.index` and `.columns`
