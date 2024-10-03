import streamlit as st
import acercaDe  # Importar la página 'home.py'
import dashboard  # Importar la página 'dashboard.py'
import modelos  # Importar la página 'modelos_ml.py'
import inicio # Importar la página 'inicio.py'
import base64
from PIL import Image


def set_background(png_file):
    # Cargar la imagen y codificarla en base64
    with open(png_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # Insertar la imagen en el fondo usando CSS y base64
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )






def inicio_page():
    # Establecer fondo usando la imagen local codificada en base64
    set_background('./Streamlit/images/wallpaper_uber.png')

    # Estructura de la página con Bootstrap y centrado
    st.markdown("""
        <div class="container-fluid d-flex justify-content-center align-items-center" style="height: 100vh;">
            <div class="row text-center">
                <div class="col">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png" alt="Uber Logo" style="width: 150px;">
                    <h1 class="mt-3" style="color: #56B5BF;">Bienvenido a nuestro proyecto Uber</h1>
                    <p style="color: #F2F2F2;">Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)