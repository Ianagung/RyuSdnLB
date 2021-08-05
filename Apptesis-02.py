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
# -memutuskan nilai window_load_current terbesar
# -mengkorelasikan dengan alamat server

# -mempublish server mana dengan load terkecil= window_load_terbesar
#In the next step of the fuzzy system design process, the fuzzy rules base is defined (Table 2). 
#The rules are constructed to indicate that greater consumable resources cause higher load; 
#therefore, the size of the window should be smaller. 
#The opposite of this is true as well.

# -add timer to start looping data fuzzy - done
#!/usr/bin/env python3
import paho.mqtt.client as mqtt
#import numpy as np
#import skfuzzy as fuzz
import multitimer
import time
#from matplotlib import pyplot as plt
import sys
sys.path.append(".")
from fuzzyMam3inCMT import Fuzzy

broker_url = "127.0.0.1"
broker_port = 1883
add01 = 'http://192.168.147.1'
add02 = 'http://192.168.147.3'
add03 = 'http://192.168.147.5'
cpu01 = 30
cpu02 = 30
cpu03 = 30
mem01 = 50
mem02 = 50
mem03 = 50
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
window_load = [50,50]
max_window_load_server = 1
max_truput_server = 2741560 #max = 2741560 /s 2.6MB/s
truput_server01 = [1]
# getting length of list
lengths = len(listserver)

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

# total = 1024
# print(total)
# print(bytes2human(total))
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
    cpu01 = float(message.payload.decode())
    #print("Value Cpu01: "+cpu01)

def on_message_from_cpu02(client, userdata, message):
    global cpu02
    cpu02 = float(message.payload.decode())
    #print("Value Cpu02: "+cpu02)

def on_message_from_cpu03(client, userdata, message):
    global cpu03
    cpu03 = float(message.payload.decode())
    #print("Value Cpu03: "+cpu03)

def on_message_from_mem01(client, userdata, message):
    global mem01
    mem01 = float(message.payload.decode())
    #print("Value mem01: "+mem01)

def on_message_from_mem02(client, userdata, message):
    global mem02
    mem02 = float(message.payload.decode())
    #print("Value mem02: "+mem02)

def on_message_from_mem03(client, userdata, message):
    global mem03
    mem03 = float(message.payload.decode())
    #print("Value mem03: "+mem03)

def on_message_from_rsptm01(client, userdata, message):
    global rsptm01
    rsptm01 = message.payload.decode()
    #print("Value rsp time 01: "+rsptm01)

def on_message_from_rsptm02(client, userdata, message):
    global rsptm02
    rsptm02 = message.payload.decode()
    #print("Value rsp time 02: "+rsptm02)

def on_message_from_rsptm03(client, userdata, message):
    global rsptm03
    rsptm03 = message.payload.decode()
    #print("Value rsp time 03: "+rsptm03)

def on_message_from_rspstd01(client, userdata, message):
    print("Value rsp std 01: "+message.payload.decode())

def on_message_from_rspstd02(client, userdata, message):
    print("Value rsp std 02: "+message.payload.decode())

def on_message_from_rspstd03(client, userdata, message):
    print("Value rsp std 03: "+message.payload.decode())

def on_message_from_thruput01(client, userdata, message):
    global thruput01
    thruput01 = int(message.payload.decode())
    #print("Nilai thruput 01: "+ thruput01)
    #truput_server01.append(float(thruput01))

def on_message_from_thruput02(client, userdata, message):
    global thruput02
    thruput02 = int(message.payload.decode())
    #print("Nilai thruput 02: "+thruput02)

