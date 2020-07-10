"""
Given a file search for all ip addresses.

"""
import re

class IPAddress(object):
    def __init__(self, filename):
        self.filename = filename

    def get_ip_addresses_from_file(self):
        print("Enter get_ip_addresses_from_file()")
        with open(self.filename, 'r') as fh:
            data = fh.read()

        ip_exp = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        ips = ip_exp.findall(data)
        #print(ips)
        return ips

    def validate_ips(self):
        valid_ips = []
        ips = self.get_ip_addresses_from_file()
        for ipaddr in ips:
            has_incorrect_octets = False
            octets = ipaddr.split('.')
            for i, octet in enumerate(octets):
                if int(octet) not in range(0,256):
                    has_incorrect_octets = True
                    break

            if not has_incorrect_octets:
                valid_ips.append(ipaddr)

        return valid_ips

    def get_valid_ips_from_file(self):
        result = []
        with open(self.filename, 'r') as fh:
            data = fh.read()

        regex = '(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'

        ip = re.compile(regex)
        ips = ip.finditer(data)

        #ips = re.finditer(regex, data)

        for ip in ips:
            result.append((".".join(ip.groups())))
        return(result)

def main():
    inp = 'input.txt'
    ipaddr = IPAddress(inp)
    print(ipaddr.validate_ips())
    print("\n\n")
    print("Get IP address using proper ip address regex")
    print(ipaddr.get_valid_ips_from_file())


if __name__ == '__main__':
    main()




