import streamlit as st
import pandas as pd

st.set_page_config(layout='centered')


st.title('Weather Forecast for the Next Days')

place = st.text_input('Place:')
days = st.slider(label='Forecast Days', min_value=1, max_value=5,
                 help='Select a number of forecasted days')
data_to_display = st.selectbox(
    'Select data to view:',
    ('Temperature', 'Sky'))

st.subheader(f'{data_to_display} for the next {days} days in {place}')

