def fibo(n):
    if n == 1 or n == 2:    return 1
    
    d = [1, 1]
    
    for i in range(2, n):
        d.append((d[i - 1] + d[i - 2]) % 1234567) 
    
    return d[n - 1] % 1234567