def on_message_from_thruput03(client, userdata, message):
    global thruput03
    thruput03 = int(message.payload.decode())
    #print("Nilai thruput 03: "+thruput03)

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
        print("Perhitungan Fuzzy - Perubahan Load Window server-", listserver[i])

        if listserver[i]==1:
            cpu_val = cpu01
            mem_val = mem01
            #truput_val = thruput01
            truput_val = round(((thruput01 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
            print("Cpu val "+str(cpu_val)+" Mem Val "+str(mem_val)+" Thruput Val "+ str(truput_val))
        elif listserver[i]==2:
            cpu_val = cpu02
            mem_val = mem02
            #truput_val = thruput02
            truput_val = round(((thruput02 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
            print("Cpu val "+str(cpu_val)+" Mem Val "+str(mem_val)+" Thruput Val "+ str(truput_val))
        #do fuzzy untuk setiap server
        #print("Cpu val "+str(cpu_val)+" Mem Val "+str(mem_val)+" Thruput Val "+ str(truput_val))
        myFuzzy = Fuzzy(cpu_val, mem_val, truput_val)
        delta_ld_window = myFuzzy.get_fuzzy()
        print("Perubahan Load Window Server-%s is %.3f" % ( listserver[i], delta_ld_window))
        #hitung total workload
        window_load[i] += delta_ld_window
        print("Load Window Server-%s is %.3f" % ( listserver[i], window_load[i]))
        #reset jika sudah kena threshold atas dan bawah
        #reset window_load
        if window_load[i] > 100:
            window_load[i] = 90
        if window_load[i] < 0:
            window_load[i] = 10
        
    #compare nilai window_load terbesar
    #find index of maximum element
    ## index of maximum element
    #update global value window load
    #max_window_load_server = 1
    max_window_load_server = window_load.index(max(window_load)) + 1 
    #jika index = 0 maka server1
    #jika index = 1 maka server2
    #print ("Server dg Load window terbesar "+max_window_load_server)
    # message you send to server
    msg = str(max_window_load_server)
    print("Server yang punya max window load =", msg)
    client.publish(topic="sdn/fuzzyout", payload=msg, qos=0, retain=False)

# This timer will run job() five times, one second apart
timer1 = multitimer.MultiTimer(interval=5, function=job1, count=-1)
# Also, this timer would run indefinitely...
timer1.start()

#publish data ke mqtt broker
#data = which server has max window load
# def job2():
    
#     # message you send to server
#     msg = max_window_load_server
#     print("Server dg max window load =", msg)
#     client.publish(topic="sdn/fuzzyout", payload=msg, qos=0, retain=False)
    
# This timer will run job() five times, one second apart
#timer2 = multitimer.MultiTimer(interval=1, function=job2, count=-1)
# Also, this timer would run indefinitely...
#timer2.start()

#fungsi tes
def job3():
    global max_truput_server
    cpu01 = 30
    cpu02 = 90
    cpu03 = 30
    mem01 = 50
    mem02 = 90
    mem03 = 50
    #time01 = 10
    #time02 = 10
    #time03 = 10
    #rsptm01 = 1
    #rsptm02 = 1
    #rsptm03 = 1
    #rspstd01 = 1
    #rspstd02 = 1
    #rspstd03 = 1
    truput01 = round(((1000000 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
    truput02 = round(((2000000 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
    truput03 = round(((1000000 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen    
    # message you send to server
    msg = cpu01
    client.publish(topic="sdn/cpu01", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = cpu02
    client.publish(topic="sdn/cpu02", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = cpu03
    client.publish(topic="sdn/cpu03", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = mem01
    client.publish(topic="sdn/mem01", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = mem02
    client.publish(topic="sdn/mem02", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = mem03
    client.publish(topic="sdn/mem03", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = truput01
    client.publish(topic="sdn/thruput01", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = truput02
    client.publish(topic="sdn/thruput02", payload=msg, qos=0, retain=False)
    # message you send to server
    msg = truput03
    client.publish(topic="sdn/thruput03", payload=msg, qos=0, retain=False)
    
# This timer will run job() five times, one second apart
#timer3 = multitimer.MultiTimer(interval=10, function=job3, count=5)
# Also, this timer would run indefinitely...
#timer3.start()

#fungsi tes
def job4():
    max_truput_server = max(truput_server01)
    print("Maksimal truput: "+str(max_truput_server)+" /s "+ bytes2human(max_truput_server)+"Bytes/s")  
    
# This timer will run job() five times, one second apart
#timer4 = multitimer.MultiTimer(interval=1, function=job4, count=-1)
# Also, this timer would run indefinitely...
#timer4.start()
