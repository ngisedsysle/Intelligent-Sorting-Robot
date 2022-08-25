# Intelligent-Sorting-Robot

## Description

This repository allows you to reocnstruct the project I worked on during my 6 months internship. The first part of my internship was devoted to creating a machine learning model that can efficiently sort three electronical components. The training of this model was possible thanks to a database that I 
created myself. The model was created using the Keras and Tensorflow python libraries.
Later, I worked with a robotic arm which is able to grab small objects and 
move them. In order to make the link between my artificial intelligence and the robot, I also wrote a 
python script that links the robot’s behavior to the predictions of the artificial intelligence. Thus, by 
detecting one of the components via a camera connected to the PC, the robot is able to grab the 
component and place it at the desired location. 
Finally, I created a Linux distribution for an Atmel card. The objective was to connect the camera to this card rather than 
the computer. Thus, the card would be in charge of taking a photo of the component to be moved, 
then sending that picture to the artificial intelligence located on the PC. In order to create this Linux distribution, I used Yocto.

## Getting Started

### The artificial intelligence

#### Construction of the dataset

Use Intelligent-Sorting-Robot/IA/Pre-processing/image_harvesting.py if you want to construct your dataset with pictures you take yourself. This scripts opens the camera "0" of your PC and takes a picture when the user press "c" on the keyboard. The storage location of this picture can and has to be edited.

Use Intelligent-Sorting-Robot/IA/Pre-processing/images_harvesting_script.py to automatically construct a dataset with images found on google. The components the script will look for depends on what is written line 20.


Use Intelligent-Sorting-Robot/IA/Pre-processing/Prepared_dataset_kaggle.ipynb to pre process the data before passing it to the neural network: Creation of the classes (Capacitor, Inductance, led), size of each image (can be modified), label associated with each class, creation of two files: X_kaggle and Y_kaggle

#### The Neural-network

CNN_kaggle.ipynb presents the structure of the neural network I created. Running all the cells will create the file "new_model_CNN_kaggle_8585.h5" which can then be used to make predictions.

#### Testing the model

The script Intelligent-Sorting-Robot/IA/Test/detect_composant_nn_test.ipynb can be used to test the model previously created on data the algorithm has not seen before. The user has to indicate where are the pictures he wants to use for the test in the third cell.



