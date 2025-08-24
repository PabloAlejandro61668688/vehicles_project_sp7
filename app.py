import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('C:\\Users\\PABLITO\\Sprint 7 tripleten\\vehicles_project_sp7\\vehicles_us.csv')

st.header("Análisis de datos de anuncios de vehículos")

# Crear una casilla de verficación para el histograma
buid_histogram = st.checkbox('Construir histograma')

if buid_histogram: # si la casilla de verificacion está seleccionada
    # escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')   
    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verficación para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter: # si la casilla de verificacion está seleccionada
    # escribir un mensaje
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')   
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
