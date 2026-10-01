# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     notebook_metadata_filter: kernelspec
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Introduction to Python basics
# The user interface consists of a notebook with different cells. Each cell can be either
# - **Code** Here we write our Python syntax
# - **Markdown** Here we write our comments
# - **Raw** Used for raw text (not very much used)
#
# To run a cell we can use the play button, or we can use key combinations
# - **Ctrl+Enter** Run cell and stay in the cell
# - **Shift+Enter** Run cell and go to the next cell
# - **Alt+Enter** Run cell and insert new cell below
#

# ## Computations and data types
# We can use Python as a calculator by adding, subtracting, multyplying, dividing and so on.
#
# We have different data types in Python. These are a few of them:
# - *Number* Integer numbers (can not be missing)
# - *Float* Decimal numbers (can be missing)
# - *String* Plain text, can include numbers and floats
# - *Bool* Either True or False

import numpy as np
import pandas as pd

2 + 2

type(2)

'2' + '2'

type('2' + '2')

2 * 3

'2' * 3

True + True

type(False)

type('False')

true = True
true + true

x = 3
y = 6
z = x + y
print(z)
print(x, y, z)
print('{x} + {y} = {z}')
print(f'{x} + {y} = {z}')

4 % 3 # modulus, returns the remainder of the division

# ## More on strings
# A string is a set of characters in an order. We can extract parts of the string with indexes. The first position within the string has the number 0.

capital = 'Windhoek'
print(capital)
print(type(capital))
print(capital[0])
print(capital[1])
print(capital[1:3])
print(capital[-1])
print(capital[5:])
print(capital[:4])
print(capital[-2])
print(capital[6])


# ## Lists
# Lists consist of a number of elements. Elements can be extracted the same way as when we extracted from a string. We can loop through a list with a `for` command.

capitals = ['Windhoek', 'Luanda', 'Lusaka', 'Oslo']
print(len(capitals))
print(capitals[0])
print(capitals[-1])
print(type(capitals[-1]))
print(capitals[2:])
print(type(capitals[2:]))
print(capitals[2][1:3])

for c in capitals:
    print(c)

list_of_things = ['Windhoek', 25, True]
print(type(list_of_things))
for l in list_of_things:
    print(type(l))

# ## Dictionaries
# A dictionary consist of pairs of key and value sets. It is widely used, for instance for lookup tables.

country_labels = {
    'NA': 'Namibia',
    'AO': 'Angola',
    'ZM': 'Zambia',
    'NO': 'Norway',
    'ZW': 'Zimbabwe'
}
print(country_labels)
print(country_labels.keys())
print(country_labels.values())
print(country_labels['NA'])

countries = ['NA', 'AO', 'ZM', 'NO']
country_names = []
for c in countries:
    country_names.append(country_labels[c])
print(country_names)

# ## Conditions
# The most common operators for conditional expressions are:
# - **==** Equals to
# - **>** Greater than
# - **<** Less than
# - **>=** Greater than or equal
# - **<=** Less than or equal

5 > 2

'A' > 'a'

2 < 1

for c in capitals:
    if c[0] == 'L':
        print(c)

# ## Constants, lists and dicionary exercises
# 1. Add 34 to 98
# 2. Multiply 40 with 28
# 3. Concatenate the text 'Ha' 10 times
# 4. Put a number in an object and another number in another object. Then create a third object by multyplying the two objects. Print the third object
# 5. Print the whole expression above with an f-string showing each element and the result of the calculation
# 6. Create a shopping list of 6 elements and print the list
# 7. Print the first element of the shopping list
# 8. Print the last element of the shopping list
# 9. Print elements 2-4 of the shopping list
# 10. Print the first position in the third element in the shopping list
# 11. Add an element to the shopping list and print the updated list
# 12. Make a dictionary with the elements of your shopping list as the key and the price of the commodity as the value
# 13. Print the keys of the dictionary
# 14. Print the values of the dictionary
# 15. Print the elements in the shopping list starting with a specific letter
# 16. Make a list of the prices for the commodities in the shopping list by using the dictionary as a lookup table
# 17. Make a sum of all the prices by using the sum() function on the list of prices
# 18. Make a list of the number of each commodity you will buy

