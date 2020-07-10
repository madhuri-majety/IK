"""
Given an unsorted array of unique integers (size n + 1) and a second array that is identical to the
first array but missing one integer (size n), find and output the missing integer
"""

def missing_num_in_identical_arrays(nums1, nums2):
    nums1_xor_sum = 0
    nums2_xor_sum = 0

    for i in range(len(nums1)):
        nums1_xor_sum = nums1_xor_sum ^ nums1[i]
    print("Nums1 XOR sums: {}".format(nums1_xor_sum))

    for j in range(len(nums2)):
        nums2_xor_sum = nums2_xor_sum ^ nums2[j]
    print("Nums2 XOR sum: {}".format(nums2_xor_sum))

    missing_number = nums1_xor_sum ^ nums2_xor_sum

    print("Missing number using XOR is : {}".format(missing_number))

def missing_number_using_set(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    missing_number = set1-set2

    print("Missing number using set operation is {}".format(missing_number))


def main():
    nums1 = [10,20,30,40,50]
    nums2 = [20,30,40,50]

    missing_num_in_identical_arrays(nums1, nums2)
    missing_number_using_set(nums1, nums2)


if __name__ == '__main__':
    main()

