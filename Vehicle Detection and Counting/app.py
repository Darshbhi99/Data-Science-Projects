from flask import render_template, request, Flask
import numpy as np
from PIL import Image
import cv2
import random
import string
import os

app = Flask(__name__)

INITIAL_FILE_UPLOADS= "./static/images"
car_cascade_src = "static/car_front.xml"
bus_cascade_src = "static/bus_front.xml"

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        full_filename = "../static/images/white_bg.png"
        return render_template('index.html', full_filename = full_filename, text = ['No Text'])
    # Executing 
    if request.method == "POST":
        image = request.files['image_upload']
        image = Image.open(image)

        letter = string.ascii_lowercase
        name = "".join(random.sample(letter, 10))+".png"
        #location where final file will be stored
        full_filename = "../static/images/"+ name 

        img_array = np.array(image) # Converting image to array
        img_gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY) # Converting array to gray
        # blur = cv2.GaussianBlur(img_gray, (5,5), 0) # converting the grey image into blur
        # dilated = cv2.dilate(blur, np.ones((3,3))) # Converting blur image into dilated image
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2)) # creating a kernel for morphing the image
        # closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel) # Converting the dilated image into morphed
        # Cars Detection
        car_cascade = cv2.CascadeClassifier(car_cascade_src) # Initializing the casacade classifier function
        cars = car_cascade.detectMultiScale(img_gray, 1.1, 1) # detecting the cars in the image
        cnt = 0 # setting the counter for cars detected
        for (x,y,w,h) in cars:
            # Adding the rectangle around the cars detected
            cv2.rectangle(img_array, (x,y), (x+w,y+h), (255,0,0), 2) 
            cnt+=1
        print(cnt, "Cars found")
        # Buses Detection 
        bus_cascade = cv2.CascadeClassifier(bus_cascade_src) # Initializing the classifier 
        bus = bus_cascade.detectMultiScale(img_gray, 1.1, 1) # Detecting the buses
        bcnt = 0
        for (x,y,w,h) in bus:
            cv2.rectangle(img_array, (x,y),(x+h,y+w), (0,255,0), 2)
            bcnt+=1
        img = Image.fromarray(img_array) # Converting array to image
        img.save(os.path.join(INITIAL_FILE_UPLOADS,name)) # saving the output image
        result = f"The image has {cnt} number of cars and {bcnt} number of buses"
        return render_template('index.html', full_filename = full_filename, prediction = result)

if __name__ == "__main__":
    app.run(debug = True)