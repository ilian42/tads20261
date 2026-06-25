import streamlit as st
from functions.plot import create_plot

st.title('Stock History')
st.write("Inform a ticker and check it's stock recent values.")

ticker = st.sidebar.text_input(
    'Choose the ticker:',
    value = 'NVDA'
)

fig = create_plot(ticker)
st.plotly_chart(fig)
