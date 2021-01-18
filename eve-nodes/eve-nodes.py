#!/usr/bin/env python
import requests
import json
from os import path
from jinja2 import Environment, FileSystemLoader

EVE_SERVER = 'dns name or ip'
LAB = 'lab name without .unl extension'
ITERM2 = 'Library/Application Support/iTerm2/DynamicProfiles'

login = '{"username": "admin", "password": "eve", "html5": "-1"}'
authurl = f'https://{EVE_SERVER}/api/auth/login'
nodesurl = f'https://{EVE_SERVER}/api/labs/{LAB}.unl/nodes'

j2_env = Environment(loader=FileSystemLoader('.'))
requests.packages.urllib3.disable_warnings()
session = requests.Session()
session.post(authurl, data=login, verify=False)

nodes = json.loads(session.get(nodesurl, verify=False).content)

nodelist = []
for node in nodes['data'].keys():
    name = nodes['data'][node]['name']               # node name
    type = nodes['data'][node]['template']           # template: xrv, vios, etc
    tport = nodes['data'][node]['url'].split(':')[2] # dynamic telnet port
    uuid = nodes['data'][node]['uuid']               # node uuid
    nodelist.append((name, type, tport, uuid))

template = j2_env.get_template('iterm2.j2')
render = template.render(nodes=sorted(nodelist), lab=LAB, eve=EVE_SERVER)
rfile = f'{path.expanduser("~")}/{ITERM2}/{LAB}.json'
with open(rfile, 'w') as f:
    f.write(render)
