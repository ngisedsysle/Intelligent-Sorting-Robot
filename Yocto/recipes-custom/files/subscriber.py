import paho.mqtt.client as mqtt 
import time

def callback(client,userdate,message):
	print("message received", str(message.payload.decode("utf-8")))
	print("Message topic", message.topic)

broker_adress ="localhost"
topic_name="laura/laura"

client= mqtt.Client("Lolow the client") #create a new instance
client.on_message = callback  #lien avec la fonction callback

print("About to connect to the broker...")
client.connect(broker_adress)

client.loop_start()
print("About to subscribe to the topic: ", topic_name)
client.subscribe(topic_name)



time.sleep(20)
client.loop_stop()