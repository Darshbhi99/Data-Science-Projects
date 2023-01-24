
# 🐕🐶 Dog Breed Prediction 🐕‍🦺🐩

In this project we will see how to use Keras and Tensorflow to build, train and test a convolution neural 
network capable of identifying a breed of a dog in a supplied image. This is supervised learning problem, 
specifically a multiclass classification problem

Classification Labels:

'scottish_deerhound', 'maltese_dog', 'bernese_mountain_dog'

## CNN Model Architecture

![Model](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Dog%20Breed%20Prediction/model.png?raw=true)

## Roadmap

- Finding Data on Kaggle and Loading it into Google 
  Colab

- Preprocessing the Images and Visualising them

- Finding out the 3 breeds with most images in 
  the training dataset and extrcting the images for 
  the same for classification

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
  gives the dog breed  


## Tech Stack

**Tech:** Python, Google Colab, Visual Studio Code, 
          Internet Explorer

**Libraries:** TensorFlow, Keras, Flask, Numpy, Pandas,
               Pillow, OpenCV, Streamlit


![Logo](https://raw.githubusercontent.com/Darshbhi99/Data-Science-Projects/main/Traffic%20Sign%20Prediction/logo.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Darshbhi99/Data-Science-Projects.git
```

Go to the project directory

```bash
  cd c:\Downloads\Data-Science-Projects\Dog Breed Prediction
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

Copy the "builder.py" file from the folder to "<environment_name>\Lib\site-packages\google\protobuf\internal"

Start the server

```bash
  streamlit run main_app.py
```


## Screenshots

![App Screenshot](https://github.com/Darshbhi99/Data-Science-Projects/blob/main/Dog%20Breed%20Prediction/app.png?raw=true)


## Lessons Learned

### Conclusion
We started with downloading the dataset, preprocessing it, 
created the model and found out the predictions using the
model.During preprocessing compressed my dataset to 3 classes. 
Model reached an accuracy of 88%+ in just 100 epochs, we can
further increase number of classes and optimize the model using 
hyperparameter tuning and can classify more dog breeds

### Scope
This model can be used to predict different breeds of dogs which
can be further used by different NGO's working on saving animals 
and for educational purpose also.

## Acknowledgements

 - [Dataset Download](https://www.kaggle.com/datasets/catherinehorng/dogbreedidfromcomp)
 - [Colab Notebook](https://drive.google.com/drive/folders/1Uo0o8cZfOHw8SX6kH2i_qrio5L1byxVp?usp=sharing)

