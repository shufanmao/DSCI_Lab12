import streamlit as st
import pandas as pd

# Load the car data
@st.cache
def load_data():
    data = pd.read_csv('car_data.csv')
    return data

data = load_data()

# Sidebar
st.sidebar.header('Filter Options')
# Text input for car name
car_name = st.sidebar.text_input('Car Name')
# Multiselect for transmission type
transmission_type = st.sidebar.multiselect('Transmission Type', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])
# Slider for selling price range, adjust min and max according to your data
price_range = st.sidebar.slider('Selling Price Range', float(data['Selling_Price'].min()), float(data['Selling_Price'].max()), (float(data['Selling_Price'].min()), float(data['Selling_Price'].max())))
# Slider for year range, adjust min and max according to your data
year_range = st.sidebar.slider('Year Range', int(data['Year'].min()), int(data['Year'].max()), (int(data['Year'].min()), int(data['Year'].max())))
# Button to apply filters
if st.sidebar.button('Submit'):
    filtered_data = data
    
    # Filter by car name if provided
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False)]
    
    # Filter by transmission type
    filtered_data = filtered_data[filtered_data['Transmission'].isin(transmission_type)]
    
    # Filter by selling price range
    filtered_data = filtered_data[(filtered_data['Selling_Price'] >= price_range[0]) & (filtered_data['Selling_Price'] <= price_range[1])]
    
    # Filter by year range
    filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & (filtered_data['Year'] <= year_range[1])]
    
    st.write(filtered_data)
else:
    # Display original data
    st.write(data)
