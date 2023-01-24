
# Image Watermarking App © 

In this project we will see how to add watermark to an image.
Adding watermark works as copyright for your image so that no 
one can illegally use your image or document. I have used 
opencv for adding logos and text as an watermark. 


## Roadmap

- Loading the image and logo from the Flask app

- Resizing the images 

- Convert images into RGB Format and then convert it 
  into numpy array 

- Storing the height and width of the image and logo

- Finding the coordinates of the center of the image

- Finding out the region of interest to draw logo

- Merging the logo with the image and visualizing it

- Creating the text watermark

- Using the cv2 function to define text properties and 
  applying it at specific co-oridinates

- Converting the image into RGB and visualizing it  


## Tech Stack

**Tech:** Python, Visual Studio Code, 
          Internet Explorer

**Libraries:** TensorFlow, Keras, Flask, Numpy, Pandas,
               Pillow, OpenCV, Flask


![Logo](https://raw.githubusercontent.com/Darshbhi99/Data-Science-Projects/main/Traffic%20Sign%20Prediction/logo.png)


## Run Locally

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

![App Screenshot](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Image%20Watermarking%20App/static/Image_watermark.jpg?raw=true)


## Lessons Learned

### Conclusion
We started with loading the image and logo, resizing the image and
logo, finding the height and width of both, finding the center of 
the image and calculating the ROI for the logo and merging the logo 
on the image similarly adding the text watermark as well.

### Scope
This model can be used in organization to make their content secure 
so that their content cannot be misused without their licence or a 
paid version.