34 + 98

40 * 28

'Ha' * 10

a = 23
b = 34
c = a * b
print(f'{a} * {b} = {c}')

shopping_list = ['Bread', 'Milk', 'Bananas', 'Apples', 'Butter', 'Fish']

shopping_list.append('Maize')

item_prices = {
    'Apples': 45, 
    'Bananas': 29, 
    'Bread': 25, 
    'Butter': 37, 
    'Cheese': 97,
    'Fish': 230,
    'Maize': 15,
    'Meat': 210,
    'Milk': 26,
}
item_prices

prices = []
for item in shopping_list:
    prices.append(item_prices[item])
prices

print(item_prices.keys())
print(item_prices.values())

for item in item_prices:
    if item[0] == 'M':
        print(item)

sum(prices)

amounts = [2, 5, 1, 3, 6, 2, 4]

# ## Dataframes
# A dataframe consists of rows and columns in two dimensions. We can create dataframes in different ways, for instance by importing data files, like a csv file or an excel spreadsheet. We can also make our own dataframes from a dictionary.

area = [823_290, 1_246_700, 743_390, 365_268]
area

population = [3_092_816, 39_040_039, 21_913_874, 5_623_071]
population

highest_elevation = [2573, 2620, 2339, 2469]
highest_elevation

data = {
    'name': country_names,
    'capital': capitals,
    'area': area,
    'population': population,
    'elevation': highest_elevation
}
data

# We can transform a dictionary where the values are lists into a dataframe. We will here look at Pandas dataframes. To be able to work with Pandas dataframes we need to import the Pandas package as it is not part of the Python that is available when the interface is started.

df = pd.DataFrame(data)
df

# We can make a new column in this dataframe, for instance the population density

df['density'] = df['population'] / df['area']
df

df.sort_values('density')

df.sort_values('density', ascending=False)

df.columns

df.dtypes

df.info()

df['area'].sum()

df['area'].mean()

# ## Dataframe exercises
# 1. Create a dictionary for the shopping list with these keys: commodity, price, amount
# 2. Transform the dictionary into a dataframe
# 3. Calculate a new column for the value spent
# 4. Print the info about the columns
# 5. Sort the columns descending by value
# 6. Calculate the sum and mean of the expenditures

comm_dict = {
    'item': shopping_list,
    'price': prices,
    'amount': amounts
}
comm_dict

basket = pd.DataFrame(comm_dict)
basket

basket['value'] = basket['price'] * basket['amount']
basket

basket.info()

basket.sort_values('value', ascending=False)

basket['value'].sum()

basket['value'].mean()

# ## Export and import of data
# We can export to and import from different data formats, like:
# - csv files
# - excel spreadsheets
# - parquet files
#
# We use Pandas functions for the export and import. But first we must decide where we shall store our data.

DATA_PATH = 'c:/users/krl/course-python-intermediate/data/source/'

import os
os.getcwd()

# Export to a csv file

df.to_csv(f'{DATA_PATH}countries.csv', index=False)

# Export to an excel file

df.to_excel(f'{DATA_PATH}countries.xlsx', index=False)

# Export to parquet file

df.to_parquet(f'{DATA_PATH}countries.parquet')

# Import from csv file

countries_from_csv = pd.read_csv(f'{DATA_PATH}countries.csv')
countries_from_csv

# Import from excel

countries_from_excel = pd.read_excel(f'{DATA_PATH}countries.xlsx')
countries_from_excel

# Import from parquet

countries_from_parquet = pd.read_parquet(f'{DATA_PATH}countries.parquet')
countries_from_parquet

# ## Export and import exercises
# 1. Check in your notebook that you don't overwrite the country dataframe with the shopping list. If they have the same names the shopping list will overwrite the countries dataframe. Change name for the shopping list if it has the same name as the countries.
# 2. Re-run your notebook and check that the countries csv and excel files contain countries and not shopping lists.
# 3. Export the shopping list dataframe to a csv file
# 4. Export the shopping list dataframe to an excel file
# 5. Export the shopping list dataframe to a parquet file
# 6. Import the shopping list csv file to a dataframe with the name shoplist_from_csv
# 7. Import the shopping list excel file to a dataframe with the name shoplist_from_excel
# 8. Import the shopping list parquet file to a dataframe with the name shoplist_from_parquet
#

