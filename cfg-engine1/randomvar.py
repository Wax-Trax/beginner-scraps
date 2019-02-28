import re
from random import *
from netaddr import *

# This file requires the netaddr library  pip3 install netaddr

### This file contains both the real values to place within the variables,
###  as well as the function to actually replace the variables within the
###  tasks that are passed to the function.

'''
netaddr primer:

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
str(choice(list1)) # random IP from range, includes net/bcast

for ip in rndnet1:        # print all IPs in range
    print(ip)

for ip in rndnet1.iter_hosts():  # print all host IPs in range (ex net/bcast)
    print(ip)

range1 = IPRange('start-ip', 'end-ip')  # creates arbitrary range

for ip in range1:   # print all IPs in arbitrary range
    print(ip)

# You can also compare IPAddress and IPNetwork in == < > <= >- != manner

'''

# takes task presented from tasks.py (via start.py) and puts actual values
def random_replace(task,answer):

    # Placing new function calls within this function is how new random
    #  values are selected for each new task, otherwise the same 'random'
    #  variable is selected over and over again. Sadly it took me many
    #  hours to work this out :-)


    # The following lines instantiate new randomized variables from other
    #  functions within this file

    rndser = rand_serial()       # List of 16 random serial interfaces
    rndeth = rand_ethernet()     # List of 16 random ethernet interfaces
    rnduser = rand_user()        # List of 10 random silly usernames from 25
    rndpass = rand_pass()        # List of 10 random silly passwords from 25
    rndname = rand_name()        # List of 10 random silly words from 500

    rnd10x = rand_10()           # List 1 - 10 randomized
    rnd100x = rand_100()         # List 10 of 1 - 100 randomized
    rnd1000x = rand_1000()       # List 10 of 1 - 1000 randomized
    rnd4094x = rand_4094()       # List 10 of 1 - 4094 excluding 1002 - 1005
    rnd24 = rand_2_4()           # 2, 3 or 4
    rndbw = rand_bw()            # List 10 of 1 - 10,000,000 in 100k increments

    # Generate single random unicast IP addresses
    rndip1 = rand_ip()
    rndip2 = rand_ip()
    rndip3 = rand_ip()
    rndip4 = rand_ip()

    # Place the random unicast IP addresses into a random /8 - /30
    rndnet1 = IPNetwork(rndip1 + '/' + str(randint(8,30)))
    rndnet2 = IPNetwork(rndip2 + '/' + str(randint(8,30)))
    rndnet3 = IPNetwork(rndip3 + '/' + str(randint(8,30)))
    rndnet4 = IPNetwork(rndip4 + '/' + str(randint(8,30)))

    # Choose a different random IP address and prefix if = net/bcast address
    while rndnet1.ip is rndnet1.network or rndnet1.ip is rndnet1.broadcast:
        rndip1 = rand_ip()
        rndnet1 = IPNetwork(rndip1 + '/' + str(randint(8,30)))
    while rndnet2.ip is rndnet2.network or rndnet2.ip is rndnet2.broadcast:
        rndip2 = rand_ip()
        rndnet2 = IPNetwork(rndip2 + '/' + str(randint(8,30)))
    while rndnet3.ip is rndnet3.network or rndnet3.ip is rndnet3.broadcast:
        rndip3 = rand_ip()
        rndnet3 = IPNetwork(rndip3 + '/' + str(randint(8,30)))
    while rndnet4.ip is rndnet4.network or rndnet4.ip is rndnet4.broadcast:
        rndip4 = rand_ip()
        rndnet4 = IPNetwork(rndip4 + '/' + str(randint(8,30)))

    # This function's IPs are completely isolated and separate from the above
    rndiprange1 = rand_iprange()  # returns random /24 range, start ip, end ip
    rndiprange2 = rand_iprange()  #  as list elements 0,1,2
    rndiprange3 = rand_iprange()  #  useful for small IP pools
    rndiprange4 = rand_iprange()

    rndmac1 = rand_mac()          # returns random MAC in xxxx.yyyy.zzzz format
    rndmac2 = rand_mac()
    rndmac3 = rand_mac()
    rndmac4 = rand_mac()

    rndstpbid = rand_stpbid()     # random choice from acceptable choices
    rndstppid = rand_stppid()


    # This is where the placeholders from the task/answer are actually replaced
    #  with real values. All verification logic must be worked out above
    #  before reaching this point.

