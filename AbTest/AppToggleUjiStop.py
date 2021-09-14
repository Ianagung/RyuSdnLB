#!/usr/bin/env python3
import paho.mqtt.client as mqtt
#import numpy as np
#import skfuzzy as fuzz
import multitimer

broker_url = "192.168.146.8"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " ,rc)
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#To Process Every Other Message
#client.on_message = on_message
# edit code for passwords
print("setting  password")
client.username_pw_set(username="user01",password="mqtt")

client.connect(broker_url, broker_port)

msg = "0"
print("Pengujian Load Balancing berhenti")
client.publish(topic="sdn/startstoptes", payload=msg, qos=0, retain=False)