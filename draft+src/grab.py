import socket
s = socket.socket()

try:
    s.connect(("packtpub.samsclass.info", 22))
    print s.recv(1024)
    s.close()
# error statement is printed if connection not made or refused
except socket.error as err:
    print err
#
