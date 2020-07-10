def missing_integer(n, list):
    sum_of_all_integers = 0
    sum_of_integers = 0
    for i in range(1, n+1):
        sum_of_all_integers = sum_of_all_integers ^ i
    for j in range(len(list)):
        sum_of_integers = sum_of_integers ^ j

    missing_number = sum_of_all_integers ^ sum_of_integers

    return missing_number


list = [1,2,4,5]
print(missing_integer(5, list))