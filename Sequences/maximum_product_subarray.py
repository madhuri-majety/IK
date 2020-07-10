import sys

def max_product_subarray_brute_force(arr):
    n = len(arr)
    max_product = -sys.maxsize

    for i in range(n):
        for j in range(i+1, n+1):
            prod = 1
            temp = arr[i:j]
            for item in temp:
                prod = prod * item

            if max_product < prod:
                max_product = prod

    print(max_product)

def max_product_subarray_greedy(arr):
    n = len(arr)
    max_prod = -sys.maxsize
    most_neg = 1
    most_pos = 1

    for num in arr:
        most_pos, most_neg = max(num, num * most_pos, num * most_neg), min(num, num * most_pos, num * most_neg)
        max_prod = max(max_prod, most_pos, most_neg)

    print(max_prod)



def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr1 = [2,3,-4]

    print("Printing using Brute Force way")
    max_product_subarray_brute_force(arr)
    max_product_subarray_brute_force(arr1)

    print("Printing using Greedy approach")
    max_product_subarray_greedy(arr)
    max_product_subarray_greedy(arr1)

if __name__ == '__main__':
    main()


