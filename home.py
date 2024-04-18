import streamlit as st

st.title("Weather Forecast for the next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")
dataType = st.selectbox("Select Data to View", ['Temperature', 'Sky'])
st.subheader(f"{dataType} for the next {days} days in {place}")

