# Ex.2:

# Write a recursive function that calculates the factorial of a given number.
# The function should take an integer as input and return its factorial.
#
# Examples:
# factorial(5) → 120 (since 5 * 4 * 3 * 2 * 1 = 120)
# factorial(2) → 2 (since 2 * 1 = 2)
# factorial(0) → 1 (by definition, 0! = 1)
#____________________________________________________________________________

def factorial(n):
    if n == 0:
        return 1  # Base case: 0! = 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120
print(factorial(2))  # Output: 2
print(factorial(0))  # Output: 1

#____________________________________________________
#
# factorial(5)
#  ├── 5 * factorial(4)
#       ├── 4 * factorial(3)
#            ├── 3 * factorial(2)
#                 ├── 2 * factorial(1)
#                      ├── 1 * factorial(0)
#                           ├── factorial(0) = 1 (Base case)
#                      ├── 1 * 1 = 1
#                 ├── 2 * 1 = 2
#            ├── 3 * 2 = 6
#       ├── 4 * 6 = 24
#  ├── 5 * 24 = 120
