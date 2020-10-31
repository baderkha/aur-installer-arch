#!/usr/bin/env python3.8
import subprocess
import sys
import os

## puls an aur git dir
def pull_git(gitRepo):
    tmp_file_cloned_to = "/tmp/aur-installer/"+gitRepo
    try :
        process = subprocess.run(["git","clone",gitRepo,tmp_file_cloned_to])
        code = process.returncode
    except: 
        print('here')
        code = 1
    return (tmp_file_cloned_to,code)

## builds the packages
def build(git_location):
    process=subprocess.Popen(["makepkg","-sri"],cwd=git_location)
    process.wait()

## orchestrates the 2 commands
def main ():
    argsLen = len(sys.argv)

    if argsLen == 1 :
        gitRepo = input ("Enter the Aur Git Repository : ")
    else :    
        gitRepo = sys.argv[1]

    location,status_code = pull_git(gitRepo)
    if status_code  != 0 :
        print("\nFailed To pull repo , make sure you're using a valid repo")
        return

    build(location)
    

if __name__ == "__main__" : 
    main()
