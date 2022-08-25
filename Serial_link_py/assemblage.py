import cv2
import tensorflow as tf
from calendar import leapdays
from urllib.parse import ParseResultBytes
import serial
import time 
import function_serial_link

# Initialize Video Capture, create a video capture object

photo_taken =0


cap= cv2.VideoCapture(0)

if not cap.isOpened():
    print('Could not open the camera')
    exit()

#Capture image when we press 'c' on the keyboard

while photo_taken == 0:
    
    ret,frame = cap.read() 
    cv2.imshow("Live Video",frame)


    if(cv2.waitKey(1)  & 0xFF == ord('c')):
        cv2.imwrite(r"C:\Users\kouadio\Robox\Dataset\Camera1\condensateur_1.jpg",frame)
        photo_taken = 1

#Load the model

CATEGORIES = ["Inductance", "Diode"]

def prepare(filepath):
    IMG_SIZE = 227
    img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
    new_array = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))

    return new_array.reshape(-1,IMG_SIZE,IMG_SIZE,3)


model = tf.keras.models.load_model("NN7370.h5")

#Predictions

prediction = model.predict([prepare(r'C:\Users\kouadio\Robox\Dataset\Camera1\condensateur_1.jpg')])
print(prediction)

#If the prediction is good let's move the cube

if(prediction[0][0]==1.0):
    print("A capacitor has been detected.")
   


    #Lien série avec la carte

    serialInst=serial.Serial('COM6',9600)
    serialInst.timeout =1




    command=0x00;
    data=0x00;
    #Clé de début de trame

    key_start_1=18
    key_start_2= 18
    key_start_1 = key_start_1.to_bytes(1,'big')
    key_start_2 = key_start_2.to_bytes(1,'big')


    previous_data =0 
    previous_data = previous_data.to_bytes(2,"big")

    while True:
        desire = input("You can either turn the led on/off or move the cube by entering one of the following command:\n -led on\n -led off\n -pose_cube + angle between 0° and 180°\n Input? ").strip()
        [command_temp,space_separator,data_temp ]= desire.partition(" ")

        #Trame prête à être envoyé?

        ready_to_send=1


        #Gestion de la LED

        if command_temp == 'led':
            command = 8
            command = command.to_bytes(1,'big')

            if data_temp == 'off':
                data = 0
                data= data.to_bytes(2,'big')
                trame= key_start_1 + key_start_2+ command +data + previous_data
            else:
                data =1
                data = data.to_bytes(2,'big')
                trame= key_start_1  + key_start_2 + command + data + previous_data
                
        #Gestion du moteur 0

        elif command_temp =='moteur0':
            command = 0
            command = command.to_bytes(1,'big')
            data_temp = int(data_temp)
            if (data_temp <0) or (data_temp>180):
                print("The angle value you entered is out of range. Please enter a correct value.")
                ready_to_send=0

            elif(data_temp==90):
                data= function_serial_link.f_moteur_0(data_temp)-10
                data= data.to_bytes(2,'big')
                trame = key_start_1 +key_start_2 + command + data + previous_data
                print(trame)
                


            else:
                data= function_serial_link.f_moteur_0(data_temp)
                data= data.to_bytes(2,'big')
                trame = key_start_1+ key_start_2+ command + data + previous_data

        elif command_temp == 'pose_cube':
            command = 9
            command = command.to_bytes(1,'big')
            data_temp = int(data_temp)
            if (data_temp <0) or (data_temp >180):
                print("The angle value you entered is out of range. Please enter a correct value.")
                ready_to_send=0

            elif(data_temp == 90):
                data = function_serial_link.f_moteur_0(data_temp)-10
                data = data.to_bytes(2,'big')
                trame = key_start_1 + key_start_2 + command + data + previous_data

            else:
                data= function_serial_link.f_moteur_0(data_temp)
                data= data.to_bytes(2,'big')
                trame = key_start_1+ key_start_2+ command + data + previous_data
                print("The trame is: ",trame)

        else:
            print("Your input is invalid. Please enter a correct input.")        
            ready_to_send =0

        if ready_to_send == 1:
            bytes = serialInst.write(trame)
            previous_data = data

    #        time.sleep(0.5)
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())
            print(serialInst.readline())

            

    serialInst.close()

else:
    print("There is probably an error...")