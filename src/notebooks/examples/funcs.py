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
# ## What is a function?
#
# A function is a reusable block of code that performs a specific task.
#
# You give it input (parameters), and it can return a result.
#
# Advantages:
# - Avoids duplication of code
# - Makes code easier to read because function names are self-documenting
# - Makes it easier to test and maintain

# %%
import os
import pandas as pd


# %%
def double_value(x):
    return 2*x

# %%
double_value(10)

# %%
def multiply_values(a, b):
    print(a*b)

# %%
multiply_values(3, 10)

# %% [markdown]
# ### Example from the course
# It should be imported from `"src/functions/"`, but is written explicitly here:

# %%
def read_pq(folder, filename):
    pq_file = f'{folder}{filename}.parquet'
    df = pd.read_parquet(pq_file)
    print(f'{df.shape[0]} rows and {df.shape[1]} columns read from {pq_file}')
    return df

# %%
local_user_folder = os.environ["USERPROFILE"] 
project_name = 'course-python-intermediate'
working_folder = f'{local_user_folder}/{project_name}/data/input/'

# %%
lcs_survey = read_pq(
    folder=working_folder, 
    filename='lcs_survey_2023'
)
lcs_survey


# %% [markdown]
# ### Why use a function here?
#
# Instead of writing this every time:
#
# ```
# survey_data = pd.read_parquet(survey_file)
# print(f'{survey_data.shape[0]} rows and {survey_data.shape[1]} columns read from {survey_file}')
# ```
#
# we put the logic inside a function.
#
# Advantages:
# - Can be reused in multiple places
# - Keeps logic in one place
# - Easier to modify and maintain later

# %% [markdown]
# ### When should you create a function?
#
# Typical cases:
#
# - When you do the same thing multiple times
# - When the code starts getting long or hard to read
# - When you want to give a clear name to an operation
#

# %% [markdown]
# ### Tips
#
# - Give functions descriptive names (verb + what it does)
# - Keep them small and simple
# - Avoid making them do too many things at once

# %% [markdown]
# ## Naming functions
#
# In Python, there is no required "standard prefix".
# The most important thing is that the name describes what the function does.

# %% [markdown]
# ### Common style (Python / PEP 8)
#
# - snake_case (lowercase with underscores)
# - verb first (what does the function do?)

# %% [markdown]
# ### Common patterns (not rules)
#
# These are often used to improve readability:

# %%
# is_ / has_ → returns True/False
def is_valid(filename): ...

def has_data(df): ...

# %%
# create_ / build_ → creates something new
def create_dataframe(files): ...

# %%
# load_ / read_ → read data
def load_data(path): ...

# %%
# save_ / write_ → save data
def save_data(df, path): ...

# %% [markdown]
# ### Rule of thumb
#
# - Start with a verb
# - The name should read like a sentence:
#
#   `read_pq()`
#
# - Avoid unnecessary prefixes if they do not add value
# - Writing good function names is hard, and improves over time

# %% [markdown]
# ## Docstrings
#
# A docstring is a text that describes what a function does.
# It is written as a string (`""" ... """`) right below the function definition.
#
# Docstrings are used for:
# - documentation
# - editor help (hover / autocomplete)
# - making the code easier for others to understand

# %%
# Note that double_value from earlier is overwritten here:
def double_value(x):
    """Returns twice the value of x."""
    return 2 * x

# %%
# The docstring can be retrieved like this:
print(double_value.__doc__)

# %% [markdown]
# Or by clicking on the function name and pressing `SHIFT + TAB` in JupyterLab.

# %%
double_value(5)

# %%
# ### Example with more details

def multiply_values(a, b):
    """
    Multiplies two numbers.

    Parameters:
        a (int | float): First number
        b (int | float): Second number

    Returns:
        int | float: The product of a and b

    Example:
        print(multiply(3, 5))
        >> 15
    """
    return a * b

# %% [markdown]
# ### Why use docstrings?
#
# - Makes functions easier to understand without reading all the code
# - Useful when sharing code with others
# - Important in larger projects and libraries

# %% [markdown]
# ### Tips
#
# - Write at least one short sentence describing what the function does
# - Describe input and output if the function is more advanced
# - Keep it simple — don’t write more than necessary

# %% [markdown]
# ## Type hints
#
# Type hints are used to show what types a function expects
# and what it returns.
#
# They do not affect how the code runs, but make it easier to understand
# and provide better help in editors like VSCode.

# %%
def double_value(x: int) -> int:
    return 2 * x

# %%
def multiply_values(a: int, b: int) -> int:
    return a * b

# %% [markdown]
# ### Example with type hints and docstring
# Every function should have a docstring which is a documentation of what the function do and an explanation of the arguments. It should also have type hints to show what instance the arguments shall have. Furthemore, some examples on how to use the function will always enhance the docstring.

# %%
import pandas as pd


def read_pq(folder: str, filename: str) -> pd.DataFrame:
    """
    Read a Parquet file into a pandas DataFrame.

    The function constructs the file path from `folder` and `filename`,
    reads the Parquet file, prints its dimensions, and returns the
    resulting DataFrame.

    Parameters
    ----------
    folder : str
        Folder containing the Parquet file. Include the path separator
        at the end, e.g. ``"data/"``.
    filename : str
        Name of the Parquet file without the ``.parquet`` extension.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the data read from the Parquet file.

    Examples
    --------
    >>> persons = read_pq("data/", "persons_2025")
    1250 rows and 15 columns read from data/persons_2025.parquet

    >>> households = read_pq("data/", "households_2025")
    500 rows and 14 columns read from data/households_2025.parquet
    """
    pq_file = f"{folder}{filename}.parquet"
    df = pd.read_parquet(pq_file)
    print(f"{df.shape[0]} rows and {df.shape[1]} columns read from {pq_file}")
    return df

# %%
population = read_pq(
    folder=working_folder, 
    filename='population_2023'
)

# %% [markdown]
# ### What does this mean?
#
# - `filename: str`
#     - filename is expected to be a string
# - `-> pd.DataFrame`
#     - the function returns a Pandas dataframe
# - `bool`, `str`, `float`, `int`, `pd.Series` are also commonly used

# %%
# ## More types

from math import isqrt


def is_prime(number: int) -> bool:
    """Check whether an integer is a prime number."""
    if number < 2:
        return False

    # isqrt (integer square root) returns the whole-number square root, rounded down.
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            return False

    return True

# %%
primes = []
start = 100000
end = 100100 
for x in range(start,end+1):
    if is_prime(x):
        primes.append(x)
print(f'Prime numbers from {start} to {end}: {primes}')


# %%
# Lists:
def sum_list(values: list[int]) -> int:
    return sum(values)


# %%
incomes = [100, 300, 500, 900]
sum_list(incomes)

# %% [markdown]
# ### Important to remember
#
# - Python does not enforce types automatically
# - It is only guidance (for you and others)
#
# But:
# - Editors can give warnings
# - The code becomes more readable by clearly stating what is expected
#
# Is `adults` a list, a dataset, or a column name?
# This can be clarified with:
#
# `adults: list[str] = ["Peter", "Jane", "Siri"]`

# %% [markdown]
# ### Tips
#
# - Use type hints in functions
# - Don’t overcomplicate
# - Start with simple types (int, str, list) and expand as needed
