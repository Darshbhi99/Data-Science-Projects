
# ☘ Plant Disease Prediction 🦟

Human Society needs to increase food production by an estimate 70% by 2030. 
To feed the expected population which is said to be 9 billion people. Currently, 
infectious disease reduce the potential yield by around 40% with many farmers in
the developing world experiencing yeild losses as high as 100%. The widespread of 
distribution of smartphones around the crop growers around the world with an expected 
5 billion smartphones by 2025 offers the potential of turning the smartphones into a
valuable tools for diverse communities growing food.
   
In this project we will see how to use Keras and Tensorflow to build, train and test a convolution neural 
network capable of identifying a plant is diseased or not in a supplied image. This is supervised learning problem, 
specifically a multiclass classification problem

Classification Labels:

'Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot'

## CNN Model Architecture

![Model](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Plant%20Disease%20Prediction/static/model.png?raw=true)

## Roadmap

- Finding Data on Kaggle and Loading it into Google 
  Colab

- Preprocessing the Images and Visualising them

- Extracting the images for 3 plants for 
  classification

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

- Creating a Streamlit app which takes an image and 
  predicts if the plant is diseased or not 


## Tech Stack

**Tech:** Python, Google Colab, Visual Studio Code, 
          Internet Explorer

**Libraries:** TensorFlow, Keras, Flask, Numpy, Pandas,
               Pillow, OpenCV, Streamlit


![Logo](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Dog%20Breed%20Prediction/logo.png?raw=true)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Darshbhi99/Data-Science-Projects.git
```

Go to the project directory

```bash
  cd c:\Downloads\Data-Science-Projects\Plant Disease Prediction
```

Create Virtual Environment

```bash
  conda create <environment_name> -p python=3.10
```

Activate the Virtual Environment

```bash
  conda activate ./<environment_name>
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Copy the "builder.py" file from the folder to "<environment_name>\Lib\site-packages\google\protobuf\internal"

Start the server

```bash
  streamlit run app.py
```


## Screenshots

![App Screenshot](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Plant%20Disease%20Prediction/static/app.png?raw=true)


## Lessons Learned

### Conclusion
We started with loading the data and visualizing the images.
Normalizing is an important step when working on any type of 
dataset. After that we created a CNN model which is further 
used for predicting the plant diseases using the image supplied
to the model.

### Scope
This model is highly beneficial as it can be used for different
agricultural firms and farmers to increase their yield and stop 
wastage of crop due to disease

## Acknowledgements

 - [Dataset Download](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
 - [Colab Notebook](https://colab.research.google.com/drive/1BlZV6QdpzVWyKMVOIcJfqWP6uFikwb4y?usp=share_link)

