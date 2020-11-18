import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

st.title('House pricing')

DATE_COLUMN = 'date/time'
price = pd.read_csv("house_pricing.csv")

st.subheader('Raw data')
st.write(price)

st.subheader('Liste des colonnes')
st.write(price.columns.tolist())

st.subheader('Type des colonnes')
st.write(price.dtypes)

st.subheader('Shape du dataset')
c = alt.Chart(price).mark_circle().encode(
    x='LotArea', y='SalePrice'
)
st.write(c)

st.subheader('Statistiques descriptives du dataset')
st.write(price.describe())

st.subheader('Heatmap')
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(price.corr(), annot=True, ax=ax)
st.pyplot(fig)
#df_price = pd.DataFrame(price)
#st.dataframe(df_price)