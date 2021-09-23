import getpass
import json
import requests
import shutil
import subprocess
import sys

from find import find_file
# From list of projects, filter for ones that use Thread
def filter_for_thread_projects(projects):
    thread_projects = []
    flag=0
    for project_url in projects:
        project=project_url.split('/')[-1] 
       # print(project)
        command = 'git clone ' + project_url + project + ' --depth=1'
        subprocess.call(command.split())
        project = project.rstrip()
        grep_command = ['grep',  '-r' 'new Thread(', project]
        try:
             output = subprocess.check_output(grep_command)
             print("GOT MATCH")
             flag+=1
             print(flag) 
             thread_projects.append(project)
             thread_projects.append("\n")
        except subprocess.CalledProcessError as grepexc: 
             print( "NO MATCH error code", grepexc.returncode, grepexc.output) 
             shutil.rmtree(project)
#       if not output == '':
           #print("GOT MATCH")  
           #thread_projects.append(project)
        #shutil.rmtree('tmp')
    return thread_projects

def main(args):
   # projects = ['']
    file_list =open('/media/shanto/Education/Research/idoft/project-list','r')# grep ,NOD, pr-data.csv | cut -d , -f1 | sort -u
   # print(file_list)
    output = filter_for_thread_projects(file_list)
    file1 = open("output_file.txt","w")
    file1.writelines(output)
    file1.close()
    print(output)

if __name__ == '__main__':
    main(sys.argv)

