def water_area(heights):
    l, r = 0, len(heights) - 1
    l_max, r_max = heights[l], heights[r]
    
    res = 0

    while l < r:
        if heights[l] < heights[r]:
            l += 1
            l_max = max(l_max, heights[l])
            res += l_max - heights[l]

        else:
            r -= 1
            r_max = max(r_max, heights[r])
            res += r_max - heights[r]

    return res


print(water_area([0, 8, 0, 1, 0, 3, 0, 2, 0, 9, 0, 2, 0, 1]))
