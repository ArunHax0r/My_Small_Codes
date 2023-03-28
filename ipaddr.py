#!/usr/bin/python3

import socket

# Gets the IP of the site and saves it in a txt file
def getip():
    host = input('Enter the site: ')
    ip = socket.gethostbyname(host)
    print('The ip is:', ip)
    with open("ip.txt", "a") as f:
        f.write(f'\n{ip}')


getip()


# Gets the IP address and Returns the Host
def gethost():
    ip = input("Enter the ip: ")
    host = socket.gethostbyaddr(ip)
    print("The Host is:", host)
    with open('host.txt', 'a') as f:
        f.write(f"\n{host}")


gethost()







