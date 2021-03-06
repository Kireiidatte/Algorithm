from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    
    return True

def solution(user_id, banned_id):
    banned_Set = []
    all_users_list = list(permutations(user_id, len(banned_id)))
    
    for users in all_users_list:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in banned_Set:
                banned_Set.append(users)
    
    return len(banned_Set)