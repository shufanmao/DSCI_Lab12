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
# Slider for selling price range
price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))
# Slider for year range
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))
# Button to apply filters
if st.sidebar.button('Submit'):
    filtered_data = data
    
    # Filter by car name if provided
    if car_name:
        filtered_data = filtered_data[filtered_data['car_name'].str.contains(car_name, case=False)]
    
    # Filter by transmission type
    filtered_data = filtered_data[filtered_data['transmission'].isin(transmission_type)]
    
    # Filter by selling price range
    filtered_data = filtered_data[(filtered_data['selling_price'] >= price_range[0]) & (filtered_data['selling_price'] <= price_range[1])]
    
    # Filter by year range
    filtered_data = filtered_data[(filtered_data['year'] >= year_range[0]) & (filtered_data['year'] <= year_range[1])]
    
    st.write(filtered_data)
else:
    # Display original data
    st.write(data)

