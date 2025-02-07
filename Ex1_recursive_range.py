#________ EX.1

# Write a function that implements range recursively.
# The function should take three arguments:
#
# A starting number
# A target number (final number)
# A step size (jump size)
# The function should print all numbers from the starting number to the final number in the given step size without exceeding the final number.
#
# Example:
# For start=8, jump=3, final=21:
# The output should be:
# ---------------       8 11 14
#____________________________________________________

def recursive_range(start, final, jump):
    """Recursively prints numbers from start to final with a given jump without exceeding final."""
    if start > final:  # Base case: Stop if start exceeds final
        return
    print(start, end=" ")  # Print the current number
    recursive_range(start + jump, final, jump)  # Recursive call with next step

# Example usage:
recursive_range(8, 15, 3)


#______________________________________________________________________________________________________
# The function works by starting from 8 and adding jump (3) each time, as long as the next number does not exceed final = 15.

# Step-by-Step Execution:
# 1st Call: recursive_range(8, 15, 3)
# start = 8, which is less than 15, so we print 8.
# The next step: 8 + 3 = 11
# Calls recursive_range(11, 15, 3)
# 2nd Call: recursive_range(11, 15, 3)
# start = 11, which is less than 15, so we print 11.
# The next step: 11 + 3 = 14
# Calls recursive_range(14, 15, 3)
# 3rd Call: recursive_range(14, 15, 3)
# start = 14, which is less than 15, so we print 14.
# The next step: 14 + 3 = 17
# Calls recursive_range(17, 15, 3)
# 4th Call: recursive_range(17, 15, 3)
# start = 17, but 17 is greater than 15, so the function stops here (base case met).

# Diagrama:
# recursive_range(8, 15, 3)
# │
# ├── Prints: 8
# │   └── Calls recursive_range(11, 15, 3)
# │
# ├── Prints: 11
# │   └── Calls recursive_range(14, 15, 3)
# │
# ├── Prints: 14
# │   └── Calls recursive_range(17, 15, 3)
# │
# └── Stops (17 > 15) → Base case reached



