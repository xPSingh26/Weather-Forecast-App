import streamlit as st
import plotly.express as px
from data import get_data

st.title("Weather Forecast for the next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")
dataType = st.selectbox("Select Data to View", ['Temperature', 'Sky'])
st.subheader(f"{dataType} for the next {days} days in {place}")

d, t = get_data(place, days, dataType)
figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
