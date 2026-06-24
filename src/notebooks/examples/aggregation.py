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
# # Aggregating data with groupby()
#
# `groupby()` is used when we want to group data by the values in one or more columns.
#
# Typical examples:
# - total income per household
# - number of persons per household
# - average age by gender
#
# This is one of the most commonly used operations in data processing with pandas.

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Example data

# %%
df = pd.DataFrame(
    {
        "hh": ["1", "1", "1", "2", "2", "3", "3", "4", "4", "4"],
        "person": ["1", "2", "3", "1", "2", "1", "2", "1", "2", "3"],
        "income": [100, 200, np.nan, 300, np.nan, np.nan, np.nan, 400, 0, 150],
        "age": [54, 50, 16, 30, 28, 66, 72, 26, 0, np.nan],
        "sex": ["1", "2", "2", "1", np.nan, "", "2", "1", "1", "9"],
    }
)

df

# %% [markdown]
# ## Aggregation into a new DataFrame
# One row is created for each value of the column(s) specified in groupby.
# The aggregated columns keep the names of the original columns

# %%
agg_df = df.groupby("hh").agg({"income": "sum", "age": "mean"})

agg_df

# %% [markdown]
# Result:
# - sum of income per household
# - average age per household

# %% [markdown]
# ## as_index=False
#
# groupby() uses the grouping column(s) as the index unless specified otherwise.
#
# Often we want regular columns instead of an index. Then we use `as_index=False`.

# %%
agg_df = df.groupby("hh", as_index=False).agg({"income": "sum"})

agg_df

# %% [markdown]
# This is often easier to work with later in the pipeline

# %% [markdown]
# ## Adding aggregates to each row in a DataFrame
# We add the aggregates to each row within the respective groups

# %%
df['income_hh'] = df.groupby("hh")["income"].transform("sum")
df

# %% [markdown]
# ## Multiple aggregates at the same time
# The example below gives MultiIndex columns, which can be cumbersome to work with.
#
# The next example produces regular column names.
#
# Note that `count` does not include missing values (NaN)

# %%
agg_df = df.groupby("hh", as_index=False).agg(
    {
        "income": ["sum", "mean", "count"], 
        "age": ["mean", "max"]
    }
)

agg_df

# %%
agg_df.columns

# %%
agg_df = df.groupby("hh", as_index=False).agg(
    income_sum=("income", "sum"),
    income_mean=("income", "mean"),
    income_count=("income", "count"),
    age_mean=("age", "mean"),
    age_max=("age", "max"),
)

agg_df

# %%
agg_df.columns

# %% [markdown]
# We can group by multiple columns, specifying them as a list.
# Also, if we only need one aggregated column, we can specify the function directly without using agg.

# %%
agg_df = df.groupby(["hh", "sex"], as_index=False)["age"].mean()
agg_df

# %% [markdown]
# ## Missing values (NaN)
#
# Many aggregation functions automatically skip NaN values:
#
# - sum()
# - mean()
# - min()
# - max()
# - count()
#
# Important difference:
#
# - count() → counts only non-missing values
# - size()  → counts all rows, including NaN

# %%
df.groupby("hh", as_index=False).agg(
    sum_income=("income", "sum"),
    mean_income=("income", "mean"),
    count_income=("income", "count"),
    size_income=("income", "size"),
)

# %% [markdown]
# Missing values are not a function themselves,
# but we can count them using a lambda function.
#
# We can also compute the share of missing values by taking the mean,
# since `isna()` returns True (1) or False (0).
# The average gives the share of missing values.
#
# We can also compute shares of specific values,
# for example the share of males, as shown below.

# %%
df.groupby("hh", as_index=False).agg(
    income_count=("income", "count"),
    income_size=("income", "size"),
    income_missing=("income", lambda x: x.isna().sum()),
    income_missing_share=("income", lambda x: x.isna().mean()),
    male_share=("sex", lambda x: (x == "1").mean()),
)

# %% [markdown]
# ## Missing values and calculations within groups
#
# Missing values (NaN) can lead to very different results,
# depending on how they are handled.
#
# This is especially important when calculating shares within groups,
# for example income share per person in a household.

