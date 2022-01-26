import subprocess
import sys
if __name__ == '__main__':
    argvs =(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    subprocess.call(["python", "../logic/classes.py",*argvs])
    