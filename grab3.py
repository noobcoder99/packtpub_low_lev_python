import socket
s = socket.socket()
# sets socket objecct timout at two seconds
s.settimeout(2)
# choose what port
port = raw_input("Port Number:  ")
try:                                      # port number
    s.connect(("packtpub.samsclass.info", int(port)))
    print s.recv(1024)
    s.close()
# error statement is printed if connection not made or refused
except socket.error as err:
    print err
#
