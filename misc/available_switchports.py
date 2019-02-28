#!/usr/bin/env python3

#############################################################################
# 2017-09-06
#
# This script uses SNMP to poll a list of switches, determine if they are
# Cisco 48-port GE, 48-port FE, 24-port FE, or generate a message if not,
# and then display ports that are available for re-use.
# Based on (and requires) info from Kirk Byers:
# https://pynet.twb-tech.com/blog/snmp/python-snmp-intro.html
#
# Next step: Modularize with functions (Hey, I'm still learning!)
#  I'm just glad that it runs as it is :-)
#############################################################################

from snmp_helper import snmp_get_oid,snmp_extract
from datetime import datetime

print('\nTime of Report:', datetime.now(),'\n')

dev = ('switch1','switch2')

for i in dev:

              # public = SNMP community
    device = (i, 'public', 161)

    # I know these can be generated programmatically, I'll get there, I promise

    FE24 = ('10001','10002','10003','10004','10005','10006','10007','10008',
            '10009','10010','10011','10012','10013','10014','10015','10016',
            '10017','10018','10019','10020','10021','10022','10023','10024',)

    FE48 = ('10001','10002','10003','10004','10005','10006','10007','10008',
            '10009','10010','10011','10012','10013','10014','10015','10016',
            '10017','10018','10019','10020','10021','10022','10023','10024',
            '10025','10026','10027','10028','10029','10030','10031','10032',
            '10033','10034','10035','10036','10037','10038','10039','10040',
            '10041','10042','10043','10044','10045','10046','10047','10048',)

    GE48 = ('10101','10102','10103','10104','10105','10106','10107','10108',
            '10109','10110','10111','10112','10113','10114','10115','10116',
            '10117','10118','10119','10120','10121','10122','10123','10124',
            '10125','10126','10127','10128','10129','10130','10131','10132',
            '10133','10134','10135','10136','10137','10138','10139','10140',
            '10141','10142','10143','10144','10145','10146','10147','10148',)

    try:

        #Determine which type of switch we are dealing with
        #Is it a Cisco 48-port Gigabit?
        g48raw = snmp_get_oid(device, oid='.1.3.6.1.2.1.2.2.1.2.10148')
        g48desc = snmp_extract(g48raw)
        #Is it a Cisco 48-port FastEthernet?
        f48raw = snmp_get_oid(device, oid='.1.3.6.1.2.1.2.2.1.2.10048')
        f48desc = snmp_extract(f48raw)
        #Is it a Cisco 24-port FastEthernet?
        f24raw = snmp_get_oid(device, oid='.1.3.6.1.2.1.2.2.1.2.10024')
        f24desc = snmp_extract(f24raw)

        if g48desc == 'GigabitEthernet0/48':

            print('-----------------------------------------------------------------')
            print('Interface:          VLAN:  Status:      Device:', i)
            print('-----------------------------------------------------------------')

            #system uptime .1.3.6.1.2.1.1.3.0
            uptimeraw = snmp_get_oid(device, oid='.1.3.6.1.2.1.1.3.0')
            uptime = snmp_extract(uptimeraw)
            uptint = int(uptime)
            #print('System Uptime (ticks): ', uptint)

            for o in GE48:
                #last interface state change .1.3.6.1.2.1.2.2.1.9
                oidbase = '.1.3.6.1.2.1.2.2.1.9.'
                oidstate = oidbase + o
                if1raw = snmp_get_oid(device, oidstate)
                if1 = snmp_extract(if1raw)
                if1m = int(if1)
                if1m = (uptint - if1m) / 6000 / 60 / 24
                if1m = round(if1m,1)
                if1m = abs(if1m)

                #interface description .1.3.6.1.2.1.2.2.1.2
                oidbase = '.1.3.6.1.2.1.2.2.1.2.'
                oiddesc = oidbase + o
                descraw = snmp_get_oid(device, oiddesc)
                desc = snmp_extract(descraw)

                #interface VLAN .1.3.6.1.4.1.9.9.68.1.2.2.1.2
                oidbase = '.1.3.6.1.4.1.9.9.68.1.2.2.1.2.'
                oidvlan = oidbase + o
                vlanraw = snmp_get_oid(device, oidvlan)
                vlan = snmp_extract(vlanraw)

                #interface alias .1.3.6.1.2.1.31.1.1.1.18
                oidbase = '.1.3.6.1.2.1.31.1.1.1.18.'
                oidalias = oidbase + o
                aliasraw = snmp_get_oid(device, oidalias)
                alias = snmp_extract(aliasraw)

                #current interface status .1.3.6.1.2.1.2.2.1.8  (1=up 2=down)
                oidbase = '.1.3.6.1.2.1.2.2.1.8.'
                oidstatus = oidbase + o
                statusraw = snmp_get_oid(device, oidstatus)
                status = snmp_extract(statusraw)
                statusint = int(status)


                # I ended up using only one of these options, and I tried to
                # rewrite the code appropriately, but I couldn't get it to
                # work properly, so I just left it for now. The a=1 are
                # basically just placeholders and have no meaning.
                # Remember, I'm just a beginner :-) 

                #print(status)
                if statusint == 1:
                    #Can't be used it it's currently in use
                    #print("Interface", desc, vlan, alias, "is Up for", if1m,
                    #      "days and cannot be used")
                    a=1

                elif statusint == 2:
                    if if1m < 14:
                        #Can't be used if it's been down for less than 14 days
                        #print("Interface", desc, vlan, alias, "is Down for", if1m,
                        #      "days and cannot be used")
                        a=1

                    elif alias != "":
                        #Can't be used if it has an alias set via the description command
                        #print("Interface", desc, vlan, alias, "is Down for", if1m,
                        #      "days and cannot be used")
                        a=1

                    else:
                        #Interface has been down for 14+ days and has no description set
                        print(desc, vlan,"is Down for", if1m,
                              "days and can be used")

                else:
                    #To catch unintended interfaces
                    #print("Interface", desc, vlan, alias, "status is Unknown for",
                    #      if1m, "days and cannot be used")
                    a=1


        elif f48desc == 'FastEthernet0/48':

            print('-----------------------------------------------------------------')
            print('Interface:       VLAN:  Status:         Device:', i)
            print('-----------------------------------------------------------------')

            #system uptime .1.3.6.1.2.1.1.3.0
            uptimeraw = snmp_get_oid(device, oid='.1.3.6.1.2.1.1.3.0')
            uptime = snmp_extract(uptimeraw)
            uptint = int(uptime)
            #print('System Uptime (ticks): ', uptint)

            for o in FE48:
                #last interface state change .1.3.6.1.2.1.2.2.1.9
                oidbase = '.1.3.6.1.2.1.2.2.1.9.'
                oidstate = oidbase + o
                if1raw = snmp_get_oid(device, oidstate)
                if1 = snmp_extract(if1raw)
                if1m = int(if1)
                if1m = (uptint - if1m) / 6000 / 60 / 24
                if1m = round(if1m,1)
                if1m = abs(if1m)

                #interface description .1.3.6.1.2.1.2.2.1.2
                oidbase = '.1.3.6.1.2.1.2.2.1.2.'
                oiddesc = oidbase + o
                descraw = snmp_get_oid(device, oiddesc)
                desc = snmp_extract(descraw)

                #interface VLAN .1.3.6.1.4.1.9.9.68.1.2.2.1.2
                oidbase = '.1.3.6.1.4.1.9.9.68.1.2.2.1.2.'
                oidvlan = oidbase + o
                vlanraw = snmp_get_oid(device, oidvlan)
                vlan = snmp_extract(vlanraw)

                #interface alias .1.3.6.1.2.1.31.1.1.1.18
                oidbase = '.1.3.6.1.2.1.31.1.1.1.18.'
                oidalias = oidbase + o
                aliasraw = snmp_get_oid(device, oidalias)
                alias = snmp_extract(aliasraw)

                #current interface status .1.3.6.1.2.1.2.2.1.8  (1=up 2=down)
                oidbase = '.1.3.6.1.2.1.2.2.1.8.'
                oidstatus = oidbase + o
                statusraw = snmp_get_oid(device, oidstatus)
                status = snmp_extract(statusraw)
                statusint = int(status)


                #print(status)
                if statusint == 1:
                    #Can't be used it it's currently in use
                    #print("Interface", desc, vlan, alias, "is Up for", if1m,
                    #      "days and cannot be used")
                    a=1

                elif statusint == 2:
                    if if1m < 14:
                        #Can't be used if it's been down for less than 14 days
                        #print("Interface", desc, vlan, alias, "is Down for", if1m,
                        #      "days and cannot be used")
                        a=1

                    elif alias != "":
                        #Can't be used if it has an alias set via the description command
                        #print("Interface", desc, vlan, alias, "is Down for", if1m,
                        #      "days and cannot be used")
                        a=1

                    else:
                        #Interface has been down for 14+ days and has no description set
                        print(desc, vlan,"is Down for", if1m,
                              "days and can be used")

                else:
                    #To catch unintended interfaces
                    #print("Interface", desc, vlan, alias, "status is Unknown for",
                    #      if1m, "days and cannot be used")
                    a=1


        elif f24desc == 'FastEthernet0/24':

            print('-----------------------------------------------------------------')
            print('Interface:       VLAN:  Status:         Device:', i)
            print('-----------------------------------------------------------------')

            #system uptime .1.3.6.1.2.1.1.3.0
            uptimeraw = snmp_get_oid(device, oid='.1.3.6.1.2.1.1.3.0')
            uptime = snmp_extract(uptimeraw)
            uptint = int(uptime)
            #print('System Uptime (ticks): ', uptint)

            for o in FE24:
                #last interface state change .1.3.6.1.2.1.2.2.1.9
                oidbase = '.1.3.6.1.2.1.2.2.1.9.'
                oidstate = oidbase + o
                if1raw = snmp_get_oid(device, oidstate)
                if1 = snmp_extract(if1raw)
                if1m = int(if1)
                if1m = (uptint - if1m) / 6000 / 60 / 24
                if1m = round(if1m,1)
                if1m = abs(if1m)

                #interface description .1.3.6.1.2.1.2.2.1.2
                oidbase = '.1.3.6.1.2.1.2.2.1.2.'
                oiddesc = oidbase + o
                descraw = snmp_get_oid(device, oiddesc)
                desc = snmp_extract(descraw)

                #interface VLAN .1.3.6.1.4.1.9.9.68.1.2.2.1.2
                oidbase = '.1.3.6.1.4.1.9.9.68.1.2.2.1.2.'
                oidvlan = oidbase + o
                vlanraw = snmp_get_oid(device, oidvlan)
                vlan = snmp_extract(vlanraw)

                #interface alias .1.3.6.1.2.1.31.1.1.1.18
                oidbase = '.1.3.6.1.2.1.31.1.1.1.18.'
                oidalias = oidbase + o
                aliasraw = snmp_get_oid(device, oidalias)
                alias = snmp_extract(aliasraw)

                #current interface status .1.3.6.1.2.1.2.2.1.8  (1=up 2=down)
                oidbase = '.1.3.6.1.2.1.2.2.1.8.'
                oidstatus = oidbase + o
                statusraw = snmp_get_oid(device, oidstatus)
                status = snmp_extract(statusraw)
                statusint = int(status)


                #print(status)
                if statusint == 1:
                    #Can't be used it it's currently in use
                    #print("Interface", desc, vlan, alias, "is Up for", if1m,
                    #      "days and cannot be used")
                    a=1

                elif statusint == 2:
                    if if1m < 14:
                        #Can't be used if it's been down for less than 14 days
                        #print("Interface", desc, vlan, alias, "is Down for", if1m,
                        #      "days and cannot be used")
                        a=1

                    elif alias != "":
                        #Can't be used if it has an alias set via the description command
                        #print("Interface", desc, vlan, alias, "is Down for", if1m,
                        #      "days and cannot be used")
                        a=1

                    else:
                        #Interface has been down for 14+ days and has no description set
                        print(desc, vlan,"is Down for", if1m,
                              "days and can be used")

                else:
                    #To catch unintended interfaces
                    #print("Interface", desc, vlan, alias, "status is Unknown for",
                    #      if1m, "days and cannot be used")
                    a=1


        print('-----------------------------------------------------------------\n')

    except:
        print(i, 'is not a device that this script can map, sorry.')
        print('-----------------------------------------------------------------\n')


