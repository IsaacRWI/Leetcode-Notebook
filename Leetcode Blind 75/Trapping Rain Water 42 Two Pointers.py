def trap(height):
    l_wall = 0  # height of left wall
    r_wall = 0  # height of right wall
    max_left = [0] * len(height)  # array for left pointer to go through the main array
    max_right = [0] * len(height)

    for i in range(len(height)):  # for item in the main array
        j = -i - 1  # j starts from the back
        max_left[i] = l_wall  # add l_wall to left pointer array
        max_right[j] = r_wall
        l_wall = max(l_wall, height[i])  # set l_wall to new tallest wall if new wall is taller than previous left wall  then add to left pointer array in next loop
        r_wall = max(r_wall, height[j])

    summ = 0
    for i in range(len(height)):
        pot = min(max_left[i], max_right[i])  # potential volume is the shorter of the two walls that make up the container
        summ += max(0, pot - height[i])  # then minus the height of the element itself from the potential and add 0 if the result is negative

    return summ

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))