#!/usr/bin/env python

#load netmiko
from netmiko import ConnectHandler

#load time 
from datetime import datetime

#for test ping
import subprocess

#ping a host twice (because sometimes the first packet 
#is lost due to ARP) and return True if reachable
def pingTest(host):
    try:
        subprocess.check_output("ping -c 2 "+host, shell=True)
    except Exception, e:
        return False
    return True

#take file input.txt and create a list (hostnames) with each line as an element
with open('t1s.txt') as var1:
    hostnames = var1.read().splitlines()

#make file output.txt available for appending
outfile = open('output.txt','a')

cmd = raw_input("Enter the Cisco command: ")

for var2 in hostnames:

    #initiate ping of host prior to taking action
    testping = pingTest(var2)

    if testping == True:
            #connect to device
        net_connect = ConnectHandler(device_type='cisco_ios', ip=var2, username='user', password='pass')
            #send command to device
        output = net_connect.send_command(cmd)
            #assign current time to resulttime variable
        resulttime = "%s" % (datetime.now())
            #display for screen
        print "%-5s %-10s \n\n %-10s \n\n" % (resulttime,var2,output)
            #create results to append to file
        result = "%-5s %-10s \n\n %-10s \n\n" % (resulttime,var2,output)
            #write to file
        outfile.write(result)
            #disconnect from SSH session
        net_connect.disconnect()
    else:
            #display host that is not reachable for screen
        print var2 + " is not reachable at this time.\n\n"
            #assign current time to noresulttime to variable
        noresulttime = "%s" % (datetime.now())
            #create noresult to append to file
        noresult = noresulttime + "\t" + var2 + " is not reachable at this time.\n\n"
            #write to file
        outfile.write(noresult)

#close output file
outfile.close()
