array = [8, 4, 6, 2, 9, 1, 3, 7, 5]

def quickSort(array):
    def sort(low, high):
        if high <= low:
            return
        
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        # 리스트의 정 가운데 있는 값 pivot으로 선택
        pivot = array[(low + high) // 2]
        # 시작 인덱스(low)를 계속 증가시키고 끝 인덱스(high)를 계속 감소시키며
        # 두 인덱스가 서로 교차할때까지 반복
        while low <= high:
            # pivot보다 크고 좌측에 있는 값 탐색
            while array[low] < pivot:
                low += 1
            # pivot보다 작고 우측에 있는 값 탐색
            while array[high] > pivot:
                high -= 1
            # 두 인덱스가 교차하지 않았다면 시작 인덱스(low), 끝 인덱스(high) Swap
            if low <= high:
                array[low], array[high] = array[high], array[low]
                # 상호 교대 후 두 인덱스를 각자 진행방향으로 한 칸씩 이동
                low, high = low + 1, high - 1
        
        # 두 인덱스가 서로 교차해서 루프를 빠져나왔으면 
        # 다음 재귀 호출의 분할 기준점이 될 시작 인덱스 리턴
        return low

    return sort(0, len(array) - 1)

print("before: ",array)
quickSort(array)
print("after:", array)