# Export to a csv file

basket.to_csv(f'{DATA_PATH}basket.csv', index=False)

# Export to an excel file

basket.to_excel(f'{DATA_PATH}basket.xlsx', index=False)

# Export to parquet file

basket.to_parquet(f'{DATA_PATH}basket.parquet')

# Import from csv file

shoplist_from_csv = pd.read_csv(f'{DATA_PATH}basket.csv')
shoplist_from_csv

# Import from excel

shoplist_from_excel = pd.read_excel(f'{DATA_PATH}basket.xlsx')
shoplist_from_excel

# Import from parquet

shoplist_from_parquet = pd.read_parquet(f'{DATA_PATH}basket.parquet')
shoplist_from_parquet

# ## More import of data
# Let us look at the import of a statistical data file. We will use the read_csv function again.
#
# To decide which columns that should be string columns, we can do a small test: If it is reasonable to calculate the *sum* and/or the *mean* of a column, it should be a numeric column (int, float). If not, and if it is not a date, it should be defined as a string column.

# +
lcs = pd.read_csv(
    f'{DATA_PATH}lcs_survey_2023.csv',
    dtype={
        'hh_id': 'string',
        'state': 'string',
        'urbrur': 'string',
        'no_of_persons': 'float',
        'years_in_community': 'float',
        'building_type': 'string',
        'no_of_rooms': 'float',
        'owns_car': 'float',
        'owns_motorcycle': 'float'
    }
)

lcs
# -

# ## Look closer into the data
# We will check data types, make som value counts, look at some statistics for the dataframe.

lcs.info()

lcs['state'].value_counts()

lcs['state'].value_counts(sort=False)

lcs['owns_car'].value_counts(dropna=False)

lcs['owns_motorcycle'].value_counts(dropna=False)

lcs[['owns_motorcycle', 'owns_car']].value_counts(dropna=False)

lcs['owns_car'].sum()

lcs['years_in_community'].mean()

lcs.describe()

lcs.describe().T

# ## Data overview exercises
# 1. Import the file population_2023 from the source folder (the same folder as previously) and call the dataframe pop
# 2. Check what data types Python guessed for the columns
# 3. Import again, but now with your definition of what the data types should be
# 4. Check if there are any missing values for any of the columns
# 5. Make value counts for the columns state, urbrur, sampled
# 6. Make an overview of the numeric columns in the dataframe
# 7. If you have some source data file from your own statistics in csv or excel format, import it and do the same as in exercise 2-6 

pop = pd.read_csv(f'{DATA_PATH}population_2023.csv')
pop

pop.info()

# +
pop = pd.read_csv(
    f'{DATA_PATH}population_2023.csv',
    dtype={
        'hh_id': 'string',
        'state': 'string',
        'urbrur': 'string',
        'no_of_persons': 'float',
        'sampled': 'bool'
    }
)

pop
# -

pop.info()

pop['state'].value_counts()

pop['urbrur'].value_counts()

pop['sampled'].value_counts()

pop.describe()

# ## Selection on rows
# We can select rows in different ways. Here are some ways:
# - **head** Select first `n` rows
# - **tail** Select last `n` rows
# - **sample** Select `n` random rows
# - **loc** Select rows based on conditions

lcs.head(11)

lcs.tail(7)

lcs.sample(3)

# Select one value for a column

lcs.loc[lcs['state'] == '1']

# Select more values for a column

lcs.loc[lcs['state'].isin(['2', '3'])]

# Select rows where column is missing

lcs.loc[lcs['owns_motorcycle'].isna()]

# Select rows where column is **not** missing

lcs.loc[lcs['owns_motorcycle'].notna()]

# Select rows based on more than one condition. We must have brackets around each expression
# - **&** And
# - **|** Or

lcs.loc[(lcs['state'] == '1') & (lcs['urbrur'] == '2')] # Both must be true

