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
    print(": ", i, j)
    v_temp = v + j - i + 1
    
    if v_temp == N: # reach the goal
        print(i, j)
        return v_temp
    
    if m==K-1: # reach max K value
        if v<N: # invalid skip, continue iter
            print('invalid')
            return None
    
    # loop next row with i+1, j+1
    for k in range(j+1, N):
        #print(i+1, k)
        rst = iter_matrix(j+1, k, v_temp, m+1, N, K)
        if rst is not None:
            print(i,j)
        #return rst
