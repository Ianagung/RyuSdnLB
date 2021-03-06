#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import multitimer
import time
import pandas as pd 

broker_url = "localhost"
broker_port = 1883
cpu01 = 10
cpu02 = 10
cpu03 = 10
mem01 = 10
mem02 = 10
mem03 = 10
time01 = 10
time02 = 10
time03 = 10
add01 = 'http://192.168.8.1'
add02 = 'http://192.168.8.2'
add03 = 'http://192.168.8.3'
rsp_tm_s1 = 1
rsp_tm_s2 = 1
rsp_tm_s3 = 1
rsp_std_s1 = 1
rsp_std_s2 = 1
rsp_std_s3 = 1

#create initial dataframe
# intialise data of lists. 
datadf = {'id':['server1','server2','server3'],'cpu':[cpu01,cpu02,cpu03], 'mem':[mem01,mem02,mem03],'rsp_tm':[time01,time02,time03]}  
# Create DataFrame 
df1 = pd.DataFrame(datadf)

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " ,rc)
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

#Start get Cpu Mem Data from here
def on_message_from_cpumem01(client, userdata, message):
	global cpu01
	global mem01
	cpumem = str(message.payload.decode("utf-8"))
    print("Message Recieved from Server01: "+ cpumem)
    x = cpumem.split(";")
	cpu01 = float(x[1])
	mem01 = float(x[2])

def on_message_from_cpumem02(client, userdata, message):
	global cpu02
	global mem02
	cpumem = str(message.payload.decode("utf-8"))
    print("Message Recieved from Server02: "+ cpumem)
    x = cpumem.split(";")
	cpu02 = float(x[1])
	mem02 = float(x[2])
    

def on_message_from_cpumem03(client, userdata, message):
	global cpu03
	global mem03
	cpumem = str(message.payload.decode("utf-8"))
    print("Message Recieved from Server03: "+ cpumem)
    x = cpumem.split(";")
	cpu03 = float(x[1])
	mem03 = float(x[2])

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

client.subscribe("sdn/cpumem01", qos=0)

client.message_callback_add("sdn/cpumem01", on_message_from_cpumem01)

client.subscribe("sdn/cpumem02", qos=0)

client.message_callback_add("sdn/cpumem02", on_message_from_cpumem02)

client.subscribe("sdn/cpumem03", qos=0)

client.message_callback_add("sdn/cpumem03", on_message_from_cpumem03)


#Start getting Server Response From Here
def job1():
	global time01
    global add01
    c = pycurl.Curl()
    buffer = BytesIO()
    #c.setopt(c.URL, 'http://pycurl.io/')
    now1 = datetime.datetime.now() # time object
    print("now =", now1)
    print("do curl")    
    c.setopt(c.URL, add01)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    now2 = datetime.datetime.now() # time object
    selisih = now2 - now1
    #print("selisih :", selisih)
    #hasil dalam seconds
    hasil = selisih.seconds + (selisih.microseconds/1000000)
    print("Server1 Respons time =", hasil)
    time01 = float(hasil)

# This timer will run job() five times, one second apart
timer1 = multitimer.MultiTimer(interval=10, function=job1, count=-1)
# Also, this timer would run indefinitely...
timer1.start()

#Start getting Server Response From Here
def job2():
	global time02
	global add02
    c = pycurl.Curl()
    buffer = BytesIO()
    #c.setopt(c.URL, 'http://pycurl.io/')
    now1 = datetime.datetime.now() # time object
    print("now =", now1)
    print("do curl")    
    c.setopt(c.URL, add02)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    now2 = datetime.datetime.now() # time object
    selisih = now2 - now1
    #print("selisih :", selisih)
    #hasil dalam seconds
    hasil = selisih.seconds + (selisih.microseconds/1000000)
    print("Server2 Respons time =", hasil)
    time012 = float(hasil)

# This timer will run job() five times, one second apart
timer2 = multitimer.MultiTimer(interval=10, function=job2, count=-1)
# Also, this timer would run indefinitely...
timer2.start()

