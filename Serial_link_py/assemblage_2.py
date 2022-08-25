import cv2
import tensorflow as tf
from calendar import leapdays
from urllib.parse import ParseResultBytes
import serial
import time 
import function_serial_link
import paho.mqtt.client as mqtt
import publish_command_mqtt
import subprocess
MQTT_SERVER = "192.168.94.93"
MQTT_PATH = "Image"




#Lien série avec la carte

serialInst=serial.Serial('COM6',9600)
serialInst.timeout =1
photo_taken=0

#Request a picture
    
subprocess.call("publish_command_mqtt.py", shell=True)
print("The picture has been received")
    
#Class and prepare the entrance data



def prepare(filepath):
    IMG_SIZE = 227
    img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
    new_array = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))

    return new_array.reshape(-1,IMG_SIZE,IMG_SIZE,3)

# #Load the model

model = tf.keras.models.load_model("NN7370.h5")


prediction = model.predict([prepare(r'C:\Users\kouadio\Robox\Dataset\Camera1\output.jpg')])
print(prediction)

#If the prediction is good let's move the cube

if((prediction[0][0]>prediction[0][1]) & (prediction[0][0]>prediction[0][2]) ):
    print("A capacitor has been detected.")
    data_temp =90
    command = 9
else:
    print("An object that I don't know has been identified")
    data_temp=180
    command = 0
    
    

#Clé de début de trame

key_start_1=18
key_start_2= 18
key_start_1 = key_start_1.to_bytes(1,'big')
key_start_2 = key_start_2.to_bytes(1,'big')
    
    
command = command.to_bytes(1,'big')  
data = function_serial_link.f_moteur_0(data_temp)-10
data = data.to_bytes(2,'big')
trame = key_start_1 + key_start_2 + command + data # + previous_data

    
    #Sending stuff
time.sleep(7)
bytes = serialInst.write(trame)
    
print(serialInst.readline())
print(serialInst.readline())
print(serialInst.readline())
print(serialInst.readline())
print(serialInst.readline())
print(serialInst.readline())
print(serialInst.readline())
print(serialInst.readline())
    

serialInst.close()
            