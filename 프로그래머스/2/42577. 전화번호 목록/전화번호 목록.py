def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        cur = phone_book[i]
        nxt = phone_book[i+1]
        if nxt[:len(cur)] == cur:
            return False
    return True