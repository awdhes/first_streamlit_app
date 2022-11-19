
import streamlit
import pandas
streamlit.header('Breakfast Menu')
streamlit.text('🤷‍♂️ Omega 3 & Blueberry Oatmeal')
streamlit.text('🎂🎂🎂🎂🎂🎂Kale, Spinach & Rocket Smoothie')
streamlit.text('✌Hard-Boiled Free-Range Egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# set first column as index on list
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets pick the fruits what they wanted to include 
fruits_selected=streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
