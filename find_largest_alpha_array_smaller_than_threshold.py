# find_largest_alpha_array_smaller_than_threshold in alphab order

import numpy as np
a = np.array(
    [
        [1,2,3,4],
        [3,2,2,3],
        [3,2,2,3]
    ]
)

b = np.array(
    [3,2,3,4]
)

def is_a_smaller_than_b(a, b):
    length = len(a)
    for i in range(length):
        if a[i]<b[i]:
            i = -1
            break
        elif a[i]>b[i]:
            break
            
    return i == -1

#print(is_a_smaller_than_b(a[2,:], a[1,:]))

def find_max_less_than_threshold(inp, th):
    list_len, item_len = a.shape
    print(list_len, item_len)
    
    best_list_id = -1
    
    for i in range(list_len):
        if is_a_smaller_than_b(inp[i,:], th):
            if best_list_id == -1:
                best_list_id = i
            else:
                if is_a_smaller_than_b(inp[best_list_id,:], inp[i,:]):
                    best_list_id = i
    
    return best_list_id
