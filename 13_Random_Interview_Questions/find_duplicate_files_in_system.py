"""
https://leetcode.com/problems/find-duplicate-file-in-system/

Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]


Approach using Hashmap:
For every input file with directory, store the file contents as key and its value as filename with directory heirarchy.

Key Points:
Key should be file content.
- If the file content is very small then use the content as Key
- If the file content is significantly big then calculate the hash of the file content and use that hash as key

https://www.howtogeek.com/67241/htg-explains-what-are-md5-sha-1-hashes-and-how-do-i-check-them/

Using Python Hashlib

hashlib.md5('b').hexdigest()
'92eb5ffee6ae2fec3ad71c777531578f'

hashlib.md5("When we talk about hash tables, we're actually talking about dictionary. While an array can be used
to construct hash tables, array indexes its elements using integers. However, if we want to store data and use keys
other than integer, such as 'string', we may want to use dictionary.").hexdigest()
'7f098aa5ceec8f7b88213503cb95d611'


"""
from collections import defaultdict
import hashlib

def find_duplicates_files(list_files):
    file_hash = {}
    output = []

    for item in list_files:
        fields = item.split(" ")
        directory = fields[0]
        files = fields[1:]
        for file in files:
            file_path = directory+"/"+file
            with open(file_path, 'r') as fh:
                data = fh.read()
                content_hash = hashlib.md5((data).encode('utf-8')).hexdigest()
            if content_hash in file_hash:
                file_hash[content_hash] = file_hash[content_hash] + [file_path]
            else:
                file_hash[content_hash] = [file_path]


    print(file_hash)

    for key, value in file_hash.items():
        if len(value) > 1:
            output.append(value)

    return output



def main():
    input = ["test/a 1.txt 2.txt", "test/c 3.txt", "test/c/d 4.txt", "test 4.txt"]
    print(find_duplicates_files(input))

if __name__ == '__main__':
    main()

