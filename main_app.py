import numpy as np
from keras.models import load_model
import streamlit as st
import cv2

model = load_model('dog_breed.h5')
Classes = ['scottish_deerhound', 'maltese_dog', 'bernese_mountain_dog']

# Set title of the App
st.title("Dog Breed Prediction")
# Asking the user to upload the image
st.markdown("Upload the image of the dog")

# Uploading the dog image
dog_image = st.file_uploader("Choose the Image....", type='png')
# Submit the image
submit = st.button('Predict')

# If submit is clicked
if submit:
    if dog_image is not None:
        # Convert the file into opencv image
        file_bytes = np.asarray(bytearray(dog_image.read()),dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes,1)
        # Displaying the Image
        st.image(opencv_image, channels='BGR')
        # Resizing the Image
        opencv_image  = cv2.resize(opencv_image, (224,224))
        # Convert image to 4 Dimensions
        opencv_image.shape = (1,224,224,3)
        # Predicting the image label
        y_pred = model.predict(opencv_image)
        st.title(str("The Dog breed is "+Classes[np.argmax(y_pred)]))