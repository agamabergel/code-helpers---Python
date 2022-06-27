############### Code helpers in python ###############

# function 1: recvall implementation
# This function receive all data sent back decoded
import socket
def recvall(sock: socket.socket) -> str:

    BUFFER = 4096
    data = ""

    while True:
        block = sock.recv(BUFFER)
        data += block
        if len(block) < BUFFER:
            break
    
    return data


