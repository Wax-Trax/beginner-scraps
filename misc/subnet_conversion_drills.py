#!/usr/bin/env python3
from random import *
from netaddr import *  # pip3 install netaddr

# Please visit neckercube.com for more network engineering stuff :-)

'''
netaddr primer: Use this information to modify this script to suit your own needs

rndip1 = rand_ip()   # my function to generate a random unicast IP (1 - 223, -127)

rndnet1 = IPNetwork(rndip1 + '/' + str(randint(8,30)))
rndnet1 is rndnet1.network     # is it the network address?
rndnet1 is rndnet1.broadcast   # is it the broadcast address?

rndnet1.ip                # ip address without CIDR notation
str(rndnet1)              # ip address with CIDR notation
rndnet1.network           # network address
rndnet1.broadcast         # broadcast address
rndnet1.netmask           # subnet mask
rndnet1.hostmask          # wildcard
rndnet1.prefixlen = 20    # change / assign different prefix length later
rndnet1.ip.bits()         # binary octets of IP address
rndnet1.network.bits()    # binary octets of network address
rndnet1.netmask.bits()    # binary octets of subnet mask
rndnet1.broadcast.bits()  # binary octets of broadcast address

list1 = list(rndnet1)     # creates a list of every IPAddress('x.x.x.x') in the range
len(list1)                # how many IPs are in the range
str(list1[1])             # access individual addresses in the range
str(choice(list1))        # random IP from range, includes net/bcast

for ip in rndnet1:        # print all IPs in range
    print(ip)

for ip in rndnet1.iter_hosts():  # print all host IPs in range (ex net/bcast)
    print(ip)

range1 = IPRange('start-ip', 'end-ip')  # creates arbitrary range

for ip in range1:   # print all IPs in arbitrary range
    print(ip)

# You can also compare IPAddress and IPNetwork in == < > <= >- != manner

'''


def rand_ip():   # Generate single random unicast IP address
    oct1 = randint(1,223)    # unicast range
    oct2 = randint(1,254)
    oct3 = randint(1,254)
    oct4 = randint(1,254)

    while oct1 == 127:   # choose a different value if 127
        oct1 = randint(1,223)
    rndip = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.' + str(oct4)
    return rndip


def rand_net():  # Generate singe random unicast IP and place it into random subnet
    rndip1 = rand_ip()

    # Place the random unicast IP addresses into a random /8 - /30
    rndnet1 = IPNetwork(rndip1 + '/' + str(randint(8,30)))

    # Choose a different random IP address and prefix if it == net/bcast address
    while rndnet1.ip is rndnet1.network or rndnet1.ip is rndnet1.broadcast:
        rndip1 = rand_ip()
        rndnet1 = IPNetwork(rndip1 + '/' + str(randint(8,30)))

    return rndnet1


def binconv(binary): # take IP and convert to dotted binary string
    binx = str(binary)
    biny = binx.split('.')
    binz = str(format(int(biny[0]), 'b').zfill(8)) + '.' + \
           str(format(int(biny[1]), 'b').zfill(8)) + '.' + \
           str(format(int(biny[2]), 'b').zfill(8)) + '.' + \
           str(format(int(biny[3]), 'b').zfill(8))
    return binz


def num_questions():
    x = 0
    while x == 0:
        try:
            qnum = int(input('\nHow many exercises do you want?: '))
            x = 1
        except:
            print('\nPlease enter a regular number: ')
    return qnum



### Basic Conversion Questions

def cidr_sub(binchoice): # CIDR > subnet
    rndnet = rand_net()
    answer = input('\nWhat is the subnet mask for /' + str(rndnet.prefixlen) + '?: ')
    if answer == str(rndnet.netmask):
        print('\n  --> Correct!')
        binary = binconv(rndnet.netmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)
    else:
        print('\n  --> Sorry, incorrect. It was ' + str(rndnet.netmask))
        binary = binconv(rndnet.netmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)

def cidr_wc(binchoice): # CIDR > wildcard
    rndnet = rand_net()
    answer = input('\nWhat is the wildcard mask for /' + str(rndnet.prefixlen) + '?: ')
    if answer == str(rndnet.hostmask):
        print('\n  --> Correct!')
        binary = binconv(rndnet.hostmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)
    else:
        print('\n  --> Sorry, incorrect. It was ' + str(rndnet.hostmask))
        binary = binconv(rndnet.hostmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)

