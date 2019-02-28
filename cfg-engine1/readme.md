This is the framework for a study tool I am creating written in Python3. 
The premise is similar to how flash cards work, except monotony is reduced 
by way of random variable replacement within the tasks. The Q&A format 
is generic enough that this script can be used for a wide range of 
quiz-type applications.

I created this script as a method to drill Cisco IOS configurations into
my head in a way that attempts to keep things interesting by inserting
randomness into the tasks (such as different interfaces, usernames and
passwords) with each generation.

Currently, the script is assembled in three parts:

-start.py holds the main logic

-randomvar.py holds the random variables and the logic to replace the 
  placeholders in tasks.py

-tasks.py holds the tasks and solutions in dictionary format

The tasks.py file is one large dictionary that contains tasks and solutions 
as key/value pairs. Within each task are variables that are replaced with
random actual values held within the randomvar.py file.

When you run start.py, it determines how many total tasks are available in
the pool, and asks you how many tasks you would like to generate, up to the
total amount of tasks available. If there are 10 tasks available, and you
choose any number between 1 and 10, the number of tasks you chose are selected
from the pool at random, their variables are replaced with actual values,
and the results are written to two files: tasks.txt and answers.txt.

You then open the tasks.txt file and attempt to solve all of the presented
tasks. When finished, open the answers.txt file and compare your results.

What I have presented here is meant to be a starting point. There are certainly
better ways to code what I have done (I'm just not that experienced with it
as of yet), and I know there are various optimizations and expansions that could
be done was well (like input validation, and providing the solutions while
the script is still running -- this is something I may try to work on in a
future version).

Additionally, I have provided a few of my own variables and tasks/solutions
for example purposes. I may include more later, I'm not sure yet. However, 
this can be used as a framework to add/create your own.

==============================
Updates
==============================

-12/13/2017: I changed some of the matching/replacing logic in randomvar.py to make things more efficient and reduce the number of lines of code. Additionally, I have included in the tasks.py file 79 example questions that utilize all of the defined variable replacements. All of the questions involve "link layer" Cisco IOS configurations (interfaces, STP, etc).

-11/15/2017: I refactored the code removing a couple of my own functions to work with IP addresses and replaced them with the 'netaddr' library. It's a much cleaner and easier way of working with IP addresses than my little hack :-)
