import streamlit as st
from streamlit_option_menu import option_menu
import Car, Analysis,Filter, Predict
from PIL import Image
from streamlit_extras.dataframe_explorer import dataframe_explorer

img = Image.open("C:\\Users\\prem\\Desktop\\Ranjana\\3.Car Project\\Car.jpg")
st.set_page_config(page_title = "Cardekho Resale Price Prediction", page_icon = img,layout = "wide")

class multiapp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({'title':title,'function':function})
    def run(self):
        with st.sidebar:
            app = option_menu('Car Resale Price Prediction', ["Home","Data Filtering","Data Analysis","Data Prediction"], 
                icons=['house', 'search',"reception-4","dice-5-fill"], 
                menu_icon='cash', default_index=0, orientation="vertical",
                styles={
                    "container": {"padding": "0!important", "background-color": "#FCC737"}, # #008080
                    "icon": {"color": "Red", "font-size": "20px"}, 
                    "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#C4A484"},
                    "nav-link-selected": {"background-color": "#F26B0F"}, 
                }
            )
        if app == 'Home':
            Car.app()
        elif app == 'Data Filtering':
            Filter.app()
        elif app == 'Data Analysis':
            Analysis.app()
        elif app == 'Data Prediction':
            Predict.app()
    
        
    
        
app = multiapp()

# Add your apps to the multiapp instance
app.add_app("Home", Car.app)
app.add_app("Data Filtering", Filter.app)
app.add_app("Data Analysis", Analysis.app)
app.add_app("Data Prediction", Predict.app)

# Run the multiapp
app.run()