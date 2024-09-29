import streamlit as st

import home  # Importar la página 'home.py'

import dashboard  # Importar la página 'dashboard.py'

import modelos  # Importar la página 'modelos_ml.py'

import base64



# Configuración general de la página (debe ir antes de cualquier otro comando de Streamlit)

st.set_page_config(page_title="ARCOPE App", layout="wide", initial_sidebar_state="auto")

# Limpiar la caché al cargar la página

st.cache_data.clear()





# Función para cargar imágenes en base64

def get_image_b64(image_path):

    try:

        with open(image_path, "rb") as image_file:

            return base64.b64encode(image_file.read()).decode()

    except FileNotFoundError:

        return None



# Incluir Bootstrap CSS y JavaScript
st.markdown("""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9P/ScQsAP7hUibX39j13EVY4pQ11VVn1+kpZ60" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)


# Capturar los parámetros de consulta
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]  # Página predeterminada es 'home'


# CSS para personalizar el navbar y eliminar los espacios sobrantes

st.markdown(""" 

    <style>

        footer {visibility: hidden;} /* Ocultar el pie de página */

        header {visibility: hidden;} /* Ocultar el header */

        .css-18e3th9 {padding: 0;} /* Eliminar padding sobrante */

        #MainMenu {visibility: visible;} /* Asegurarse de que el menú de Streamlit esté visible */

        .nav-item {

            background-color: #F2A649;

            color: #FFF;

            padding: 10px 20px;

            border-radius: 5px;

            text-decoration: none; /* Eliminar subrayado */

        }



        .nav-item:hover {

            background-color: #F25E3D; /* Color más oscuro para el hover */
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2); /* Sombra suave */
            text-decoration: none; /* Eliminar subrayado */
            transform: scale(1.2); /* Aumentar el tamaño al pasar el mouse */

        }



        .navbar-custom {

            background-color: #000000;

            padding: 20px;

            display: flex;

            justify-content: space-around;

            width: 100%; /* Ocupa todo el ancho de la pantalla */

            margin: 0; /* Eliminar margen superior */

            position: fixed; /* Fijar el navbar en la parte superior */

            top: 0;

            left: 0;

            z-index: 1000; /* Asegurar que quede encima de otros elementos */

        }



        .css-18e3th9 {

            padding: 0;

        }



        .main-content {

            margin-top: 80px;  /* Ajusta según la altura del navbar */

        }



    </style>

""", unsafe_allow_html=True)


# HTML para el Navbar utilizando Bootstrap con los botones personalizados
st.markdown(f"""
    <nav class="navbar-custom">
        <a href="?page=home" class="nav-item" style="color: whitesmoke; font-size: 18px;">Home</a>
        <a href="?page=dashboard" class="nav-item" style="color: whitesmoke; font-size: 18px;">Dashboard</a>
        <a href="?page=modelos" class="nav-item" style="color: whitesmoke; font-size: 18px;">Modelos</a>
    </nav>
""", unsafe_allow_html=True)

# Mostrar el menú de Streamlit (los tres puntos) debajo del navbar
st.markdown("""
    <div style="margin-top: 10px;">
        <div id="MainMenu"></div> <!-- Esto mostrará el menú de Streamlit -->
    </div>
""", unsafe_allow_html=True)

if page == "home":
    st.experimental_set_query_params(page="home")
    home.home_page()
elif page == "dashboard":
    st.experimental_set_query_params(page="dashboard")
    dashboard.dashboard_page()
elif page == "modelos":
    st.experimental_set_query_params(page="modelos")
    modelos.modelos_page()
else:
    st.error("Página no encontrada")