def sub_cidr(binchoice): # Subnet > CIDR
    rndnet = rand_net()
    answer = input('\nWhat is the CIDR prefix for ' + str(rndnet.netmask) + '?: /')
    if answer == str(rndnet.prefixlen):
        print('\n  --> Correct!')
    else:
        print('\n  --> Sorry, incorrect. It was ' + str(rndnet.prefixlen))

def sub_wc(binchoice): # Subnet > wildcard
    rndnet = rand_net()
    answer = input('\nWhat is the wildcard mask for ' + str(rndnet.netmask) + '?: ')
    if answer == str(rndnet.hostmask):
        print('\n  --> Correct!')
        binary = binconv(rndnet.hostmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)
    else:
        print('\n  --> Sorry, incorrect. It was ' + str(rndnet.hostmask))
        binary = binconv(rndnet.hostmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)

def wc_cidr(binchoice): # Wildcard > CIDR
    rndnet = rand_net()
    answer = input('\nWhat is the CIDR prefix for ' + str(rndnet.hostmask) + '?: /')
    if answer == str(rndnet.prefixlen):
        print('\n  --> Correct!')
    else:
        print('\n  --> Sorry, incorrect. It was ' + str(rndnet.prefixlen))

def wc_sub(binchoice): # Wildcard > Subnet
    rndnet = rand_net()
    answer = input('\nWhat is the subnet mask for ' + str(rndnet.hostmask) + '?: ')
    if answer == str(rndnet.netmask):
        print('\n  --> Correct!')
        binary = binconv(rndnet.netmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)
    else:
        print('\n  --> Sorry, incorrect. It was ' + str(rndnet.netmask))
        binary = binconv(rndnet.netmask)
        if binchoice == 'y' or binchoice == 'Y':
            print('        Binary: ' + binary)

def basic_conversion(): ### Basic Conversion Menu
    basic_choice = ['1','2','3','4','5','6','7','q','Q']
    print('\nPlease enter your choice of the following drill types:\n')
    print('(1) CIDR notation to subnet mask')
    print('(2) CIDR notation to contiguous wildcard mask')
    print('(3) Subnet mask to CIDR notation')
    print('(4) Subnet mask to contiguous wildcard mask')
    print('(5) Contiguous wildcard mask to CIDR notation')
    print('(6) Contiguous wildcard mask to subnet mask')
    print('(7) Random')
    print('(Q) Quit\n')
    basic_mode = input('Please enter 1-7 or q: ')
    while str(basic_mode) not in basic_choice:
        basic_mode = input('Please enter 1-7 or q: ')
    if basic_mode == 'q' or basic_mode == 'Q':
        print('\n\nThanks for trying out my script. Please visit neckercube.com for more network engineering goodness.')
        quit()
    return basic_mode


def conversion(binchoice):
    loop = True
    while loop == True:
        basic_mode = basic_conversion()
        qnum = num_questions()
        count = 1
        while count < qnum+1:
            if basic_mode == '1': # CIDR > subnet
                q = cidr_sub(binchoice)
                count = count+1
            if basic_mode == '2': # CIDR > wildcard
                q = cidr_wc(binchoice)
                count = count+1
            if basic_mode == '3': # Subnet > CIDR
                q = sub_cidr(binchoice)
                count = count+1
            if basic_mode == '4': # Subnet > wildcard
                q = sub_wc(binchoice)
                count = count+1
            if basic_mode == '5': # Wildcard > CIDR
                q = wc_cidr(binchoice)
                count = count+1
            if basic_mode == '6': # Wildcard > Subnet
                q = wc_sub(binchoice)
                count = count+1
            if basic_mode == '7': #Random
                rndconv=randint(1,6)
                if rndconv == 1:
                    cidr_sub(binchoice)
                if rndconv == 2:
                    cidr_wc(binchoice)
                if rndconv == 3:
                    sub_cidr(binchoice)
                if rndconv == 4:
                    sub_wc(binchoice)
                if rndconv == 5:
                    wc_cidr(binchoice)
                if rndconv == 6:
                    wc_sub(binchoice)
                count = count+1



def main():
    print('\n---neckercube.com Subnet/Wildcard/CIDR drills---\n')
    bin_choice = ['y', 'Y', 'n', 'N']
    binchoice = input('Enable training-wheels mode (display binary in answers)? (y/n): ')
    while str(binchoice) not in bin_choice:
        binchoice = input('Please enter y or n: ')
    mode = conversion(binchoice)

main()
