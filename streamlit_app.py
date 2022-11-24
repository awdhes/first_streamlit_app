
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
#create repeatable code through function 
def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
# New section to display Fruitvice API response
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
 if not fruit_choice:
  streamlit.error("please select fruite to get information")
 else:
   back_from_function=get_fruitvice_data(fruit_choice)
   streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
streamlit.stop()
# Snowflake related function 
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    retun my_cur.fetchall()
# add button to load the fruit
if streamlit.button('Get Fruit Load List')
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  my_cur = my_cnx.cursor()

streamlit.header("What fruit would you like to add!")
add_my_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for Adding: ', add_my_fruit)
my_cur.execute("insert into  fruit_load_list values ('peach')")




