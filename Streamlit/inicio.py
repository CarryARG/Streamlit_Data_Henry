import streamlit as st
import base64
from PIL import Image
import acercaDe
import inicio
import modelos
import dashboard


    # Configuración de la página
    # st.set_page_config(page_title="Inicio", page_icon="🏠")

# Función para convertir imagen a base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image not found at {image_path}")
        return None

def inicio_page():
    # Estilos CSS para la página
    st.markdown(
        """
        <style>
            .index-page {
                background-image: url('ruta/a/tu/fondo.jpg'); /* Asegúrate de colocar la ruta correcta */
                background-size: cover;
                background-position: center;
                height: 100vh;
                color: white;
            }
            .logo {
                display: flex;
                align-items: center;
                font-size: 24px;
                color: #fff;
            }
            .hero {
                padding: 50px 0;
            }
            .btn-get-started {
                background-color: #F25A38; /* Color del botón */
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                text-decoration: none;
                margin-right: 10px;
            }
            .btn-get-started:hover {
                background-color: #F25041; /* Color del botón al pasar el mouse */
            }
            h1, h2 {
                font-weight: bold;
            }
        </style>
        """, unsafe_allow_html=True
    )
    
    # Contenido de la página
    st.markdown('<div class="index-page">', unsafe_allow_html=True)
    
    # Encabezado
    st.markdown('''
    <header id="header" class="header d-flex align-items-center fixed-top">
        <div class="container-fluid container-xl position-relative d-flex align-items-center">
            <a href="#" class="logo d-flex align-items-center me-auto">
                <img src="ruta/a/logo_uber.png" alt="Logo Uber" style="width: 150px;"> <!-- Asegúrate de colocar la ruta correcta -->
            </a>
            <nav id="navmenu" class="navmenu">
                <ul>
                    <li><a href="#hero" class="active">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#team">Team</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
            <a class="btn-get-started" href="#about">Get Started</a>
        </div>
    </header>
    ''', unsafe_allow_html=True)
    
    # Sección Hero
    st.markdown('''
    <main class="main">
        <section id="hero" class="hero section dark-background">
            <div class="container">
                <div class="row gy-4">
                    <div class="col-lg-6 d-flex flex-column justify-content-center" data-aos="zoom-out">
                        <h1>Better Solutions For Your Business</h1>
                        <p>We are team of talented designers making websites with Bootstrap</p>
                        <div class="d-flex">
                            <a href="#about" class="btn-get-started">Get Started</a>
                            <a href="https://www.youtube.com/watch?v=Y7f98aduVJ8" class="btn-watch-video d-flex align-items-center"><i class="bi bi-play-circle"></i><span>Watch Video</span></a>
                        </div>
                    </div>
                    <div class="col-lg-6 hero-img" data-aos="zoom-out" data-aos-delay="200">
                        <img src="assets/img/hero-img.png" class="img-fluid animated" alt="">
                    </div>
                </div>
            </div>
        </section>
    </main>
    ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


