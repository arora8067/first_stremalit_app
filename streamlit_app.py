import streamlit
streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text( '🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text( '🐔 Hard-Boiled Free-Range Egg')
streamlit.text( '🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv( 'https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list =my_fruit_list.set_index('Fruit')

#lets put a pick list here so that user can pick the fruits they want

fruits_selected = streamlit.multiselect('Pick Some Fruits: ',list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# normalize the response
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# put it in a table
streamlit.dataframe(fruityvice_normalized)