lcs.loc[(lcs['state'] == '1') | (lcs['urbrur'] == '2')] # Only one need to be true

# We can update values based on a condition

lcs['owns_motorcycle'].value_counts(dropna=False)

lcs.loc[lcs['owns_motorcycle'].isna(), 'owns_motorcycle'] = 0

lcs['owns_motorcycle'].value_counts(dropna=False)

# We can check for duplicates also

lcs.duplicated()

lcs.duplicated(subset='hh_id')

# We can select the duplicates by using the `duplicated` function within a `loc`

lcs.loc[lcs.duplicated(subset='hh_id')]

lcs.loc[lcs.duplicated(subset='hh_id', keep='first')]

lcs.loc[lcs.duplicated(subset='hh_id', keep='last')]

lcs.loc[lcs.duplicated(subset='hh_id', keep=False)]

# When we want to remove duplicates we can use a negation (~) in our `loc`

lcs_nodup = lcs.loc[~lcs.duplicated(subset='hh_id', keep='first')]
lcs_nodup

# ## Data selection exercises
# 1. List the first 22 rows from the pop dataframe
# 2. List the last 11 rows from the pop dataframe
# 3. List a sample of 8 rows from the pop dataframe
# 4. Select the rows from pop where state is 1
# 5. Select the rows from pop where state is either 4 or 9
# 6. Select the rows from pop where state is 3 and urbrur is 1
# 7. Select the rows from pop where no_of_persons is missing
# 8. Select the rows from pop where no_of_persons is not missing
# 9. Select the rows from pop which are marked as sampled
# 10. Select the rows from pop which are duplicates
# 11. Select the rows from pop which are duplicates for hh_id
# 12. Select the rows from pop where the no_of_persons are above the average number of persons

pop.head(2)

pop.tail(11)

pop.sample(8)

pop.loc[pop['state'] == '1']

# Select more values for a column

pop.loc[pop['state'].isin(['4', '9'])]

pop.loc[(pop['state'] == '3') & (pop['urbrur'] == '1')]

pop.loc[pop['no_of_persons'].isna()]

pop.loc[pop['no_of_persons'].notna()]

pop.loc[pop['sampled']]

pop.loc[pop.duplicated()]

pop.loc[pop.duplicated(subset='hh_id')]

pop['no_of_persons'].mean()

pop.loc[pop['no_of_persons'] > pop['no_of_persons'].mean()]

lcs.columns

# ## Spilt the dataframe
# We want to split the dataframe into one dataframe with information about the household and one about the persons within the household

hh = lcs_nodup[['hh_id', 'state', 'urbrur', 'no_of_persons', 'years_in_community',
       'building_type', 'no_of_rooms', 'owns_car', 'owns_motorcycle',
       'owns_bicycle', 'owns_fridge', 'owns_freezer', 'owns_tv']]
hh

person = lcs_nodup[['hh_id', 'state', 'relationship_to_head_1', 'relationship_to_head_2',
       'relationship_to_head_3', 'relationship_to_head_4',
       'relationship_to_head_5', 'relationship_to_head_6',
       'relationship_to_head_7', 'relationship_to_head_8',
       'relationship_to_head_9', 'sex_1', 'sex_2', 'sex_3', 'sex_4', 'sex_5',
       'sex_6', 'sex_7', 'sex_8', 'sex_9', 'marital_status_1',
       'marital_status_2', 'marital_status_3', 'marital_status_4',
       'marital_status_5', 'marital_status_6', 'marital_status_7',
       'marital_status_8', 'marital_status_9', 'birth_date_1', 'birth_date_2',
       'birth_date_3', 'birth_date_4', 'birth_date_5', 'birth_date_6',
       'birth_date_7', 'birth_date_8', 'birth_date_9', 'occupation_1',
       'occupation_2', 'occupation_3', 'occupation_4', 'occupation_5',
       'occupation_6', 'occupation_7', 'occupation_8', 'occupation_9',
       'income_1', 'income_2', 'income_3', 'income_4', 'income_5', 'income_6',
       'income_7', 'income_8', 'income_9']]
person

