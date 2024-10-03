import streamlit as st
import base64
from PIL import Image

# Función para convertir imagen a base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image not found at {image_path}")
        return None

# Establecer el fondo utilizando una imagen
def set_background(png_file):
    encoded_image = get_image_b64(png_file)
    if encoded_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_image}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

# Estilos de Bootstrap para el card y navbar
def navbar_style():
    st.markdown(
        """
        <style>
        /* Card centrado en el medio de la pantalla */
        .card {{
            max-width: 400px;
            margin: auto;
            background-color: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            padding: 20px;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }}

        /* Imagen del perfil dentro del card */
        .card img {{
            border-radius: 50%;
            width: 150px;
            height: 150px;
            margin: 0 auto;
            display: block;
        }}

        /* Título y subtítulo centrados */
        .card h2, .card h4 {{
            text-align: center;
            margin-top: 15px;
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

# Página principal con la tarjeta de perfil y el fondo
def inicio_page():
    # Establecer el estilo con Bootstrap
    navbar_style()

    # Colocar la imagen de fondo
    set_background('./Streamlit/images/wallpaper_uber.png')

    # Obtener imagen de perfil en base64
    profile_pic_b64 = get_image_b64('./Streamlit/images/uber_logo1.png')

    # Estructura del card en Bootstrap
    if profile_pic_b64:
        st.markdown(
            f"""
            <div class="card">
                <img src="data:image/png;base64,{profile_pic_b64}" alt="Profile Picture">
                <h2>Nick Perez</h2>
                <h4>Ingeniero de Software - Experto UI/UX</h4>
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
        st.error("Profile image not found!")

