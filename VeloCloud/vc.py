#!/usr/bin/env python3

###
### Jedadiah Casey, 2019-02-27
###   Please see my blog post associated with this code at neckercube.com
###

import json
import requests
import time
import threading

# Main function
def edgelivemode(edge):

    # Part of the batched multi-threading framework, this claims one of the
    #   available maxthreads
    sema.acquire()

    # While writing the script, I discovered that if an edge had not yet fully
    #   entered live mode by the time I requested the desired information, it
    #   causes the script to crash. The while/try/except construct attempts to
    #   account for this and re-run things if there is an exception
    exceptionvalue = 0

    while exceptionvalue == 0:

        try:

            # Append to existing output file
            file = open(filename, 'a')

            # JSON sent to individual edge to cause it to enter "Live" mode
            #   The first ID is the real ID of the edge itself. The second ID
            #   can be arbitrary, but I kept it the same as the edge ID so
            #   that it is the same per-edge per-session.
            livejson = '{"jsonrpc":"2.0","method":"liveMode/enterLiveMode",\
                       "params":{"id":' + str(edge['id']) \
                       + '},"id":' + str(edge['id']) + '}'

            # Send the JSON request to the VCO for the edge to enter live mode
            livemode = session1.post(urlportal, data=livejson)

            # After the live mode request is issued, the response will contain
            #   a token value that we will need to use for further information
            #   requests against the particular edge.
            jsonlive = json.loads(livemode.text)
            jsonlivedict = dict(jsonlive.get('result'))
            token = jsonlivedict.get('token')

            # JSON to set up the edge information request. ID may be arbitrary
            edgeselectjson = '{"jsonrpc":"2.0",\
                "method":"liveMode/requestLiveActions",\
                "params":{"actions":[{"action":"listDiagnostics",\
                "parameters":{}}],"token":"' + token + '"},"id":1}'
            edgeselect = session1.post(urllivedata, data=edgeselectjson)

            '''
            You must give the VC edge time to fully enter live mode before
            trying to get information from it. Some enter faster than others
            for some reason. I recommend 60 seconds as a good number that
            seems to work 99% of the time. The script will throw an exception
            if you try to access the information requested later in the script
            and the edge has not fully entered live mode. That's why I designed
            the script with while/try/except so that if it fails, it will try
            again.
            '''
            # Output for screen only, not written to file
            print('Waiting 60 seconds for ' + str(edge['name']) + \
                  ' (Edge ' + str(edge['id']) + ') live mode...')
            time.sleep(60)

            # JSON to request the results of the live mode data. ID may be
            #   arbitrary but must be unique from the last JSON request for
            #   this particular edge.
            localipjson = '{"jsonrpc":"2.0","method":"liveMode/readLiveData",\
                "params":{"token":"' + token + '"},"id":2}'

            # POST the JSON
            localip = session1.post(urllivedata, data=localipjson)

            # Use the returned data for the remainder of the function
            ip = json.loads(localip.text)

            print('\n\n' + str(edge['name']) + ' (Edge ID ' + str(edge['id'])\
                  + ')\n')
            file.write('\n\n' + str(edge['name']) + ' (Edge ID '\
                       + str(edge['id']) + ') \n')

            '''
            These next blocks of code with the four different "if" sections
            are determining if there are 1 - 4 WAN uplinks present on the edge.
            If there were 0, the edge would not be connected and would not even
            be in the list due to the previous 'CONNECTED' check. After the
            proper case of 1 - 4 is determined, the local IP address is read
            from the JSON data. This script exists in this current form because
            I needed to determine the local interface IP address. Sometimes
            this IP address is different from the WAN IP, such as with a
            cable modem that is not in bridged mode.
            
            Please see my associated blog post at neckercube.com to see how I
            arrived at the desired data locations listed in the next blocks
            of code. In each block, I am grabbing the name of the interface, 
            the local interface IP address, and the name of the WAN overlay
            attached to the interface.  
            
            All "live" information returned from the edge is present now in the
            'ip' variable. You can take this script as it is now and just
            modify the next blocks of code to retrieve your desired information.
            This is detailed in my blog post.

            I am positive there is a much more elegant way to write
            these next blocks of code, but I just needed to get the job done
            in a way that I could still understand what I did :-)            
            '''
            if len(ip['result']['data']['linkStats']['data'][1]['data']) == 1:

                interface1 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['name'] + '\n'
                print(interface1)
                file.write(interface1)

            if len(ip['result']['data']['linkStats']['data'][1]['data']) == 2:

                interface1 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['name'] + '\n'
                print(interface1)
                file.write(interface1)

                interface2 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['name'] + '\n'
                print(interface2)
                file.write(interface2)

            if len(ip['result']['data']['linkStats']['data'][1]['data']) == 3:

                interface1 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['name'] + '\n'
                print(interface1)
                file.write(interface1)

                interface2 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['name'] + '\n'
                print(interface2)
                file.write(interface2)

                interface3 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][2]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][2]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][2]['name'] + '\n'
                print(interface3)
                file.write(interface3)

            if len(ip['result']['data']['linkStats']['data'][1]['data']) == 4:

                interface1 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][0]['name'] + '\n'
                print(interface1)
                file.write(interface1)

                interface2 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][1]['name'] + '\n'
                print(interface2)
                file.write(interface2)

                interface3 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][2]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][2]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][2]['name'] + '\n'
                print(interface3)
                file.write(interface3)

                interface4 = ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][3]['interface'] + ': ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][3]['localIpAddress'] + ' / ' + \
                             ip['result']['data']['linkStats']['data'][1]\
                                 ['data'][3]['name'] + '\n'
                print(interface4)
                file.write(interface4)

            # We got our desired information without causing an exception, so
            #   we can break out of the while loop.
            exceptionvalue = 1

        except:

            '''
            If the desired information was not available as defined in the try
            block, the script will throw an exception because the data does not
            exist in the location the script is asking for. Most often this is 
            because the edge did not fully enter live mode for some reason,
            and the script logic will cause it to try the edge again after
            waiting for another 60 seconds (or whatever sleep time value you
            set). 
            '''

            # For execution display only, not written to the output file
            print('exception')

        # Part of the batched multi-threading framework, this releases one of
        #   the threads back into the maxthreads pool.
        sema.release()


