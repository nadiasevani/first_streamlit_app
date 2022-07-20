import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://nadiasevani-first-streamlit-app-streamlit-app-lfcfsi.streamlitapp.com/") #read csv and pull the data into a dataframe
streamlit.dataframe(my_fruit_lsit) #display the dataframe to streamlit
