import getpass
import json
import requests
import shutil
import subprocess
import sys

from find import find_file
COUNT = 0
# From list of projects, filter for ones that use Thread
def filter_for_thread_projects(project_url):
    thread_projects = []
    project_url=project_url.split('\n')[0]
    project=project_url.split('/')[-1] 
    command = 'git clone ' + project_url + ' '+ project + ' --depth=1'
    subprocess.call(command.split())
    project = project.rstrip()
    grep_command = ['grep',  '-r' 'new Thread(', project]
    try:
        output = subprocess.check_output(grep_command)
        print("GOT MATCH")
        global COUNT
        COUNT += 1
        print(COUNT) 
        thread_projects.append(project)
    except subprocess.CalledProcessError as grepexc: 
        print( "NO MATCH error code", grepexc.returncode, grepexc.output) 
        shutil.rmtree(project)
    return thread_projects

def main(args):
    thread_project_list = []
    with open(args) as f1: 
        for line in f1:       
            url =line.strip()
            output = filter_for_thread_projects(url)
            thread_project_list.append(output)
        with open('output.txt','w') as f2:
            f2.write(str(thread_project_list)) 
        print("Total Number of Thread Projects = ", COUNT) 

# grep ,NOD, pr-data.csv | cut -d , -f1 | sort -u
if __name__ == '__main__':
    main(sys.argv[1])

