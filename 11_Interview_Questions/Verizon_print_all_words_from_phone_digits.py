"""
Print all possible words from phone digits
Before advent of QWERTY keyboards, texts and numbers were placed on the same key.
For example 2 has “ABC” if we wanted to write anything starting with ‘A’ we need to type key 2 once.
If we wanted to type ‘B’, press key 2 twice and thrice for typing ‘C’. below is picture of such keypad.

Given a keypad as shown in diagram, and a n digit number, list all words which are possible by pressing these numbers.
For example if input number is 234, possible words which can be formed are (Alphabetical order):
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi

https://www.geeksforgeeks.org/find-possible-words-phone-digits/

For number above 234. Do you see any pattern? Yes, we notice that the last character always either G,H or I and
whenever it resets its value from I to G, the digit at the left of it gets changed.
Similarly whenever the second last alphabet resets its value, the third last alphabet gets changes and so on.
First character resets only once when we have generated all words. This can be looked from other end also.
That is to say whenever character at position i changes, character at position i+1 goes through all possible
characters and it creates ripple effect till we reach at end.
Since 0 and 1 don’t have any characters associated with them. we should break as there will no iteration for these digits.
Let’s take the second approach as it will be easy to implement it using recursion. We go till the end and come back
one by one. Perfect condition for recursion. let’s search for base case.
When we reach at the last character, we print the word with all possible characters for last digit and return.
Simple base case.
When we reach at the last character, we print the word with all possible characters for last digit and return.
Simple base case.

"""

hashtable = {2: 'abc',
             3: 'def',
             4: 'ghi',
             5: 'jkl',
             6: 'mno',
             7: 'pqrs',
             8: 'tuv',
             9: 'wxyz'}

def printWordsUtil(number, num_idx, temp, res, n):
    """
    Time Complexity = O(4 ^ N) (where 4 is the max number of characters possible for a number)
    :param number:
    :param num_idx:
    :param temp:
    :param res:
    :param n:
    :return:
    """
    # Base case: If the last digit is reached collect word into end result
    if num_idx == n:
        res.append("".join(temp))
        return

    # Recursive case:
    # Try all possible characters for current digit in number
    # and recur for remaining digits
    # *** Imagine a tree with lead nodes as last digits characters
    for i in range(len(hashtable[number[num_idx]])):
        temp.append(hashtable[number[num_idx]][i])
        printWordsUtil(number, num_idx+1, temp, res, n)
        temp.pop()

    return res


def printWords(nums):
    numbers = []
    for i, num in enumerate(nums):
        if num in hashtable.keys():
            numbers.append(num)

    return printWordsUtil(numbers, 0, [], [], len(numbers))

if __name__ == '__main__':
    numbers = [2, 1, 3, 4, 0, 5]
    print(printWords(numbers))
