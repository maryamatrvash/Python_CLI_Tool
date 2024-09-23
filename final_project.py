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
 
def ls(): 
    if arguments.ls != "":
        path = arguments.ls
        path = path.replace(" ", "")
        for p, dir, file in os.walk(path):
            for d in dir:
                print(str(d))
            for f in file:
                print(str(f)) 

def cd():
    cwd = os.getcwd() 
    print("current working directory: {0}".format(cwd))
    os.chdir('/tmp')
    print("current working directory: {0}".format(os.getcwd()))
    handeling_cd() 

def handeling_cd():

    path = '/var/www'

    try :  
        os.chdir(path)
        print("current working directory: {0}".format(path)) 
    except FileNotFoundError:
        print("directory: {0} dose not exist".format(path))
    except NotADirectoryError :
        print("{0} is not a directory".format(path))
    except PermissionError :
        print("you do not have permissions to change to {0}".format(path))

def mkdir():
    path = arguments.mkdir 
    try : 
        os.makedirs(path)
    except OSError :
        print("creation of the directory %s failed" % path)
    else :
        print("Successfully created the directory %s" % path)

def rmdir():
    path = arguments.rmdir 
    try : 
        os.rmdir(path)
    except OSError :
        print("Deletion of the directory %s failed" % path) 
    else :
        print("Successfullyy deleted the directory %s" % path)

def rm():
    path = arguments.rm
    try:
        os.remove(path)
    except OSError:
        print("Deletion of the file %s failed" % path) 
    else:
        print("Successfullyy deleted the file %s" % path) 

def rm_r():
    ...

def cp():
    ...

def mv():
    ...

def find():
    ...

def cat():
    ...           

parser = setup() 
arguments = parser.parse_args() 
cmd = " ".join(sys.argv) 
log_command(cmd)
if arguments.ls:
    ls()
elif arguments.cd:
    cd() 
elif arguments.mkdir:
    mkdir()
elif arguments.rmdir:
    rmdir()  
elif arguments.rm:
    rm()
elif arguments.rm_r:
    ...
elif arguments.cp:
    ...
elif arguments.mv:
    ...
elif arguments.find:
    ...
elif arguments.cat:
    ...