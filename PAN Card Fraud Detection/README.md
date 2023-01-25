
# 🛑 PAN Card Fraud Detection 💳 

In this project we will see how to verify whether PAN Card is 
Original or Fake.
I have used opencv for finding the difference between an 
Original and Fake PAN Card. 


## Roadmap

- Loading the image from the Flask app

- Resizing the image 

- Convert image into Grayscale numpy array

- Comparing the image structure with the original using
  structural_similarity library which gives an difference 
  image and a similarity score.

- Get the threshold of the difference image using Opencv

- Find the contours in the image using the threshold

- Merge the contours using blue rectrangles with the 
  original image

- Getting the SSIM(Structural Similarity Index Measurement) 
  and Converting the image into RGB and visualizing it.


## Tech Stack

**Tech:** Python, Visual Studio Code, 
          Internet Explorer

**Libraries:** Numpy, Pillow, OpenCV, Flask, skimage, 
               imutils


![Logo](https://raw.githubusercontent.com/Darshbhi99/Data-Science-Projects/main/Traffic%20Sign%20Prediction/logo.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Darshbhi99/Data-Science-Projects.git
```

Go to the project directory

```bash
  cd c:\Downloads\Data-Science-Projects\PAN Card Fraud Detection
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

![App Screenshot](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/PAN%20Card%20Fraud%20Detection/static/PAN_Card_Fraud_Detection.jpg?raw=true)


## Lessons Learned

### Conclusion
We started with loading the image, resizing the image, 
finding the height and width of both, converting the image 
into grayscale and finding the SSIM(Structural_Similarity_Index), 
getting the threshold and contours of the image and applying it
on the original image.

### Scope
This model can be used in organization to make sure that a PAN
Card shown during Check IN/Entry is Real or Fake. This web app will save 
illegal Entry and Frauds in the Government and Private Organizations.  
