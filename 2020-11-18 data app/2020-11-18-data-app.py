import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import os

def main(df, filename):
    page = st.sidebar.selectbox('Choisir', ['Accueil', 'Shape', 'Statistiques descriptives', 'Data visualisation'])

    if page == 'Accueil':
        st.subheader('Raw data')
        st.write(df)

        st.subheader('Liste des colonnes')
        st.write(df.columns.tolist())

        st.subheader('Type des colonnes')
        st.write(df.dtypes)
    elif page == 'Shape':
        st.subheader('Shape du dataset')
        if filename == '.\dataset\indian_food.csv':
            nuage_points = alt.Chart(df).mark_circle().encode(x='cook_time', y='diet')
            st.write(nuage_points)
        elif filename == ".\dataset\\top_500_songs.csv":
            nuage_points = alt.Chart(df).mark_circle().encode(x='title', y='streak')
            st.write(nuage_points)
    elif page == 'Statistiques descriptives':
        st.subheader('Statistiques descriptives du dataset')
        st.dataframe(df.describe())
    else:
        st.subheader('Heatmap')
        if filename == ".\dataset\\top_500_songs.csv":
            st.write('Il n\'y a pas de données numériques dans ce dataset.')
        else:
            fig, ax = plt.subplots(figsize=(5,5))
            sns.heatmap(df.corr(), annot=True, ax=ax)
            st.pyplot(fig)
            st.subheader('Bar chart')
            st.bar_chart(df)

def file_selector(folder_path='.\dataset'):
    filenames = os.listdir(folder_path)
    selected_filename = st.sidebar.selectbox('Choisir un fichier', filenames)
    return os.path.join(folder_path, selected_filename)

if __name__ == '__main__':
    filename = file_selector()
    df = pd.read_csv(filename)
    if filename == ".\dataset\indian_food.csv":
        st.title('Indian Food')
    elif filename == ".\dataset\\top_500_songs.csv":
        st.title('Top 500 Songs')
    main(df, filename)