# make subarrays of array for every item in the array with the length determined by k
# find smallest element for each subarray the find largest element of all the smallests

def MinMax(arr, k):
    sub_list = []
    min_list = []
    for i in range(len(arr)):
        if i+k < len(arr):
            subarray = arr[i : i+1+k]
            # print(subarray)
            sub_list.append(subarray)
    for j in sub_list:
        min_list.append(min(j))
    return max(min_list)



print(MinMax([1,2,3,4], 1))