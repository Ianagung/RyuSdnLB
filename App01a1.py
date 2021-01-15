#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import multitimer
import time
from psutil import cpu_percent, cpu_count, virtual_memory

#MQTT connection
broker_url = "localhost"
broker_port = 1883
client = mqtt.Client()
# edit code for passwords
print("setting  password")
client.username_pw_set(username="user01",password="mqtt")
client.connect(broker_url, broker_port)
time.sleep( 5 )

def job():
	
	# message you send to server
	msg = str(cpu_percent()) + ';' + str(virtual_memory().percent)
	print("Publish Cpu/Ram data", msg)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/cpumem01", payload=msg, qos=0, retain=False)

# This timer will run job() five times, one second apart
timer = multitimer.MultiTimer(interval=1, function=job, count=-1)
# Also, this timer would run indefinitely...
timer.start()

print("Do other job")