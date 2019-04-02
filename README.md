# beginner-scraps
Scraps of code for the GitHub & Python beginner that I am :-) 

Entries below in reverse chronological order:

* **2019-02-38 VeloCloud:** Multi-threaded Python script I wrote to interrogate VeloCloud Edge devices through the VeloCloud Orchestrator API

* **2018-09-26 ios-l2vpn-vpls1:** Files that accompany ny blog post on creating an automated simple Cisco VPLS lab: https://neckercube.com/index.php/2018/09/26/easy-cisco-vpls-l2vpn-automated-lab/

* **2018-08-21 mikrotik-l3vpn-lab1:** Files that accompany my blog post on creating an automated MikroTik MPLS L3VPN lab: https://neckercube.com/index.php/2018/08/21/mikrotik-automated-mpls-l3vpn-lab/

* **2018-04-24 subnet_conversion_drills:** This script is useful for introductory-level (CCNA, JNCIA, Network+, etc) subnet/CIDR/wildcard conversion drills. This was originally part of a larger script I was working on to do more advanced things like noncontiguous wildcards, but working out the logic for it was taking too much time away from my CCIE studies. So I decided to take out all of that stuff and release the easy part that actually works. Uses Python3 and the netaddr library.

* **2017-11-12 cfg-engine1:** This is the very beginning of an idea I had while studing for the CCIE R&S lab. With the current R&S lab exam (and all previous versions as well), there is a focus on knowing the Cisco IOS syntax pretty much inside and out so that you can evaluate the individual task and enter the appropriate configuration quickly. Being able to do this is mostly a byproduct of actually knowing the protocols inside and out, but there is also an element of having the syntax memorized as well. This script is similar in concept to flash cards, except the presented tasks contain variables that are replaced with random real variables each time the script is run. When running the script in its current form, you select how many tasks you would like generated (up to the total number of tasks available in the pool). The selected number of tasks are pulled randomly from the pool, variables are replaced with real values, and the results are output to two files, tasks.txt and answers.txt. Open the tasks.txt file and attempt to answer everything. Then open answers.txt to see how you did. This is very basic, but it's not a bad starting point.

* **2017-09-06 available_switchports.py:** Spent a couple of days attempting to work in Python3. I'm sure I got some syntax wrong. I wrote a script that uses SNMP to poll a switch, determine if it's a Cisco 48-port Gigabit, 48-port FE, or 24-port FE (that's what I have in my environment right now), or none of those. It then polls for the system uptime, and the timer for the last interface state change is subtracted. If the interface has been down for longer than 14 days, and doesn't have a description set, it is available for re-use and is displayed in the output. I wrote this script because people kept asking me which ports were available on which switches, and while I had a switch port mapping tool to handle this, I found running this script to gather the specific information I was looking for was much faster. 

* **2017-08-09 ansible-cisco-1:** First attempt with Ansible to push out configs to Cisco routers

* **2017-03-17 backup-configs.ps1:** Added an old script that I found in my archives that truly is a beginner scrap :-) It's a PowerShell script to log into SSH devices and issue a command, with the intended use case of logging into a bunch of Cisco equipment and issuing "show run" and saving the output to separate files for configuration backup.

* **2017-01-19 host-device1:** Created an iteration of the last script that attempts to log into each pingable device to grab its configured hostname to see how it compares to the configured DNS A-record

* **2017-01-13 ping-routers1.py:** Created my second script based off my first one. The script pings a list of IPs, uses nslookup to see if they have a hostname associated with them, and writes the results to a file. The list of IPs are generated programmatically instead of being entered in entirely manually, with room for a few outliers to be added manually. The goal of this script is to see if a device is reachable, and to see if the DNS entry is what it should be. Putting this script together gave me a bunch of ideas for other things :-)

* **2016-09-15 cmdinput.py:** Created my first script used on a production network, cmdinput1.py. Very simple, asks for input command, runs command against list of Cisco IOS routers listed in file "input.txt", saves the results of the command to "output.txt". I first used it to run a "show cdp n | inc SEP" across all our routers to see which locations do not have a Cisco switch, but have more than a certain number of phones connected. 
