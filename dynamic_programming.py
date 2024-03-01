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
        
