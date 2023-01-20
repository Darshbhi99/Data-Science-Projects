from flask import render_template, request, Flask
import numpy as np
from PIL import Image
import random
import string
import cv2
import os

app = Flask(__name__)

INITIAL_FILE_UPLOADS= "./static/uploads"

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        full_filename = "../static/images/white_bg.png"
        return render_template('index.html', full_filename = full_filename)
    # Executing 
    if request.method == "POST":
        option = request.form['options']
        print(option)
        image = request.files['image_upload']
        image = Image.open(image)
        image = np.array(image.convert('RGB'))
        h_image, w_image, _ = image.shape

        letter = string.ascii_lowercase
        name = "".join(random.sample(letter, 10))+".png"
        #location where final file will be stored
        full_filename = "../static/uploads/"+ name 

        if option == "logo_watermark":
            logo_upload = request.files['logo_upload']
            logo = Image.open(logo_upload)
            logo = np.array(logo.convert('RGB'))
            h_logo, w_logo, _ = logo.shape
            centre_y = int(h_image/2)
            centre_x = int(w_image/2)
            top_y = centre_y - int(h_logo/2)
            bottom_y = top_y + h_logo
            left_x = centre_x - int(w_logo/2)
            right_x = left_x + w_logo

            roi = image[top_y:bottom_y,left_x:right_x]
            result = cv2.addWeighted(roi, 1, logo, 1, 0)
            cv2.line(image, (0,centre_y),(left_x, centre_y), (0,0,255), 1)
            cv2.line(image, (right_x,centre_y),(w_image, centre_y), (0,0,255), 1)
            image[top_y:bottom_y,left_x:right_x] = result

            img = Image.fromarray(image, "RGB")
            img.save(os.path.join(INITIAL_FILE_UPLOADS,name))
            return render_template('index.html', full_filename = full_filename)
        else:
            text = request.form['text_mark']
            cv2.putText(image, text=text, org = (w_image-1000,h_image-10),
                            color=(0,0,255),fontFace=cv2.FONT_HERSHEY_DUPLEX,
                            fontScale=2, thickness=2, lineType=cv2.LINE_AA)
            img = Image.fromarray(image, "RGB")
            img.save(os.path.join(INITIAL_FILE_UPLOADS,name))
            return render_template('index.html', full_filename = full_filename)

if __name__ == "__main__":
    app.run(debug = True)