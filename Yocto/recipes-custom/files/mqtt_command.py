#from asyncio import subprocess
import subprocess
import paho.mqtt.client as mqtt 
import paho.mqtt.publish as publish
import time
MQTT_SERVER= "localhost"
MQTT_PATH ="Image"

def callback(client,userdate,message):

    #Fetch the message on topic "command/request_image"
    print("message received", str(message.payload.decode("utf-8")))
    print("Message topic", message.topic)
    if(str(message.payload.decode("utf-8")== 'Image?')):

        #take a picture
        subprocess.run(["ffmpeg","-f", "video4linux2", "-i", "/dev/video0", "-vframes", "1","-video_size", "640x480", "image_webcam.jpeg"])

        #Publish it on topic Image
        f= open("image_webcam.jpeg", "rb")
        fileContent = f.read()
        byteArr = bytearray(fileContent)
        publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)    


    else:
        print("Not waiting for a picture.")


broker_adress = MQTT_SERVER
topic_name="command/request_image"

client= mqtt.Client("Atmel") #create a new instance
client.on_message = callback  #lien avec la fonction callback

print("About to connect to the broker...")
client.connect(broker_adress)

client.loop_start()
print("About to subscribe to the topic: ", topic_name)
client.subscribe(topic_name)

time.sleep(20)
client.loop_stop() #stop the loop