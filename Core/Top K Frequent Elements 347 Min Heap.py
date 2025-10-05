from collections import Counter
import heapq

def topKFrequent(self, nums, k):
    counter_dict = Counter(nums)  # dictionary with items from the list and the times they appear  (item : times appeared)
    heap = list()  # python list where the heap functions will be applied to

    for key, value in counter_dict.items():  # for key and value in the counter_dict  .items() returns the key value pairs in a tuple
        if len(heap) < k:  # if there are less elements in the heap list than they want top however many elements
            heapq.heappush(heap, (value, key))  # heap push the element into the heap list without removing any of them  the heap will sort
        else:  # else
            heapq.heappushpop(heap, (value, key))  # heap push the new element into the heap and call the pop function to pop the smallest elements in the list, judged based on the "value" paremeter

    return [i[1] for i in heap]  # return a list of "key" values (the key are the elements and the values are the times they appear) that remain in the heap