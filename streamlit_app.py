import streamlit 
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# importing data and creating dataframe 

import pandas as pd 
data_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
data_list = data_list.set_index('Fruit')

# adding multiselect
# picking the variables only to show in select 
fruits_selected = streamlit.multiselect('Pick some fruits', list(data_list.index),['Avocado','Strawberries'])
# fruits to show 
fruits_to_show = data_list.loc[fruits_selected]

streamlit.dataframe(data_list)


