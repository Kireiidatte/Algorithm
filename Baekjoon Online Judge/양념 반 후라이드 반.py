# 양념치킨 가격, 후라이드치킨 가격, 반반치킨 가격, 양념 치킨 최소 X마리, 후라이드 치킨 최소 Y마리
A, B, C, X, Y = map(int, input().split())

money = 0

if A+B < 2*C:
    money += (A*X + B*Y)
else:
    money += (2*min(X, Y)*C + min(A, 2*C)*max(0, X-Y) + min(B, 2*C)*max(0, Y-X))

print(money)