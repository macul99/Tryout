def fibseq(n):
    buf = [0, 1]
    buf_cnt = len(buf)
    
    if n<buf_cnt:
        return n
    
    for i in range(buf_cnt, n+1):
        result = sum(buf[i-2:i])
        buf.append(result)
        
    return result

