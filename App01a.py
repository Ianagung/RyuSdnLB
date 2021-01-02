#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Script Get Data Cpu - Ram
# Import socket module 
import socket 
import time
from psutil import cpu_percent, cpu_count, virtual_memory
def Main(): 
   
    hostName = socket.gethostname()
 
    ipaddr = socket.gethostbyname(hostName + ".local")
    print(" Host Name Is : {} " .format(hostName))
    print(" IP Address Is : {} " .format(ipaddr))

    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 1234
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
   
    
    #statInit = True
    while True: 
  
        # message you send to server 
        #message = "client3"
        message = ipaddr + ';' + str(cpu_percent()) 
                + ';' + str(virtual_memory().percent)
        print(message)
        # message sent to server 
        s.send(message.encode('ascii')) 
  
        '''if(statInit)
            # messaga received from server 
            data = s.recv(1024) 
            strdata = str(data.decode('ascii')
            # print the received message 
            # here it would be a reverse of sent message
        
            print('Received from the server :',strdata)) 
            if(strdata == 'y'||'Y')
            statInit = False
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break'''
        time.sleep( 5 )
    # close the connection 
    s.close() 


# In[ ]:


if __name__ == '__main__': 
    Main()


# In[ ]:




