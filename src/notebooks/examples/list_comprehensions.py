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
# ## List comprehension
#
# List comprehension is a concise way to iterate over lists.
#
# Instead of using a for-loop with append(),
# you can write it more compactly on a single line.

# %% [markdown]
# ## Standard approach

# %%
numbers = [1, 2, 3, 4]

squares = []
for x in numbers:
    squares.append(x**2)

squares

# %% [markdown]
# ## List comprehension

# %%
squares = [x**2 for x in numbers]

squares

# %% [markdown]
# ## What is happening here?
#
# [expression for element in list]
#
# - x**2 → what we create
# - for x in numbers → what we iterate over

# %% [markdown]
# ## With condition (filter)

# %%
even_squares = [x**2 for x in numbers if x % 2 == 0]
even_squares

# %% [markdown]
# ## Typical use in data processing

# %% [markdown]
# File paths → file names without path

# %%
files = ["data/a.parquet", "data/b.parquet"]

filenames = [file.split("/")[-1] for file in files]

filenames

# %% [markdown]
# Create column names dynamically

# %%
columns = [f"value_{i}" for i in range(5)]

columns

# %% [markdown]
# Convert values

# %%
values = ["1", "2", "3"]

as_int = [int(v) for v in values]

as_int

# %% [markdown]
# ## Comparison
#
# for-loop:
#
# ```
# result = []
# for x in data:
#     result.append(...)
# ```
#
# list comprehension:
#
# `result = [... for x in data]`

# %% [markdown]
# ## When to use list comprehension?
#
# - When the logic is simple
# - When you want shorter and more readable code
#
# Avoid if:
# - the expression becomes long or hard to read

# %% [markdown]
# ## Tips
#
# - Keep it simple (one line, one idea)
# - If it takes effort to understand → use a regular loop

# %% [markdown]
# ## Using zip()
#
# `zip()` is used to iterate over multiple lists simultaneously.
# Think of it like zipping or pairing elements together.
#
# This is useful when you want to combine or process multiple columns/values in parallel.

# %%
names = ["Anna", "Per", "Kari"]
ages = [28, 35, 22]

combined = list(zip(names, ages))

combined

# %% [markdown]
# ## Together with list comprehension

# %%
descriptions = [f"{n} is {a} years old" for n, a in zip(names, ages)]

descriptions

# %% [markdown]
# ## Typical use in data processing
#
# - Combine columns
# - Create new variables based on multiple lists
# - Iterate over multiple data series simultaneously

# %%
# Example: two columns → one new value

prices = [10, 20, 30]
quantities = [1, 3, 2]

total = [p * a for p, a in zip(prices, quantities)]

total

# %% [markdown]
# ## Combine two lists into a dictionary
# Note that the order of the lists is important for this to be correct.

# %%
keys = ["A", "B", "C"]
values = ["Oslo", "Bergen", "Trondheim"]

mapping = {k: v for k, v in zip(keys, values)}
mapping

# %% [markdown]
# ## Important to remember
#
# - zip stops at the shortest list
# - The result is an iterator (can be converted to a list)
