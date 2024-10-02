import streamlit as st
import acercaDe  # Importar la página 'home.py'
import dashboard  # Importar la página 'dashboard.py'
import modelos  # Importar la página 'modelos_ml.py'
import inicio # Importar la página 'inicio.py'
import base64
from PIL import Image

def modelos_page():
    st.title("Modelos de Machine Learning")
    st.write("Aquí se mostrarán los modelos de Machine Learning.")
