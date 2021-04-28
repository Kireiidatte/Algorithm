def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for idx, i in enumerate(phone_book[:-1]):
        if i == phone_book[idx+1][:len(i)]:
            return False
    
    return True