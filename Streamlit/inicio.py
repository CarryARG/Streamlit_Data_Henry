import streamlit as st
import acercaDe  # Importar la página 'home.py'
import dashboard  # Importar la página 'dashboard.py'
import modelos  # Importar la página 'modelos_ml.py'
import inicio # Importar la página 'inicio.py'
import base64
from PIL import Image


# Función para establecer el fondo
def set_background():
    st.markdown(
        """
        <style>
        .stApp {{
            background-image: url("https://www.example.com/your-image-path.png");
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
    # Establecer fondo (si es una URL pública o una ruta correcta)
    set_background()

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
