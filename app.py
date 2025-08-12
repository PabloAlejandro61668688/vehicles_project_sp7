import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv(r'C:\Users\PABLITO\Sprint 7 tripleten\vehicles_project_sp7\vehicles_us.csv')

st.header("Vehicle Data Analysis")
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)