def solution(numbers):
    answer = ''
    tmp = []

    if sum(numbers) == 0:
        return '0'

    for num in numbers:
        num4 = (str(num) * 4)[:4]
        num_length = len(str(num))
        tmp.append((num4, num_length))
    
    tmp.sort(reverse=True)
    
    for num, length in tmp:
        answer += num[:length]

    return answer
