import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import plotly.express as px

def app():
    # Header
    colored_header(
        label='You are in Data :green[Analysis] page',
        color_name='green-70',
        description=''
    )

    # Cache the data loading function
    @st.cache_data
    def load_data():
        return pd.read_csv('C:\\Users\\prem\\Desktop\\Ranjana\\3.Car Project\\Cleaned_Car_Dheko.csv')
    
    df = load_data()

    # Add 'Car_Age' column if it doesn't exist
    if 'Car_Age' not in df.columns:
        df['Car_Age'] = 2024 - df['Car_Produced_Year']

    # Select feature for analysis
    choice = st.selectbox("**Select an option to Explore their data**", df.drop('price', axis=1).columns)

    # Visualization: Car Price vs Selected Feature
    st.markdown(f"## :rainbow[Car Price vs {choice}]")
    hist = px.histogram(df, x=choice, y='price', width=950, height=500)
    st.plotly_chart(hist)

    # Visualization: Most Available Car Brands
    st.markdown(f"## :rainbow[Which Car Brand is highly available]")
    brand = df.groupby('Manufactured_By').count().reset_index()[['Manufactured_By', 'Fuel_Type']]
    bar = px.bar(brand, x='Manufactured_By', y='Fuel_Type', width=950, height=500, labels={'Fuel_Type': 'Total Count of Car Brand'})
    st.plotly_chart(bar)

    # Additional Visualizations
    st.markdown(f"## :rainbow[Which Car Model available in highest prices]")
    model = df[['Car_Model', 'price', 'Manufactured_By', 'Car_Produced_Year', 'Kilometers_Driven', 'No_of_Owners']].sort_values('price', ascending=False).head(60)
    bar = px.bar(model, x='Car_Model', y='price', width=1000, height=500, color='price', color_continuous_scale='hot', hover_name='Manufactured_By')
    st.plotly_chart(bar)

    # Select Car Brand and Model for Detailed Analysis
    col, col1 = st.columns(2)
    with col:
        select_brand = st.selectbox("**Select a Car Brand**", df['Manufactured_By'].unique())
        brand = df[df['Manufactured_By'] == select_brand]
    with col1:
        select_model = st.selectbox('**Select a Car Model**', options=brand['Car_Model'].unique())

    # Car Model Year vs Price
    model = brand.groupby(['Car_Model', 'Car_Produced_Year'])['price'].mean().reset_index()
    specific_model = model[model['Car_Model'] == select_model]
    st.markdown(f"## :rainbow[Car model year vs Prices]")
    bar = px.bar(specific_model, x='Car_Produced_Year', y='price', width=950, height=500, color='price', color_continuous_scale='rainbow')
    st.plotly_chart(bar)

    # Select Location and Central Tendency
    col, col1 = st.columns(2)
    with col:
        radio = st.radio('**Select any Location 📍**', options=df['city'].unique(), horizontal=True)
    with col1:
        select_CT = st.selectbox('**Select any Central Tendency**', options=['mean', 'median', 'mode'])

    # Filter Data Based on Selection
    location_brand = df[(df['Manufactured_By'] == select_brand) & (df['city'] == radio)]
    
    if select_CT == 'mean':
        result = location_brand.groupby(['Manufactured_By', 'Car_Model'])['price'].mean().reset_index()
    elif select_CT == 'median':
        result = location_brand.groupby(['Manufactured_By', 'Car_Model'])['price'].median().reset_index()
    elif select_CT == 'mode':
        result = location_brand.groupby(['Manufactured_By', 'Car_Model'])['price'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None).reset_index()

    # Plot Pie Chart
    st.markdown(f"## :rainbow[Cars in {radio} with {select_CT} Price]")
    pie = px.pie(result, names='Car_Model', values='price', width=900, height=500, hole=0.3)
    st.plotly_chart(pie)

# Run the app
if __name__ == '__main__':
    app()
