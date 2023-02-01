
# 🚕🚌 Vehicle Detection and Counting App 🚜🚑🚝 

In this project we will be working on detecting and 
counting vehicles in a given images or videos. We will 
be using opencv for image processing and haar cascade 
which is used for object detection. We can also create 
our own customized haar cascade classifier. 


## Roadmap

- Loading the image from the Flask app

- Resizing the images and then convert it 
  into numpy array

- Convert image into Greyscale Format  

- Load the xml file containing the haar cascade.

- Using haar cascade to detect the vehicle in the
  image. 

- Use the contours to create a rectangle around all 
  the detected vehicles(cars)

- Similarly will also use it on Bus Detection using
  Bus Detection

- Will perform these operations on the video

- Save the video with object detection.


## Tech Stack

**Tech:** Python, Visual Studio Code, 
          Internet Explorer

**Libraries:** Pillow, OpenCV, Flask
               Haar Cascade library  

![Logo](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Text%20Extractor%20App/static/logo4.png?raw=true)


## Run Locally


Clone the project

```bash
  git clone https://github.com/Darshbhi99/Data-Science-Projects.git
```

Go to the project directory

```bash
  cd c:\Downloads\Data-Science-Projects\Vehicle Detection and Counting App
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

![App Screenshot](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Vehicle%20Detection%20and%20Counting/static/app.png?raw=true)


## Lessons Learned

### Conclusion
We started with loading the image, performed multiple operations 
on the image. We saw how we can use haar cascade which is used 
for detection. We saw different haar cascade is used for car 
detection and bus detection. Similarly we can use different 
cascades for different cascade detection.

### Scope
This model can be use this app at various object detection and 
vehicle tracking on traffic areas. 
