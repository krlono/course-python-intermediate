# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     notebook_metadata_filter: kernelspec
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Calculate weights


# %%
import pandas as pd
import os
from glob import glob


# %% [markdown]
# ## Set working folder and import settings


# %%
local_user_folder = os.environ["USERPROFILE"]

project_name = "course-python-intermediate"
working_folder = f"{local_user_folder}/{project_name}"

working_folder


# %%
os.chdir(working_folder)

os.getcwd()


# %% [markdown]
# ## Import settings and define working directories


# %%
from config.config import settings

year = settings.year
print(f"Current year is {year}")

data_dir = settings.data_dir
data_dir = f"{local_user_folder}\\{data_dir}"

print(f"Data directory is {data_dir}")

process_dir = f"{data_dir}/processed/"
print(f"Process directory is {process_dir}")


# %% [markdown]
# ## Read from parquet


# %%
population_file = f"{process_dir}population_{year}.parquet"

population = pd.read_parquet(population_file)

print(
    f"{population.shape[0]} rows and "
    f"{population.shape[1]} columns read from {population_file}"
)

population


# %%
persons_file = f"{process_dir}lcs_persons_{year}.parquet"

persons = pd.read_parquet(persons_file)

print(
    f"{persons.shape[0]} rows and "
    f"{persons.shape[1]} columns read from {persons_file}"
)


# %%
households_file = f"{process_dir}lcs_households_{year}.parquet"

households = pd.read_parquet(households_file)

print(
    f"{households.shape[0]} rows and "
    f"{households.shape[1]} columns read from {households_file}"
)


# %% [markdown]
# ## Add weights
#
# First we prepare for weights calculation.


# %% [markdown]
# ### Household totals by state


# %%
stats = (
    population
    .groupby("state")
    .agg(
        N_households=("hh_id", "size"),
        n_households=("sampled", "sum"),
        N_persons=("no_of_persons", "sum"),
        n_persons=(
            "no_of_persons",
            lambda x: x[
                population.loc[x.index, "sampled"]
            ].sum()
        )
    )
)

stats


# %% [markdown]
# ### Household weights


# %%
stats["weight_household"] = (
    stats["N_households"]
    / stats["n_households"]
)

stats


# %% [markdown]
# ### Person weights


# %%
stats["weight_person"] = (
    stats["N_persons"]
    / stats["n_persons"]
)

stats


# %% [markdown]
# ### Same syntax, but as a function


# %%
def calc_weights(level):
    stats[f"weight_{level}"] = (
        stats[f"N_{level}"]
        / stats[f"n_{level}"]
    )


# %%
calc_weights("households")
calc_weights("persons")

stats


# %% [markdown]
# ## Add weights to sampled households


# %%
households_wgt = pd.merge(
    households,
    stats[["weight_household"]],
    left_on="state",
    right_index=True,
    how="left"
)

households_wgt


# %% [markdown]
# ## Add weights to sampled persons


# %%
persons_wgt = pd.merge(
    persons,
    stats[["weight_person"]],
    left_on="state",
    right_index=True,
    how="left"
)

persons_wgt.style


# %% [markdown]
# ## Export to parquet


# %%
persons_file = (
    f"{process_dir}lcs_persons_wgt_{year}.parquet"
)

persons_wgt.to_parquet(persons_file)

print(
    f"{persons_wgt.shape[0]} rows and "
    f"{persons_wgt.shape[1]} columns written to "
    f"{persons_file}"
)


# %%
households_file = (
    f"{process_dir}lcs_households_wgt_{year}.parquet"
)

households_wgt.to_parquet(households_file)

print(
    f"{households_wgt.shape[0]} rows and "
    f"{households_wgt.shape[1]} columns written to "
    f"{households_file}"
)
