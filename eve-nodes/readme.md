I wrote this simple script to solve a little problem I have with EVE-NG Pro
(as of v3.0.1). When I am working with large labs, I prefer to use my own
telnet client (iTerm2 on macOS) to access each device console instead of
working within the web interface. This is particularly important when you
want to send the same command to many devices simultaneously.

Part of the issue with using an external telnet client with EVE-NG Pro is
that the telnet console ports change randomly every time you power up a
device. The author says this is due to a combination of node, lab, and user
limits, though I think the issue of port persistance could probably be solved
easily with a small SQLite database on the EVE-NG VM to keep track of used ports.

This Python3 script (and associated Jinja2 template) logs into your EVE-NG Pro
VM via API, loads the running lab that you specify, and grabs the details of
all the running nodes. A list is generated containing each node name,
the node type (based on EVE-NG template name), the dynamically-assigned telnet
port, and the node's UUID.

This information is then fed to the Jinja2 template to create a JSON file
to be used with iTerm2's Dynamic Profiles feature. iTerm2 monitors the
`~/Library/Application Support/iTerm2/DynamicProfiles` folder for new XML or
JSON files. If it detects any changes to the folder, it automatically loads
the contained profiles. 

This script automatically generates this JSON file and places it in your
user's iTerm2 dynamic profiles folder. Within a few seconds, you can then
right-click on the iTerm2 icon in the Dock, and you'll have the option to
telnet to any of the running nodes in your lab. This script as written
creates a tag based on the lab name and node type so that you can telnet
to all nodes of the same type simultaneously. You could easily modify this
to create tags based on other values, such as prefixes or suffixes in the
node name.

This script is written using the default EVE-NG Pro username and password.
Modify all values as necessary for your environment. This script could be
a good starting point for you to dig deeper into automating things with
EVE-NG. The API has some [limited documentation]
[https://www.eve-ng.net/index.php/documentation/howtos/how-to-eve-ng-api/]
available, but you may need to reverse-engineer a couple things yourself
using the web browser developer tools.
