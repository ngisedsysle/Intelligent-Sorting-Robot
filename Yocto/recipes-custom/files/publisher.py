import paho.mqtt.client as mqtt

ip_adress = "localhost"
client_name = "Laura the publisher"

client = mqtt.Client(client_name)
client.connect(ip_adress)

print("Publish to topic laura/laura")
client.publish("laura/laura", "Bonjour le monde")
