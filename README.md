# Intelligent-Sorting-Robot

## Description

This repository allows you to reocnstruct the project I worked on during my 6 months internship. The first part of my internship was devoted to creating a machine learning model that can efficiently sort three electronical components. The training of this model was possible thanks to a database that I 
created myself. The model was created using the Keras and Tensorflow python libraries.
Later, I worked with a robotic arm which is able to grab small objects and 
move them. In order to make the link between my artificial intelligence and the robot, I also wrote a 
python script that links the robot’s behavior to the predictions of the artificial intelligence. Thus, by 
detecting one of the components via a camera connected to the PC, the robot is able to grab the 
component and place it at the desired location. 
Finally, I created a Linux distribution for an Atmel board. The objective was to connect the camera to this card rather than 
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


### Robot control

Both programms have been created in the Arduino IDE, since it is the card the robotic arm is working with.

Intelligent-Sorting-Robot/Robot Control/serial_trame.ino: Depending on the command received (see the serial trame section), this scripts can turn a led connecting to the robot's card on, move the motor which has 0 for ID or moving around a small paper cube. This programm must be used with "assemblage.py".


Intelligent-Sorting-Robot/Robot Control/serial_trame_2.ino: According to the result of the prediction of the IA, the robot will take the object from a pre-defined postion: 90° degrees from its initial postion if the IA successfully detected the capacitor, 180° from its initial position otherwise. This programm must be used with "assemblage_2.py".

One of these programms has to be flashed on the ArbotiX borad via the Arduio IDE.


### Python Serial link

Intelligent-Sorting-Robot/Serial_link_py/assemblage.py passes a picture located on the PC to the artificial intelligence and makes a prediction. If a capacitor has been detected with a probability equal to 1, the user will be able to choose between 3 commands the robot will execute.  This programm must be used with "serial_trame.ino".


Intelligent-Sorting-Robot/Serial_link_py/function_serial_link.py is used in "assemblage.py".

Intelligent-Sorting-Robot/Serial_link_py/assemblage_2.py asks the Atmel board (see the Yocto part) to take a picture with the webcam plugged on the board and to send it back to the PC. The script then passes the picture to the IA, which will make a prediction, allowing the robot to move according to this prediction. This programm must be used with "serial_trame_2.ino".


To launch on of these scripts, use the following command: "python3 ./assemblage.py" or "python3 ./assemblage_2.py". For "assemblage_2.py", the linux distribution presented in the next part has to be set on the Atmel board.

### Yocto and the Atmel board

The image has been built on a server with Yocto and docker already installed.

Yocto release used: Dunfell

This image contains the following layers: 
   * meta-atmel
   * meta-aws
   * meta-openembedded
   * meta-poky
   * meta-custom
In the "meta-atmel" layer, delete the file "u-boot-atmel.inc" and replace it by the file "Intelligent-Sorting-Robot/meta-atmel/u-boot-atmel.inc"

The recipes I added in my own layer called "meta-custom" are:
   * recipes-connectivity: Used to configure the mosquitto broker
   * recipes-core/images/core-image-laura.bb where I manually added some recipes
   * mqtt-participants_1.1.bb with files to subscribe and publish on topics located on the mosquitto broker
   * Intelligent-Sorting-Robot/Yocto/recipes-kernel/linux-mchp_%.bbappend which resume the configuration of the kernel

The kernel has to be configurated the board will be able to detect the webcam:
   * in a terminal on the server: kas-container shell path-to-the-yml/.yml -c "bitbake -c menuconfig virtual/kernel"
   * In the menuconfig, I activated “USB Video Class” in Device Drivers/Mulimedia Support/Media drivers/Media USB Adaptaters.

To launch a build:
   * kas-container build path-to-the-yml/.yml

Once the build is done, flash a micro SD card using Balena etcher for example. Put the micro SD card in a SD card adaptater and then on the board. Use the terminal of your choice to access your liux distribution. I used Tera Term.

In /etc/init.d/mosquitto add the following lines under "echo "Starting Mosquitto message broker" "mosquitto"":
   * mosquitto -d
   * echo "Mosquitto is running in the background"

To test the installation:

In /usr/bin:
   * plug a webcam on the board
   * python3 mqtt_command.py
   * WAIT until you see About to subscribe to the topic: command/request_image on the terminal

QUICKLY on your PC:
   * python ./assemblage_2.py 

If you put a capacitor in front of the camera, the robot should take the object placed on its initial postion and put it 90° away from its initial position, 180° otherwise.





