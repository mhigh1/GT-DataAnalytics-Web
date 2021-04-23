# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies and Setup
import pandas as pd

# File to Load
city_data_source = "resources/cities.csv"

# Read cities data csv
city_data = pd.read_csv(city_data_source)


# %%
city_data.head()


# %%
# Output the dataframe to an html file
city_data.to_html('cities_table.html', index=False, )


