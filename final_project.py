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

def cd(path):
    if arguments.cd:
        cwd = os.getcwd(path)
        print("current working directory: {0}".format(cwd))
        os.chdir('/tmp')
        print("current working directory: {0}".format(os.getcwd()))
    else :
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
    
    if arguments.mkdir :

        path = "/tmp/year/month/week/day"

        try : 
            os.makedirs(path)
        except OSError :
            print("creation of the directory %s failed" % path)
        else :
            print("Successfully created the directory %s" % path)

def rmdir():

    if arguments.rmdir :

        path = "/tmp/year"

        try :
            os.rmdir(path)
        except OSError :
            print("Deletion of the directory %s filed" % path)
        else :
            print("Successfullyy deleted the directory %s" % path)

def rm():
    ...

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