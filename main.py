import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place:')
days = st.slider(label='Forecast Days', min_value=1, max_value=5,
                 help='Select a number of forecasted days')
data_to_display = st.selectbox(
    'Select data to view:',
    ('Temperature', 'Sky'))
st.subheader(f'{data_to_display} for the next {days} days in {place}')
if place:
    try:
        filtered_data = get_data(place, days)

        if data_to_display == "Temperature":
            temperatures = [((dict["main"]["temp"] / 10) - 32) * (5 / 9) for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={'x': f'Days',
                                     'y': 'Temperature'})
            st.plotly_chart(figure)
        if data_to_display == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            list_of_paths = []
            for condition in sky_conditions:
                image_path = f"images/{condition.lower()}.png"
                list_of_paths.append(image_path)

            st.image(list_of_paths, width=100)
    except KeyError:
        st.write("The place you entered does not exist")


