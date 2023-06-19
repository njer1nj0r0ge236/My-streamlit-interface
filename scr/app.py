import streamlit as st

# Set the page title
st.write("MY STREAMLIT APP INTERFACE")
st.title("Welcome to my interface using Streamlit.")


import os
import pickle
import numpy as np
import pandas as pd
import re
from pathlib import Path
from PIL import Image
import sklearn


# Load the Machine Learning model using 'pickle.load()'
model_file_path = r"C:\Users\USER\Downloads\path_to_folder\model.pkl" 
with open(model_file_path, 'rb') as pickle_file:
    loaded_model = pickle.load(pickle_file)



# Main parts of the app
header = st.container()
dataset = st.container()
features_and_output = st.container()


# Design the sidebar
st.sidebar.header("Brief overview of the Columns")
st.sidebar.markdown(""" 
                    - **store_nbr** identifies the store at which the products are sold.
                    - **family** identifies the type of product sold.
                    - **sales** is the total sales for a product family at a particular store at a given date. Fractional values are possible since products can be sold in fractional units(1.5 kg of cheese, for instance, as opposed to 1 bag of chips).
                    - **onpromotion** gives the total number of items in a product family that were being promoted at a store at a given date.
                    - **date** is the date on which a transaction / sale was made
                    - **city** is the city in which the store is located
                    - **state** is the state in which the store is located
                    - **store_type** is the type of store, based on Corporation Favorita's own type system
                    - **cluster** is a grouping of similar stores.
                    - **oil_price** is the daily oil price
                    """)


# Structure the dataset section
with dataset:
    if dataset.checkbox("Preview the dataset"):
       dataset.write("Take a look at the  sidebar for further information")
    dataset.write("---")




# Give the icon for the page a variable
image = Image.open(r"C:\Users\USER\Downloads\D.png")

# Inputs from the user
form = st.form(key="information", clear_on_submit=True)

# Structuring the header section
with header:
    header.write("THIS APP PREDICTS SALES FOR CORPORITA FAVORITA")

    header.image(image)
   
    header.write("---")

 # Get the user input using "text_input" widget
   


 


