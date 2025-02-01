import streamlit as st

# Set the page to wide layout
st.set_page_config(layout='wide')

# Set the title of the app
st.title("My Cool Streamlit App")  

# Add a header and subheader
st.header("Welcome to My App")
st.subheader("This is a simple app with metrics and a chart")
st.divider()  # Adds a line divider

# Metrics with f-strings showing the delta as a percentage
old_temperature = 68
new_temperature = 70
temperature_delta = ((new_temperature - old_temperature) / old_temperature) * 100

old_wind_speed = 8
new_wind_speed = 9
wind_speed_delta = ((new_wind_speed - old_wind_speed) / old_wind_speed) * 100

old_humidity = 80
new_humidity = 86
humidity_delta = ((new_humidity - old_humidity) / old_humidity) * 100

# Create columns for layout
col1, col2, col3 = st.columns(3)

# Display metrics in columns using f-strings to show the delta as a percentage
col1.metric("Temperature", f"{new_temperature} °F", f"{temperature_delta:.2f}%")
col2.metric("Wind Speed", f"{new_wind_speed} mph", f"{wind_speed_delta:.2f}%")
col3.metric("Humidity", f"{new_humidity}%", f"{humidity_delta:.2f}%")

# Create a simple DataFrame for the line chart
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x': np.arange(100),  # X-axis data (numbers from 0 to 99)
    'y': np.random.randn(100)  # Y-axis data (random numbers)
})

# Display the line chart
st.line_chart(data)





