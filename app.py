import cv2
import numpy as np
import streamlit as st
from PIL import Image

# App title
st.title("Image Thresholding App")

# Sidebar: Information about the app
st.sidebar.title("About This App")
st.sidebar.info(
    """
    Welcome to the Image Thresholding App! 🎨

    - **Purpose**: Apply custom RGB thresholds to images.
    - **Features**:
      - Upload any RGB image (JPG, JPEG, PNG).
      - Adjust Red, Green, and Blue channel thresholds interactively.
      - View the thresholded result instantly.
    """
)

# Upload image
uploaded_file = st.file_uploader("Upload an RGB image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Display the original image
    st.subheader("Original Image")
    st.image(image, caption="Original Image", use_container_width=True)

    # Sliders for thresholds on the main page
    st.subheader("Adjust Thresholds for Each Channel")
    col1, col2, col3 = st.columns(3)

    with col1:
        r_threshold = st.slider("Red Threshold", 0, 255, 127, key="red_thresh")
    with col2:
        g_threshold = st.slider("Green Threshold", 0, 255, 127, key="green_thresh")
    with col3:
        b_threshold = st.slider("Blue Threshold", 0, 255, 127, key="blue_thresh")

    # Function to apply threshold
    def apply_threshold(image, r_thresh, g_thresh, b_thresh):
        # Split channels
        b, g, r = cv2.split(image)
        # Apply thresholds
        _, r_bin = cv2.threshold(r, r_thresh, 255, cv2.THRESH_BINARY)
        _, g_bin = cv2.threshold(g, g_thresh, 255, cv2.THRESH_BINARY)
        _, b_bin = cv2.threshold(b, b_thresh, 255, cv2.THRESH_BINARY)
        # Merge channels back
        thresholded_image = cv2.merge([b_bin, g_bin, r_bin])
        return thresholded_image

    # Apply threshold
    thresholded_image = apply_threshold(image_np, r_threshold, g_threshold, b_threshold)

    # Display the thresholded image
    st.subheader("Thresholded Image")
    st.image(thresholded_image, caption="Thresholded Image", use_container_width=True)

else:
    st.info("Upload an image to start thresholding.")
