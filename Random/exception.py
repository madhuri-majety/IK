#! /usr/bin/python

def divide(n):
    try:
        for i in [5,4,0,1,2]:
            res = n/i
            print(res)
        return True
    except:
        print('Handling run-time error')
        return False

def main():
    #num = int(input('Please enter a number: "))
    num = 100
    print('Calling divide() finction')
    if divide(num):
        print("Sucessfully executed")
    print('Done....')

if __name__ == '__main__':
    main()

