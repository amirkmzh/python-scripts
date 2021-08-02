#! /usr/bin/python3

from os import system, environ
import subprocess
from time import sleep
from sys import stderr, stdout

# environment variables will set with 'export' command
# export DWS_TESTER_COMMNAD=ls 
# export DWS_TESTER_INTERVAL=5
# export DWS_TESTER_THRESHOLD=3

def run_command():
    command = environ.get('DWS_TESTER_COMMNAD')
    threshold = environ.get('DWS_TESTER_THRESHOLD')
    interval = environ.get('DWS_TESTER_INTERVAL')

    try: 
        # run command in loop
        for _ in range(int(threshold)): 
            command_exec_result = system(command)
            if( command_exec_result == 0):
                print('result is 0')
                return command_exec_result
            else: 
                print('result is not 0')
                if _ != int(threshold) -1 :
                    sleep(int(interval))
                continue
        return 1;

    except Exception as e:
        stderr.write(e)
        return 1; 


if __name__ == '__main__' : 
    command_result = run_command()

    if(command_result == 0 ):
        stdout.write(f'command exceuted successfully')
    else: 
        stderr.write('command excution failed!')