### Task = Question portion

    task = re.sub(r'\bSINT(\d+)\b', lambda m: rndser[int(m.group(1)) - 1], task)
    task = re.sub(r'\bEINT(\d+)\b', lambda m: rndeth[int(m.group(1)) - 1], task)
    task = re.sub(r'\bUSERNAME(\d+)\b', lambda m: rnduser[int(m.group(1)) - 1], task)
    task = re.sub(r'\bPASSWORD(\d+)\b', lambda m: rndpass[int(m.group(1)) - 1], task)
    task = re.sub(r'\bNAMEx(\d+)\b', lambda m: rndname[int(m.group(1)) - 1], task)
    task = re.sub(r'\bRND10x(\d+)\b', lambda m: rnd10x[int(m.group(1)) - 1], task)
    task = re.sub(r'\bRND100x(\d+)\b', lambda m: rnd100x[int(m.group(1)) - 1], task)
    task = re.sub(r'\bREVPCNTx(\d+)\b', lambda m: \
           str(100 - int(rnd100x[int(m.group(1)) - 1])), task) # 100 - rnd100x
    task = re.sub(r'\bRND1000x(\d+)\b', lambda m: rnd1000x[int(m.group(1)) - 1], task)
    task = re.sub(r'\bRND4094x(\d+)\b', lambda m: rnd4094x[int(m.group(1)) - 1], task)
    task = task.replace('RND24', str(rnd24))
    task = re.sub(r'\bRNDBW(\d+)\b', lambda m: \
           str(float(rndbw[int(m.group(1)) - 1]) / 1000000), task)  # As Mbps

    task = task.replace('RNDNET1IP', str(rndnet1.ip))        # IP
    task = task.replace('RNDNET1PFX', str(rndnet1.prefixlen))# the x in /x
    task = task.replace('RNDNET1CIDR', str(rndnet1))         # x.x.x.x/x
    task = task.replace('RNDNET1NET', str(rndnet1.network))  # network address
    task = task.replace('RNDNET1BC', str(rndnet1.broadcast)) # bcast address
    task = task.replace('RNDNET1MSK', str(rndnet1.netmask))  # subnet mask
    task = task.replace('RNDNET1WC', str(rndnet1.hostmask))  # wildcard mask

    task = task.replace('RNDNET2IP', str(rndnet2.ip))        # IP
    task = task.replace('RNDNET2PFX', str(rndnet2.prefixlen))# the x in /x
    task = task.replace('RNDNET2CIDR', str(rndnet2))         # x.x.x.x/x
    task = task.replace('RNDNET2NET', str(rndnet2.network))  # network address
    task = task.replace('RNDNET2BC', str(rndnet2.broadcast)) # bcast address
    task = task.replace('RNDNET2MSK', str(rndnet2.netmask))  # subnet mask
    task = task.replace('RNDNET2WC', str(rndnet2.hostmask))  # wildcard mask

    task = task.replace('RNDNET3IP', str(rndnet3.ip))        # IP
    task = task.replace('RNDNET3PFX', str(rndnet3.prefixlen))# the x in /x
    task = task.replace('RNDNET3CIDR', str(rndnet3))         # x.x.x.x/x
    task = task.replace('RNDNET3NET', str(rndnet3.network))  # network address
    task = task.replace('RNDNET3BC', str(rndnet3.broadcast)) # bcast address
    task = task.replace('RNDNET3MSK', str(rndnet3.netmask))  # subnet mask
    task = task.replace('RNDNET3WC', str(rndnet3.hostmask))  # wildcard mask

    task = task.replace('RNDNET4IP', str(rndnet4.ip))        # IP
    task = task.replace('RNDNET4PFX', str(rndnet4.prefixlen))# the x in /x
    task = task.replace('RNDNET4CIDR', str(rndnet4))         # x.x.x.x/x
    task = task.replace('RNDNET4NET', str(rndnet4.network))  # network address
    task = task.replace('RNDNET4BC', str(rndnet4.broadcast)) # bcast address
    task = task.replace('RNDNET4MSK', str(rndnet4.netmask))  # subnet mask
    task = task.replace('RNDNET4WC', str(rndnet4.hostmask))  # wildcard mask

    task = task.replace('RNDIPRANGE1', rndiprange1[0])   #x.x.x.x - y
    task = task.replace('RNDIPRANGEst1', rndiprange1[1]) #x.x.x.x
    task = task.replace('RNDIPRANGEen1', rndiprange1[2]) #x.x.x.y
    task = task.replace('RNDIPRANGE2', rndiprange2[0])
    task = task.replace('RNDIPRANGEst2', rndiprange2[1])
    task = task.replace('RNDIPRANGEen2', rndiprange2[2])
    task = task.replace('RNDIPRANGE3', rndiprange3[0])
    task = task.replace('RNDIPRANGEst3', rndiprange3[1])
    task = task.replace('RNDIPRANGEen3', rndiprange3[2])
    task = task.replace('RNDIPRANGE4', rndiprange4[0])
    task = task.replace('RNDIPRANGEst4', rndiprange4[1])
    task = task.replace('RNDIPRANGEen4', rndiprange4[2])

    task = task.replace('RNDMAC1', str(rndmac1))
    task = task.replace('RNDMAC2', str(rndmac2))
    task = task.replace('RNDMAC3', str(rndmac3))
    task = task.replace('RNDMAC4', str(rndmac4))

    task = task.replace('RNDSTPBID', str(rndstpbid))
    task = task.replace('RNDSTPPID', str(rndstppid))

