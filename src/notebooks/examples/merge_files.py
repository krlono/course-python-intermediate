# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Merging files
# We use `merge` to join datasets. Usually, we join on one or more key columns.
# When the keys match in both datasets, the rows are joined. Otherwise, they are not.
# We can choose whether to include rows that do not match in the result.
#
# These situations can occur when joining datasets on a key:
# - 1:1
# - 1:many
# - many:1
# - many:many
# - 1:none
# - many:none
# - none:1
# - none:many
#
# We will now look at some examples of different types of joins.

import pandas as pd
import numpy as np

# We start by creating two datasets that contain all of the situations mentioned above.

reg1file = {
    "id": ["3", "1", "2", "4", "3", "4", "4", "7", "5", "7"],
    "mstat": ["c", "a", "b", "e", "d", "f", "g", "i", "h", "j"],
    "county": ["03", "", "02", "05", "04", "06", "07", "09", "08", "10"],
}
reg1 = pd.DataFrame(reg1file).replace("", np.nan)

reg2file = {
    "id": ["2", "1", "2", "4", "3", "4", "8", "6", "8"],
    "cstat": ["y", "z", "x", "v", "w", "u", "s", "t", "r"],
    "county": ["19", "20", "18", "06", "17", "15", "12", "14", "11"],
}
reg2 = pd.DataFrame(reg2file)

display(reg1.sort_values('id'), reg2.sort_values('id'))

# The simplest join first. Here, all rows with the same value for id are joined
# and included in the result. Rows that do not match are not included.
# This is called an *inner join*.

pd.merge(reg1, reg2, on='id')

# We can sort the result after joining

pd.merge(reg1, reg2, on='id').sort_values('id')

# We can explicitly specify the keys for the two DataFrames.
# This is useful if they have different names (they do not here,
# but this shows the syntax).

pd.merge(reg1, reg2, left_on='id', right_on='id').sort_values('id')

# We see above that common columns not used as keys get suffixes:
# _x from the first DataFrame and _y from the second.
# We can change this using the suffixes argument.

pd.merge(reg1, reg2, on='id', suffixes=('_1', '_2')).sort_values('id')

# We have several join types, selected with the how argument.
# If we omit how, an inner join is performed.
# Here we choose a full join (outer join).
# Then all rows from both DataFrames are included, also those that do not match.
# It is useful to include an indicator that shows which rows matched,
# which come only from the first DataFrame, and which only from the second.

pd.merge(reg1, reg2, on='id', how='outer', indicator=True).sort_values('id')

# With a *left join*, matched rows and rows only in the first DataFrame are included

pd.merge(reg1, reg2, on='id', how='left', indicator=True).sort_values('id')

# With a *right join*, matched rows and rows only in the second DataFrame are included

pd.merge(reg1, reg2, on='id', how='right', indicator=True).sort_values('id')

# We can check the result of the join by creating a table for the *_merge* indicator.

reg1_reg2 = pd.merge(reg1, reg2, on='id', how='outer', indicator=True).sort_values('id')
pd.crosstab(reg1_reg2['_merge'], columns='Frequency', margins=True)

# We can also create a Cartesian join, also known as a cross join.
# This means that all rows are combined with each other.
# No key is used.
# Be careful: this can produce very large DataFrames.
# The number of resulting rows is the product of the row counts of both datasets.

pd.merge(reg1, reg2, how='cross')

# If we want to see which rows exist in another dataset with the same key,
# but without actually joining, we can use `loc` and `isin`.
# This only works when we have a single key column.
# With multiple keys, the syntax becomes more complex.

reg1.loc[reg1['id'].isin(reg2['id']) == True]

# Conversely, we can find those that do not exist in the other DataFrame.
# This is called an anti-join.

reg1.loc[reg1['id'].isin(reg2['id']) == False]

# Here we use two keys and find those present in both datasets

reg1.loc[(reg1['id'].isin(reg2['id']) == True) & (reg1['county'].isin(reg2['county']) == True)]

# Equivalent using merge, where we also get data from the second DataFrame

pd.merge(reg1, reg2, on=['id', 'county'], how='inner')

# We can also perform an anti-join using `merge`.
# This includes columns from the second DataFrame.
# It is also easier when working with multiple key columns.

pd.merge(reg1, reg2, on='id', how='left_anti')

# Similarly, there is a `right_anti`

pd.merge(reg1, reg2, on='id', how='right_anti')

# A full anti-join can be done using an outer join
# and then selecting the rows that did not match

anti = (
    pd.merge(reg1, reg2, on="id", how="outer", indicator=True)
      .query('_merge != "both"')
)
anti

# With this variant, we avoid creating county_x and county_y columns.
# However, we do not get an indicator showing which DataFrame each row comes from.

anti = pd.concat([
    reg1[~reg1["id"].isin(reg2["id"])],
    reg2[~reg2["id"].isin(reg1["id"])]
])
anti
