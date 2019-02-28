#!/usr/bin/env python

  #load time 
from datetime import datetime

  #for test ping and nslookup
import subprocess

  #perform the ping action and return true if host pings, false if it doesn't
def pingTest(host):
    try:
        subprocess.check_output("ping -c 1 -W 1 "+host, shell=True)
    except Exception, e:
        return False
    return True

  #perform nslookup on the IP in attempt to resolve the hostname
def nslookupTest(host):
    try:
        nslookup = subprocess.check_output("nslookup "+host,shell=True)
        for data in nslookup:
            data_line = nslookup.split("\n")
        for line in data_line:
            if "name =" in line:
                templist = line.split("name =")
                temphost = templist[1]
                tempsplit = temphost.split(".")
                dnshost = tempsplit[0]
    except Exception, e:
        return ""   #Return an empty string if there is no hostname
    return dnshost   #Return the DNS hostname



  #intialize generic integer list
range255 = range(255)
  #copy the integer list
ip_generic_range = range255[:]
  #convert integer list to string
i = 0
for x in ip_generic_range:
    ip_generic_range[i] = str(x)
    i += 1
  #create new lists with ip addresses
tenonerange = ip_generic_range[:]
tentworange = ip_generic_range[:]
  #build 10.1.x.1 list
i = 0
for x in tenonerange:
    tenonerange[i] = "10.1." + ip_generic_range[i] + ".1"
    i += 1
  #build 10.2.x.1 list
i = 0
for x in tentworange:
    tentworange[i] = "10.2." + ip_generic_range[i] + ".1"
    i += 1
  #Misc range list
misclist = ['10.3.1.1', '10.3.233.1', '10.11.23.1'] 


  #combine lists
ip_ranges = tenonerange + tentworange + misclist

  #The first ping may take a few seconds
print "Preparing to ping hosts..."

  #Create/open output file for appending
outfile = open('output.txt','a')

  #Display and write the results of ping + hostname
for ip in ip_ranges:

    testping = pingTest(ip) #Call pingTest function for each IP
    dnshost = nslookupTest(ip) #Call nslookupTest function for each IP

    time = "%s" % (datetime.now()) #Generate current date/time for each iteration

    if testping == True:
        print ip + dnshost + " pings" #Write results to screen 
        result = time + " " + ip + dnshost + " pings\n"  
        outfile.write(result)  #Write results to file
    else:
        print ip + dnshost + " does not ping"  #Write results to screen
        noresult = time + " " + ip + dnshost + " does not ping at this time\n"
        outfile.write(noresult)  #Write results to file

  #Close output file
outfile.close()

