import streamlit as st
import base64
from PIL import Image
import acercaDe
import inicio
import modelos
import dashboard

# Función para convertir imagen a base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image not found at {image_path}")
        return None

def inicio_page():
    # Importa los otros módulos o scripts si es necesario
    # import home, dashboard, modelos, etc.
    
    # Contenido HTML para la tarjeta con Bootstrap
    card_html = """
    <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh; background: url('background-image-url.jpg') no-repeat center center fixed; background-size: cover;">
      <div class="card text-center" style="width: 18rem; background-color: rgba(0, 0, 0, 0.7); border: none;">
        <div class="card-body">
          <img src="logo.png" class="rounded-circle" style="width: 150px; height: 150px; object-fit: cover;" alt="Logo">
          <h5 class="card-title text-white mt-3">Nick Perez</h5>
          <p class="card-text text-white">Ingeniero de Software - Experto UI/UX</p>
          <div>
            <a href="#" class="btn btn-outline-light btn-sm mx-1"><i class="fab fa-facebook"></i></a>
            <a href="#" class="btn btn-outline-light btn-sm mx-1"><i class="fab fa-twitter"></i></a>
            <a href="#" class="btn btn-outline-light btn-sm mx-1"><i class="fab fa-linkedin"></i></a>
            <a href="#" class="btn btn-outline-light btn-sm mx-1"><i class="fab fa-github"></i></a>
          </div>
        </div>
      </div>
    </div>
    """
    
    # Usamos st.markdown para integrar el HTML con Streamlit
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Recuerda ajustar las rutas de las imágenes y cualquier otro archivo externo

