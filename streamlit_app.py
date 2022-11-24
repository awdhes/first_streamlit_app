
import streamlit
import pandas
import snowflake.connector
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
# New section to display Fruitvice API response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response.json())
# Normalied the JSON version of data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display JSON data on table view
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list conatins")
streamlit.text(my_data_row)




