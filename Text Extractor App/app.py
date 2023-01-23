from flask import render_template, request, Flask
import numpy as np
from PIL import Image
import cv2
import random
import string
import pytesseract
import os

# r = requests.get("https://raw.githubusercontent.com/tesseract-ocr/tessdata/4.00/ind.traineddata", stream=True)
# # Writing data to file to avoid path issues
# with open("/usr/share/tesseract-ocr/4.00/tessdata/ind.traineddata", 'wb') as file:
#     for block in r.iter_content(chunk_size=1024):
#         if block:
#             file.write(block)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DARSHAN\AppData\Local\Programs\Tesseract-OCR\tesseract'

app = Flask(__name__)

INITIAL_FILE_UPLOADS= "./static/images"

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
        image.save(os.path.join(INITIAL_FILE_UPLOADS,name))

        img_array = np.array(image.convert('RGB')) # Converting image to array
        img_gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY) # Converting array to gray
        img = Image.fromarray(img_gray) # Converting array to image
        custom_config = r"-l eng --oem 3 --psm 6" # Custom configuration for the pytesseract 
        text = pytesseract.image_to_string(image, config=custom_config) # Extracting text
        characters_to_remove = "!()@-*>+/,'|#%$&^_~" 
        new_string = text
        for character in characters_to_remove:
            new_string = new_string.replace(character,"") # Cleaning the text
        new_string = new_string.split('\n')
        return render_template('index.html', full_filename = full_filename, text = new_string)

if __name__ == "__main__":
    app.run(debug = True)