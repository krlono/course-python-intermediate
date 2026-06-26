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
# ## What is glob?
#
# `glob` is used to find files and folders based on patterns (wildcards),
# similar to how it works in the terminal.
#
# Typical wildcards:
# - `*` → matches everything
# - `?` → matches a single character
# - `[...]` → matches one of several characters

# %%
import os
import pathlib
from datetime import datetime
os.getcwd()

# %%
pip install dynaconf

# %%
from glob import glob
import sys
sys.path.append("../../../")
from config.config import settings
data_dir = settings.data_dir
data_dir

# %%
local_user_folder = os.environ["USERPROFILE"] 
local_user_folder

# %% [markdown]
# ## Simple examples

# %%
# Folder
print(data_dir)

# All files and folders in the directory
all_files = glob(f"{local_user_folder}/{data_dir}/*")
print(all_files)

# %% [markdown]
# All parquet files in the folder (without subfolders)

# %%
csv_files = glob(f"{local_user_folder}/{data_dir}/*.csv")
print(csv_files)

# %% [markdown]
# All parquet files in the folder (including subfolders)

# %%
py_files = glob(f"{local_user_folder}/**/*.py", recursive=True)
print(py_files)

# %% [markdown]
# Important:
# - `**` means "all levels downward"
# - `recursive=True` must be included to search all nested subfolders

# %% [markdown]
# ## Sorting and control

# %% [markdown]
# glob returns a list – but the order is not guaranteed

# %%
for path in sorted(all_files):
    print(path)

# %%
# All files containing "_p2024"
specific_paths = glob(f"{local_user_folder}/{data_dir}/*2024*.*", recursive=True)
specific_paths

# %% [markdown]
# ## File information
# We can extract information about files, like:
# - name
# - extension
# - size
# - date made
# - date changed
#

# %%
folder = Path(data_dir)
files = folder.glob('*')

records = []
for file in files:
    stat = file.stat()
    records.append({
        'name_full': file.resolve(),
        'path': file.parent,
        'name': file.name,
        'suffix': file.suffix,
        'size': stat.st_size,
        'created': datetime.fromtimestamp(stat.st_ctime),
        'modified': datetime.fromtimestamp(stat.st_mtime)
    })
file_info = pd.DataFrame(records)
file_info

# %% [markdown]
# ## Tips (useful in practice)
#
# - Use `sorted()` for reproducible results
# - Print the list first when debugging
# - Be explicit in your patterns (avoid `*` if you know the structure more precisely)
