def inside_range(num, low, high):
    if low <= num <= high:
        return True
    else:
        return False

print(inside_range(5, 2, 7))

def inside_range1(num, low, high):
    if num in range(low, high+1):
        return True
    return False

print(inside_range1(5, 2, 7))
