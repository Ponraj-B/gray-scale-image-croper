import streamlit as st
from PIL import Image
import numpy as np

def crop_image(img_array, x, y, width, height):
    cropped = img_array[y:y+height, x:x+width]
    cropped_gray = cropped.mean(axis=2).astype(np.uint8)
    return cropped_gray

st.title("🖼️ Image Cropper & Grayscale Converter")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    h, w = image_np.shape[:2]

    st.image(image, caption="Original Image", use_column_width=True)
    st.write(f"Image Dimensions: {w} x {h}")

    x = st.number_input("Start X", min_value=0, max_value=w - 1, value=0)
    y = st.number_input("Start Y", min_value=0, max_value=h - 1, value=0)
    crop_width = st.number_input("Crop Width", min_value=1, max_value=w - x, value=min(300, w - x))
    crop_height = st.number_input("Crop Height", min_value=1, max_value=h - y, value=min(300, h - y))

    if st.button("Crop and Convert to Grayscale"):
        result_array = crop_image(image_np, x, y, crop_width, crop_height)
        result_image = Image.fromarray(result_array)

        st.image(result_image, caption="Cropped Grayscale Image", use_column_width=True)

        st.download_button(
            label="📥 Download Cropped Image",
            data=result_image.tobytes(),
            file_name="cropped_image.jpg",
            mime="image/jpeg"
        )
