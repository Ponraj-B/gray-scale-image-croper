# 🖼️ Image Cropper & Grayscale Converter

A simple and interactive web app that allows you to upload images, crop any portion of them, and convert the cropped area to grayscale — all powered by Python, NumPy, and Streamlit.

---

## 🚀 Try It Online

Access the live app here:  
👉 [https://grayscaleimagecropper.streamlit.app/](https://grayscaleimagecropper.streamlit.app/)

---

## Features

- Upload images in JPG, JPEG, or PNG format  
- Specify cropping rectangle by entering starting coordinates (`x`, `y`) and size (`width`, `height`)  
- Convert the cropped portion into a grayscale image  
- Preview the cropped grayscale image instantly  
- Download the cropped grayscale image with one click  

---

## Tech Stack

- [Streamlit](https://streamlit.io/) — Web UI and deployment  
- [NumPy](https://numpy.org/) — Image array manipulation  
- [Pillow (PIL)](https://python-pillow.org/) — Image processing  

---

## How to Use

1. Click **Upload an image** and select a file from your computer  
2. Enter the starting pixel coordinates `(x, y)` for cropping  
3. Specify the `width` and `height` for the crop area  
4. Click **Crop and Convert to Grayscale**  
5. View the result and download the grayscale cropped image if desired  

---

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/image-crop-app.git
   cd image-crop-app

2. Instal dependencies

   ```bash
   pip install -r requirements.txt

3. Run the App

   ```bash
   streamlit run image_crop_app.py

   
