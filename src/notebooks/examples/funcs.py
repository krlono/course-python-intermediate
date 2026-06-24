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
# It should be imported from `"src/functions/paths"`, but is written explicitly here:

# %%
def set_use_temp(temporary_run: bool):
    if temporary_run:
        return "/temp"
    return ""

# %%
use_temp = set_use_temp(False)

# %%
type(use_temp)

# %% [markdown]
# ### What is happening here?
#
# - The function takes one value: `temporary_run` (True/False)
# - If it is True → returns "/temp"
# - Otherwise → returns an empty string
#
# The result is stored in the variable `use_temp`

# %% [markdown]
# ### Why use a function here?
#
# Instead of writing this every time:
#
# ```
# if settings.temporary_run:
#     use_temp = "/temp"
# else:
#     use_temp = ""
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
# Example:
#
# `set_use_temp(...)` may be easier to understand than an inline if-statement

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

# %%
def use_temp(temporary_run):
    if temporary_run:
        return "/temp"
    return ""

# %% [markdown]
# ### Common patterns (not rules)
#
# These are often used to improve readability:

# %%
# get_ → retrieve a value
def get_use_temp(temporary_run): ...

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
# ### Important point
#
# These prefixes are conventions — not requirements.
#
# Often it is even better to avoid them if the function name is already clear:

# %%
def temp_path(temporary_run):
    if temporary_run:
        return "/temp"
    return ""

# %% [markdown]
# ### Rule of thumb
#
# - Start with a verb
# - The name should read like a sentence:
#
#   `use_temp(True)`
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
# ### Example from the course

# %%
def set_use_temp(temporary_run: bool) -> str:
    if temporary_run:
        return "/temp"
    return ""

# %% [markdown]
# ### What does this mean?
#
# - `x: int`
#     - x is expected to be an integer
# - `-> int`
#     - the function returns an integer
# - `bool`, `str`, `float`, `pd.DataFrame`, `pd.Series` are commonly used

# %%
# ## More types

def format_name(name: str) -> str:
    return name.upper()

# %%
# Lists:
def sum_list(values: list[int]) -> int:
    return sum(values)

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
