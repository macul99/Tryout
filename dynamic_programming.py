def fibseq(n):
    buf = [0, 1]
    buf_cnt = len(buf)
    
    if n<buf_cnt:
        return n
    
    for i in range(buf_cnt, n+1):
        result = sum(buf[i-2:i])
        buf.append(result)
        
    return result

def iter_matrix(i, j, v, m, N, K):
    # set i=-1 and j=-1 to start the process
    # (i, j) is the cell index of 2D matrix, matrix has shape of (K, N)
    # v is number of space before this function call
    # m is the number of K used so far, max can only use up to K
    # K<N
    if i>=0:
        #print(": ", i, j)
        v_temp = v + j - i + 1 # (i,j) cell occupy space of j-i+1, eg (0,0),(1,1) have space of 1, (1,4) has space of 4

        if v_temp == N: # reach the goal
            #print(i, j)
            return [[(i, j)]]
            #return v_temp

        if m==K-1: # reach max K value
            if v<N: # not reaching target value N, continue iter with item of next item in the same row
                #print('invalid')
                return None
    else:
        v_temp = 0
        m = -1
    
    # loop next row with i+1, j+1
    rst_list = []
    for k in range(j+1, N):
        #print(k)
        # j actually tracking number of space so far and need to jump row j+1 to continue search
        # eg: (0,0)=>(1,2)=>(3,3) or (0,0)=>(1,2)=>(3,4), not (0,0)=>(1,2)=>(2,3)
        rst = iter_matrix(j+1, k, v_temp, m+1, N, K) 
        if rst is not None:
            for l in rst:
                if i==-1:
                    rst_list.append(l) # don't add (-1,-1) in the list
                else:
                    rst_list.append([(i,j)]+l)
    return rst_list
    
    
iter_matrix(-1,-1,0,0,5,4)

def go_through_cost(k_set, idx_list):
    rst = []
    for s in k_set:
        cost_item_0 = 0 # value at idx locaiton of s
        if len(idx_list)==1:
            rst.append((s,cost_item_0))
    
        rst.append((s, cost_item_0 + go_through_cost(k_set.difference(s), idx_list[1:])))


def num_of_matching_seq(d, arr):
    ln = len(arr)
    
    diff = [0]*(ln-1)
    
    for i in range(1, ln):
        diff[i-1] = arr[i] - arr[i-1]
    
    print(f"diff: {diff}")
    rst = 0
    sm = 0
    
    for i in range(len(diff)):
        idx = i
        sm = diff[idx]
        state = 0
        loop_flag = 1
        
        while loop_flag:
            #print(i, idx, sm, state, rst)
            if sm>d:
                loop_flag = 0
            elif sm == d:
                if state == 0:
                    state=1
                    idx += 1
                    if idx<ln-1:
                        sm = diff[idx]
                    else: # end of list
                        loop_flag = 0
                elif state == 1:
                    rst += 1
                    loop_flag = 0
            else: # sm<d, coninue add up next diff value
                idx += 1
                if idx<ln-1:
                    sm += diff[idx]
                else:
                    loop_flag = 0
                    
    return rst
