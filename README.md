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
