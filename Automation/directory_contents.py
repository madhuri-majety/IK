"""

    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.

********* Three imp functions ************
os.listdir(path)
os.path.join(path, file)
os.path.isdir(path)
"""
import os

def print_dir_contents(path):
    for child in os.listdir(path):
        childpath = os.path.join(path, child)
        if os.path.isdir(childpath):
            print_dir_contents(childpath)
        else:
            print(childpath)

def main():
    path = '/Users/sumanthkakaraparthi/Documents/MacPro-2019/Documents/scripts'
    print_dir_contents(path)

if __name__ == '__main__':
    main()
