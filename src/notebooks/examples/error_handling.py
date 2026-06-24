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
# # Error Handling in Python
#
# Error handling is about detecting, explaining,
# and stopping errors in a controlled way.
#
# This is important in data processing because:
#
# - files may be missing
# - columns may have the wrong data type
# - data may contain invalid values
# - calculations may produce incorrect results
#
# Good error handling makes code:
#
# - safer
# - easier to debug
# - easier to maintain

# %% [markdown]
# ## The most common errors in data processing
#
# - ValueError
# - TypeError
# - KeyError
# - FileNotFoundError
# - ZeroDivisionError
# - IndexError
# - AttributeError
# - NameError
# - PermissionError
# - MemoryError

# %% [markdown]
# ## Examples of common error types

# %% [markdown]
# ### ValueError
#
# The value exists, but is invalid

# %%
int("abc")

# %% [markdown]
# Example:
# text that cannot be converted to a number

# %% [markdown]
# ### TypeError
#
# Wrong data type

# %%
"10" + 5

# %% [markdown]
# Example:
# text + number

# %% [markdown]
# ### KeyError
#
# Key or column does not exist

# %%
import pandas as pd

df = pd.DataFrame({
    "income": [100, 200]
})

df["age"]

# %% [markdown]
# ### FileNotFoundError
#
# The file does not exist

# %%
pd.read_csv("does_not_exist.csv")

# %% [markdown]
# ### ZeroDivisionError
#
# Division by zero

# %%
10 / 0

# %% [markdown]
# ### IndexError
#
# Invalid position in a list

# %%
values = [1, 2, 3]

values[10]

# %% [markdown]
# ### AttributeError
#
# The object does not have this method

# %%
text = "abc"

text.append("d")

# %% [markdown]
# Strings do not have append()

# %% [markdown]
# ### NameError
#
# The variable does not exist

# %%
print(unknown_variable)

# %% [markdown]
# ### ImportError
#
# Python cannot find the package

# %%
import module_does_not_exist

# %% [markdown]
# ### ModuleNotFoundError
#
# Variant of ImportError,
# often for missing libraries

# %%
import completely_unknown_module

# %% [markdown]
# ### PermissionError
#
# Missing access to file/folder

# %% [markdown]
# Typical case:
# trying to write to a protected location

# %% [markdown]
# ### RuntimeError
#
# General runtime error

# %% [markdown]
# Less commonly used directly,
# but may appear in libraries

# %% [markdown]
# ### AssertionError
#
# Error in an assert statement

# %%
assert 2 + 2 == 5

# %% [markdown]
# Often used in testing

# %% [markdown]
# ### StopIteration
#
# No more values in an iterator

# %% [markdown]
# More advanced use,
# often hidden in loops

# %% [markdown]
# ### OverflowError
#
# Number becomes too large

# %% [markdown]
# Less common in normal pandas use

# %% [markdown]
# ### MemoryError
#
# Not enough memory

# %% [markdown]
# Important with large datasets

# %% [markdown]
# ## Tips
#
# Catch specific errors:
#
# Good:
#
# `except ValueError:`
#
# Bad:
#
# `except Exception:`
#
# The more specific the error handling, the easier debugging becomes

# %% [markdown]
# ## `raise` for real errors

# %% [markdown]
# `raise` is used when:
#
# - something is seriously wrong
# - continuing execution makes no sense
# - we want to stop the program

# %%
age = -5

if age < 0:
    raise ValueError(f"Age cannot be negative, given value is {age}")

# %% [markdown]
# Here the program stops immediately

# %% [markdown]
# ## When to use `raise` vs `print`

# %% [markdown]
# Use `print()` when:
#
# - it is just informational
# - the user should be informed
# - the code can continue

# %% [markdown]
# Use `raise` when:
#
# - data is invalid
# - the result would be incorrect
# - execution should stop

# %% [markdown]
# Rule of thumb:
#
# If an incorrect result is worse than stopping,
# use `raise`

# %% [markdown]
# ## Custom checks in functions

# %%
def calculate_share(value, total):
    if total == 0:
        raise ZeroDivisionError(
            "Total cannot be 0"
        )

    return value / total

# %%
calculate_share(100, 200)

# %%
calculate_share(100, 0)

# %% [markdown]
# This is much better than encountering an error later in the process.

# %% [markdown]
# ## Checking columns before use

# %%
required_cols = [
    "income",
    "age"
]

missing_cols = [
    col for col in required_cols
    if col not in df.columns
]

if missing_cols:
    raise KeyError(
        f"Missing columns: {missing_cols}"
    )

# %% [markdown]
# This is very common in production code

# %% [markdown]
# ## `try` / `except`

# %% [markdown]
# Used when we expect
# something might fail,
# and we want to handle it in a controlled way

# %%
try:
    value = int("abc")
except ValueError:
    print("Could not convert to number")

# %% [markdown]
# The program continues

# %% [markdown]
# ## Multiple error types

# %%
try:
    df["age"]
except KeyError:
    print("The column does not exist")

# %% [markdown]
# ## `except Exception`
#
# Catches almost everything,
# but should be used carefully

# %%
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")

# %% [markdown]
# Good for debugging, but often too general for production code

# %% [markdown]
# ## Logging vs print
#
# In larger projects, we often use:
#
# `logging`
#
# instead of:
#
# `print()`
#
# because it provides better control,
# file logging, and traceability

# %% [markdown]
# ## Common errors in data processing

# %% [markdown]
# - missing files
# - incorrect file format
# - missing columns
# - wrong data types
# - duplicates
# - unexpected missing values
# - division by zero
# - merges producing incorrect number of rows

# %% [markdown]
# ## Good practices

# %% [markdown]
# - check inputs early
# - fail fast
# - use clear error messages
# - do not hide errors with print()
# - test edge cases
# - be explicit about what is allowed

# %% [markdown]
# ## Tips
#
# Good error messages save a lot of time.
#
# Good:
#
# `raise ValueError(f"income must be greater than 0, given value is {income}")`
#
# Bad:
#
# `raise ValueError("Error")`