# wide_to_long will transform from the wide format to the long format.
# We specify the dataframe, the columns to transform (stubs), the identification columns (i), the counter (j) and the separator (sep).

persons = pd.wide_to_long(
    person,
    ['relationship_to_head', 'sex', 'marital_status', 'birth_date', 'occupation', 'income'],
    i=['hh_id', 'state'],
    j='member',
    sep='_'
)
persons.head(27)

# We drop the rows where all columns are missing to delete non-existing persons from our dataframe.
# To do that we use dropna(how='all'). Then all rows where all values are missing will be dropped.

persons = persons.dropna(how='all')
persons.head(25)

# Change the index columns to ordinary columns with the reset_index function

persons = persons.reset_index()
persons

# ## Merge files
# We usually we merge only two files at the time. It is common to have one or more columns as key columns, that is columns to match by.
#
# When we find the same value for the key column(s), they match. When we have a key in the one of the dataframes that does not match any keys in the other dataframe, there is no match.
#
# Types of merge:
# - **inner** only the rows that merge with be added to the result
# - **left** the rows that merge and the rows only from the left dataframe will be added to the result
# - **right** the rows that merge and the rows only from the right dataframe will be added to the result
# - **outer** all rows will be included in the result
#
# When there is a column that is in both dataframes without being part of the key, both will be added to the dataframe. However, they will get a suffix, x for the left dataframe and y for the right.

hh_with_pop = pd.merge(hh, pop, on='hh_id', how='inner')
hh_with_pop

hh_with_pop_l = pd.merge(hh, pop, on='hh_id', how='left')
hh_with_pop_l

hh_with_pop_r = pd.merge(hh, pop, on='hh_id', how='right')
hh_with_pop_r

hh_with_pop_o = pd.merge(hh, pop, on='hh_id', how='outer', indicator=True)
hh_with_pop_o

hh_with_pop_o['_merge'].value_counts()

# ## Merge dataframes exercises
# 1. Merge the pop dataframe with the persons dataframe with an inner merge
# 2. Merge the pop dataframe with the persons dataframe with a left merge
# 3. Merge the pop dataframe with the persons dataframe with a right merge
# 4. Merge the pop dataframe with the persons dataframe with an outer merge
# 5. Add the indicator _merge to the result for the outer join and do a value count for it

pop_with_persons_i = pd.merge(pop, persons, on='hh_id', how='inner')
pop_with_persons_i

pop_with_persons_l = pd.merge(pop, persons, on='hh_id', how='left')
pop_with_persons_l

pop_with_persons_r = pd.merge(pop, persons, on='hh_id', how='right')
pop_with_persons_r

pop_with_persons_o = pd.merge(pop, persons, on='hh_id', how='outer', indicator=True)
pop_with_persons_o

pop_with_persons_o['_merge'].value_counts()

# ## Aggregation
# We can aggregate in two ways
# 1. Create a new dataframe on the aggregated level. Here we use the agg function.
# 2. Add aggregated values to each row in the original dataframe. Here we use the transform function
#
# We use groupby for our aggregation.

pop_by_state = pop.groupby('state').agg(
    sum_persons = ('no_of_persons', 'sum'),
    mean_persons = ('no_of_persons', 'mean'),
    number_of_rows = ('no_of_persons', 'size')
)
pop_by_state

pop_by_state_sampled = pop.groupby(['state', 'sampled']).agg(
    sum_persons = ('no_of_persons', 'sum'),
    mean_persons = ('no_of_persons', 'mean'),
    number_of_rows = ('no_of_persons', 'size')
)
pop_by_state_sampled

pop_by_state_sampled = pop.groupby(['state', 'sampled'], as_index=False).agg(
    sum_persons = ('no_of_persons', 'sum'),
    mean_persons = ('no_of_persons', 'mean'),
    number_of_rows = ('no_of_persons', 'size')
)
pop_by_state_sampled

pop_with_added_cols = pop.copy()
pop_with_added_cols['sum_persons'] = pop_with_added_cols.groupby(['state', 'sampled'])['no_of_persons'].transform('sum')
pop_with_added_cols

