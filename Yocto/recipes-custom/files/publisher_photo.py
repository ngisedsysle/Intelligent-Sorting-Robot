import paho.mqtt.publish as publish
MQTT_SERVER= "localhost"
MQTT_PATH ="Image"

f= open("image_webcam.jpeg", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)

publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)