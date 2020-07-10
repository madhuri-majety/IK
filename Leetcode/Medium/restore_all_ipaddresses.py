"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"

https://leetcode.com/problems/restore-ip-addresses/
https://www.geeksforgeeks.org/program-generate-possible-valid-ip-addresses-given-string/
https://www.geeksforgeeks.org/program-to-generate-all-possible-valid-ip-addresses-from-given-string-set-2/

A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255.
The numbers cannot be 0 prefixed unless they are 0.

Input : 25525511135
Output : [“255.255.11.135”, “255.255.111.35”]
Explanation:
These are the only valid possible
IP addresses.

Input : "25505011535"
Output : []
Explanation :
We cannot generate a valid IP
address with this string.

"""

import re

class BruteForceSolution(object):
    """
    First, we will place 3 dots in the given string and then Try out all the possible combinations for the 3 dots.

    Split the string with ‘ . ‘ and then check for all corner cases. Before entering the loop, check the size of string.
    Generate all the possible combinations using looping through the string.
    If IP is found to be valid then return the IP address, else simply return empty list.

    Time Complexity = O(N-1 * N-2 * N-3) = O(N^3)
    If string of lenght 12, 11*10*9 = 990 iterations for a single string
    :param object:
    :return:
    """
    def is_valid(self, ip):
        octets = ip.split('.')

        for octet in octets:
            if len(octet) > 3 or int(octet) < 0 or int(octet) > 255:
                return False
            if len(octet) > 1 and int(octet) == 0:
                return False
            if len(octet) > 1 and int(octet) != 0 and octet[0] == '0':
                return False

        return True

    def is_valid_regex(self, ip):
        ip_regex = '^(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])$'

        if re.match(ip_regex, ip):
            return True
        else:
            return False


    def restore_ip_address(self, str):
        n = len(str)

        if n > 12:
            return []
        snew = str

        output = []

        # Generate all possible combinations for the placement of 3 dots
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    snew = snew[:k] + '.' + snew[k:]
                    snew = snew[:j] + '.' + snew[j:]
                    snew = snew[:i] + '.' + snew[i:]

                    if self.is_valid_regex(snew):
                        output.append(snew)

                    snew = str

        print(output)


def main():
    restore_bruteforce = BruteForceSolution()
    restore_bruteforce.restore_ip_address("25525511135")
    restore_bruteforce.restore_ip_address("25505011535")
    restore_bruteforce.restore_ip_address("255255111351")


if __name__ == '__main__':
    main()



