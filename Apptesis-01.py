# App01
# Adalah aplikasi yg berfungsi sebagai sensor untuk mendapatkan data dari setiap server
# menggunakan ligrary PSUTIL
# mengirimkan data ke MQTT Broker
# data= cpu usage, memory usage, network bandwith persecond
# server=1,2,3
#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import multitimer
import time
from psutil import cpu_percent, cpu_count, virtual_memory

#MQTT connection
broker_url = "192.168.53.3"
broker_port = 1883
client = mqtt.Client()
# edit code for passwords
print("setting  password")
client.username_pw_set(username="user01",password="mqtt")
client.connect(broker_url, broker_port)
time.sleep( 5 )

def job():
	
	# message you send to server	
	msg1 = str(cpu_percent())
	msg2 = str(virtual_memory().percent)
	client.publish(topic="sdn/cpu01", payload=msg, qos=0, retain=False)
	client.publish(topic="sdn/mem01", payload=msg, qos=0, retain=False)
	msg = msg1 + ';' + msg2
	print("cpu & ram usage", msg)

# This timer will run job() five times, one second apart
timer = multitimer.MultiTimer(interval=1, function=job, count=-1)
# Also, this timer would run indefinitely...
timer.start()
#finish