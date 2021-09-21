from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from httplib import HTTPResponse
from os import curdir,sep
import paho.mqtt.client as mqtt

#Create a index.html aside the code
#Run: python server.py
#After run, try http://localhost:8080/
broker_url = "192.168.53.101"
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

#msg = "1"
print("Pengujian Load Balancing dimulai")

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path  = '/index.html'
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimeType = 'text/html'
                sendReply = True
            if sendReply == True:
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimeType)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                msg = "1"
                client.publish(topic="sdn/request01", payload=msg, qos=0, retain=False)
                # client.publish(topic="sdn/request02", payload=msg, qos=0, retain=False)
                # client.publish(topic="sdn/request02", payload=msg, qos=0, retain=False)
            return
        except IOError:
            self.send_error(404,'File not found!')


def run():
    print('http server is starting...')
    #by default http server port is 80
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    try:
        print ('http server is running...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()

if __name__ == '__main__':
    run()