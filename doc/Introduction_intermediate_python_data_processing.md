# Introduction to intermediate training in data processing in Python

## Data flow for a simplified living conditions survey
Surveys are using a sample from a population to describe aspects for the whole population. The sample should be drawn in a way that makes it possible to actually be for representative the whole population. When the data is collected for the sample we will process them to make statistics. This is the data flow for our simplified data processing:

 ![Dataflow](img/Survey_dataflow.jpg 'Data flow for the simplified Living conditions survey')

## Steady states of data

The data we collect is what we call source data. For each step in the statistical process we store data according to the steady states of statistical data:

![Steady states of data](img/Steady_states_of_data.jpg 'Steady states of data')


## The basic folder structure

The data folders are named according to the the steady states of data.

```text
├───config
├───data
│   ├───source
│   ├───input
│   ├───processed
│   ├───output
│   └───statistics
├───doc
│   └───img
└───src
    ├───functions
    └───notebooks
        └───examples
```

If you don't have all these folders you must create the missing ones. At the beginning of the training these files will be in the `source` folder:

- lcs_survey_2023.csv
- lcs_survey_2024.csv
- lcs_survey_2025.csv
- population_2023.csv
- population_2024.csv
- population_2025.csv

As we see, there are data files for three years: 2023, 2024 and 2025. The population files contains the population for each year and the lcs_survey files contains the survey data.

The `src` folder is used for Python syntax files. In the notebooks folder there are syntax files for each step in the process shown above:

- a_import.py
- b_restructure.py
- c_calculate_weights.py
- d_impute_and_add_columns.py
- e_analyse.py

There is also an `examples` folder where there are more examples on syntax used in the main process, some exercises and solutions to the exercises. These are the example syntax files:

- **aggregation.py** Aggregation of data
- **data_types.py** Overview of basic data types
- **date_time_handling.py** Dates in pandas
- **error_handling.py** How to handle errors using `try/except`
- **funcs.py** What functions are, how to build and when to use them
- **glob_file_search.py** How to find files and folders
- **lists_sets_tuples.py** The difference between Python data types list, set, and tuple
- **list_comprehensions.py** A concise way to create and update lists
- **map_vs_replace.py** The difference between `map()` and `replace()` in pandas
- **merge_files.py** Joining dataframes
- **missing_values.py** How to handle missing values 
- **restructuring.py** Examples of restructuring dataframes

The config folder contains a settings file and a configuration file. Thir contents will be explained during the training.

## The data used in the training
All the data used in this training is fictional and they may have some strange combinations. They illustrate a Living Conditions Survey based on a population. From the population there is a drawn sample. The sample file consist of some basic Living Conditions Survey questions and is organized in the same way as an exported file from [CSPro](https://www.census.gov/data/software/cspro.html "CSPro, short for the Census and Survey Processing System, is a public domain and Open source data collection and processing software package developed by the U.S. Census Bureau and ICF International." ) may be. 

The Living Conditions Survey data files contain data both on person and household level. These are the columns for the households:

- **hh_id** Household identification
- **state** State where the household lives
- **urbrur** Urban or rural area
- **building_type** Building type for the housing
- **no_of_persons** Number of persons in the household
- **years_in_community** Number of years the household have lived in the community
- **no_of_rooms** Number of rooms in the housing
- **owns_car** Does the household own a car?
- **owns_motorcycle** Does the household own a motorcycle?
- **owns_bicycle** Does the household own a bicycle?
- **owns_fridge** Does the household own a fridge?
- **owns_freezer** Does the household own a freezer?
- **owns_tv** Does the household own a TV?

Here are the columns for the person level (there can be up to 9 persons in this example):

- **relationship_to_head** The relationship to the head of household
- **sex** Sex
- **marital_status** Marital status
- **occupation** Occupation
- **birth_date** Birth date

The population files have these columns:

- **hh_id** Household identification
- **state** State
- **urbrur** Urban or rural area
- **no_of_persons** Number of persons in the household
- **sampled** Is household in the sample?
