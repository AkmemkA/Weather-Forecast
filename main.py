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

data = get_data(place, days, data_to_display)

st.write(data)

#figure = px.scatter(x=df[x_axis], y=df[y_axis],
              #      labels={'x': f'{x_axis.replace("_", " ").title()}',
                            'y': f'{y_axis.replace("_", " ").title()}'})
#st.plotly_chart(figure)

