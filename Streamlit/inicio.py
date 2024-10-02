import streamlit as st
import acercaDe  # Importar la página 'home.py'
import dashboard  # Importar la página 'dashboard.py'
import modelos  # Importar la página 'modelos_ml.py'
import inicio # Importar la página 'inicio.py'
import base64
from PIL import Image

# Función para cargar imágenes en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None

def inicio_page():
    # CSS básico para personalizar el estilo
    st.markdown("""
    <style>
    /* Fondo de pantalla sombreado */
    .stApp {
        background-image: url('https://via.placeholder.com/1920x1080.png');  /* Cambia por la ruta correcta */
        background-size: cover;
        background-position: center;
        filter: brightness(0.7);
    }

    /* Contenedor centrado */
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh; /* Altura para centrar verticalmente */
        flex-direction: column;
        text-align: center;
    }

    /* Título de bienvenida */
    h1 {
        color: #1fbad6;
        font-size: 48px;
        margin-top: 20px;
    }

    /* Descripción */
    p {
        color: #c0c0c8;
        font-size: 24px;
        max-width: 800px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    # Contenedor para centrar el contenido
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    
    # Mostrar logo de Uber centrado
    st.image("./Streamlit/images/uber_logo.png", width=300)

    # Título y descripción centrados
    st.markdown("<h1>Bienvenido a nuestro proyecto Uber</h1>", unsafe_allow_html=True)
    st.markdown("<p>Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>", unsafe_allow_html=True)
    
    # Cerrar el contenedor
    st.markdown('</div>', unsafe_allow_html=True)
