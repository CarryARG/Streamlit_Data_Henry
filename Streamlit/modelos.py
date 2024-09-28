import streamlit as st
import home  # Importar la página 'home.py'
import dashboard
import modelos
import base64
from PIL import Image

def modelos_page():
    st.title("Modelos de Machine Learning")
    st.write("Aquí se mostrarán los modelos de Machine Learning.")