pop_with_added_cols['share_persons'] = pop_with_added_cols['no_of_persons'] / pop_with_added_cols['sum_persons']
pop_with_added_cols

pop_with_added_cols.loc[pop_with_added_cols['state'] == '1']

# ## Aggregation exercises
# 1. Aggregate the hh dataframe to the urbrur level and sum up the number who owns a car
# 2. Aggregate the hh dataframe to the urbrur level and sum up the number who owns a car, who owns a motorcycle and who owns a bycycle
# 3. Aggregate the h dataframe to the urbrur and state level and sum up the number who owns a car, who owns a motorcycle and who owns a bycycle
# 4. Aggregate the persons dataframe to state level and make sum and mean of the income
# 5. Aggregate the persons dataframe to state and sex level and make sum, mean and count (size) of the income
# 6. Create a copy of the persons dataframe
# 7. Add a column called sum_income to the new dataframe which is grouped by hh_id
# 8. Create a new column that calculates the share of income for each person in the households

hh_urbrur = hh.groupby('urbrur').agg(
    num_cars = ('owns_car', 'sum')
)
hh_urbrur

hh_urbrur = hh.groupby('urbrur').agg(
    num_cars = ('owns_car', 'sum'),
    num_motorcycles = ('owns_motorcycle', 'sum'),
    num_bicycles = ('owns_bicycle', 'sum')
)
hh_urbrur

persons_state = persons.groupby('state').agg(
    sum_income = ('income', 'sum'),
    mean_income = ('income', 'mean')
)
persons_state

persons_state = persons.groupby(['state', 'sex']).agg(
    sum_income = ('income', 'sum'),
    mean_income = ('income', 'mean'),
    count_income = ('income', 'size'),
)
persons_state

persons_add = persons.copy()
persons_add['sum_income'] = persons.groupby('hh_id', as_index=False)['income'].transform('sum')
persons_add    

persons_add['share_income'] = persons_add['income'] / persons_add['sum_income']
persons_add

# ## Recoding
# Recoding is usually to group values, for instance make value an age group based on age. We create a new column that contains the grouped value. One way to recode is to use numpy select. That means we have to import the numpy package first, because it is not in the core Python. We give the numpy package the alias np. 
#
# The np.select consists of a list of conditions and a list of values for each condition. We can also include a value when none of the conditions are True.

persons['age'] = 2023 - persons['birth_date'].str[0:4].astype('float')
persons

persons['age_group'] = np.select(
    [
        (persons['age'] >= 0) & (persons['age'] < 11),
        (persons['age'] >= 11) & (persons['age'] < 21),
        (persons['age'] >= 21) & (persons['age'] < 61),
        (persons['age'] >= 61)
    ],
    ['1','2', '3', '4'],
    default='9'
)
persons['age_group'].value_counts()

persons.loc[persons['age_group'] == '9']

# ## Replace codes with text (labels)
# In dataframes we usually store the in numbers. For categorical columns we can replace the codes with texts. First we need to make a dictionary with the codes as keys and the labels as values.
#
# Next we want to use the dictionary to replace the codes in our dataframe with the texts. To do that we can use the `map` function

age_group_label = {
    '1': '0-10 years',
    '2': '11-20 years',
    '3': '21-60 years',
    '4': '61 years and above',
    '9': 'Missing or invalid age'
}

persons['age_group_t'] = persons['age_group'].map(age_group_label)

persons['age_group_t'].value_counts()

# ## Recoding exercises
# 1. Recode the number of years in the community in the hh dataframe into three groups: 0-20 years, 21-40 years and 41 years and above and give them the codes 1, 2 or 3
# 2. Make a dictionary for the labels of the grouped years in the community
# 3. Make a new column with the text for the grouped years in the community
# 4. Make a value_counts for the new column
# 5. Make a dictionary for the urban (1) and rural (2) codes
# 6. Make a new column with the texts for urban/rural
# 7. Make a value_counts for this urban/rural column
# 8. Make a dictionary for sex: Male (1) and female (2)
# 9. Use the persons dataframe and make a new column with the texts for sex
# 10. Make a value_counts for the new column

hh

