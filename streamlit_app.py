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

#lets put a pick list here so that user can pick the fruits they want
streamlit.multiselect('Pick Some Fruits: ',list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
