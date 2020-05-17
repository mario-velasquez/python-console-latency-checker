import subprocess
import platform

# ------
# The IP Addresses on the video
# NA - 104.160.131.3
# EUW - 104.160.141.3
# EUNE - 104.160.142.3
# OCE - 104.160.156.1
# LAN - 104.160.136.3
# ------

menu = "1. North America \n2. Europe West \n3. Europe Nordic East \n4. Latin America North \n5. Oceania\n Choice: "

server = "104.160.131.3"

print("Which server do you wish to ping?: ")

choice = input(menu.rstrip())
accouracy = input("Accuracy (1-10):")
if(choice == "1"): server =  "104.160.131.3"
if(choice == "2"): server =  "104.160.141.3"
if(choice == "3"): server =  "104.160.142.3"
if(choice == "4"): server =  "104.160.136.3"
if(choice == "5"): server =  "104.160.156.1"

scanme = str(subprocess.check_output(['ping', '-n', accouracy, server]))

#print(scanme)
#b'\r\nPinging 104.160.131.3 with 32 bytes of data:\r\nReply from 104.160.131.3: bytes=32 time=54ms TTL=54\r\n\r\nPing statistics for 104.160.131.3:\r\n    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),\r\nApproximate round trip times in milli-seconds:\r\n    Minimum = 54ms, Maximum = 54ms, Average = 54ms\r\n'

Average = scanme.split("Average",1)[1] 
Maximum = scanme.split("Maximum",1)[1]
Minimum = scanme.split("Minimum",1)[1]

nuMin = ""
nuMax = ""
nuAvg = ""

for x in Minimum:
    if(x == 'm'): break
    
    if(x == "0"):
        #store
        nuMin += x
    if(x == "1"):
        #store
        nuMin += x
    if(x == "2"):
        #store
        nuMin += x
    if(x == "3"):
        #store
        nuMin += x
    if(x == "4"):
        #store
        nuMin += x
    if(x == "5"):
        #store
        nuMin += x
    if(x == "6"):
        #store
        nuMin += x
    if(x == "7"):
        #store
        nuMin += x
    if(x == "8"):
        #store
        nuMin += x
    if(x == "9"):
        #store
        nuMin += x

for x in Maximum:
    if(x == 'm'): break
    
    if(x == "0"):
        #store
        nuMax += x
    if(x == "1"):
        #store
        nuMax += x
    if(x == "2"):
        #store
        nuMax += x
    if(x == "3"):
        #store
        nuMax += x
    if(x == "4"):
        #store
        nuMax += x
    if(x == "5"):
        #store
        nuMax += x
    if(x == "6"):
        #store
        nuMax += x
    if(x == "7"):
        #store
        nuMax += x
    if(x == "8"):
        #store
        nuMax += x
    if(x == "9"):
        #store
        nuMax += x

for x in Average:
    if(x == 'm'): break
    
    if(x == "0"):
        #store
        nuAvg += x
    if(x == "1"):
        #store
        nuAvg += x
    if(x == "2"):
        #store
        nuAvg += x
    if(x == "3"):
        #store
        nuAvg += x
    if(x == "4"):
        #store
        nuAvg += x
    if(x == "5"):
        #store
        nuAvg += x
    if(x == "6"):
        #store
        nuAvg += x
    if(x == "7"):
        #store
        nuAvg += x
    if(x == "8"):
        #store
        nuAvg += x
    if(x == "9"):
        #store
        nuAvg += x


print("Maximum: " + nuMax)
print("Miminium: "+ nuMin)
print("Average: " + nuAvg)
#ping score is equal to nuMax + nuMin + nuMax + nuMin + nuAvg / 5