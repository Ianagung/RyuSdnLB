#!/usr/bin/env python3
import paho.mqtt.client as mqtt

broker_url = "localhost"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " ,rc)
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

def on_message_from_fuzzyout(client, userdata, message):
    print("Message Recieved from Fuzzy Module: "+message.payload.decode())

def on_message(client, userdata, message):
    print("Message Recieved from Others: "+message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#To Process Every Other Message
client.on_message = on_message
# edit code for passwords
print("setting  password")
client.username_pw_set(username="user01",password="mqtt")

client.connect(broker_url, broker_port)

client.subscribe("sdn/fuzzyout", qos=1)

client.message_callback_add("sdn/fuzzyout", on_message_from_fuzzyout)

client.loop_forever()

print("Do Something else")
