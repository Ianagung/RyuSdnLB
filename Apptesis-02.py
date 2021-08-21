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
import datetime
#from matplotlib import pyplot as plt
import sys
sys.path.append(".")
from fuzzyMam3inCMTv03 import Fuzzy
import random
import pycurl
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO
# Import writer class from csv module
from csv import writer
# Importing the statistics module
from statistics import mean

broker_url = "127.0.0.1"
broker_port = 1883
add01 = 'http://192.168.146.4:80'
add02 = 'http://192.168.146.15:80'
add03 = 'http://192.168.146.16:80'
alamat_ip = [add01, add02, add03]
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
listserver = [1,2,3]
window_load = [0.1,0.1,0.1]
respon_time =[1,1,1]
max_window_load_server = 1
max_truput_server = 2741560 #max = 2741560 /s 2.6MB/s
truput_server01 = [1]
truput_server02 = [1]
truput_server03 = [1]
cpu_server01 = [1]
cpu_server02 = [1]
cpu_server03 = [1]
mem_server01 = [1]
mem_server02 = [1]
mem_server03 = [1]
mean_truput_server01 = 1
mean_truput_server02 = 1
mean_truput_server03 = 1
mean_cpu_server01 = 1
mean_cpu_server02 = 1
mean_cpu_server03 = 1
mean_mem_server01 = 1
mean_mem_server02 = 1
mean_mem_server03 = 1
f_name = 'Uji01-FZ01.csv'
# getting length of list
lengths = len(listserver)
serverCount = 1
togglestartstoptes = 2

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
    print("Value Cpu01: "+str(cpu01))

def on_message_from_cpu02(client, userdata, message):
    global cpu02
    cpu02 = float(message.payload.decode())
    print("Value Cpu02: "+str(cpu02))

def on_message_from_cpu03(client, userdata, message):
    global cpu03
    cpu03 = float(message.payload.decode())
    print("Value Cpu03: "+str(cpu03))

def on_message_from_mem01(client, userdata, message):
    global mem01
    mem01 = float(message.payload.decode())
    print("Value mem01: "+str(mem01))

def on_message_from_mem02(client, userdata, message):
    global mem02
    mem02 = float(message.payload.decode())
    print("Value mem02: "+str(mem02))

def on_message_from_mem03(client, userdata, message):
    global mem03
    mem03 = float(message.payload.decode())
    print("Value mem03: "+str(mem03))

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
    print("Nilai thruput 01: "+ str(thruput01))
    #truput_server01.append(float(thruput01))

def on_message_from_thruput02(client, userdata, message):
    global thruput02
    thruput02 = int(message.payload.decode())
    print("Nilai thruput 02: "+str(thruput02))

def on_message_from_thruput03(client, userdata, message):
    global thruput03
    thruput03 = int(message.payload.decode())
    print("Nilai thruput 03: "+str(thruput03))

def on_message_from_toggleuji(client, userdata, message):
    global togglestartstoptes
    togglestartstoptes = int(message.payload.decode())
    if togglestartstoptes == 1 :
        print("Pengujian dimulai")
    elif togglestartstoptes == 0 :
        print("Pengujian berhenti")
    

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

client.subscribe("sdn/startstoptes", qos=1)

client.message_callback_add("sdn/startstoptes", on_message_from_toggleuji)

#myFuzzy = Fuzzy(cpu_val, mem_val, truput_val)
#print(mycar.get_fuzzy())

#client.loop_forever()
client.loop_start()

print("Do Something else")

