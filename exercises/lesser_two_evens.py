def lesser_two_evens(a, b):
    if a%2 == 0 and b%2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b
        
print(lesser_two_evens(2, 4))
print(lesser_two_evens(2, 5))