#Start getting Server Response From Here
def job3():
	global time03
	global add03
    c = pycurl.Curl()
    buffer = BytesIO()
    #c.setopt(c.URL, 'http://pycurl.io/')
    now1 = datetime.datetime.now() # time object
    print("now =", now1)
    print("do curl")    
    c.setopt(c.URL, add03)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    now2 = datetime.datetime.now() # time object
    selisih = now2 - now1
    #print("selisih :", selisih)
    #hasil dalam seconds
    hasil = selisih.seconds + (selisih.microseconds/1000000)
    print("Server3 Respons time =", hasil)
    time03 = float(hasil)

# This timer will run job() five times, one second apart
timer3 = multitimer.MultiTimer(interval=10, function=job3, count=-1)
# Also, this timer would run indefinitely...
timer3.start()


time.sleep( 2 )
#Start collect all data
#save to dataframe
#ready to print to csv
#publish data clean to MQTT broker
def job4():
	global df1
	global rsp_tm_s1
	global rsp_tm_s2
	global rsp_tm_s3
	global rsp_std_s1
	global rsp_std_s2
	global rsp_std_s3
	global cpu01
	global cpu02
	global cpu03
	global mem01
	global mem02
	global mem03
	global time01
	global time02
	global time03
	global client
	# Appending a Data Frame
	s = pd.DataFrame({'id':['server1','server2','server3'],'cpu':[cpu01,cpu02,cpu03], 'mem':[mem01,mem02,mem03],'rsp_tm':[time01,time02,time03]}) 
	  
	# makes index continuous 
	df1= df1.append(s, ignore_index = True)   
	print(df1, "\n")

	#select column dataframe for rsp_tm only
	# Set 'Name' column as index  
	# on a Dataframe 
	df = df1
	df.set_index('id', inplace = True) 
	  
	# Using the operator .loc[] to  
	# select multiple rows with some 
	# particular columns 
	df_s1 = df.loc[['server1'], 
	               ['rsp_tm'] ]
	rsp_tm_s1 = df_s1['rsp_tm'].tail().mean()
	rsp_std_s1 = df_s1['rsp_tm'].std()
	# Show the dataframe 
	print("s1 respon time mean(last 5) = ", rsp_tm_s1)
	print("s1 respon time std = ", rsp_std_s1)
	print(df_s1, "\n")

	df_s2 = df.loc[['server2'], 
	               ['rsp_tm']]   
	rsp_tm_s2 = df_s2['rsp_tm'].tail().mean()
	rsp_std_s2 = df_s2['rsp_tm'].std()
	# Show the dataframe 
	print("s2 respon time mean(last 5) = ", rsp_tm_s2)
	print("s2 respon time std = ", rsp_std_s2)
	print(df_s2, "\n")

	df_s3 = df.loc[['server3'], 
	               ['rsp_tm'] ]  
	rsp_tm_s3 = df_s3['rsp_tm'].tail().mean()
	rsp_std_s3 = df_s3['rsp_tm'].std()
	# Show the dataframe 
	print("s3 respon time mean(last 5) = ", rsp_tm_s3)
	print("s3 respon time std = ", rsp_std_s3)
	print(df_s3, "\n")

	#Publish data to MQTT Broker
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/rsptm01", payload=rsp_tm_s1, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/rsptm02", payload=rsp_tm_s2, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/rsptm03", payload=rsp_tm_s3, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/rspstd01", payload=rsp_std_s1, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/rspstd02", payload=rsp_std_s2, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/rspstd03", payload=rsp_std_s3, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/cpu01", payload=cpu01, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/cpu02", payload=cpu02, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/cpu03", payload=cpu03, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/mem01", payload=mem01, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/mem02", payload=mem02, qos=0, retain=False)
	#client.publish(topic="sdn/cpumem01", payload=msg, qos=1, retain=False)
	client.publish(topic="sdn/mem03", payload=mem03, qos=0, retain=False)

# This timer will run job() five times, one second apart
timer4 = multitimer.MultiTimer(interval=1, function=job4, count=5)
# Also, this timer would run indefinitely...
timer4.start()
#Do Fuzzy

#Start Lopp MQTT
client.loop_forever()

print("Do Something else")
