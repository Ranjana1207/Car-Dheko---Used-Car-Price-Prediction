import streamlit as st 
from streamlit_extras.colored_header import colored_header
import pandas as pd
import pickle
import numpy as np

def app():
    colored_header(
        label='Welcome to Data :red[Prediction] page 👋🏼',
        color_name='red-70',
        description='CarDekho Used Cars Price Prediction'
    )

    @st.cache_data
    def load_data():
        try:
            df = pd.read_csv("Cleaned_Car_Dheko.csv")
            df1 = pd.read_csv("Preprocessed_Car_Dheko11.csv")
            return df, df1
        except FileNotFoundError as e:
            st.error("Error: Required data files are missing.")
            st.stop()

    df, df1 = load_data()

    # Create the form
    with st.form(key='prediction_form'):
        # Streamlit interface
        col1, col2 = st.columns(2)
        with col1:
            car_brand = st.selectbox("Select Car Brand", options=df['Manufactured_By'].unique())
            fuel_type = st.selectbox("Select Fuel Type", options=df['Fuel_Type'].unique())
            Body_Type = st.selectbox("Select Body Type", options=df['Body_Type'].unique())

            filtered_models = df[
                (df['Manufactured_By'] == car_brand) &
                (df['Body_Type'] == Body_Type) &
                (df['Fuel_Type'] == fuel_type)
            ]['Car_Model'].unique()

            if filtered_models.size == 0:
                st.warning("No models available for the selected combination.")
                filtered_models = ['No Models Found']

            car_model = st.selectbox("Select Car Model", options=filtered_models)
            model_year = st.selectbox("Select Car Produced Year", options=sorted(df['Car_Produced_Year'].unique().astype(int)))
            transmission = st.radio("Select Transmission Type", options=df['Transmission_Type'].unique(), horizontal=True)
            No_of_cylinders = st.selectbox("Select Number of Cylinders", options=df['No_of_Cylinder'].unique())
            
        with col2:    
            location = st.selectbox("Select Location", options=df['city'].unique())

            km_driven = st.slider("Enter Kilometer Driven:", min_value=100, max_value=100000, step=1000)

            engine_cc = st.number_input(
                "Enter Engine CC",
                min_value=int(df['Engine_CC'].min()),
                max_value=int(df['Engine_CC'].max()),
                help="Enter the engine capacity in cubic centimeters (cc)."
            )

            mileage = st.number_input(
                "Enter Mileage (kmpl)",
                min_value=5,
                max_value=50,
                step=1,
                help="Enter the car's mileage in kilometers per liter."
            )

            no_of_owners = st.number_input("Enter Number of Previous Owners", min_value=1, max_value=5, value=1)
            no_of_seats = st.number_input("Enter Number of Seats", min_value=2, max_value=10, value=5)
            
            Wheel_Base = st.selectbox("Select Wheel Base(mm)", sorted(df['Wheel_Base'].unique()))

        # Submit button
        submit_button = st.form_submit_button('Predict')

        if submit_button:
            # Load the model
            try:
                with open('pipeline.pkl', 'rb') as files:
                    pipeline = pickle.load(files)

                # Prepare input data as a DataFrame
                input_data = pd.DataFrame([{
                    "Kilometers_Driven": km_driven,
                    "Transmission_Type": transmission,
                    "Car_Model": car_model,
                    "Car_Produced_Year": model_year,
                    "Engine_CC": engine_cc,
                    "Mileage(kmpl)": mileage,
                    "city": location,
                    "Fuel_Type": fuel_type,
                    "Body_Type": Body_Type,
                    "No_of_Owners": no_of_owners,
                    "Manufactured_By": car_brand,
                    "No_of_Seats": no_of_seats,
                    "No_of_Cylinder": No_of_cylinders,
                    "Wheel_Base": Wheel_Base,
                }])

                # Make prediction
                result = pipeline.predict(input_data)

                # Display prediction
                st.markdown(f"## :green[*Predicted Car Price is {result[0]:,.2f}*]")

            except Exception as e:
                st.error(f"Error during prediction: {e}")
                st.write("Debug Input Data:", input_data)

# Run the app
if __name__ == '__main__':
    app()
