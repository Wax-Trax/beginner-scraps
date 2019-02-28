#!/usr/bin/env python3

'''
This file contains the main logic of the script. I decided to break out the
tasks/solutions into another file because it is going to be very large when
it is more complete. Likewise, the list of variables is going to be somewhat
large as well, so I thought it would be best to put it into a separate file
for clarity.
'''

from random import *
from tasks import *      # tasks file where the tasks & solutions live
from randomvar import *  # randomvar file where the task variables live
from datetime import datetime

# I created the filename variable in case I want to change the filename later
tfilevar = 'tasks.txt'
afilevar = 'answers.txt'
tfile = open(tfilevar, 'w')
afile = open(afilevar, 'w')

# convert dictionary in tasks.py to list with each task/answer as an element
tlist = list(tasks.items())

# number of total tasks available in the tasks.py file
total_tasks = len(tasks)

# Should probably make an exception handler here
tnum = int(input(f'How many tasks (up to {total_tasks}) would you '\
                      'like generated?: '))

# generate list of tnum tasks in random order from total number of tasks in pool
tasklist = sample(range(1, total_tasks+1), tnum)

# set counter for numerical task order used in upcoming for loop
task = 1

# Writes the time of generation at the top of the files
gentime = 'Generated: ' + str(datetime.now())
tfile.write(gentime)
afile.write(gentime)

for task_number in tasklist:
#    print(f' -task_number: {task_number}')  # debug, e.g. 3,4,2,7,1
#    print(f' -task: {task}')                # debug, e.g. 1,2,3,4,5

    # Create a new temp list out of the specific list element passed in
    t1 = tlist[task_number - 1]

    temp_task = str(t1[0])    # task element from temp list
    temp_answer = str(t1[1])  # answer element from temp list

    # pass string element to function in randomvar.py
    #  to replace variables with actual values
    results = random_replace(temp_task,temp_answer)
    temp_task = results[0]    # task element with variables inserted
    temp_answer = results[1]  # answer element with variables inserted

    #Tasks file
    tfile.write('\n' + '-' * 20 + '\n')  # dashes for visual clarity
    tfile.write(f'\nTask {task}: \n\n')  # numerical order
    tfile.write(temp_task)               # current task with variables

    #Answers file
    afile.write('\n' + '-' * 20 + '\n')  # dashes for visual clarity
    afile.write(f'\nTask {task}: \n\n')  # numerical order
    afile.write(temp_task)               # current task with variables
    afile.write('\n\nAnswer:\n\n')
    afile.write(temp_answer)             # current task solution with variables
    afile.write('\n\n')

    task += 1   # for display/file purposes

# final dashed lines at bottom of file
tfile.write('\n\n' + '-' * 20 + '\n')
afile.write('-' * 20 + '\n')

# Every Good Boy Discontinues Files
tfile.close()
afile.close()

print(f'\n{tnum} tasks have been written to {tfilevar} and {afilevar}.\n')
