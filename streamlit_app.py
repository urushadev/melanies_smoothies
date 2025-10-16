# #------------- Database----------------------

# # Import python packages
# import streamlit as st
# from snowflake.snowpark.functions import col

# # Write directly to the app
# st.title(f"Customize Your Smoothie:cup_with_straw:")
# st.write(
#   """Choose the fruits you want in your custom Smoothie!
#   """
# ) 

# name_on_order= st.text_input("Name on Smoothie:")
# st.write("The name on your smoothie would be: ", name_on_order)


# # We brought col here to select from column

# # session = get_active_session()
# cnx=st.connection("snowflake")
# session=cnx.session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)


# ingredients_list= st.multiselect(
#     'Choose up to 5 ingredients:'
#     ,my_dataframe,
#     max_selections=5
    
# )

# import streamlit as st


# if ingredients_list:

#  ingredients_string=''
    
#  for x in ingredients_list:
#      ingredients_string += x+ ' '

#  # st.write(ingredients_string)
#  my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
#             values ('""" + ingredients_string + """','"""+name_on_order+"""')"""
            
#  # st.write(my_insert_stmt)

#  time_to_insert=st.button('Submit Order')

#  if time_to_insert:
#     session.sql(my_insert_stmt).collect()
#     st.success('Your Smoothie is ordered!', icon="✅")




#------------- API ----------------------

# # Import python packages
# import streamlit as st
# from snowflake.snowpark.functions import col
# import requests


# # Write directly to the app
# st.title(f"Customize Your Smoothie:cup_with_straw:")
# st.write(
#   """Choose the fruits you want in your custom Smoothie!
#   """
# ) 

# name_on_order= st.text_input("Name on Smoothie:")
# st.write("The name on your smoothie would be: ", name_on_order)


# # We brought col here to select from column

# # session = get_active_session()
# cnx=st.connection("snowflake")
# session=cnx.session()
# # my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# # st.dataframe(data=my_dataframe, use_container_width=True)


# ingredients_list= st.multiselect(
#     'Choose up to 5 ingredients:',
#     # ,my_dataframe,
#     # max_selections=5
# )


# if ingredients_list:

#   ingredients_string=''
    
#   for x in ingredients_list:
#       ingredients_string += x+ ' '
#       smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
#       sf_df=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)

#   st.write(ingredients_string)

    
#   my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
#             values ('""" + ingredients_string + """','"""+name_on_order+"""')"""
            
#   st.write(my_insert_stmt)

#  time_to_insert=st.button('Submit Order')

#  if time_to_insert:
#     session.sql(my_insert_stmt).collect()
#     st.success('Your Smoothie is ordered!', icon="✅")

# Import required packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

# App title
st.title("🥤 Customize Your Smoothie")
st.write("Choose the fruits you want in your custom smoothie!")

# Input for name
name_on_order = st.text_input("Name on Smoothie:")
if name_on_order:
    st.write("The name on your smoothie will be:", name_on_order)

# Connect to Snowflake
cnx = st.connection("snowflake")
session = cnx.session()

# (Optional) Get fruit options from Snowflake table
# fruit_options = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME')).to_pandas()

# Multi-select for ingredients (you can replace with fruit_options['FRUIT_NAME'] if you have data)
ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    ["strawberry", "banana", "mango", "blueberry", "pineapple", "watermelon"],  # example list
    max_selections=5
)

# When user selects ingredients
if ingredients_list:
    ingredients_string = ", ".join(ingredients_list)
    st.write("You selected:", ingredients_string)

    # Example API call (currently fixed to watermelon for demo)
    smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
    st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)

    # Prepare SQL insert statement
    my_insert_stmt = f"""
        INSERT INTO smoothies.public.orders(ingredients, name_on_order)
        VALUES ('{ingredients_string}', '{name_on_order}')
    """
    st.write(my_insert_stmt)

    # Button to submit order
    if st.button("Submit Order"):
        session.sql(my_insert_stmt).collect()
        st.success("Your Smoothie is ordered! ✅")

