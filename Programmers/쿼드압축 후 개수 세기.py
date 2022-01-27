def solution(arr):
    result = [0, 0]
    length = len(arr)

    def compression(x, y, l):
        start = arr[x][y] 
        for i in range(x, x+l):
            for j in range(y, y+l):
                if arr[i][j] != start:
                    l = l // 2
                    compression(x, y, l)
                    compression(x, y+l, l)
                    compression(x+l, y, l)
                    compression(x+l, y+l, l)
                    return
        
        result[start] += 1
    
    compression(0, 0, length)
    
    return result