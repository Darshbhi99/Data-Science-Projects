
# Text Extractor App © 

In this project we will see how to Extract Text from an 
image. This project will save time and effort of typing
text from an image.


## Roadmap

- Loading the image from the Flask app

- Resizing the images 

- Convert images into RGB Format and then convert it 
  into numpy array 

- Using pytesseract library for extracting text from 
  the image.

- Removing the special characters from the text. 


## Tech Stack

**Tech:** Python, Visual Studio Code, 
          Internet Explorer

**Libraries:** Pillow, OpenCV, Flask
               pytesseract 

![Logo](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Text%20Extractor%20App/static/logo4.png?raw=true)


## Run Locally

Download the pytesseract software suitable for your pc from below link

"https://github.com/UB-Mannheim/tesseract/wiki"

Install the software and keep the track for the path where it is installed

Clone the project

```bash
  git clone https://github.com/Darshbhi99/Data-Science-Projects.git
```

Go to the project directory

```bash
  cd c:\Downloads\Data-Science-Projects\Image Watermarking App
```

Create Virtual Environment

```bash
  conda create <environment_name> -p python==3.10.6
```

Activate the Virtual Environment

```bash
  conda activate ./<environment_name>
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```


## Screenshots

![App Screenshot](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Text%20Extractor%20App/static/Text_Extractor_App.jpg?raw=true)


## Lessons Learned

### Conclusion
We started with loading the image, resizing the image, extracting 
the text from the image, cleaning the text.

### Scope
This model can be used in Organizations which use images as 
reference for documentation.