####



'''
#original base working code

for i in dev:

    print('Device:', i)

    COMM = "public"
    PORT = 161
    device = (i, COMM, PORT)

    #system uptime .1.3.6.1.2.1.1.3.0
    uptimeraw = snmp_get_oid(device, oid='.1.3.6.1.2.1.1.3.0')
    uptime = snmp_extract(uptimeraw)
    uptint = int(uptime)
    #print('System Uptime (ticks): ', uptint)

    #last interface state change .1.3.6.1.2.1.2.2.1.9
    if1raw = snmp_get_oid(device, oid='.1.3.6.1.2.1.2.2.1.9.10142')
    if1 = snmp_extract(if1raw)
    if1m = int(if1)
    if1m = (uptint - if1m) / 6000 / 60 / 24
    if1m = round(if1m,1)
    if1m = abs(if1m)

    #interface description .1.3.6.1.2.1.2.2.1.2
    descraw = snmp_get_oid(device, oid='.1.3.6.1.2.1.2.2.1.2.10142')
    desc = snmp_extract(descraw)

    #interface VLAN .1.3.6.1.4.1.9.9.68.1.2.2.1.2
    vlanraw = snmp_get_oid(device, oid='.1.3.6.1.4.1.9.9.68.1.2.2.1.2.10142')
    vlan = snmp_extract(vlanraw)

    #interface alias .1.3.6.1.2.1.31.1.1.1.18
    aliasraw = snmp_get_oid(device, oid='.1.3.6.1.2.1.31.1.1.1.18.10142')
    alias = snmp_extract(aliasraw)

    #current interface status .1.3.6.1.2.1.2.2.1.8  (1=up 2=down)
    statusraw = snmp_get_oid(device, oid='.1.3.6.1.2.1.2.2.1.8.10142')
    status = snmp_extract(statusraw)
    statusint = int(status)


    #print(status)
    if statusint == 1:
        #Can't be used it it's currently in use
        print("Interface", desc, vlan, alias, "is Up for", if1m, "days and cannot be used")
    elif statusint == 2:
        if if1m < 14:
            #Can't be used if it's been down for less than 14 days
            print("Interface", desc, vlan, alias, "is Down for", if1m, "days and cannot be used")
        elif alias != "":
            #Can't be used if it has an alias set via the description command
            print("Interface", desc, vlan, alias, "is Down for", if1m, "days and cannot be used")
        else:
            #Interface has been down for 14+ days and has no description set
            print("Interface", desc, vlan, alias, "is Down for", if1m, "days and can be used")
    else:
        #To catch unintended interfaces
        print("Interface", desc, vlan, alias, "status is Unknown for", if1m, "days and cannot be used")

'''
