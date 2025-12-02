import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
df_california = pd.DataFrame(housing.data, columns=housing.feature_names)

df_california["Target"] = housing.target

df_california.head()

faltantes = df_california.isnull().sum()
st.write("Valores faltantes por columna")
st.write(faltantes)

#%%
st.write("Primeras 5 filas del DataFrame")
st.dataframe(df_california.head())

st.write("Tipos de datos de cada columna")
st.write(df_california.dtypes)

st.sidebar.markdown("Analisis de housing en California")

min_age = df_california["HouseAge"].min()
max_age = df_california["HouseAge"].max()

age_range = st.slider(
    "Selecciona el rango de edad de la vivienda",
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age))

min_lat = df_california["Latitude"].min()
max_lat = df_california["Latitude"].max()

lat_min = st.number_input(
    "Selecciona la latitud mínima",
    min_value=min_lat,
    max_value=max_lat,
    value=min_lat)

df_filtered = df_california[df_california["Latitude"] >= lat_min]

plt.hist(df_filtrado['MedHouseVal'])
st.pyplot()

plt.scatter(df_filtrado['MedInc'], df_filtrado['MedHouseVal'])
st.pyplot()