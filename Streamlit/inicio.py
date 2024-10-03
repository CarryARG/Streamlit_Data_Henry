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
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

# Estilos personalizados para el navbar, logo circular y eliminar espacios
def navbar_style():
    st.markdown(
        """
        <style>
        /* Estilo del navbar */
        .navbar {{
            background-color: #000;
            padding: 10px 20px;
        }}

        /* Botones del navbar */
        .navbar a {{
            color: #fff;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
        }}

        /* Efecto hover en los botones del navbar */
        .navbar a:hover {{
            background-color: #1c1c1c;
            border-radius: 4px;
        }}

        /* Eliminar espacios en la parte superior */
        .block-container {{
            padding-top: 0 !important;
        }}

        /* Logo circular */
        .logo {{
            border-radius: 50%;
            width: 150px;
            height: 150px;
            border: 5px solid #56B5BF;  /* Borde de color similar a la referencia */
        }}

        /* Centrando el contenido principal */
        .content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;  /* Asegurarse de ocupar toda la pantalla */
            color: white;
            text-align: center;
        }}

        /* Íconos sociales centrados */
        .social-icons {{
            display: flex;
            justify-content: center;
            margin-top: 15px;
        }}
        .social-icons a {{
            color: white;
            margin: 0 10px;
            font-size: 24px;
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

    # Mostrar el logo circular y el texto
    if logo_b64:
        st.markdown(
            f"""
            <div class="content">
                <img src="data:image/png;base64,{logo_b64}" alt="Uber Logo" class="logo">
                <h1 style="color: #56B5BF; margin-top: 20px;">Nick Perez</h1>
                <h3 style="color: #F2F2F2;">Ingeniero de Software - Experto UI/UX</h3>
                <div class="social-icons">
                    <a href="#"><i class="fab fa-facebook"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-linkedin"></i></a>
                    <a href="#"><i class="fab fa-github"></i></a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("Logo image not found!")

