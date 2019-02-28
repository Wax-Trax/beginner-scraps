'''
This file contains the various tasks, along with the configuration solutions.
The tasks are in dictionary format, with the task (question) as the key, and
the solution (answer) as the value.

Variables and meanings used inside the strings in this file:
These variables get passed to randomvar.py and are replaced with actual values.

These are just for quick easy personal reference, you should change these to whatever
 is appropriate for you.

SINT(1-16) = random serial interfaces
EINT(1-16) = random ethernet interfaces
USERNAME(1-10) = random silly usernames
PASSWORD(1-10) = random silly passwords
NAMEx(1-10) = random hostnames, group names, etc.
RND10x(1-10) = randomized list 1 - 10
RND100x(1-10) = 10 random samples from 100
REVPCNTx(1-10) = 100 - RND100x(1-10) for reverse percent
RND1000x(1-10) = 10 random samples from 1000
RND4094x(1-10) = 10 random samples from 1 - 4094, excluding 1002-1005, for VLANs
RND24 = random 2, 3, or 4
RNDBW(1-10) = 10 random samples from 100k - 10M in 100k increments
              Tasks display as Mbps, Answers display as kbps

RNDNET(1-4)IP    = random IP
RNDNET(1-4)PFX   = prefix length (the x in /x)
RNDNET(1-4)CIDR  = x.x.x.x/x
RNDNET(1-4)NET   = network address
RNDNET(1-4)BC    = bcast address
RNDNET(1-4)MSK   = subnet mask
RNDNET(1-4)WC    = wildcard mask

RNDIPRANGE(1-4) = standalone unicast IP range with /24   x.x.x.x - y
  RNDIPRANGEst(1-4) = starting address from that range   x.x.x.x
  RNDIPRANGEen(1-4) = ending address from that range     x.x.x.y

RNDMAC(1-4) = random MAC address in xxxx.yyyy.zzzz format

RNDSTPBID = random choice 0  4096  8192  12288 16384 20480 24576 28672
                       32768 36864 40960 45056 49152 53248 57344 61440
RNDSTPPID = random choice 0 64 128 192

Key/Value pairs below are separated with a #. This is just for visual clarity.

'''

