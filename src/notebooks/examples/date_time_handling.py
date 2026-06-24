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
# ## Date and time in pandas (.dt)
#
# `.dt` is used to extract or work with parts of date/time columns.
#
# Before using `.dt`, the column must be in datetime format.

# %%
import pandas as pd

# %% [markdown]
# ## Example data

# %%
df = pd.DataFrame({"date": ["2024-02-01", "2024-04-15", "2025-06-20"]})

print(df.dtypes)
df

# %% [markdown]
# ## Convert to datetime

# %%
df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
df

# %% [markdown]
# ## Extract parts of the date

# %%
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

print(df.dtypes)
df

# %% [markdown]
# ## Weekday

# %%
df["weekday_num"] = df["date"].dt.weekday  # 0 = Monday
df["weekday_name"] = df["date"].dt.day_name()

df

# %% [markdown]
# ## Filter by year

# %%
df_2024 = df[df["date"].dt.year == 2024]
df_2024

# %% [markdown]
# ## Filter by month

# %%
df_feb = df[df["date"].dt.month == 2]
df_feb

# %% [markdown]
# ## Create period (year-month/quarter)

# %%
df["year_month"] = df["date"].dt.to_period("M")
df["year_quarter"] = df["date"].dt.to_period("Q")

print(df.dtypes)
df

# %% [markdown]
# ## Time differences

# %%
df["next_date"] = df["date"].shift(-1)
df["days_between"] = (df["next_date"] - df["date"]).dt.days
df["next_easter_sunday"] = df["date"] + pd.offsets.Easter()
df

# %% [markdown]
# Avoid the warning above. Be aware that this finds Easter for the given year,
# while the previous example gave the next Easter relative to the input date.

# %%
from dateutil.easter import easter

df["easter_sunday"] = pd.to_datetime(df["date"].dt.year.apply(easter))
df

# %% [markdown]
# ## Important to remember
#
# - `.dt` only works on datetime columns
# - Use `pd.to_datetime()` if you get errors

# %% [markdown]
# ## Common `.dt` attributes
#
# - `.dt.year`
# - `.dt.month`
# - `.dt.day`
# - `.dt.weekday`
# - `.dt.day_name()`
# - `.dt.to_period()`

# %% [markdown]
# ## Tips
#
# - Convert to datetime early in the process
# - Use `.dt` for filtering and grouping

# %% [markdown]
# ## Different string formats for date/time
#
# Dates can appear in many different formats as strings.
# `pd.to_datetime()` can often interpret them automatically,
# but sometimes we need to assist with `format=`.
#
# Examples of different formats:

# %%
df_str = pd.DataFrame({
    "date_str": [
        "2024-02-01",        # ISO format (YYYY-MM-DD)
        "01-02-2024",        # DD-MM-YYYY
        "02/01/2024",        # MM/DD/YYYY (American)
        "2024/02/01 14:30",  # with time
        "1 Feb 2024"         # text format
    ]
})

df_str

# %%
# ## Automatic parsing (may raise error due to mixed formats in the same column)

df_str["date_auto"] = pd.to_datetime(df_str["date_str"])
df_str

# %% [markdown]
# ## When it can go wrong
#
# Some formats are ambiguous, for example:
# - "02/01/2024" → is it 2 January or 1 February?
# - "02.01.24" → is it 2 January 2024 or 24 January 2002?

# %%
# Solution: specify format

df_str["date_formatted"] = pd.to_datetime(
    df_str["date_str"],
    format="%d-%m-%Y",
    errors="coerce"  # returns NaT if parsing fails
)

df_str

# %% [markdown]
# ## Common format codes
#
# - `%Y` → year (2024)
# - `%m` → month (01–12)
# - `%d` → day (01–31)
# - `%H` → hour (00–23)
# - `%M` → minute
#
# Example:
# "15-01-2024 08:30" → "%d-%m-%Y %H:%M"

# %% [markdown]
# ## Tips
#
# - Use standard format (YYYY-MM-DD) if possible
# - If you get errors → try `format=`
# - Use `errors="coerce"` to identify problematic values

# %% [markdown]
# ## Deriving date from a personal identification number
#
# In some datasets, the date is not directly available but can be derived.
# A typical example is a national identification number (11 digits in Norway).
#
# Structure (simplified):
# DDMMYY + the rest
#
# We can extract the birth date from the first 6 digits.

# %%
df_fnr = pd.DataFrame({
    "fnr": [
        "15022412345",  # 15.02.2024 (simplified example)
        "01019954321",  # 01.01.1999
        "31129967890"   # 31.12.1999
    ]
})

df_fnr

# %%
# ## Extract the date part

df_fnr["date_str"] = df_fnr["fnr"].str[:6]

df_fnr

# %%
# ## Convert to datetime
#
# Format: DDMMYY → "%d%m%y"

df_fnr["date"] = pd.to_datetime(
    df_fnr["date_str"],
    format="%d%m%y"
)

df_fnr

# %% [markdown]
# ## Important in practice
#
# - The century is not always unambiguous (1900 vs 2000)
# - In real data, rules are needed to interpret the year correctly
# - Personal ID numbers also contain control digits and individual numbers

# %% [markdown]
# ## Further use
#
# Once converted, we can use `.dt` as usual:

# %%
df_fnr["year"] = df_fnr["date"].dt.year
df_fnr["month"] = df_fnr["date"].dt.month

df_fnr
