import streamlit as st
import acercaDe  # Import the page 'home.py'
import dashboard  # Import the page 'dashboard.py'
import modelos  # Import the page 'modelos_ml.py'
import inicio  # Import the page 'inicio.py'
from PIL import Image

def set_background(png_file):
    """Loads the image and sets it as the background using CSS."""
    with open(png_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

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
        unsafe_allow_html=True,
    )


def inicio_page():
    """Displays the 'inicio' page with the logo from the specified path."""

    # Set the background using the set_background function
    set_background('./Streamlit/images/wallpaper_uber.png')

    # Structure the page with Bootstrap and center the content
    st.markdown(
        """
        <div class="container-fluid d-flex justify-content-center align-items-center" style="height: 100vh;">
            <div class="row text-center">
                <div class="col">
                    <img src="./Streamlit/images/uber_logo.png" alt="Uber Logo" style="width: 150px;">  <h1 class="mt-3" style="color: #56B5BF;">Bienvenido a nuestro proyecto Uber</h1>
                    <p style="color: #F2F2F2;">Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Assuming your app starts from the 'inicio' page
inicio_page()