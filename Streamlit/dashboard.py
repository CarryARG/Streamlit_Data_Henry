import streamlit as st
import home  # Importar la página 'home.py'
import dashboard
import modelos
import base64
from PIL import Image

def dashboard_page():
    st.title("Dashboard")
    st.write("Aquí se mostrará el dashboard con gráficas y KPIs.")
