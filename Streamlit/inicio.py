import streamlit as st
import base64
from PIL import Image

# Función para convertir una imagen en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image not found at {image_path}")
        return None

# Función para establecer el fondo de la página
def set_background(png_file):
    encoded_image = get_image_b64(png_file)
    if encoded_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_image}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

# Estilos personalizados para el navbar y logo circular
def navbar_style():
    st.markdown(
        """
        <style>
        /* Estilo del navbar con colores de Uber */
        .navbar {{
            background-color: #000; /* Color negro */
            padding: 10px 20px;
        }}

        /* Botones del navbar */
        .navbar a {{
            color: #fff;  /* Texto en blanco */
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
        }}

        /* Efecto hover en los botones del navbar */
        .navbar a:hover {{
            background-color: #1c1c1c; /* Color gris oscuro al hacer hover */
            border-radius: 4px;
        }}

        /* Eliminar espacios en la parte superior */
        .block-container {{
            padding-top: 0 !important;
        }}

        /* Logo circular */
        .logo {{
            border-radius: 50%;  /* Borde circular */
            width: 150px;
            height: 150px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Página de inicio
def inicio_page():
    # Aplicar el estilo del navbar
    navbar_style()

    # Establecer el fondo
    set_background('./Streamlit/images/wallpaper_uber.png')

    # Obtener la imagen del logo en base64
    logo_b64 = get_image_b64('./Streamlit/images/uber_logo1.png')
    
    # Comprobar si se ha cargado correctamente el logo
    if logo_b64:
        # Mostrar el logo circular y el texto
        st.markdown(
            f"""
            <div class="container-fluid d-flex justify-content-center align-items-center" style="height: 100vh;">
                <div class="row text-center">
                    <div class="col">
                        <img src="data:image/png;base64,{logo_b64}" alt="Uber Logo" class="logo">
                        <h1 class="mt-3" style="color: #56B5BF;">Bienvenido a nuestro proyecto Uber</h1>
                        <p style="color: #F2F2F2;">Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("Logo image not found!")
    
    # Agregar contenido debajo de la imagen con scroll
    st.markdown(
        """
        <div style="margin-top: 50px;">
            <h2 style="color: #56B5BF;">Información del Proyecto</h2>
            <p style="color: #F2F2F2;">Aquí puedes agregar información relevante sobre el proyecto de Uber...</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