hh['year_group'] = np.select(
    [
        (hh['years_in_community'] >= 0) & (hh['years_in_community'] < 21),
        (hh['years_in_community'] < 41),
        (hh['years_in_community'] >= 41)
    ],
    ['1','2', '3'],
    default='9'
)
hh['year_group'].value_counts()

year_group_label = {
    '1': '0-20 years',
    '2': '21-40 years',
    '3': '41 years and above',
    '9': 'Missing or invalid age'
}

hh['year_group_t'] = hh['year_group'].map(year_group_label)

hh['year_group_t'].value_counts()

urbrur_label = {
    '1': 'Urban',
    '2': 'Rural'
}

hh['urbrur_t'] = hh['urbrur'].map(urbrur_label)

hh['urbrur_t'].value_counts()

sex_label = {
    1: 'Male',
    2: 'Female'
}

persons['sex_t'] = persons['sex'].map(sex_label)

persons['sex_t'].value_counts()

# ## Cross tabulation
# For cross tabulation we can use a module called pd.crosstab. We can use this for simple cross tabulations. It can make tables in two dimensions, with possibilties for nesting columns. We can add totals, we can make percentage tables. We can count the number of rows of the value of a measure column.

# Table with a distribution in the rows and the count of rows in the columns.

pd.crosstab(hh['state'], columns='Count')

# Table with a distribution in the rows and the count of rows in the columns and totals. We get this by adding `margins=True`

pd.crosstab(hh['state'], columns='Count', margins=True)

# Instead of counting just number of rows in the columns, we can make distribution of a categorical column.

pd.crosstab(hh['state'], columns=hh['owns_car'], margins=True)

# We can have nested columns in the rows. The nested columns shall be placed within a list.

pd.crosstab([hh['state'], hh['urbrur']], columns=hh['owns_car'], margins=True)

# We can also have nested columns in the columns of the table. We do it the same way as for the way by putting the columns within a list.

pd.crosstab([hh['state'], hh['urbrur']], columns=[hh['building_type'],hh['owns_car']], margins=True)

# The order within the list decides the levels

pd.crosstab([hh['urbrur'], hh['state']], columns=[hh['owns_car'], hh['building_type']], margins=True)

# Instead of counting the number of rows, we can use a measure column and calculate for instance sum or mean

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    values=hh['years_in_community'],
    aggfunc='sum',
    margins=True
)

# Without the values and aggfunc we count the number of rows

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    margins=True
)

# We can calculate the mean instead of the sum

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    values=hh['years_in_community'],
    aggfunc='mean',
    margins=True
)

# We can also make percentage tables. Then we use the parameter `normalize`. We have three different ways to make the percentages:
# - **Percent of total** normalize=True
# - **Percent of rows** normalize='index'
# - **Percent of columns** normalize='columns'
#
# The default is actually not percentages, but shares. That means the total adds up 1, not 100

# Percentage of the grand total

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    margins=True,
    normalize=True
).mul(100)

# Percentage of the rows

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    margins=True,
    normalize='index'
)

# Percentage of the columns

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    margins=True,
    normalize='columns'
)

# We can multiply the table with 100 to have percentages instead of shares

# Percentage of the rows

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    margins=True,
    normalize='index'
).mul(100)

# Percentage of the columns

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    margins=True,
    normalize='columns'
).mul(100)

# We can decide the number of decimals by styling the table
# For the formats we may use:
# - **precision** Number of decimals
# - **thousands** Thousands separator
# - **na_rep** Missing values in cell representation

pd.crosstab(
    hh['urbrur'], 
    columns=hh['building_type'], 
    margins=True,
    normalize='columns'
).mul(100).style.format(precision=0, thousands=' ')

