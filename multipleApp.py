
import streamlit as st
import os
import shutil
from PIL import Image
import numpy as np
from io import BytesIO
from API import transfer_style


# Set page configs. Get emoji names from WebFx
st.set_page_config(page_title="PixelMix - Style Transfer",
                   page_icon="./assets/favicon.png", layout="centered")

# -------------Header Section------------------------------------------------

title = '<p style="text-align: center;font-size: 50px;font-weight: 350;font-family:Cursive "> PixelMix </p>'
st.markdown(title, unsafe_allow_html=True)


st.markdown(
    "<b> <i> Create Digital Art using Machine Learning ! </i> </b>  &nbsp; We takes 2 images — Content Image & Style Image — and blends "
    "them together so that the resulting output image retains the core elements of the content image, but appears to "
    "be “painted” in the style of the style reference image.", unsafe_allow_html=True
)


# Example Image
st.markdown("</br>", unsafe_allow_html=True)


# -------------Sidebar Section------------------------------------------------

# -------------Body Section------------------------------------------------

# Upload Images
col1, col2 = st.columns(2)
content_image = None
style_image = None
with col1:
    content_images = st.file_uploader(
        "Upload Content Image (PNG & JPG images only)", type=['png', 'jpg'], accept_multiple_files=True)
with col2:
    style_image = st.file_uploader(
        "Upload Style Image (PNG & JPG images only)", type=['png', 'jpg'], accept_multiple_files=True)


st.markdown("</br>", unsafe_allow_html=True)
st.warning("Nothing to see here")



if content_images and style_image:
        
    for content_image in content_images:

        with st.spinner("Loading!"):

            #content_image = Image.open(content_image)
            #style_image = Image.open(style_image)
            
            name = content_image.name


            style_image = Image.open("/Users/basverhaak/Downloads/space.jpg")
            content_image = Image.open("/Users/basverhaak/Documents/INPUT_MGMT1/italy4/" + name)


            # Convert PIL Image to numpy array
            content_image = np.array(content_image)
            style_image = np.array(style_image)

            # Path of the pre-trained TF model
            model_path = r"model"

            # output image
            styled_image = transfer_style(content_image, style_image, model_path)

            col1, col2 = st.columns(2)
            with col1:
                # Display the output
                st.image(styled_image)
            with col2:

                st.markdown("</br>", unsafe_allow_html=True)
                st.markdown(
                    "<b> Your Image is Ready ! Click below to download it. </b>", unsafe_allow_html=True)

                # de-normalize the image
                styled_image = (styled_image * 255).astype(np.uint8)
                # convert to pillow image
                img = Image.fromarray(styled_image)
                buffered = BytesIO()
                img.save(buffered, format="JPEG")
                st.download_button(
                    key = name,
                    label="Download image",
                    data=buffered.getvalue(),
                    file_name="output" + name,
                    mime="image/png")
