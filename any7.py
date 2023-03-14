def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    num_str = str(nums)
    if num_str.__contains__('7'):
        return True
    else:
        return False

        
    # YOUR CODE HERE 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

# test_list = [1,2,7,4,5]

# str_test = str(test_list)
# print(str_test)

# s = 'abc'

# print(s.__contains__('a'))

