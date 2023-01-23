
# 🚦 Traffic Sign Classification 🚸⛔

This project is about classifying the Traffic Sign using
Convolution Neural network model which will use Keras 
and Tensorflow Libraries. It is a Multiclass Classification Model 
which will classify Images with Traffic Sign given below.

Classification Labels:

'Speed limit (20km/h)', 'Speed limit (30km/h)', 'Speed limit (50km/h)', 'Speed limit (60km/h)',
'Speed limit (70km/h)', 'Speed limit (80km/h)', 'End of speed limit(80km/h)', 'Speed limit (100km/h)',
'Speed limit (120km/h)', 'No passing', 'No passing for vehicles over 3.5 metrics tons',
'Right-of-way at the next intersection','Priority road', 'Yield', 'Stop', 'No vehicle',
'Vehicle over 3.5 metric tons prohibited', 'No entry', 'General caution', 'Dangerous curve to the left',
'Dangerous curve to the right', 'Double curve', 'Bumpy Road', 'Slippery Road', 'Road narrows to the right',
'Road work','Traffic Signals', 'Pedestrians', 'Chidren Crossing', 'Bicycle Crossing', 'Beware of ice/snow',
'Wild Animals Crossing', 'End of all speeds and crossing limits', 'Turn Right Ahead', 'Turn Left Ahead',
'Ahead only', 'Go straight or right', 'Go straight or left', 'Keep right', 'Keep left',
'Roundabout mandatory', 'End of no passing', 'End of no passing by vehicles over 3.5 metric'


## Roadmap

- Finding Data on Kaggle and Loading it into Google 
  Colab

- Preprocessing the Images and Visualising them

- Finding out the mean of the Dimensions of all 
  the images and Resizing all the images accordingly

- Converting the images into a numpy array and 
  normalize them 

- Checking the class imbalance

- Splitting the data and performing One-hot encoding

- Creating a model architecture, compiling the model 
  and then fitting it

- Plotting the Accuracy and Loss against each epoch

- Preproccessing the Test Data and Make Predictions 
  on it

- Visualizing the Original and Predicted Labels for 
  the Test Images  



## Tech Stack

**Tech:** Python, Google Colab, Visual Studio Code, 
          Internet Explorer

**Libraries:** TensorFlow, Keras, Flask, Numpy, Pandas,
               Pillow, OpenCV 


![Logo](https://raw.githubusercontent.com/Darshbhi99/Data-Science-Projects/main/Traffic%20Sign%20Prediction/logo.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Darshbhi99/Data-Science-Projects.git
```

Go to the project directory

```bash
  cd c:\Downloads\Data-Science-Projects\Traffic Sign Prediction
```

Create Virtual Environment

```bash
  conda create -m <environment_name>
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

![App Screenshot](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Traffic%20Sign%20Prediction/static/Traffic%20Signal%20Classifier.jpg?raw=true)


## Lessons Learned

### Conclusion
We started with downloading the dataset, preprocessing it, 
created the model and found out the predictions using the
model.During preprocessing we found out that this dataset
has 43 classes. Model reached an accuracy of 98%+ in just
50 epochs, we can further optimize the model using hyperparameter
tuning and reach a higher accuracy

### Scope
This model can be used in self driving cars which will 
enable them to automatically recognize traffic signs 
similarly the driver alert system inside cars will help 
by understanding the traffic signs around them

## Acknowledgements

 - [Dataset Download](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)

