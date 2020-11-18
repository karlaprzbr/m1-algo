import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

def main():
    st.title('House pricing')
    df_house_pricing = pd.read_csv("house_pricing.csv")
    page = st.sidebar.selectbox('Choisir', ['Accueil', 'Shape', 'Statistiques descriptives', 'Heatmap'])

    if page == 'Accueil':
        st.subheader('Raw data')
        st.write(df_house_pricing)

        st.subheader('Liste des colonnes')
        st.write(df_house_pricing.columns.tolist())

        st.subheader('Type des colonnes')
        st.write(df_house_pricing.dtypes)
    elif page == 'Shape':
        st.subheader('Shape du dataset')
        nuage_points = alt.Chart(df_house_pricing).mark_circle().encode(
            x='LotArea', y='SalePrice'
        )
        st.write(nuage_points)
    elif page == 'Statistiques descriptives':
        st.subheader('Statistiques descriptives du dataset')
        st.dataframe(df_house_pricing.describe())
    else :
        st.subheader('Heatmap')
        fig, ax = plt.subplots(figsize=(90,90))
        sns.heatmap(df_house_pricing.corr(), annot=True, ax=ax)
        st.pyplot(fig)

if __name__ == '__main__':
    main()