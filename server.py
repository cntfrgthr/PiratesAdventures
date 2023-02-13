import socket
import time
  
                                                                        # { 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #      
server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)     # ->Creating new socket with 2 
server_socket.bind(('localhost', 9090))                                 #   parameters
server_socket.setblocking(0)                                            # ->Set socket unblocking for working 
server_socket.listen(5)                                                 #   everytime without pause on this func()
print('Server is running...')                                           # }



#Mainloop#Mainloop#Mainloop
#Mainloop#Mainloop#Mainloop
#Mainloop#Mainloop#Mainloop
player_sockets = []
while True:
    
    #Join request checking
    try:
        player_socket, addr = server_socket.accept()   #Creating player socket for subsequent entering 
        print(f'Player: {addr} was joined')            #commands.
        player_socket.setblocking(0)                   #Set unblocking mode for socket for server don't 
        player_sockets.append(player_socket)           #checking only accept() func.
    except:
        print('Currently not connected')
    
    #Get players commands
    for sock in player_sockets:
        try:
            date = sock.recv(1024)  #Enter user data for handling
            date = date.decode()
        except:
            pass

    #Handling commands


    #Send new game statement
    for sock in player_sockets:         
        try:
            sock.send(''.encode())                  
        except:
            player_sockets.remove(sock)
            sock.close()         
            print('Player disconnect')           

    time.sleep(1500 * 10 ** -3)        
