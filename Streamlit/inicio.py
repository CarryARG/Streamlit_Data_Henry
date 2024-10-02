import streamlit as st
import base64

# Función para cargar imágenes en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None

def inicio_page():
    # CSS para personalizar el estilo de la página
    page_bg_img = '''
    <style>
    body {
        background-image: url("./Streamlit/images/wallpaper_uber.jpg");
        background-size: cover;
        background-position: center;
        filter: brightness(0.7); /* Sombra sobre la imagen de fondo */
    }
    
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh; /* Altura para centrar verticalmente */
        flex-direction: column;
    }

    h1 {
        color: #1fbad6;
        text-align: center;
        font-size: 48px;
        margin-top: 20px;
    }

    p {
        color: #c0c0c8;
        font-size: 24px;
        text-align: center;
        max-width: 800px;
        margin: auto;
    }

    </style>
    '''
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    # Contenedor para centrar el contenido
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    
    # Mostrar logo de Uber centrado
    st.image("./Streamlit/images/uber_logo.png", width=300)
    
    # Título y descripción
    st.markdown("<h1>Bienvenido a nuestro proyecto Uber</h1>", unsafe_allow_html=True)
    st.markdown("<p>Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>", unsafe_allow_html=True)
    
    # Cerrar el contenedor
    st.markdown('</div>', unsafe_allow_html=True)

