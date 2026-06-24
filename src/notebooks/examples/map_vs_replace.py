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
# ## map() vs replace() (with dictionary)
#
# Both are often used with a dictionary in data processing,
# but they behave slightly differently.

# %%
import pandas as pd

s = pd.Series(["0301", "4601", "1234", "0301"])

mapping = {"0301": "Oslo", "4601": "Bergen"}

# %% [markdown]
# ## map()
#
# Replaces values based on the dictionary
# Values that are not found → become NaN

# %%
s_map = s.map(mapping)
s_map

# %% [markdown]
# Result:
# "1234" is not found in the dictionary → becomes NaN

# %% [markdown]
# ## replace()
#
# Replaces values that exist in the dictionary
# Values that are not found → remain unchanged

# %%
s_replace = s.replace(mapping)
s_replace

# %% [markdown]
# ## Important difference
#
# map():
# - uses the dictionary as a "lookup"
# - anything not matched → NaN
#
# replace():
# - only performs explicit replacements
# - all other values are kept

# %% [markdown]
# ## When to use what?
#
# Use map() when:
# - you expect all values to be matched
# - you want to detect missing mappings (NaN)
#
# Use replace() when:
# - you only want to change some values
# - and keep the rest as they are

# %% [markdown]
# ## Example: renaming categories
#
# map() (strict):
# - good if you want to validate data
#
# replace() (flexible):
# - good if you only want to update some values