tasks = {


'''
Configure the SINT1 interface using a Cisco-proprietary encapsulation.
''':
'''
interface SINT1
 encapsulation hdlc
''',
#
'''
Configure the SINT1 interface using a standard (non-frame-relay) encapsulation.
''':
'''
interface SINT1
 encapsulation ppp
 ''',
#
'''
Configure the synchronous serial interface SINT1 to use the default
encapsulation.
''':
'''
interface SINT1
 encapsulation hdlc
 ''',
#
'''
Configure the router to request PAP authentication on the SINT1 interface.
The expected username is 'USERNAME1', and the expected
password is 'PASSWORD1'.
''':
'''
username USERNAME1 password PASSWORD1
interface SINT1
 encapsulation ppp
 ppp authentication pap
''',
#
'''
Configure the router to authenticate to its neighbor on the SINT1 interface
via PAP with the username 'USERNAME1', and the
password 'PASSWORD1'.
''':
'''
interface SINT1
 encapsulation ppp
 ppp pap sent-username USERNAME1 password PASSWORD1
''',
#
'''
Configure the router to authenticate its neighbor on the SINT1 interface
via CHAP with the username 'USERNAME1', and the
password 'PASSWORD1'.
''':
'''
username USERNAME1 password PASSWORD1
interface SINT1
 encapsulation ppp
 ppp authentication chap
''',
#
'''
Configure the router to authenticate to its neighbor on the SINT1 interface
via CHAP. The router's hostname is 'rtr-NAMEx1'. The neighbor
(rtr-NAMEx2) has already been properly configured. It uses the password
'PASSWORD1' for CHAP authentication.
''':
'''
username rtr-NAMEx2 password PASSWORD1
interface SINT1
 encapsulation ppp
 ppp authentication chap
 ppp chap hostname rtr-NAMEx1
''',
#
'''
Configure the router to attempt to authenticate on the SINT1 interface with
CHAP. Fall back to PAP authentication if CHAP fails.
''':
'''
interface SINT1
 encapsulation ppp
 ppp authentication chap pap
''',
#
'''
Configure the router to drop the PPP session on the SINT1 interface if more
than RND100x1 percent of the traffic is dropped.
''':
'''
interface SINT1
 encapsulation ppp
 ppp quality REVPCNTx1
 ''',
 #
'''
Configure the router to use PPP with Predictor compression on interface SINT1.
''':
'''
interface SINT1
 encapsulation ppp
 compress predictor
 ''',
 #
'''
Router 'rtr-NAMEx1' is configured for PPP on its SINT1 interface.
Configure the router to automatically assign IP address 'RNDNET1IP'
to the connected device.
''':
'''
interface SINT1
 peer default ip address RNDNET1IP
''',
#
'''
Router 'rtr-NAMEx1' is configured for PPP on its SINT1 interface.
Configure the router to automatically receive its IP address as part
of the PPP link establishment process.
''':
'''
interface SINT1
 ip address negotiated
''',
#
'''
Router 'rtr-NAMEx1' is configured for PPP on its SINT1 interface.
Configure the router to automatically assign IP addresses via PPP from
the pool 'NAMEx2' with the range of IP addresses
from RNDIPRANGE1.
''':
'''
ip address-pool local
ip local pool NAMEx2 RNDIPRANGEst1 RNDIPRANGEen1

interface SINT1
 peer default ip address pool NAMEx2
''',
#
'''
Prevent the router from automatically installing a PPP host route to the
other end of the link on interface SINT1.
''':
'''
interface SINT1
 no peer neighbor-route
''',
#
'''
Router 'rtr-NAMEx1' is configured for PPP on its SINT1 interface.
Configure the router to automatically install a default route to its
connected peer on the SINT1 interface.
''':
'''
interface SINT1
 ppp ipcp route default
''',
#
'''
Configure the router to use PPP to bundle together interfaces SINT1 and SINT2
using bundle number 'RND100x1'. Configure the bundle with IP 'RNDNET1IP' with
the '/RNDNET1PFX' prefix.
''':
'''
interface multilink RND100x1
 ip address RNDNET1IP RNDNET1MSK
 encapsulation ppp
 ppp multilink
 ppp multilink group RND100x1

 interface SINT1
  no ip address
  encapsulation ppp
  ppp multilink
  ppp multilink group RND100x1

 interface SINT2
  no ip address
  encapsulation ppp
  ppp multilink
  ppp multilink group RND100x1
''',
#
'''
Configure the PPP multilink bundle RND100x1 to go down if there are fewer
than RND24 operational interfaces.
''':
'''
interface multilink RND100x1
 ppp multilink min-links RND24 mandatory
 ''',
#
'''
Configure rtr-NAMEx1 as a PPPoE server.

-Assign addresses to connected clients from the local IP
  pool 'NAMEx2' in the range of 'RNDIPRANGE1'.
-Configure Virtual Template RND100x1 to use interface Loopback RND100x2
  for its IP address source.
-Loopback RND100x2's IP address is 'RNDNET1IP' with a /RNDNET1PFX mask.
-Account for PPPoE overhead on the Virtual Template interface.
-Assign the EINT1 interface to the 'NAMEx3' PPPoE server.
''':
'''
ip local pool NAMEx2 RNDIPRANGEst1 RNDIPRANGEen1

interface loopback RND100x2
 ip address RNDNET1IP RNDNET1MSK

interface virtual-template RND100x1
 ip unnumbered loopback RND100x2
 peer default ip address pool NAMEx2
 mtu 1492
 ip tcp adjust-mss 1452

bba-group pppoe NAMEx3
 virtual-template RND100x1

interface EINT1
 pppoe enable group NAMEx3
''',
#
'''
Configure rtr-NAMEx1 as a PPPoE client on interface EINT1. The PPPoE
server will assign an IP address. Be sure to account for PPPoE overhead,
and ensure a default route toward the PPPoE server is installed automatically.
''':
'''
interface dialer 1
 encapsulation ppp
 ip address negotiated
 ppp ipcp route default
 mtu 1492
 ip tcp adjust-mss 1452
 dialer pool 1

interface EINT1
 pppoe-client dial-pool-number 1
''',
#
'''
Configure tunnel interface RND100x1 using point-to-point GRE encapsulation.
The interface is assigned IP 'RNDNET1CIDR'. The source is interface 'EINT1'.
The tunnel destination is 'RNDNET2IP'. Set the tunnel to report a
bandwidth of RNDBW1 Mbps.
''':
'''
interface tunnel RND100x1
 ip address RNDNET1IP RNDNET1MSK
 tunnel source EINT1
 tunnel destination RNDNET2IP
 bandwidth RNDBW1
''',
#
'''
Configure the tunnel RND100x1 interface to use a mode that places the inner
IP packet inside another IP header. The source IP address is 'RNDNET1IP'.
The destination address is 'RNDNET2IP'. Assign the IP
address 'RNDNET3CIDR' to the tunnel interface.
''':
'''
interface tunnel RND100x1
 ip address RNDNET3IP RNDNET3MSK
 tunnel source RNDNET1IP
 tunnel destination RNDNET2IP
 tunnel mode ipip
''',
#
'''
Configure the tunnel interface RND100x1 with the source EINT1 and
the IP address 'RNDNET1CIDR'. Set the appropriate tunnel mode to
support DMVPN Phase 3 operations.
''':
'''
interface tunnel RND100x1
 ip address RNDNET1IP RNDNET1MSK
 tunnel source EINT1
 tunnel mode gre multipoint
''',
#
'''
Configure the switch to participate in Layer 3 operations on
'VLAN RND4094x1' with the IP address 'RNDNET1CIDR'. Assume
VTP Transparent mode.
''':
'''
interface vlan RND4094x1
 ip address RNDNET1IP RNDNET1MSK
''',
#
'''
Configure rtr-NAMEx1 to bridge together EINT1 and EINT2. Number
the appropriate interface with 'RND100x1'. The combined links will
still participate in routing. Use IP address 'RNDNET1CIDR'
on the interface.
''':
'''
bridge irb
bridge RND100x1 protocol ieee
bridge RND100x1 route ip

interface bvi RND100x1
 ip address RNDNET1IP RNDNET1MSK

interface EINT1
 no ip address
 bridge-group RND100x1

interface EINT2
 no ip address
 bridge-group RND100x1
''',
#
'''
Configure sw-NAMEx1's EINT1 interface to participate in
VLAN RND4094x1 unconditionally. Assume VTP Transparent mode.
''':
'''
interface EINT1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 interface to participate in
VLAN RND4094x1 unconditionally. The voice VLAN is RND4094x2.
The voice VLAN should use IEEE 802.1p priority tagging.
Assume VTP Transparent mode.
''':
'''
interface EINT1
 switchport access vlan RND4094x1
 switchport voice vlan RND4094x2
 switchport voice vlan dot1p
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 interface to carry multiple VLANs using
an industry-standard protocol. The interface should carry multiple
VLANs regardless of how the other end of the link is configured.
Ensure only VLANs RND4094x1 and RND4094x2 are permitted on the link.
''':
'''
interface EINT1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan RND4094x1,RND4094x2
''',
#
'''
Configure sw-NAMEx1's EINT1 interface to carry multiple VLANs using
an industry-standard protocol. The interface should carry multiple
VLANs regardless of how the other end of the link is configured, and
should not attempt to let the other end of the link know what mode
the link is in. Prevent VLANs RND4094x1 and RND4094x2 from traversing
the link.
''':
'''
interface EINT1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport nonegotiate
 switchport trunk pruning vlan RND4094x1,RND4094x2
''',
#
'''
Configure sw-NAMEx1's EINT1 interface to carry multiple VLANs using
an industry-standard protocol, as long as the other end of the link
is willing to do the same. This end of the link should actively try
to form a trunk. If the other end of the link will not form a trunk,
the link should participate in VLAN RND4094x1. Assume VTP Transparent mode.
''':
'''
interface EINT1
 switchport trunk encapsulation dot1q
 switchport access vlan RND4094x1
 switchport mode dynamic desirable
''',
#
'''
Configure sw-NAMEx1's EINT1 interface to carry multiple VLANs using
an industry-standard protocol, as long as the other end of the link
is willing to do the same. This end of the link should not actively try
to form a trunk. If a trunk is formed, frames traversing VLAN RND4094x2
should not be tagged. If the other end of the link will not form a trunk,
the link should participate in VLAN RND4094x1. Assume VTP Transparent mode.
''':
'''
interface EINT1
 switchport trunk encapsulation dot1q
 switchport trunk native vlan RND4094x2
 switchport access vlan RND4094x1
 switchport mode dynamic auto
''',
#
'''
Configure sw-NAMEx1's EINT1 interface to carry multiple VLANs using
an industry-standard protocol, as long as the other end of the link
is willing to do the same. This end of the link should not actively try
to form a trunk. Whether a trunk is formed or not, frames on VLAN RND4094x1
should not be tagged. Assume VTP Transparent mode.
''':
'''
interface EINT1
 switchport trunk encapsulation dot1q
 switchport trunk native vlan RND4094x1
 switchport access vlan RND4094x1
 switchport mode dynamic auto
''',
#
'''
Configure sw-NAMEx1 so that all fiber interfaces are automatically
disabled if the ports are physically misconnected. Ensure probes
are sent every 10 seconds.
''':
'''
udld enable
udld message time 10
''',
#
'''
Configure sw-NAMEx1 so that all fiber interfaces are automatically
disabled if the ports are physically misconnected or if one-way
traffic is detected. Ensure probes are sent every 10 seconds.
''':
'''
udld aggressive
udld message time 10
''',
#
'''
Configure sw-NAMEx1 so that interface EINT1 is automatically
disabled if the port is physically misconnected or if one-way
traffic is detected. Ensure probes are sent every 10 seconds.
''':
'''
interface EINT1
 udld port aggressive
 udld message time 10
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces as EtherChannel RND100x1.
This is a static Layer 2 EtherChannel. The EtherChannel should participate
in VLAN RND4094x1. Assume VTP Transparent mode.
''':
'''
interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode on

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using a Cisco-proprietary protocol.
The EtherChannel should participate in VLAN RND4094x1.
Assume VTP Transparent mode.
''':
'''
interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode desirable

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to attempt to form
Layer 2 EtherChannel RND100x1 using a Cisco-proprietary protocol
if the other side initiates communications. The EtherChannel should
participate in VLAN RND4094x1. Assume VTP Transparent mode.
''':
'''
interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode auto

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to attempt to form
Layer 2 EtherChannel RND100x1 using an industry-standard protocol
if the other side initiates communications. The EtherChannel should
participate in VLAN RND4094x1. Assume VTP Transparent mode.
''':
'''
interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode passive

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.
The EtherChannel should participate in VLAN RND4094x1.
Assume VTP Transparent mode.
''':
'''
interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.
Configure the switch to have the best chance of making link bundling
decisions. Configure interface EINT1 to have the best chance
of being selected as active (as opposed to hot standby).
The EtherChannel should participate in VLAN RND4094x1.
Assume VTP Transparent mode.
''':
'''
lacp system-priority 0

interface EINT1
 switchport
 lacp port-priorty 0
 channel-group RND100x1 mode active

interface EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1, EINT2, EINT3 and EINT4 interfaces to
actively attempt to form Layer 2 EtherChannel RND100x1 using an
industry-standard protocol.

Configure the switch to have the best chance of making link
bundling decisions. Interfaces EINT1 and EINT2 should be made
active, and interfaces EINT3 and EINT4 should be hot standby.

The EtherChannel should participate in VLAN RND4094x1.
Assume VTP Transparent mode.
''':
'''
lacp system-priority 0

interface EINT1
 switchport
 lacp port-priorty 0
 channel-group RND100x1 mode active

interface EINT2
 switchport
 lacp port-priorty 0
 channel-group RND100x1 mode active

interface EINT3
 switchport
 channel-group RND100x1 mode active

interface EINT4
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
 lacp max-bundle 2
''',
#
'''
Prevent sw-NAMEx1 from displaying a message when there is
an error with the EtherChannel configuration.
''':
'''
no spanning-tree etherchannel guard misconfig
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 3 EtherChannel RND100x1 using an industry-standard protocol.
Configure the IP address 'RNDNET1CIDR'.
''':
'''
interface range EINT1,EINT2
 no switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 no switchport
 ip address RNDNET1IP RNDNET1MSK
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.

The EtherChannel should participate in VLAN RND4094x1. Assume VTP Transparent mode.

The EtherChannel should distribute traffic across the links favorable to
multiple MAC addresses communicating to a single MAC address.
''':
'''
port-channel load-balance src-mac

interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.

The EtherChannel should participate in VLAN RND4094x1. Assume VTP Transparent mode.

The EtherChannel should distribute traffic across the links favorable to
multiple IP addresses communicating to a single IP address.
''':
'''
port-channel load-balance src-ip

interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.

The EtherChannel should participate in VLAN RND4094x1. Assume VTP Transparent mode.

The EtherChannel should distribute traffic across the links favorable to
a single MAC address communicating to multiple MAC addresses.
''':
'''
port-channel load-balance dst-mac

interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.

The EtherChannel should participate in VLAN RND4094x1. Assume VTP Transparent mode.

The EtherChannel should distribute traffic across the links favorable to
a single IP address communicating to multiple IP addresses.
''':
'''
port-channel load-balance dst-ip

interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.

The EtherChannel should participate in VLAN RND4094x1. Assume VTP Transparent mode.

The EtherChannel should distribute traffic across the links favorable to
multiple source and destination MAC addresses.
''':
'''
port-channel load-balance src-dst-mac

interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1's EINT1 and EINT2 interfaces to actively attempt
to form Layer 2 EtherChannel RND100x1 using an industry-standard protocol.

The EtherChannel should participate in VLAN RND4094x1. Assume VTP Transparent mode.

The EtherChannel should distribute traffic across the links favorable to
multiple source and destination IP addresses.
''':
'''
port-channel load-balance src-dst-ip

interface range EINT1,EINT2
 switchport
 channel-group RND100x1 mode active

interface port-channel RND100x1
 switchport access vlan RND4094x1
 switchport mode access
''',
#
'''
Configure sw-NAMEx1 to automatically reset errdisabled ports
after 90 seconds.
''':
'''
errdisable recovery cause all
errdisable recovery interval 90
''',
#
'''
Configure sw-NAMEx1 to disable CDP across all ports.
''':
'''
no cdp run
''',
#
'''
Configure sw-NAMEx1 to prevent CDP from advertising on interface SINT1.
CDP should advertise on all other ports every 15 seconds, and retain
received CDP entries for 45 seconds.
''':
'''
cdp timer 15
cdp holdtime 45

interface SINT1
 no cdp enable
''',
#
'''
Configure sw-NAMEx1 to advertise information via LLDP, but prevent
LLDP from advertising on interface SINT1. Prevent interface SINT2
from accepting LLDP advertisements.

LLDP should advertise every 20 seconds, and retain received entries
for 60 seconds.
''':
'''
lldp run

lldp timer 20
lldp holdtime 60

interface SINT1
 no lldp transmit

interface SINT2
 no lldp receive
''',
#
'''
Configure sw-NAMEx1 so that MAC addresses in VLAN RND4094x1 remain
valid for 10 minutes. The switch should also create a syslog entry
whenever there is a change in the MAC address table. Configure
the switch with a static MAC address 'RNDMAC1' for
VLAN RND4094x2 on interface EINT1. The switch should drop traffic
from MAC 'RNDMAC2' on VLAN RND4094x3. Do not use an ACL to
accomplish this.
''':
'''
mac address-table aging-time 600 vlan RND4094x1
mac address-table notification change
mac address-table static RNDMAC1 vlan RND4094x2 interface EINT1
mac address-table static RNDMAC2 vlan RND4094x3 drop
''',
#
'''
Configure sw-NAMEx1 to support an MTU of 9000 bytes. Configure
interface EINT1 as routed, with IP address 'RNDNET1CIDR'
and an MTU of 9000 bytes.
''':
'''
system mtu jumbo 9000
system mtu routing 9000

reload

interface EINT1
 no switchport
 ip address RNDNET1IP RNDNET1MSK
''',
#
'''
Configure SPAN session RND24 with VLAN RND4094x1 as the source, and
interface EINT1 as the destination. Include only received traffic
in the session.
''':
'''
monitor session RND24 source vlan RND4094x1 rx
monitor session RND24 destination interface EINT1
''',
#
'''
Configure SPAN session RND24 with interface EINT1 as the source, and
interface EINT2 as the destination. EINT1 is an 802.1Q trunk. Ensure
VLAN tags are kept when mirroring the traffic to EINT2.
''':
'''
monitor session RND24 source interface EINT1
monitor session RND24 destination interface EINT2 encapsulation replicate
''',
#
'''
Configure SPAN session RND24 with interface EINT1 as the source, and
interface EINT2 as the destination. EINT1 is an 802.1Q trunk. Ensure
only VLAN RND4094x1 is mirrored to EINT2.
''':
'''
monitor session RND24 source interface EINT1
monitor session RND24 filter vlan RND4094x1
monitor session RND24 destination interface EINT2
''',
#
'''
Configure SPAN session RND24 with vlan RND4094x1 as the source, and
interface EINT1 as the destination. Enable the session to accept
incoming traffic from the SPAN destination.
''':
'''
monitor session RND24 source vlan RND4094x1
monitor session RND24 destination interface EINT1 ingress
''',
#
'''
Configure SPAN session RND24 with vlan RND4094x1 as the source, and
interface EINT1 as the destination. Only mirror traffic sourced
from RNDNET1NET/RNDNET1PFX.
''':
'''
ip access-list standard NAMEx1
 permit RNDNET1NET RNDNET1WC

monitor session RND24 source vlan RND4094x1
monitor session RND24 filter ip access-group NAMEx1
monitor session RND24 destination interface EINT1
''',
#
'''
Configure sw-NAMEx1 to mirror traffic on interface EINT1 to
interface EINT2 on sw-NAMEx2 across VLAN RND4094x1 via session RND24.
Assume proper Layer 2 connectivity between the two switches.
''':
'''
sw-NAMEx1:

vlan RND4094x1
 remote-span

monitor session RND24 source interface EINT1
monitor session RND24 destination remote vlan RND4094x1

----

sw-NAMEx2:

vlan RND4094x1
 remote-span

monitor session RND24 source remote vlan RND4094x1
monitor session RND24 destination interface EINT2
''',
#
'''
Configure sw-NAMEx1 in VTP Server mode for domain NAMEx2 using
version 2, with the password 'PASSWORD1'. The switch should not
advertise information about VLANs if there are no stations attached.
''':
'''
vtp domain NAMEx2
vtp mode server
vtp password PASSWORD1
vtp version 2
vtp pruning
''',
#
'''
sw-NAMEx1 is running VTP Version 3. Add VLAN RND4094x1 to the switch.
''':
'''
vtp primary-server vlan
vlan RND4094x1
 exit
''',
#
'''
Configure Spanning-Tree Protocol so that VLAN RND4094x1 is root. Assume
all settings are at their defaults. Configure VLAN RND4094x2 with a
base priority of RNDSTPBID. VLAN RND4094x3 should have a base priority of
28672. Do not use any priority statements to accomplish this.
''':
'''
spanning-tree vlan RND4094x1 root primary
spanning-tree vlan RND4094x2 priority RNDSTPBID
spanning-tree vlan RND4094x3 root secondary
''',
#
'''
On interface EINT1, adjust the Spanning-Tree Protocol value associated
with operational bandwidth to a value of RND1000x1. This should be applied to
all VLANs.

Interfaces EINT2 and EINT3 both connect to interfaces EINT2 and EINT3
of the upstream designated switch. Configure EINT3 so that it has a
better chance of being in the forwarding state rather than being blocked
for VLAN RND4094x1. Do not adjust the BID or the value automatically
derived from the port operational bandwidth.
''':
'''
interface EINT1
 spanning-tree cost RND1000x1

interface EINT3
 spanning-tree vlan RND4094x1 port-priority 64
''',
#
'''
Configure VLAN RND4094x1 to send STP Configuration BPDUs every RND10x1
seconds. Configure VLAN RND4094x2 to spend RND10x2 seconds in each of
the listening and learning states. VLAN RND4094x3 should maintain existing
BPDUs for RND100x1 seconds. Finally, disable STP on VLAN RND4094x4.
Do not use BPDU Filter to accomplish this.
''':
'''
spanning-tree vlan RND4094x1 hello-time RND10x1
spanning-tree vlan RND4094x2 forward-time RND10x2
spanning-tree vlan RND4094x3 max-age RND100x1
no spanning-tree vlan RND4094x4
''',
#
'''
Configure sw-NAMEx1 to quickly determine the per-VLAN Spanning-Tree
Protocol topology based on a proposal/agreement process. Interface EINT1
is operating at half-duplex, but is a physical point-to-point connection.
Ensure STP still uses this link for fast convergence. Do not adjust the
duplex setting.
''':
'''
spanning-tree mode rapid-pvst

interface EINT1
 spanning-tree link-type point-to-point
''',
#
'''
Configure sw-NAMEx1 to bundle VLAN RND4094x1 and RND4094x2 into single
Spanning-Tree Protocol instance number RND10x1, with name 'NAMEx2'
and revision number RND10x2.
''':
'''
spanning-tree mst configuration
 instance RND10x1 vlan RND4094x1,RND4094x2
 name NAMEx2
 revision RND10x2
 exit

spanning-tree mode mst
''',
#
'''
VLANs RND4094x1 and RND4094x2 are in MST Instance RND10x1 on
sw-NAMEx1. Use a single command to ensure that sw-NAMEx1
is the STP root for both of these VLANs. Assume default
settings elsewhere in the network.
''':
'''
spanning-tree mst RND10x1 root primary
''',
#
'''
On interface EINT1, adjust the Spanning-Tree Protocol value associated
with operational bandwidth to a value of RND1000x1. This should be applied to
all VLANs in MST Instance RND10x1.

Interfaces EINT2 and EINT3 both connect to interfaces EINT2 and EINT3
of the upstream designated switch. Configure EINT3 so that it has a
better chance of being in the forwarding state rather than being blocked
for VLANs in MST Instance RND10x2. Do not adjust the BID or the value
automatically derived from the port operational bandwidth.
''':
'''
interface EINT1
 spanning-tree mst RND10x1 cost RND1000x1

interface EINT3
 spanning-tree mst RND10x2 port-priority 64
''',
#
'''
Configure MST to send BPDUs every RND10x1 seconds. BPDUs should be valid
for RND100x1 seconds. A BPDU should traverse no more than RND10x2 switches
inside the region before being discarded.
''':
'''
spanning-tree mst hello-time RND10x1
spanning-tree mst max-age RND100x1
spanning-tree mst max-hops RND10x2
''',
#
'''
Use a single command to ensure all non-trunking ports on sw-NAMEx1
bypass the Spanning-Tree Protocol forward delay upon link up.
''':
'''
spanning-tree portfast default
''',
#
'''
Interface EINT1 carries multiple VLANs. Ensure this interface bypasses
the Spanning-Tree Protocol forward delay upon link up.
''':
'''
interface EINT1
 spanning-tree portfast trunk
''',
#
'''
Use a single command to enable BPDU Guard on all interfaces that
are also configured to bypass the Spanning-Tree Protocol
forward delay.
''':
'''
spanning-tree portfast bpduguard default
''',
#
'''
Use a single command to prevent BPDUs from being sent on all
interfaces that are also configured to bypass the Spanning-Tree
Protocol forward delay.
''':
'''
spanning-tree portfast bpdufilter default
''',
#
'''
Configure interface EINT1 to err-disable the port if a BPDU is received.
Configure interface EINT2 to stop sending BPDUs, and to not process any
received BPDUs.
''':
'''
interface EINT1
 spanning-tree bpduguard enable

interface EINT2
 spanning-tree bpdufilter enable
''',
#
'''
Configure interface EINT1 to protect the Spanning-Tree Protocol topology
by preventing it from becoming an STP upstream-facing port.
''':
'''
interface EINT1
 spanning-tree guard root
''',
#
'''
Configure interface EINT1 to protect the Spanning-Tree Protocol topology
by preventing it from becoming an STP downstream-facing port due to
unidirectional link issues.
''':
'''
interface EINT1
 spanning-tree guard loop
''',
#
'''
Use a single command to prevent all interfaces which are considered to be
point-to-point by Spanning-Tree Protocol from transitioning from root or
alternate ports to designated ports as a result of a unidirectional link.
''':
'''
spanning-tree loopguard default
''',
#


}
