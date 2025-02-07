# Ex.3:

# The task is to write a recursive function that receives a number and returns the sum of its digits.
#
# Example
# Input: 86 → Output: 6 + 8 = 14
# Input: 404 → Output: 4 + 0 + 4 = 8
# Recursive Approach
# Base Case: If the number is a single digit, return it.
# Recursive Case: Extract the last digit and call the function on the remaining part of the number.
#__________________________________________________________________________________________________

def sum_of_digits(n):
    if n < 10:  # Base case: single-digit number
        return n
    return (n % 10) + sum_of_digits(n // 10)  # Recursive step

# Testing the function
print(sum_of_digits(86))   # Output: 14
print(sum_of_digits(404))  # Output: 8
print(sum_of_digits(1234)) # Output: 10

#__________________________________________________

# sum_of_digits(86)
#   = (86 % 10) + sum_of_digits(86 // 10)
#   = 6 + sum_of_digits(8)
#
# sum_of_digits(8)  # Base case reached
#   = 8
#
# Now, returning:
#   = 6 + 8 = 14
