#!/usr/bin/env python3
import paho.mqtt.client as mqtt

broker_url = "localhost"
broker_port = 1883

client = mqtt.Client()

# edit code for passwords
print("setting  password")
client1.username_pw_set(username="user01",password="mqtt")

client.connect(broker_url, broker_port)

client.publish(topic="sdn/fuzzyout", payload="TestingPayload", qos=1, retain=False)

print("Do Something else")