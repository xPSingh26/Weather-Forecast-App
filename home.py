import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")
dataType = st.selectbox("Select Data to View", ['Temperature', 'Sky'])
st.subheader(f"{dataType} for the next {days} days in {place}")


def get_data(days):
    dates = ['2024-10-01', '2024-10-02', '2024-10-03']
    temperatures = [10, 9, 7]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
