n1, n2 = map(int, input().split())
g1 = list(input())
g2 = list(input())
T = int(input())

	# 방향 통일
g1.reverse()
 
# N1 N2 통합
g_sum = g1 + g2
 
for t in range(T):
 
    # swap해야하는 idx 값 저장
    tmp = []
 
    for q in range(1,len(g_sum)):
        # 왼쪽 방향으로 이동하는 경우만 확인하면 됨
        # <- -> 의 경우는 방향이 서로 달라도 swap할 필요 없음
        if g_sum[q] in g2:
            if g_sum[q-1] in g1:
                tmp.append(q)
 
    # swap 해주기
    for w in tmp:
        g_sum[w], g_sum[w-1] = g_sum[w-1], g_sum[w]
 
# 결과
result = ''
 
for r in g_sum:
    result += r

print(result)