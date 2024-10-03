import streamlit as st
import base64
from PIL import Image


def set_background(png_file):
    # Leer la imagen local y codificarla en base64
    with open(png_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # Insertar la imagen en el fondo con una superposición oscura usando CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            position: relative;
        }}
        /* Agregar una capa de superposición para oscurecer */
        .stApp::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5); /* Superposición negra con opacidad */
            z-index: -1; /* Debe estar detrás del contenido */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def inicio_page():
    # Establecer el fondo usando la imagen local
    set_background('./Streamlit/images/wallpaper_uber.png')

    # Mostrar el logo usando st.image en lugar de HTML
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)  # Espacio superior
    st.image('./Streamlit/images/uber_logo.png', width=150)

    # Texto de bienvenida
    st.markdown("""
        <h1 style='text-align: center; color: #56B5BF;'>Bienvenido a nuestro proyecto Uber</h1>
        <p style='text-align: center; color: #F2F2F2;'>Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>
    """, unsafe_allow_html=True)


# Ejecutar la página de inicio
inicio_page()
