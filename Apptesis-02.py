# App03
# Adalah aplikasi 
# -untuk menghitung nilai fuzzy per server
# -memutuskan server mana dengan nilai window_load terkecil
# -mempublish kategori server mana dengan nilai window_load terkecil ke MQTT Broker
# task:
# -ambil data dari buffer masukkan ke GLobal variable
# -buat looping utk menghitung hasil fuzzy per server (1,2,3)
# -hasil fuzzy = window_load_change
# -hitung value window_load_current = window_load_current + window_load_change
# -memutuskan nilai window_load terkecil
# -mengkorelasikan dengan alamat server
# -mempublish server mana dengan load terkecil
# -add timer to start looping data fuzzy - done
#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import numpy as np
import skfuzzy as fuzz
import multitimer
import time
from matplotlib import pyplot as plt

sys.path.append(".")
from fuzzyMam3inCMT import Fuzzy


broker_url = "localhost"
broker_port = 1883
add01 = 'http://192.168.56.101'
add02 = 'http://192.168.56.109'
add03 = 'http://192.168.56.103'
cpu01 = 10
cpu02 = 10
cpu03 = 10
mem01 = 10
mem02 = 10
mem03 = 10
time01 = 10
time02 = 10
time03 = 10
rsptm01 = 1
rsptm02 = 1
rsptm03 = 1
rspstd01 = 1
rspstd02 = 1
rspstd03 = 1
thruput01 = 10 #throughput=kbps
thruput02 = 10 #throughput=kbps
thruput03 = 10 #throughput=kbps
listserver = [1,2]
window_load = [1,1]
max_window_load_server = 1
# getting length of list
lengths = len(list)

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " ,rc)
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

def on_message(client, userdata, message):
    print("Message Recieved from Others: "+message.payload.decode())

def on_message_from_cpu01(client, userdata, message):
    global cpu01
    cpu01 = message.payload.decode()
    print("Value Cpu01: "+message.payload.decode())

def on_message_from_cpu02(client, userdata, message):
    global cpu02
    cpu02 = message.payload.decode()
    print("Value Cpu02: "+message.payload.decode())

def on_message_from_cpu03(client, userdata, message):
    global cpu03
    cpu03 = message.payload.decode()
    print("Value Cpu03: "+message.payload.decode())

def on_message_from_mem01(client, userdata, message):
    global mem01
    mem01 = message.payload.decode()
    print("Value mem01: "+message.payload.decode())

def on_message_from_mem02(client, userdata, message):
    global mem02
    mem02 = message.payload.decode()
    print("Value mem02: "+message.payload.decode())

def on_message_from_mem03(client, userdata, message):
    global mem03
    mem03 = message.payload.decode()
    print("Value mem03: "+message.payload.decode())

def on_message_from_rsptm01(client, userdata, message):
    global rsptm01
    rsptm01 = message.payload.decode()
    print("Value rsp time 01: "+message.payload.decode())

def on_message_from_rsptm02(client, userdata, message):
    global rsptm02
    rsptm02 = message.payload.decode()
    print("Value rsp time 02: "+message.payload.decode())

def on_message_from_rsptm03(client, userdata, message):
    global rsptm03
    rsptm03 = message.payload.decode()
    print("Value rsp time 03: "+message.payload.decode())

def on_message_from_rspstd01(client, userdata, message):
    print("Value rsp std 01: "+message.payload.decode())

def on_message_from_rspstd02(client, userdata, message):
    print("Value rsp std 02: "+message.payload.decode())

def on_message_from_rspstd03(client, userdata, message):
    print("Value rsp std 03: "+message.payload.decode())

def on_message_from_thruput01(client, userdata, message):
    global thruput01
    thruput01 = message.payload.decode()
    print("Value thruput 01: "+message.payload.decode())

def on_message_from_thruput02(client, userdata, message):
    global thruput02
    thruput02 = message.payload.decode()
    print("Value thruput 02: "+message.payload.decode())

