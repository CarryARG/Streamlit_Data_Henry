import streamlit as st
import base64
from PIL import Image







import streamlit as st

def inicio_page():
    st.set_page_config(layout="wide")  # Ajusta el ancho de la página

    # Establecer el fondo
    st.markdown("""
        <style>
        .stApp {
            background-image: url('./Streamlit/images/wallpaper_uber.png');
            background-size: cover;
        }
        </style>
        """, unsafe_allow_html=True)

    # Mostrar el logo
    st.image("./Streamlit/images/uber_logo.png")

    # Texto de bienvenida
    st.title("Bienvenido a nuestro proyecto Uber")
    st.write("Explorando la revolución del transporte...")

inicio_page()
