from flask import render_template, request, Flask
from keras.models import load_model
import numpy as np
from PIL import Image
import cv2
import random
import string
import os

app = Flask(__name__)

INITIAL_FILE_UPLOADS= "./static/images"

model = load_model('model.h5')

all_labels = ['Speed limit (20km/h)', 'Speed limit (30km/h)', 'Speed limit (50km/h)', 'Speed limit (60km/h)',
            'Speed limit (70km/h)', 'Speed limit (80km/h)', 'End of speed limit(80km/h)', 'Speed limit (100km/h)',
            'Speed limit (120km/h)', 'No passing', 'No passing for vehicles over 3.5 metrics tons',
            'Right-of-way at the next intersection','Priority road', 'Yield', 'Stop', 'No vehicle',
            'Vehicle over 3.5 metric tons prohibited', 'No entry', 'General caution', 'Dangerous curve to the left',
            'Dangerous curve to the right', 'Double curve', 'Bumpy Road', 'Slippery Road', 'Road narrows to the right',
            'Road work','Traffic Signals', 'Pedestrians', 'Chidren Crossing', 'Bicycle Crossing', 'Beware of ice/snow',
            'Wild Animals Crossing', 'End of all speeds and crossing limits', 'Turn Right Ahead', 'Turn Left Ahead',
            'Ahead only', 'Go straight or right', 'Go straight or left', 'Keep right', 'Keep left',
            'Roundabout mandatory', 'End of no passing', 'End of no passing by vehicles over 3.5 metric']

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        full_filename = "../static/images/white_bg.png"
        return render_template('index.html', full_filename = full_filename, prediction = 'No Image Found')
    # Executing 
    if request.method == "POST":
        image = request.files['image_upload']
        image = Image.open(image)
        letter = string.ascii_lowercase
        name = "".join(random.sample(letter, 10))+".png"
        #location where final file will be stored
        full_filename = "../static/images/"+ name 
        image.save(os.path.join(INITIAL_FILE_UPLOADS,name))
        img = cv2.imread('static/images/'+name)
        img = cv2.resize(img, (50,50))
        img.shape = (1,50,50,3)
        img = img/255
        pred = model.predict(img)
        pred = np.argmax(pred)
        prediction = all_labels[pred]
        return render_template('index.html', full_filename = full_filename, prediction = prediction)

if __name__ == "__main__":
    app.run(debug = True)