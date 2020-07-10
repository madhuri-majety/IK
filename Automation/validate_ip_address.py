"""
Regular expression that matches IP address
"""

import re

"""
IP octet can be in one of these catetgories
250 - 255
200 - 249
0 - 199

"""

regex1 = '^(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])$'

# Note: For some reason the exact below regex only works, if '(' is moved to next line the regex wont match
regex = '''^(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)$'''

def check_ip(ipaddr):
    if (re.match(regex, ipaddr)):
        print("IP address {} is Valid".format(ipaddr))
    else:
        print("IP address {} is Invalid".format(ipaddr))

def testcases():
    check_ip('0.0.0.0')
    check_ip('233.243.244.255')
    check_ip('192.168.0.1')
    check_ip('366.1.1.2')
    check_ip('255.255.255.255')
    check_ip('10.10.10.10')
    check_ip('2.55.25.511135')
    check_ip('255.050.115.35')

if __name__ == '__main__':
    testcases()
