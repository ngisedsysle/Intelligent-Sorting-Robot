import paho.mqtt.client as mqtt
MQTT_SERVER = "192.168.94.93"
MQTT_PATH = "Image"

# The callback for when the client receives a CONNACK response from the server

def on_connect(client, userdata, flags, rc):
    print("Connected with the result code" + str(rc))

    #Subscribing in on_connect() means that if we lose the connection and reconnect then the subscription will be renewed
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    #Create a file with write byte permission
    f = open('output.jpg', "wb")
    f.write(msg.payload)
    print("Image received")
    f.close()

client= mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER,1883,60)


client.loop_forever()