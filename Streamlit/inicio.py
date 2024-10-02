import streamlit as st
import acercaDe  # Importar la página 'home.py'
import dashboard  # Importar la página 'dashboard.py'
import modelos  # Importar la página 'modelos_ml.py'
import inicio # Importar la página 'inicio.py'
import base64
from PIL import Image

        
def inicio_page():
    # Función para cargar la imagen de fondo
    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = f'''
        <style>
        body {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    
    # Llamada a la función para establecer el fondo
    set_background('./Streamlit/images/wallpaper_uber.jpg')
    
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
