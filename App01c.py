#!/usr/bin/env python
# coding: utf-8

# #Aplikasi 01c
# #Data gathering from PsUtil
# #Serverside
# #Data Gathering from Udp Server Side (Cpu-Mem), read csv (Server respon)
# #Write to Csv (Id;Cpu;Mem;ServerResp)

# In[ ]:


import socket, threading
import pandas as pd 
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.addr = clientAddress
        print ("New connection added: ", self.addr)
        
    def run(self):
        print ("Connection from : ", self.addr)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        #statInit = True
        # Creating the first Dataframe using dictionary 
        df1 = pd.DataFrame({"id":[1] "cpu":[20], 
                         "mem":[20]})
        # Print df1 
        print(df1, "\n")
        # saving the dataframe
        filename = str(self.addr)+ '.csv'
        df1.to_csv(filename)
        #filename = str(self.addr)+ '2.csv'
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='bye':
              break            
            print ("from client %s %s" % (self.addr, msg))
            
            x = msg.split(";")
            # Creating the Second Dataframe using dictionary 
            df2 = pd.DataFrame({"id":[x[0]],"cpu":[float(x[1])],"mem":[float(x[2])]})
            df1 = df1.append(df2, ignore_index = True)
            print(df1, "\n")
            # saving the dataframe 
            df1.to_csv(filename ,sep=';')
        print ("Client at ", addr , " disconnected...")

LOCALHOST = "127.0.0.1"
PORT = 1234
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()


# In[ ]:





# In[ ]:




