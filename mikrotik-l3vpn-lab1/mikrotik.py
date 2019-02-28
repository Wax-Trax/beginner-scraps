#!/usr/bin/env python3
import yaml
import jinja2
import threading
import telnetlib
import time

yaml_file = 'mikrotik.yml'
jinja_template = 'mikrotik.j2'
eve_ng = '1.2.3.4' # Hostname or IP address of EVE-NG host

# Generate the configurations and send it to the devices
def confgen(vars):
    # Generate configuration lines with Jinja2
    with open(jinja_template) as f:
        tfile = f.read()
    template = jinja2.Template(tfile)
    cfg = template.render(vars)
    cfg_list = cfg.split('\n') # This is here so the lines are sent individually with a pause between each

    print(cfg_list) # So you can see what is generated

    # Use Python3's built-in telnet library to connect to your EVE-NG host.
    conn = telnetlib.Telnet() # Establish conn variable for Telnet access
    conn.open(host=eve_ng, port=vars['port']) # Connect to specified EVE-NG host using port from YAML file

    # We are expecting to boot from a completely clean image that has never been logged
    # into before, with the default login of admin and a blank password. If the router
    # is already logged into, these commands should be harmless if run again.
    conn.write(b'admin\r') # login
    time.sleep(1)
    conn.write(b'\r') # blank password
    time.sleep(1)
    conn.write(b'n\r') # do not display license
    time.sleep(1)

    for line in cfg_list:  # Send the configs one line at a time with a pause in between each
        conn.write(line.encode('ascii'))  # Send output of cfg_list to device in raw ASCII mode
        conn.write(b'\r')  # MikroTik doesn't seem to like \n
        time.sleep(1)  # Wait 1 second in between configuration lines, cfg doesn't work reliably without the pause

    # Display results
    print('\nConfiguration applied to ' + vars['host'])

    # Probably a good idea
    conn.close()


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
