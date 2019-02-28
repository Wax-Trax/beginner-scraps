#!/usr/bin/env python3
import yaml
import jinja2
import time
from netmiko import Netmiko
import threading

yaml_file = 'vpls1.yml'
jinja_template = 'vpls1.j2'
hostip = '255.255.255.255'  # EVE-NG host

# Generate the configurations and send it to the devices
def confgen(vars):
    # Generate configuration lines with Jinja2
    with open(jinja_template) as f:
        tfile = f.read()
    template = jinja2.Template(tfile)
    cfg_list = template.render(vars)

    print('-' * 80)
    print(cfg_list)
    print('-' * 80)

    # Connect directly to host via telnet on the specified port
    conn = Netmiko(host=hostip, device_type='cisco_ios_telnet', port=vars['port'])

    # Check if host is in initial config state
    conn.write_channel("\n")
    time.sleep(1)
    output = conn.read_channel()
    if 'initial configuration dialog' in output:
        conn.write_channel('no\n')
        time.sleep(1)

    # Send generated commands to host
    output = conn.enable()
    output = conn.send_config_set(cfg_list)

    # Display results
    print('-' * 80)
    print('\nConfiguration applied on ' + vars['host'] + ': \n\n' + output)
    print('-' * 80)

    # Probably a good idea
    conn.disconnect()


# Parse the YAML file
with open(yaml_file) as f:
    read_yaml = yaml.load(f)  # Converts YAML file to dictionary

# Take imported YAML dictionary and start multi-threaded configuration generation
for hosts, vars in read_yaml.items():
    # Add host to vars dictionary
    host = {'host': hosts}
    vars.update(host)

    # Send vars dictionary to confgen function using multi-threading, one thread per-host
    threads = threading.Thread(target=confgen, args=(vars,))
    threads.start()
