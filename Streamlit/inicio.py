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
    # CSS para estilizar el fondo y el contenido
    page_bg_img = f'''
    <style>
    body {{
        background-image: url("data:image/png;base64,{get_image_b64('/mnt/data/image.png')}");
        background-size: cover;
        background-position: center;
        opacity: 0.9;  /* Ajustar la opacidad */
    }}

    .stApp {{
        background: rgba(34, 34, 51, 0.7);  /* Fondo semitransparente para el contenido */
    }}

    h1 {{
        color: #1fbad6;
        text-align: center;
        margin-top: 50px;
        font-size: 48px;
        font-weight: bold;
    }}

    p {{
        color: #c0c0c8;
        text-align: center;
        font-size: 22px;
        margin-top: -10px;
    }}

    .centered {{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 80vh;  /* Para centrar verticalmente */
    }}
    </style>
    '''
    
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Crear el contenedor para centrar el contenido
    st.markdown('<div class="centered">', unsafe_allow_html=True)

    # Mostrar el logo de Uber centrado
    st.image("./Streamlit/images/uber_logo.png", width=300)

    # Título y descripción centrados
    st.markdown("<h1>Bienvenido a nuestro proyecto Uber</h1>", unsafe_allow_html=True)
    st.markdown("<p>Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Cargar la imagen de fondo en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None
