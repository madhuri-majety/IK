"""
Python script to ping all ipaddress in a network
"""

import pexpect
import ipaddress

def ping_addresses_in_network(ipnet_str):
    ipnet = ipaddress.ip_network(ipnet_str)

    all_hosts = list(ipnet.hosts())
    print("Hosts in network is : {}".format(all_hosts))

    for i in range(len(all_hosts)):
        output = pexpect.run('ping -t 1 '+str(all_hosts[i]))
        if "100.0% packet loss" in str(output):
            print("Destination {} is Offline".format(all_hosts[i]))
        else:
            print("Destination {} is Online".format(all_hosts[i]))

def main():
    ip_net = '192.168.1.0/28'
    ping_addresses_in_network(ip_net)

if __name__ == '__main__':
    main()


