def sortedSquaredArray(array):
    if len(array) == 0:
        return []
    result = []
    l, r = 0, len(array) - 1
    l_squared = 0
    r_squared = 0
    # while left pointer index is smaller than right pointer index
    while l <= r:
        l_squared = array[l] * array[l]
        r_squared = array[r] * array[r]

        # checking if left square is greater than right square
        if l_squared > r_squared:
            result.append(l_squared)
            l += 1
        else:
            result.append(r_squared)
            r -= 1

    # return the reversed array
    return result[::-1]


print(sortedSquaredArray([-6, 4, 7]))
