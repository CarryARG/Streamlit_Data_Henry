import streamlit as st
import base64
from PIL import Image

# Function to convert an image to base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image not found at {image_path}")
        return None

# Function to set the background of the page with a slight transparency
def set_background(png_file, alpha=0.8):
    encoded_image = get_image_b64(png_file)
    if encoded_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_image}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
                background-color: rgba(0,0,0,{alpha});
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

# Function to set the logo and reduce space between navbar and logo
def inicio_page():
    # Set the background with 80% opacity
    set_background('./Streamlit/images/wallpaper_uber.png', alpha=0.8)

    # Get the logo image in base64
    logo_b64 = get_image_b64('./Streamlit/images/uber_logo1.png')

    # Check if logo is loaded correctly
    if logo_b64:
        # Reduce vertical spacing with 'mt-1' class and set smaller logo size
        st.markdown(
            f"""
            <div class="container-fluid d-flex justify-content-center align-items-center" style="height: 15vh;">
                <div class="row text-center">
                    <div class="col">
                        <img src="data:image/png;base64,{logo_b64}" alt="Uber Logo" style="width: 120px; margin-top: 1rem;">  
                        <p></p>
                        <p></p>
                        <h1 class="mt-1" style="color: #ffffff; text-shadow: 1px 1px 2px #000000; font-size: 4.2rem; font-weight: bold;">Data Product by Arcope</h1>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("Logo image not found!")
