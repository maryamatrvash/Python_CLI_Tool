import argparse
import sys 
import datetime 
import os 

def setup():
    parser = argparse.ArgumentParser(description="Python CLI Tool for File Manipulation")
    parser.add_argument("--ls", type=str, help="List directory contents at path or the current directory if no path is given")
    parser.add_argument("--cd", type=str, help="Change the working directory to path")
    parser.add_argument("--mkdir",type=str, help="Create a new directory at path")
    parser.add_argument("--rmdir", type=str, help="Remove the directory at path if it is empty") 
    parser.add_argument("--rm", type=str, help="Remove the file specified by file")  
    parser.add_argument("--rm-r", type=str, help="Remove the directory at directory and its contents recursively")
    parser.add_argument("--cp", type=str, help="Copy a file or directory from source to destination")
    parser.add_argument("--mv", type=str, help="Move a file or directory from sourse to destination")
    parser.add_argument("--find", type=str, help="Search for files or directories matching pattern starting from path")
    parser.add_argument("--cat", type=str, help="Output the contents of the file") 
    return parser 

def log_command(cmd):
    with open("commands.log", "a") as file:
        time = datetime.datetime.now()
        time = time.strftime("%Y-%b-%d %H:%M:%S")
        text = f"{cmd} : {time}\n" 
        file.write(text)  

def calculate_space(path):
    path = path.replace(" ", "")

def ls_():
    if arguments.ls != "":
        path = arguments.ls
        calculate_space(path)
        for p, dir, file in os.walk(path):
            for d in dir:
                print(str(d))
            for f in file:
                print(str(f)) 

parser = setup() 
arguments = parser.parse_args() 
cmd = " ".join(sys.argv) 
log_command(cmd)
if arguments.ls:
    ls_()
elif arguments.cd:
    ...