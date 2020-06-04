def gen_range(lwr, upr):
    """ return list of all natural numbers in range [lwr^2, upr^2]
        which are products of 3-digit numbers, in descending order 
    """
    nums = []
    for i in range(lwr, upr + 1):
        for j in range(lwr, upr + 1):
            nums.append(i*j)
    nums.sort(reverse=True)
    return nums

def is_palindrome(num):
    """ returns true iff the string representation
        of num is a palindrome
    """
    str_num = str(num)
    return str_num == str_num[::-1]

def largest_palindrome(nums):
    """
        input: nums - a list of natural numbers in descending order
        output: num - the largest palindrome in nums
    """
    for num in nums:
        if is_palindrome(num):
            return num

print(largest_palindrome(gen_range(100, 999)))