#Hitung fuzzy dan window_load
def job1Fuzzy():
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
            #print("Cpu val "+str(cpu_val)+" Mem Val "+str(mem_val)+" Thruput Val "+ str(truput_val))
        elif listserver[i]==2:
            cpu_val = cpu02
            mem_val = mem02
            #truput_val = thruput02
            truput_val = round(((thruput02 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
            #print("Cpu val "+str(cpu_val)+" Mem Val "+str(mem_val)+" Thruput Val "+ str(truput_val))
        elif listserver[i]==3:
            cpu_val = cpu03
            mem_val = mem03
            #truput_val = thruput02
            truput_val = round(((thruput03 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
            #print("Cpu val "+str(cpu_val)+" Mem Val "+str(mem_val)+" Thruput Val "+ str(truput_val))

        #do fuzzy untuk setiap server
        print("Cpu val "+str(cpu_val)+" Mem Val "+str(mem_val)+" Thruput Val "+ str(truput_val))
        myFuzzy = Fuzzy(cpu_val, mem_val, truput_val)
        delta_ld_window = myFuzzy.get_fuzzy()
        print("Perubahan Load Window Server-%s is %.5f" % ( listserver[i], delta_ld_window))
        #nilai load window diambil per detik ketika dihitung, hasil dari fuzzy direct
        #bukan kumulatif
        window_load[i] = round(delta_ld_window * 100000)
        #hitung total workload
        # window_load[i] += delta_ld_window
        # print("Load Window Server-%s is %.3f" % ( listserver[i], window_load[i]))
        # #reset jika sudah kena threshold atas dan bawah
        # #reset window_load
        # if window_load[i] > 100:
        #     window_load[i] = 90
        # if window_load[i] < 0:
        #     window_load[i] = 10
        
    #compare nilai window_load terbesar
    #find index of maximum element
    ## index of maximum element
    #update global value window load
    #max_window_load_server = 1
    max_window_load_server = window_load.index(max(window_load)) + 1 
    #jika index = 0 maka server1
    #jika index = 1 maka server2
    #print ("Server dg Load window terbesar "+max_window_load_server)
    #Publish data to MQTT Broker
    msg = str(max_window_load_server)
    print("Server yang punya max window load =", msg)
    client.publish(topic="sdn/serverno", payload=msg, qos=0, retain=False)

#publish data ke mqtt broker
#data = which server has max window load
#Random Algorithm
def job1Random():
    
    server_count = random.randint(1, 3)
    #Publish data to MQTT Broker
    msg = server_count
    print("Random - Server = ", msg)
    client.publish(topic="sdn/serverno", payload=msg, qos=0, retain=False)

#publish data ke mqtt broker
#data = which server has max window load
#Round Robin Algorithm
def job1RR():
    global serverCount 
         
#     serverCount+=1
#     if(serverCount>3):
#         serverCount=1
#     #Publish data to MQTT Broker
     #msg = serverCount
    msg = '0'
    print("Round Robin Server =", msg)
    client.publish(topic="sdn/fuzzyout", payload=msg, qos=0, retain=False)

#publish data ke mqtt broker
#data = which server has max window load
# Minimum Response Time Algorithm
def job1MinRT():
    
    #Publish data to MQTT Broker
    min_RspTime = respon_time.index(min(respon_time)) + 1
    msg = min_RspTime
    print("Server dg min Respon Time =", msg)
    client.publish(topic="sdn/serverno", payload=msg, qos=0, retain=False)
    
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	#client.publish(topic="sdn/rsptm03", payload=rsp_tm_s3, qos=0, retain=False)
# This timer will run job() five times, one second apart
timer1 = multitimer.MultiTimer(interval=2, function=job1Fuzzy, count=-1)
# Also, this timer would run indefinitely...
#timer1.start()

#Start getting Server Response From Here
def job2():
    #global time01
    global alamat_ip
    global respon_time
    for i in range(lengths):
        c = pycurl.Curl()
        buffer = BytesIO()
        #c.setopt(c.URL, 'http://pycurl.io/')
        now1 = datetime.datetime.now() # time object
        #print("now =", now1)
        #print("do curl")    
        c.setopt(c.URL, alamat_ip[i])
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        now2 = datetime.datetime.now() # time object
        selisih = now2 - now1
        #print("selisih :", selisih)
        #hasil dalam seconds
        hasil = selisih.seconds + (selisih.microseconds/1000000)
        #print("Server-" + str(i) +" Respons time = ", str(hasil))
        respon_time[i] = float(hasil)
    
# This timer will run job() five times, one second apart
timer2 = multitimer.MultiTimer(interval=4, function=job2, count=-1)
# Also, this timer would run indefinitely...
#timer2.start()

#fungsi tes
# def job3():
#     global max_truput_server
#     cpu01 = 30
#     cpu02 = 90
#     cpu03 = 30
#     mem01 = 50
#     mem02 = 90
#     mem03 = 50
#     #time01 = 10
#     #time02 = 10
#     #time03 = 10
#     #rsptm01 = 1
#     #rsptm02 = 1
#     #rsptm03 = 1
#     #rspstd01 = 1
#     #rspstd02 = 1
#     #rspstd03 = 1
#     truput01 = round(((1000000 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
#     truput02 = round(((2000000 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen
#     truput03 = round(((1000000 / max_truput_server) * 100), 2) #throughput=Bytes/s dalam satuan persen    
#     #Publish data to MQTT Broker
#     msg = cpu01
#     client.publish(topic="sdn/cpu01", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = cpu02
#     client.publish(topic="sdn/cpu02", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = cpu03
#     client.publish(topic="sdn/cpu03", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = mem01
#     client.publish(topic="sdn/mem01", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = mem02
#     client.publish(topic="sdn/mem02", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = mem03
#     client.publish(topic="sdn/mem03", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = truput01
#     client.publish(topic="sdn/thruput01", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = truput02
#     client.publish(topic="sdn/thruput02", payload=msg, qos=0, retain=False)
#     #Publish data to MQTT Broker
#     msg = truput03
#     client.publish(topic="sdn/thruput03", payload=msg, qos=0, retain=False)

#fungsi tes
def job3Uji():
    global togglestartstoptes
    global cpu01, cpu02, cpu03
    global mem01, mem02, mem03
    global thruput01, thruput02, thruput03
    global cpu_server01
    global cpu_server02
    global cpu_server03
    global mem_server01
    global mem_server02
    global mem_server03
    global truput_server01
    global truput_server02
    global truput_server03
    global mean_cpu_server01
    global mean_cpu_server02
    global mean_cpu_server03
    global mean_mem_server01
    global mean_mem_server02
    global mean_mem_server03
    global mean_truput_server01
    global mean_truput_server02
    global mean_truput_server03
    global f_name
    
    if togglestartstoptes == 1 :
        cpu_server01.append(float(cpu01))
        cpu_server02.append(float(cpu02))
        cpu_server03.append(float(cpu03))
        mem_server01.append(float(mem01))
        mem_server02.append(float(mem02))
        mem_server03.append(float(mem03))
        truput_server01.append(float(thruput01))
        truput_server02.append(float(thruput02))
        truput_server03.append(float(thruput03))
    
    elif togglestartstoptes == 0:
        
        mean_cpu_server01 = round(mean(cpu_server01), 2)
        mean_cpu_server02 = round(mean(cpu_server02), 2)
        mean_cpu_server03 = round(mean(cpu_server03), 2)
        mean_mem_server01 = round(mean(mem_server01), 2)
        mean_mem_server02 = round(mean(mem_server02), 2)
        mean_mem_server03 = round(mean(mem_server03), 2)
        mean_truput_server01 = round(mean(truput_server01), 2)
        mean_truput_server02 = round(mean(truput_server02), 2)
        mean_truput_server03 = round(mean(truput_server03), 2)
        #str(max_truput_server)
        # List 
        List=[mean_cpu_server01,mean_cpu_server02,mean_cpu_server03,
              mean_mem_server01,mean_mem_server02,mean_mem_server03,
              mean_truput_server01,mean_truput_server02,mean_truput_server03]
        
        print(','.join(map(str, List)))
        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open(f_name, 'a') as f_object:
        
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
        
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(List)
            print("saved to csv")
            #Close the file object
            f_object.close()
        #reset toggle value
        togglestartstoptes = 2
        #reset value
        cpu_server01 = [1]
        cpu_server02 = [1]
        cpu_server03 = [1]
        mem_server01 = [1]
        mem_server02 = [1]
        mem_server03 = [1]
        truput_server01 = [1]
        truput_server02 = [1]
        truput_server03 = [1]
# This timer will run job() five times, one second apart
timer3 = multitimer.MultiTimer(interval=1, function=job3Uji, count=-1)
# Also, this timer would run indefinitely...
timer3.start()

#fungsi tes
def job4():
    max_truput_server = max(truput_server01)
    print("Maksimal truput: "+str(max_truput_server)+" Byte/s "+ bytes2human(max_truput_server)+"Byte/s")  
    
# This timer will run job() five times, one second apart
timer4 = multitimer.MultiTimer(interval=1, function=job4, count=-1)
# Also, this timer would run indefinitely...
timer4.start()
