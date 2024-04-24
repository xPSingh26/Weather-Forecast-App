import streamlit as st
import plotly.express as px
from data import get_data

st.title("Weather Forecast for the next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")
dataType = st.selectbox("Select Data to View", ['Temperature', 'Sky'])
st.subheader(f"{dataType} for the next {days} days in {place}")

if place:
    try:
        filteredData = get_data(place, days, dataType)
        if dataType == 'Temperature':
            temperatures = [filteredData[i]['main']['temp']/10 for i in range(len(filteredData))]
            dates = [dict['dt_txt'] for dict in filteredData]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if dataType == 'Sky':
            skyData = [dict['weather'][0]['main'] for dict in filteredData]
            dates = [dict['dt_txt'] for dict in filteredData]
            imagePath = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                         'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            images = [imagePath[condition] for condition in skyData]
            st.image(images, width=126)
    except KeyError:
        st.text("Please enter a valid location!")
