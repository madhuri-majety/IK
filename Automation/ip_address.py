"""
Python script that uses all ipaddress module functions

https://docs.python.org/3/library/ipaddress.html

"""

import ipaddress

def print_all_ipaddress_attributes(ip_str):
    ipv4 = ipaddress.ip_address(ip_str)
    print("IPv4 Address Object is : {}".format(ipv4))
    print("IP Address version is : {}".format(ipv4.version))
    print("Max prefix Length is : {}".format(ipv4.max_prefixlen))
    print("Compressed is : {}".format(ipv4.compressed))
    print("Exploded is : {}".format(ipv4.exploded))
    print("Binary representation is : {}".format(ipv4.packed))
    print("Reverse DNS Pointer Record is : {}".format(ipv4.reverse_pointer))
    print("Is Multicast: {}".format(ipv4.is_multicast))
    print("Is Private: {}".format(ipv4.is_private))
    print("Is Global : {}".format(ipv4.is_global))
    print("Is Reserved : {}".format(ipv4.is_reserved))
    print("Is Loopback : {}".format(ipv4.is_loopback))
    print("Is Link Local : {}".format(ipv4.is_link_local))

def print_all_ipnetwork_attributes(ip_net):
    """
    A string consisting of an IP address and an optional mask, separated by a slash (/). The IP address is
    the network address, and the mask can be either a single number, which means it’s a prefix, or a string
    representation of an IPv4 address. If it’s the latter, the mask is interpreted as a net mask if it starts
    with a non-zero field, or as a host mask if it starts with a zero field, with the single exception of an
    all-zero mask which is treated as a net mask. If no mask is provided, it’s considered to be /32.

    For example, the following address specifications are equivalent:
     192.168.1.0/24, 192.168.1.0/255.255.255.0 and 192.168.1.0/0.0.0.255.

    ****** hosts() *******
    Returns an iterator over the usable hosts in the network.
    The usable hosts are all the IP addresses that belong to the network, except the network address itself and the network broadcast address.
    For networks with a mask length of 31, the network address and network broadcast address are also included in the result.


    ******* subnets(prefixlen_diff=1, new_prefix=None) ********
    The subnets that join to make the current network definition, depending on the argument values.
    prefixlen_diff is the amount our prefix length should be increased by.
    new_prefix is the desired new prefix of the subnets; it must be larger than our prefix.
    One and only one of prefixlen_diff and new_prefix must be set. Returns an iterator of network objects.

    ********* supernet(prefixlen_diff=1, new_prefix=None) *******
    The supernet containing this network definition, depending on the argument values.
    prefixlen_diff is the amount our prefix length should be decreased by.
    new_prefix is the desired new prefix of the supernet; it must be smaller than our prefix.
    One and only one of prefixlen_diff and new_prefix must be set. Returns a single network object.

    ******** subnet_of(other)  **********
    Returns True if this network is a subnet of other.
    a = ip_network('192.168.1.0/24')
    b = ip_network('192.168.1.128/30')
    b.subnet_of(a)
    True

    *********  supernet_of(other)  **********
    Returns True if this network is a supernet of other.
    a = ip_network('192.168.1.0/24')
    b = ip_network('192.168.1.128/30')
    a.supernet_of(b)
    True

    :param ip_net:
    :return:
    """
    ipnet = ipaddress.ip_network(ip_net)
    print("IP Network Object is : {}".format(ipnet))
    print("Network Address is : {}".format(ipnet.network_address))
    print("Broadcast Address of Network is : {}".format(ipnet.broadcast_address))
    print("Host Mask of network is : {}".format(ipnet.hostmask))
    print("Networks Mask of network is : {}".format(ipnet.netmask))
    print("Prefix length if network is : {}".format(ipnet.prefixlen))
    print("Network address with Netmask is : {}".format(ipnet.with_netmask))
    print("Network address with Prefix Length is : {}".format(ipnet.with_prefixlen))
    print("Network address with Host mask is : {}".format(ipnet.with_hostmask))
    print("Hosts Iterator in the network address are : {}".format(ipnet.hosts()))
    print("Hosts in the network address are : {}".format(list(ipnet.hosts())))
    print("Subnets Iterator in the network address are : {}".format(ipnet.subnets()))
    print("Subnets in the network address are : {}".format(list(ipnet.subnets())))
    print("Subnets in the network address with prefix length diff 2 is : {}".format(list(ipnet.subnets(prefixlen_diff=2))))
    print("Subnets in the network address with new prefix 31 is : {}".format(list(ipnet.subnets(new_prefix=31))))

def print_all_ipv4_inteface_attributes(ip_interface):
    """
    IPv4Interface is a subclass of IPv4Address, so it inherits all the attributes from that class.
    In addition, the following attributes are available:

    :param ip_interface:
    :return:
    """
    ip_intf = ipaddress.ip_interface(ip_interface)
    print("IPv4 Interface object is : {}".format(ip_intf))
    print("IP address of interface is : {}".format(ip_intf.ip))
    print("IP Network of interface is : {}".format(ip_intf.network))



def main():
    #ipaddr = str(input("Enter the ip address:"))
    ipaddr = '192.168.1.11'
    print_all_ipaddress_attributes(ipaddr)
    print("\n\n")
    #ip_net = '192.168.2.0/255.255.255.240'  # Network mask
    ip_net = '192.168.2.0/28'               # Prefix length
    #ip_net = '192.168.2.0/0.0.0.15'          # Host mask
    print_all_ipnetwork_attributes(ip_net)

    print("\n\n")
    ip_interface = '192.168.2.5/24'
    print_all_ipv4_inteface_attributes(ip_interface)



if __name__ == '__main__':
    main()
