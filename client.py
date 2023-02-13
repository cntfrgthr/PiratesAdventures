import socket



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #Creating client socket
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)   #Set socket options
sock.connect(('localhost', 9090))                            #Conneting to the server


while True:
    
    #Reading server commands


    #Send command to the server
    sock.send(''.encode())

    #Get a new game statement from the server
    data = sock.recv(1024)
    data = data.decode()

    #Draw a new game statement
    # Any methods for draw(update) 