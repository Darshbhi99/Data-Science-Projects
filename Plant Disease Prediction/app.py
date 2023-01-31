import numpy as np
from keras.models import load_model
import streamlit as st
import cv2

model = load_model('static/model.h5')
Classes = ['Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot']

# Set title of the App
st.title("Plant Disease Prediction")
# Asking the user to upload the image
st.markdown("Upload the image of the plant leaf")

# Uploading the dog image
leaf_image = st.file_uploader("Choose the Image....", type='png')
# Submit the image
submit = st.button('Predict')

# If submit is clicked
if submit:
    if leaf_image is not None:
        # Convert the file into opencv image
        file_bytes = np.asarray(bytearray(leaf_image.read()),dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes,1)
        # Displaying the Image
        st.image(opencv_image, channels='BGR')
        # Resizing the Image
        opencv_image  = cv2.resize(opencv_image, (256,256))
        # Convert image to 4 Dimensions
        opencv_image.shape = (1,256,256,3)
        # Predicting the image label
        y_pred = model.predict(opencv_image)
        st.title(str("The Plant Disease is "+Classes[np.argmax(y_pred)]))