# %% [markdown]
# Interpretation:
#
# - hh = 1 → one missing value
# - hh = 2 → one missing value
# - hh = 3 → all values are missing
# - hh = 4 → all values are present

# %% [markdown]
# ### Variant 1
# Standard behavior:
# - sum() ignores NaN in the denominator
# - but the numerator retains NaN

# %%
df["income_share1"] = df.groupby("hh")["income"].transform(lambda x: x / sum(x))

df

# %% [markdown]
# Result:
#
# - Only households with complete data get calculated shares
# - At least one missing value leads to missing results

# %% [markdown]
# ### Variant 2
#
# fillna(0) only in the denominator

# %%
df["income_share2"] = df.groupby("hh")["income"].transform(
    lambda x: x / sum(x.fillna(0))
)

df

# %% [markdown]
# Result:
#
# - Households with complete data get shares
# - Members with income get shares
# - Members without income remain missing

# %% [markdown]
# ### Variant 3
#
# fillna(0) in both numerator and denominator

# %%
df["income_share3"] = df.groupby("hh")["income"].transform(
    lambda x: x.fillna(0) / sum(x.fillna(0))
)

df

# %% [markdown]
# Now missing values are interpreted as 0 income
#
# hh=1:
# the third person gets share 0 instead of NaN

# %% [markdown]
# ### Variant 4
#
# Handles cases where the entire group has missing values

# %%
df["income_share4"] = df.groupby("hh")["income"].transform(
    lambda x: (x.fillna(0) / sum(x.fillna(0))).fillna(0)
)

df

# %% [markdown]
# Important for hh=3:
#
# Without this:
# 0 / 0 → results in NaN or incorrect logic
#
# With this:
# the entire group gets 0

# %% [markdown]
# ## Comparison
#
# income_share1
#
# - NaN is preserved
# - default pandas behavior
#
# income_share2
#
# - groups with some missing values also get shares
#
# income_share3
#
# - NaN is treated as 0
# - useful if missing means "no income"
#
# income_share4
#
# - robust version of variant 3
# - handles groups where total = 0

# %% [markdown]
# ## Important clarification
#
# What does missing mean?
#
# - unknown value? → keep NaN or impute if possible
#
# or
#
# - actual 0? → use fillna(0)
#
# This is a domain-specific decision, not just a technical one.

# %% [markdown]
# ## Tips
#
# Do not use fillna(0) automatically.
#
# First understand what missing values actually represent.
#
# This determines whether the result is correct or incorrect.

# %% [markdown]
# ## transform()
#
# transform() is used when we want to:
#
# - compute something per group
# - but keep the same number of rows
#
# In other words:
# groupby().agg() → new dataset
# groupby().transform() → new column in the same dataset

# %% [markdown]
# ## Add average household income to each row

# %%
df["mean_hh"] = df.groupby("hh")["income"].transform("mean")

df

# %% [markdown]
# ## Calculate deviation from group mean

# %%
df["deviation_from_mean"] = df["income"] - df["mean_hh"]

df

# %% [markdown]
# ## Share of total within each group calculated by first creating sum as a separate column

# %%
df["sum_hh"] = df.groupby("hh")["income"].transform("sum")

df["share"] = df["income"] / df["sum_hh"]

df

# %% [markdown]
# ## Share of total within each group and deviation from mean calculated directly

# %%
df["share_direct"] = df.groupby("hh")["income"].transform(lambda x: x / sum(x.fillna(0)))
df["deviation_from_mean_direct"] = df.groupby("hh")["income"].transform(lambda x: x - x.mean())
df

# %% [markdown]
# ## Comparison
#
# agg()
#
# - collapses rows with the same values in grouped columns
# - aggregates columns using aggregation functions
# - fewer rows
# - new dataset
#
# transform()
#
# - equivalent to aggregating first and then merging back
# - aggregates per group
# - returns same number of rows
# - creates a new column in the existing dataset

# %% [markdown]
# ## Tips
#
# - Use as_index=False in most analyses
# - Remember the difference between count() and size()
# - Use transform() when you need group statistics at row level
