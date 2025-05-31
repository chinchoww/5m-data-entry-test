def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    if str(x).isnumeric() and str(y).isnumeric():
        x, y = y, x
        return x,y
    else:
        return -1
        

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17


x,y= "Apple" ,10
result1 = swap(x,y)
print(result1)


x, y = 9,17
result2 = swap(x,y)
print(result2)