# ## Cross tabulation exercises
# 1. Make a table from the persons dataframe with distribution of states in the rows and the count in the columns
# 2. Make a table from the persons dataframe with distribution of states in the rows and sex in the columns. Here we should add totals. Totals shall be included in the rest of the tables
# 3. Make a table from the persons dataframe with distribution of states and marital status in the rows and sex in the columns
# 4. Make a table from the persons dataframe with distribution of states and marital status in the rows and sex and relationship to the head in the columns
# 5. Make a table from the persons dataframe with distribution of marital status and states in the rows and relationship to the head and sex in the columns
# 6. Make a table from the persons dataframe with distribution of states in the rows and sex in the columns. Calculate the sum of the income instead of counting the rows
# 7. Make a table from the persons dataframe with distribution of states in the rows and sex in the columns. Calculate the average of the income instead of counting the rows
# 8. Make a percentage table with percentages of the number of rows of the grand total distributed by the states in the rows and sex in the columns
# 9. Make a percentage table with row percentages of the number of rows distributed by the states in the rows and sex in the columns
# 10. Make a percentage table with column percentages of the number of rows distributed by the states in the rows and sex in the columns
# 11. Multiply the table by 100 so it becomes real percentages
# 12. Style the table so it shows no decimals

pd.crosstab(persons['state'], columns='Count')

pd.crosstab(persons['state'], columns=persons['sex'], margins=True)

pd.crosstab(persons['state'], columns=persons['sex'], margins=True)

pd.crosstab([persons['state'], persons['marital_status'].fillna('Missing')], columns=persons['sex'], margins=True)

pd.crosstab(
    [persons['state'], persons['marital_status']],
    columns=[persons['sex'], persons['relationship_to_head']], 
    margins=True
)

pd.crosstab(
    [persons['marital_status'], persons['state']],
    columns=[persons['relationship_to_head'], persons['sex']], 
    margins=True
)

pd.crosstab(
    persons['state'],
    columns=persons['sex_t'],
    values=persons['income'],
    aggfunc='sum',
    margins=True
)

pd.crosstab(
    persons['state'],
    columns=persons['sex'],
    values=persons['income'],
    aggfunc='mean',
    margins=True
)

pd.crosstab(
    persons['state'],
    columns=persons['sex'],
    margins=True,
    normalize=True
)

pd.crosstab(
    persons['state'],
    columns=persons['sex'],
    margins=True,
    normalize='index'
)

pd.crosstab(
    persons['state'],
    columns=persons['sex'],
    margins=True,
    normalize='columns'
)

pd.crosstab(
    persons['state'],
    columns=persons['sex'],
    margins=True,
    normalize='columns'
).mul(100)

pd.crosstab(
    persons['state'],
    columns=persons['sex'],
    margins=True,
    normalize='columns'
).mul(100).style.format(precision=0)


# ## Functions
# A function is python code that can be called several times. It is used to avoid to repeat code. It can also be used for recodes and lots of other purposes.
# A function is defined by `def` and the name of the function. A function has most often parameters and returns one ore more values.

def greet():
    return 'Hello!'


greet()


def greet(name):
    return f'Hello {name}!'


greet('Carl')


# Now we want to create a function that does a recode of age

def age_group(age):
    """Calculate age groups based on age

    Parameters:
    age: the age
    
    Returns:
    The age group according to the age

    Examples:
    age_group(56)
    '3'
    
    """
    if 0 <= age < 11:
        return '1'
    if 11 <= age < 21:
        return '2'
    if 21 <= age < 61:
        return '3'
    if 61 <= age < 110:
        return '4'
    return '9'


age_group(56)

persons['age_group2'] = persons['age'].apply(age_group)
persons


# ## Function exercises
# 1. Make a function for recoding number of years in the community to 3 groups
# 2. Test the function with different values
# 3. Create a new column in the hh dataframe that recodes the years in the community into the groups defined by the function
# 4. Add a docstring to the function

def year_group(year):
    if 0 <= year < 21:
        return '1'
    if 21 <= year < 41:
        return '2'
    if 41 <= year < 110:
        return '3'
    return '9'


year_group(43)

hh['year_group2'] = hh['years_in_community'].apply(year_group)
hh


def year_group(year):
    """Calculate year groups based on a number of years

    Parameters:
    year: the number of years
    
    Returns:
    The year group according to the number of years

    Examples:
    year_group(43)
    '3'
    
    """
    if 0 <= year < 21:
        return '1'
    if 21 <= year < 41:
        return '2'
    if 41 <= year < 110:
        return '3'
    return '9'