# Establish current time variable
exectime = time.strftime("%Y-%m-%d_%H%M%S")

# Output file
filename = 'VC_Interfaces_' + exectime + '.txt'
file = open(filename,'w')

# VCO Login
username = "you@your.com"
password = "pass"

# VCO URLs -- change yourvco.com to what's correct for you
urllogin = "https://yourvco.com/portal/login/enterpriseLogin"
urlportal = "https://yourvco.com/portal/"
urllivedata = "https://yourvco.com/livepull/liveData"

# JSON String for login POST
loginjson = '{"username":"' + username + '","password":"' + password + '"}'

# JSON String for edges POST, ID may be arbitrary, I'm not sure :-)
edgesjson = '''
{"jsonrpc":"2.0","method":"enterprise/getEnterpriseEdgeList",
"params":{"with":["site","ha","configuration","recentLinks",
"cloudServices","vnfs","certificateSummary"]},"id":1}
'''

# Login to VCO and establish session cookie
session1 = requests.Session()
session1.post(urllogin, data=loginjson)

# Pull basic info for all edges
edgesinfo = session1.post(urlportal, data=edgesjson)

# Convert edge JSON data to dictionary
einfo = dict(json.loads(edgesinfo.text))

# Establish edges list and populate it. Each list element is a dictionary
#   containing the basic information of all VC edges currently in the
#   'CONNECTED' state. The current script doesn't handle things well if the
#   edge is in the VCO but not reachable, so this tries to account for that.
edges = []
for x in einfo['result']:
    if x['edgeState'] == 'CONNECTED':
        edges.append(x)

# Display and write to file the current time
print("Time of run: ", exectime)
file.write("Time of run: " + exectime + '\n')

# Display and write to file the number of edges connected
#   in the VCO at this moment
print(str(len(edges)) + ' edges currently connected\n')
file.write(str(len(edges)) + ' edges currently connected\n')

# Multi-threading section. Because each site takes time to process, I did not
#   want to risk potentially overloading the VCO with hundreds of simultaneous
#   requests, so I set it to batches of 10 sites at a time with maxthreads
maxthreads = 10
sema = threading.Semaphore(value=maxthreads)
threads = list()

'''
Side note before calling the main function: There are two different ways to try
this script out without having it attempt to connect to all of your VC edges. 
The first is to set the maxthreads to something real low like 1 or 2 and watch
it while you run the script. The second method is to define a few specific edges
like this:

edges = [einfo['result'][id1],einfo['result'][id2]]

Where 'id1' is the actual id number of the particular edge you want to test,
which you can find in the VCO by going to Monitor > Edges, then click or hover
over your desired edge and you will see the ID number in the URL.
'''

# Call the main function in parallel in batches set above with maxthreads
for edge in edges:
    threads = threading.Thread(target=edgelivemode, args=(edge,))
    threads.start()

# Close the file when the script is finished
file.close()

