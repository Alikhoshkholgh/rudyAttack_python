# rudyAttack_python
when you find a specific url to upload your content you can put it in this script to create rudy attack on that target. please note that this script only works for http web sites


+ How To run:
  + python ./dirver.py
  
  
+ About the code 'driver.py': (you should modify the variables)  
    +target = <Target-IP>
    +port = <Target-port>
    +session_count = 1 #how many connections do you want for this senario
    +uri = "upload"   #Address for uploading your content 
    +content_len = 5000000   #you should tell the target how much is your overall data 
        +(this is fake, we just want target to wait for all of packets of size:'chunksize' to be arrived)
    +chunksize = 70   #when sending junk-packets how much raw-bytes should be sent
    +timeInterval = 3 #how much this script should wait for next packet to send to target
