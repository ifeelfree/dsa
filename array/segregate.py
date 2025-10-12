# Consider an array consisting of –ve and +ve numbers.
# What would be the worst case time complexity of an algorithm
# to segregate the numbers having same sign altogether i.e all
# +ve on one side and then all -ve on the other ?

# Two-Pointer Approach
def segregate_two_pointer(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

def segregate_partiton_med(arr):
    i = 0 # boundary of negative region
    for index in range(len(arr)):
        val = arr[index]
        if val < 0:
            arr[i], arr[index] = arr[index], arr[i]
            i = i+1
    return arr

if __name__ == "__main__":
    arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
    print(segregate_two_pointer(arr))
    print(segregate_partiton_med(arr))