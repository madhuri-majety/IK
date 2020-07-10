"""
Write a smart divide function
"""

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide {} and {}".format(a,b))
        if b == 0:
            print("Cannot divide")
            return

        return func(a,b)
    return inner


@smart_divide
def divide(a,b):
    return a/b


def smart_max_list(func):
    def inner(in_list):
        if len(in_list) == 0:
            print("Empty list")
            return None
        return func
    return inner

@smart_max_list
def max_list(in_list):
    return max(in_list)

print(divide(2,5))

print(divide(3,0))

print(max_list([]))
