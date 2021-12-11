a = [11, 88, 69, 72, 21, 34, 37, 99,2]
h = len(a)

def peak(a, h):
    if a[0] >= a[1]:
        return 0
    if a[h-1] >= a[h-2]:
        return h -1
    for i in range (1, h-1):
        if a[i] >= a[i-1] and a[i] >= a[i+1]:
            return i

print("The peak is: ", peak(a, h))