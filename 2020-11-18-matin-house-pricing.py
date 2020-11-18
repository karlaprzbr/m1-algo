import streamlit as st
import pandas as pd
import numpy as np

st.title('House pricing')

DATE_COLUMN = 'date/time'
data = pd.read_csv("house_pricing.csv")
st.write(data)
data2 = data.info()
st.write(data2)