n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분  -> 피벗보다 작은 수만 들어있는 리스트 생성
    right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분    -> 피벗보다 큰 수만 들어있는 리스트 생성

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)     # 리스트 사이에 피벗 추가

sorted_list = quick_sort(array)
for i in range(n):
    print(sorted_list[i], end="\n")