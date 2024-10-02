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
    import streamlit as st
  
  # Configurar la página en modo "wide"
  st.set_page_config(layout="wide")
  
  # CSS para personalizar el estilo
  page_bg_img = '''
  <style>
  body {
      background-image: url("./Streamlit/images/wallpaper_uber.jpg");
      background-size: cover;
      background-position: center;
  }
  
  h1, h2 {
      color: #1fbad6;
      text-align: center;
  }
  
  p {
      color: #c0c0c8;
      font-size: 20px;
      text-align: center;
  }
  
  header {
      text-align: center;
      margin-bottom: 50px;
  }
  
  </style>
  '''
  
  st.markdown(page_bg_img, unsafe_allow_html=True)
  
  # Mostrar logo de Uber
  st.image("./Streamlit/images/uber_logo.png", width=300)
  
  # Título y descripción
  st.markdown("<h1>Bienvenido a nuestro proyecto Uber</h1>", unsafe_allow_html=True)
  st.markdown("<p>Explorando la revolución del transporte con análisis y predicciones para mejorar la experiencia del usuario.</p>", unsafe_allow_html=True)
