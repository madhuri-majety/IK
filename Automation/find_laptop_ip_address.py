"""
Python program to find hostname and ip address
"""
import socket

hostname = socket.gethostname()
#ipaddr = socket.gethostbyname(hostname)

print("Your Computer name is {}".format(hostname))
#print("Your IP address is {}".format(ipaddr))