### Answer = answer portion

    answer = re.sub(r'\bSINT(\d+)\b', lambda m: rndser[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bEINT(\d+)\b', lambda m: rndeth[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bUSERNAME(\d+)\b', lambda m: rnduser[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bPASSWORD(\d+)\b', lambda m: rndpass[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bNAMEx(\d+)\b', lambda m: rndname[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bRND10x(\d+)\b', lambda m: rnd10x[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bRND100x(\d+)\b', lambda m: rnd100x[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bREVPCNTx(\d+)\b', lambda m: \
             str(100 - int(rnd100x[int(m.group(1)) - 1])), answer) # 100 - rnd100x
    answer = re.sub(r'\bRND1000x(\d+)\b', lambda m: rnd1000x[int(m.group(1)) - 1], answer)
    answer = re.sub(r'\bRND4094x(\d+)\b', lambda m: rnd4094x[int(m.group(1)) - 1], answer)
    answer = answer.replace('RND24', str(rnd24))
    answer = re.sub(r'\bRNDBW(\d+)\b', lambda m: \
             str(int(float(rndbw[int(m.group(1)) - 1]) / 1000)), answer)  # As Kbps

    answer = answer.replace('RNDNET1IP', str(rndnet1.ip))        # IP
    answer = answer.replace('RNDNET1PFX', str(rndnet1.prefixlen))# the x in /x
    answer = answer.replace('RNDNET1CIDR', str(rndnet1))         # x.x.x.x/x
    answer = answer.replace('RNDNET1NET', str(rndnet1.network))  # network address
    answer = answer.replace('RNDNET1BC', str(rndnet1.broadcast)) # bcast address
    answer = answer.replace('RNDNET1MSK', str(rndnet1.netmask))  # subnet mask
    answer = answer.replace('RNDNET1WC', str(rndnet1.hostmask))  # wildcard mask

    answer = answer.replace('RNDNET2IP', str(rndnet2.ip))        # IP
    answer = answer.replace('RNDNET2PFX', str(rndnet2.prefixlen))# the x in /x
    answer = answer.replace('RNDNET2CIDR', str(rndnet2))         # x.x.x.x/x
    answer = answer.replace('RNDNET2NET', str(rndnet2.network))  # network address
    answer = answer.replace('RNDNET2BC', str(rndnet2.broadcast)) # bcast address
    answer = answer.replace('RNDNET2MSK', str(rndnet2.netmask))  # subnet mask
    answer = answer.replace('RNDNET2WC', str(rndnet2.hostmask))  # wildcard mask

    answer = answer.replace('RNDNET3IP', str(rndnet3.ip))        # IP
    answer = answer.replace('RNDNET3PFX', str(rndnet3.prefixlen))# the x in /x
    answer = answer.replace('RNDNET3CIDR', str(rndnet3))         # x.x.x.x/x
    answer = answer.replace('RNDNET3NET', str(rndnet3.network))  # network address
    answer = answer.replace('RNDNET3BC', str(rndnet3.broadcast)) # bcast address
    answer = answer.replace('RNDNET3MSK', str(rndnet3.netmask))  # subnet mask
    answer = answer.replace('RNDNET3WC', str(rndnet3.hostmask))  # wildcard mask

    answer = answer.replace('RNDNET4IP', str(rndnet4.ip))        # IP
    answer = answer.replace('RNDNET4PFX', str(rndnet4.prefixlen))# the x in /x
    answer = answer.replace('RNDNET4CIDR', str(rndnet4))         # x.x.x.x/x
    answer = answer.replace('RNDNET4NET', str(rndnet4.network))  # network address
    answer = answer.replace('RNDNET4BC', str(rndnet4.broadcast)) # bcast address
    answer = answer.replace('RNDNET4MSK', str(rndnet4.netmask))  # subnet mask
    answer = answer.replace('RNDNET4WC', str(rndnet4.hostmask))  # wildcard mask

    answer = answer.replace('RNDIPRANGE1', rndiprange1[0])   #x.x.x.x - y
    answer = answer.replace('RNDIPRANGEst1', rndiprange1[1]) #x.x.x.x
    answer = answer.replace('RNDIPRANGEen1', rndiprange1[2]) #x.x.x.y
    answer = answer.replace('RNDIPRANGE2', rndiprange2[0])
    answer = answer.replace('RNDIPRANGEst2', rndiprange2[1])
    answer = answer.replace('RNDIPRANGEen2', rndiprange2[2])
    answer = answer.replace('RNDIPRANGE3', rndiprange3[0])
    answer = answer.replace('RNDIPRANGEst3', rndiprange3[1])
    answer = answer.replace('RNDIPRANGEen3', rndiprange3[2])
    answer = answer.replace('RNDIPRANGE4', rndiprange4[0])
    answer = answer.replace('RNDIPRANGEst4', rndiprange4[1])
    answer = answer.replace('RNDIPRANGEen4', rndiprange4[2])

    answer = answer.replace('RNDMAC1', str(rndmac1))
    answer = answer.replace('RNDMAC2', str(rndmac2))
    answer = answer.replace('RNDMAC3', str(rndmac3))
    answer = answer.replace('RNDMAC4', str(rndmac4))

    answer = answer.replace('RNDSTPBID', str(rndstpbid))
    answer = answer.replace('RNDSTPPID', str(rndstppid))

    #print(task,answer)  #debug
    return task,answer

### Random Variables

def rand_serial():
    rndser = ['s0/0','s0/1','s0/2','s0/3','s1/0','s1/1','s1/2','s1/3',
              's2/0','s2/1','s2/2','s2/3','s3/0','s3/1','s3/2','s3/3']
    shuffle(rndser)
    return rndser

def rand_ethernet():
    rndeth = ['e0/0','e0/1','e0/2','e0/3','e1/0','e1/1','e1/2','e1/3',
              'e2/0','e2/1','e2/2','e2/3','e3/0','e3/1','e3/2','e3/3']
    shuffle(rndeth)
    return rndeth

def rand_user():
    # from http://jimpix.co.uk/words/random-username-generator.asp
    rnduser = sample(['skedaddleengineer','noddleresearcher','snoutannouncer',
        'bumfmillwright','dutygrammarian','idiopathiconlooker','gubbinsmourner',
        'folliclepodiatrist','doodleplayer','yahoogeologist','ladidaastronomer',
        'ciliadon','blubberbroker','masticatesinger','rigmarolemortician',
        'shenanigansoldier','shrubberytechnician','sassafrastailor','oblongphysicist',
        'poppycockdesigner','cougarshoemaker','turdiformbishop','spatulaminstrel',
        'gauzetherapist','doozypilot'], k=10)
    return rnduser

def rand_pass():
    # from http://www.dinopass.com/
    rndpass = sample(['@ngryRule41','hotS@lmon50','niceox99','wi$eLiquid28',
        '$caryParrot61','brownTh!ng51','lou)Ray12','uglyEn)15','fl@tJaguar57',
        'whi+eButton12','t!nyMoon99','f!rstGorilla15','sweetRa(coon89','longWorm97',
        '@ngryWave48','j@deMask42','oldL!quid19','heavyS!lk98','blac<Iron98',
        '<eenLead58','brownW!sh20','3mptyHelp19','!voryRing65',']adeLlama64',
        'm!styBrain92'], k=10)
    return rndpass

def rand_name():
    # from http://soybomb.com/tricks/words/
    rndname = sample(['surecred','coatemently','cognetism','patrud',
        'agonalted','tormating','comicker','shuttels','sasking','posible',
        'scophiteness','ferring','harisket','comilled','flocry','linetiones',
        'gaunlity','oducianis','broirs','antensollsy','thologicant','marred',
        'queath','aborging','capturonicale','rulexityrator','faities','condrively',
        'presseol','posignet','paraturnelasy','carillion','daligel','supertuggly',
        'bloclanch','sudatinization','boroseld','gustator','viatiosyned','coffix',
        'aferiums','cauthetinel','disgrudiscayer','sicompost','etuadom',
        'hellindistaths','cannibed','baggedoming','carrition','glintending',
        'examized','adjunce','claspeeleck','vaudity',
        'curvise','oduchibeers','adructions','leraterly','wassempods','truidled',
        'ganson','rollaheitele','saffers','turist','linoducted','barnstanizined',
        'navilizes','egarita','niannuish','forcomasizater','trings','sailostricath',
        'illsard','sclarlor','chnized','wettreving','bumpute','stinflaud',
        'saneliattently','catary','chainvey','petenny','baselled','jametaills',
        'acheal','wrappot','oligide','embefinaviner','beance','synouste',
        'bedrophitling','ementinger','heaviallism','pioneight','prever','hibility',
        'tracquises','couriner','reconven','eldevoy',
        'instiviting','kimoundiciphys','chaminglauther',
        'mounct','cornial','consing','adversers','partak','phying','dernated',
        'pliotably','footintrutes','standma','orthress','gramploy','rersessieg',
        'cheouser','chutole','saulattating','wirepers','lighwarding','fraurayized',
        'gartain','latick','scapter','shindonmenrink','parashant','expervoutwar',
        'luftovisp','wingalnes','bisquesqueged','mannerlopmenes','unimman','laxiel',
        'mastickens','gramals','hangerlance','oblity','granal','worksh',
        'nessnesshazes','delity','cought','procump','posupping','burgents',
        'bowmentionized','chewerated','chartiess','descess',
        'potefunna','medimisecrify','gradjan','catadeleves',
        'protocation','sculay','obeling','ficilliaseces','parcuring','ausconly',
        'libelarphipse','imanges','rategroide','bonderewithen','reples','diaggion',
        'eathms','bleare','streguidah','loweretersiffs','surestandes',
        'arpnesslewive','cauces','mcfaretramp','glopled','excepty','palinked',
        'jeantify','arizers','gaspiry','spirremnly','oblinatoing','fectedics',
        'coltical','stuyers','latickle','fausly','possemptorned','aggled',
        'payalivergive','mcconctuarne','supears','blenly','atioleved','disgrawbers',
        'adounctic','standyliverted','cutles','scafforthrons','acedgaternad',
        'defere','sweavelly','impromated','enturbely',
        'anations','haillicaly','misundided','forman','devors','extrous',
        'clochumousiver','mentics','stationsion','conjark','faularmobsum','allogy',
        'spanguiden','dowarex','overeliating','rouggling','stincoweasons','thertin',
        'moized','amplies','bation','acocry','gablan','soremyrocker','derson',
        'kingess','pacious','ilosely','visablons','foranow','worminvoyant',
        'perplawn','ingened','gelaring','barthweights','patherians',
        'refurrecterict','oveneshobbles','dantairs','lograms','endireburge',
        'mortighted','aphirobeds','abjuric','fudging','mounde',
        'tutitution','sembertaving','ferequainsole',
        'charremeg','throuts','oichee','contraze','confrong','rasorgeoscres',
        'livasquishoes','nosting','uratemenes','poledge','assignal','inating',
        'paripped','matects','subrington','prepar','venumbusnetrue','bossors',
        'agmatelockers','pinessur','exquennu','tahoolation','bastlessed','morammed',
        'regaton','proption','hiridises','rogenefable','crypor','safection',
        'mediff','shesseculp','reproffs','anbetraphy','dianizess','monshize',
        'unitiquit','modeouble','shdome','fleerinstria','tabovising','polina',
        'shoptorroric','gripulosive','primagic','overragger','lusible',
        'examinequetion','glitized','brassigned','tradams',
        'midley','desmalbayder','paused','somenesed','thinteril','brevitewayingf',
        'piterague','dogened','synctudete','mcbruity','tholiatorited','recognes',
        'stresomergan','garding','scendize','tionsketer','repric','prosoproquate',
        'radicaughts','chatioms','inklestal','hymelighte','rimery','mensegypt',
        'paremong','sionium','officksting','bastrily','primperper','hereve',
        'arctart','reorie','dancting','buchirrection','adraiming','caucate',
        'inizes','innond','disticithfuli','swantlinteness','sebaked','ostella',
        'porticanstine','affred','patrysics','formuteser',
        'trayantem','scotypes','fluenterrooted','unfirmico',
        'keneuted','amouncturbon','snuffsholer','sturriflece','famelowers',
        'leecterepuble','irresele','dreabound','boarcharitory','safeation','valrus',
        'maninged','compreled','shakowls','gurkinventing','exight','forchapplents',
        'honersalcoate','resencor','compet','regratomp','ronessagmens','belizes',
        'reintece','asturk','wickencevisift','notachned','bowsonal','planne',
        'drumbite','litiverns','flowinst','nicistic','thinintersest','fadiging',
        'descuffighly','redewdle','oveggs','arraten','flairingly','catter',
        'bellboottess','cogrances','derling','addeted','aldrod',
        'bowlets','fridgelizer','fewenholdson','grapprostly',
        'arescal','aboloutbition','holistraphot','triestion','trations','shadowled',
        'befruseharth','downstic','queeps','obseler','piecht','parationized',
        'autors','buttlen','sulton','scotisoffres','cushanize','pipereses',
        'focunds','gioverts','ficiese','havisignated','compeiscover','maninogard',
        'moduplifix','wagoured','shocers','putachape','shessimilly','catutall',
        'corrands','sociprehis','horric','sillanimagons','remoducer','surged',
        'dolphized','procle','dilounting','unctly','unemen','odiatio','humbrant',
        'clintrudes','lestoclar','comped',
        'nefigyroadest','irbalder','savoten','eudows',
        'apparang','baskethaverty','torious','formuting','rebourizes','calatte',
        'manuism','bottiersions','maciner','stulting','prottion','faunush',
        'discletend','cabiddy','presquility','webbon','berrots','bechindisams',
        'beessighted','anintruts','gartairding','pervists','micribily','orphilite',
        'furrecies','robuddentran','rantuingly','rooments','voyalikers','lousher',
        'bulbring','ionsibusly','reston','mither','diddadors','exconninat',
        'immelly','libeltimpectan','detructon','cheolong','darnity','mikong',
        'libesee','crypser','macheded','aimediscard'], k=10)
    return rndname

def rand_10():          #returns randomized list 1 - 10 as str
    rnd10 = list(map(str,sample(list(range(1,11)), k=10)))
    return rnd10

def rand_100():         #returns 10 of randomized list 1 - 100 as str
    rnd100 = list(map(str,sample(list(range(1,101)), k=10)))
    return rnd100

def rand_1000():        #returns 10 of randomized list 1 - 1000 as str
    rnd1000 = list(map(str,sample(list(range(1,1001)), k=10)))
    return rnd1000

def rand_4094():        # intended for random VLAN selection
    rnd4094 = list(map(str,sample(list(range(1,4095)), k=10)))

    while '1002' in rnd4094 or '1003' in rnd4094 or\
          '1004' in rnd4094 or '1005' in rnd4094:    # exclude disallowed VLANs
        rnd4094 = list(map(str,sample(list(range(1,4095)), k=10)))
    return rnd4094

def rand_2_4():
    rnd24 = choice([2,3,4])
    return rnd24

def rand_bw():         #returns 10 of randomized list 1 - 10,000,000 as str
    rndbw = list(map(str,sample(list(range(100000,10000001,100000)), k=10)))
                       # starting at 100,000 in increments of 100,000
    return rndbw

def rand_ip():   # single random unicast IP address
    oct1 = randint(1,223)    # unicast range
    oct2 = randint(1,254)
    oct3 = randint(1,254)
    oct4 = randint(1,254)

    while oct1 == 127:   # choose a different value if 127
        oct1 = randint(1,223)
    rndip = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.' + str(oct4)
    return rndip

def rand_iprange():   # single unicast IP range within /24
    oct1 = randint(1,223)
    oct2 = randint(1,254)
    oct3 = randint(1,254)
    oct4 = randint(1,253)     #one less than max since it's a range
    endrange = randint(1,254)

    while oct1 == 127:   # choose a different value if 127
        oct1 = randint(1,223)
    while endrange < oct4:  # make sure the end is greater than the beginning
        endrange = randint(1,254)
    rndiprange = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.'\
                  + str(oct4) + " - " + str(endrange)
    rangestart = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.'\
                  + str(oct4)
    rangeend = str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.'\
                  + str(endrange)
    return rndiprange,rangestart,rangeend

def rand_mac():
    rndmac = format(randint(0,65535), 'x') + '.'\
           + format(randint(0,65535), 'x') + '.'\
           + format(randint(0,65535), 'x')
    # This function does not take into account MAC rules like U/L bit, etc.
    # That functionality seemed to be overkill for what I'm trying to do here.
    return rndmac

def rand_stpbid():
    rndstpbid = choice(['0','4096','8192','12288','16384','20480','24576',
        '28672','32768','36864','40960','45056','49152','53248','57344','61440'])
    return rndstpbid

def rand_stppid():
    rndstppid = choice(['0','64','128','192'])
    return rndstppid
