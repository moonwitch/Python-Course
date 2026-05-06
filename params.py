###############################################################################
# EXERCISE 1: 2 args
###############################################################################
def twoparams(var1, var2):
    print(var1, var2)


twoparams("one", "two")


###############################################################################
# EXERCISE 2: Sum of args
###############################################################################
def testingconcat(var1, var2):
    print(var1 + var2)


testingconcat("one", "two")


###############################################################################
# EXERCISE 3: Power Function
###############################################################################
def calculate_power(base, exponent):
    return base**exponent


###############################################################################
# EXERCISE 4: Print Average
###############################################################################
def print_average(numbers):
    if not numbers:
        return
    print(sum(numbers) / len(numbers))


###############################################################################
# EXERCISE 5: Print Maximum
###############################################################################
def print_max(numbers):
    if not numbers:
        return
    print(max(numbers))


###############################################################################
# EXERCISE 6: Print Minimum
###############################################################################
def print_min(numbers):
    if not numbers:
        return
    print(min(numbers))


###############################################################################
# EXERCISE 7: Stats Summary (Min, Max, Average)
###############################################################################
def get_stats_summary(numbers):
    if not numbers:
        return None, None, None

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


###############################################################################
# EXERCISE 8: Median Calculation
###############################################################################
def calculate_median(numbers):
    if not numbers:
        return None

    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        # Even: Average of the two middle elements
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        # Odd: The middle element
        return sorted_nums[mid]


# --- Test Execution for Exercise 8 ---
list_a = [3, 1, 2, 3, 12, 2]
list_b = [5, 1, 2, 3, 9]

print(f"Median of {list_a}: {calculate_median(list_a)}")  # Expected: 2.5
print(f"Median of {list_b}: {calculate_median(list_b)}")  # Expected: 3
