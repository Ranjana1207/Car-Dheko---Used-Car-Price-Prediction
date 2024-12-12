import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header


def app():
    # st.write('dfdsff')
    colored_header(
    label = 'Welcome to :orange[Home] Page 😃',
    color_name = 'orange-70',
    description = '',
)
    with st.form(key = 'form',clear_on_submit=False):
        st.markdown("<h1 style='text-align: center;'>Car Dheko - Price Prediction</h1>", unsafe_allow_html=True)
        st.image("C:\\Users\\prem\\Desktop\\Ranjana\\3.Car Project\\FreeVector-Smiling-Car.jpg", use_column_width=True)
        st.markdown("<p class='medium-font'>Our advanced machine learning model helps you estimate car prices based on various features. Whether you're buying or selling, get accurate predictions in seconds!</p>", unsafe_allow_html=True)
        st.markdown("### How it works:")
        st.write("1. Navigate to the 'Predict' page")
        st.write("2. Input your car's details")
        st.write("3. Click 'Predict' to get an estimated price")
       

        button = st.form_submit_button('** Discover the car that perfectly matches your personality**',use_container_width = True)
    
    
