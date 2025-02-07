# EX.4:

# Write a recursive function that takes a list and a number,
# and returns how many times the number appears in the list.
# (We are allowed to add extra parameters if needed.)
# ____________________________________________________________

# Example Inputs & Outputs
# Input List	                Target Number	                Output (Occurrences)
# [1, 2, 2, 3, 2, 4]	        2	                            3
# [5, 5, 5, 5]	                5	                            4
# [1, 2, 3, 4]	                6	                            0
#_______________________________________________________________________________

# Recursive Approach:
# Base Case:
# If the list is empty ([]), return 0 because the number does not appear.
# Recursive Step:
# Check the first element of the list:
# If it matches the number, add 1 and call the function on the rest of the list.
# Otherwise, call the function on the rest of the list without adding 1.
#_________________________________________________________________________________

def count_occurrences(lst, num):
    if not lst:  # Base case: if the list is empty, return 0
        return 0
    return (1 if lst[0] == num else 0) + count_occurrences(lst[1:], num)

# Test cases
print(count_occurrences([1, 2, 2, 3, 2, 4], 2))  # Output: 3
print(count_occurrences([5, 5, 5, 5], 5))        # Output: 4
print(count_occurrences([1, 2, 3, 4], 6))        # Output: 0
#_______________________________________________________________________________

# Recursive Call Diagram
# Example: count_occurrences([1, 2, 2, 3, 2, 4], 2)

# 1. count_occurrences([1, 2, 2, 3, 2, 4], 2)
#       First element 1 ≠ 2 → Add 0
#       Recurse on [2, 2, 3, 2, 4]

# 2. count_occurrences([2, 2, 3, 2, 4], 2)
#       First element 2 == 2 → Add 1
#       Recurse on [2, 3, 2, 4]

# 3. count_occurrences([2, 3, 2, 4], 2)
#       First element 2 == 2 → Add 1
#       Recurse on [3, 2, 4]

# 4. count_occurrences([3, 2, 4], 2)
#       First element 3 ≠ 2 → Add 0
#       Recurse on [2, 4]

# 5. count_occurrences([2, 4], 2)
#       First element 2 == 2 → Add 1
#       Recurse on [4]

# 6. count_occurrences([4], 2)
#       First element 4 ≠ 2 → Add 0
#       Recurse on []

# 7. count_occurrences([], 2)
# Base case reached → Return 0

# 8. Add up values: 0 + 1 + 1 + 0 + 1 + 0 + 0 = 3