def on_message_from_thruput03(client, userdata, message):
    global thruput03
    thruput03 = message.payload.decode()
    print("Value thruput 03: "+message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#To Process Every Other Message
client.on_message = on_message
# edit code for passwords
print("setting  password")
client.username_pw_set(username="user01",password="mqtt")

client.connect(broker_url, broker_port)

client.subscribe("sdn/cpu01", qos=1)

client.message_callback_add("sdn/cpu01", on_message_from_cpu01)

client.subscribe("sdn/cpu02", qos=1)

client.message_callback_add("sdn/cpu02", on_message_from_cpu02)

client.subscribe("sdn/cpu03", qos=1)

client.message_callback_add("sdn/cpu03", on_message_from_cpu03)

client.subscribe("sdn/mem01", qos=1)

client.message_callback_add("sdn/mem01", on_message_from_mem01)

client.subscribe("sdn/mem02", qos=1)

client.message_callback_add("sdn/mem02", on_message_from_mem02)

client.subscribe("sdn/mem03", qos=1)

client.message_callback_add("sdn/mem03", on_message_from_mem03)

client.subscribe("sdn/rsptm01", qos=1)

client.message_callback_add("sdn/rsptm01", on_message_from_rsptm01)

client.subscribe("sdn/rsptm02", qos=1)

client.message_callback_add("sdn/rsptm02", on_message_from_rsptm02)

client.subscribe("sdn/rsptm03", qos=1)

client.message_callback_add("sdn/rsptm03", on_message_from_rsptm03)

client.subscribe("sdn/rspstd01", qos=1)

client.message_callback_add("sdn/rspstd01", on_message_from_rspstd01)

client.subscribe("sdn/rspstd02", qos=1)

client.message_callback_add("sdn/rspstd02", on_message_from_rspstd02)

client.subscribe("sdn/rspstd03", qos=1)

client.message_callback_add("sdn/rspstd03", on_message_from_rspstd03)

client.subscribe("sdn/thruput01", qos=1)

client.message_callback_add("sdn/thruput01", on_message_from_thruput01)

client.subscribe("sdn/thruput02", qos=1)

client.message_callback_add("sdn/thruput02", on_message_from_thruput02)

client.subscribe("sdn/thruput03", qos=1)

client.message_callback_add("sdn/thruput03", on_message_from_thruput03)

#myFuzzy = Fuzzy(cpu_val, mem_val, truput_val)
#print(mycar.get_fuzzy())

#client.loop_forever()
client.loop_start()

print("Do Something else")

#Hitung fuzzy dan window_load
def job1():
    global listserver
    global lengths
    global cpu01
    global mem01
    global thruput01
    global cpu02
    global mem02
    global thruput02
    global window_load
    global max_window_load_server
    
    # Iterating the index
    # same as 'for i in range(len(list))'
    for i in range(lengths):
        print("Perhitungan Fuzzy - Perubahan Load Window server-", list[i])
        if i == 1:
            cpu_val = cpu01
            mem_val = mem01
            truput_val = thruput01
        elif i==2:
            cpu_val = cpu02
            mem_val = mem02
            truput_val = thruput02
    #do fuzzy   
        myFuzzy = Fuzzy(cpu_val, mem_val, truput_val)
        delta_ld_window = myFuzzy.get_fuzzy()
        print("Perubahan Load Window Server-%s is %.2f" % ( listserver[i], delta_ld_window))
    #hitung total workload
        window_load[i] += delta_ld_window
    #reset jika sudah kena threshold atas dan bawah
        #reset window_load
    #compare nilai window_load terbesar
        #max(list)
    #update global value window load
        #max_window_load_server = 1

# This timer will run job() five times, one second apart
timer1 = multitimer.MultiTimer(interval=1, function=job1, count=-1)
# Also, this timer would run indefinitely...
timer1.start()

#publish data ke mqtt broker
#data = which server has max window load
def job2():
    
    # message you send to server
    msg = max_window_load_server
    print("Server dg max window load =", msg)
    client.publish(topic="sdn/fuzzyout", payload=msg, qos=0, retain=False)
    
# This timer will run job() five times, one second apart
timer2 = multitimer.MultiTimer(interval=1, function=job2, count=-1)
# Also, this timer would run indefinitely...
timer2.start()

