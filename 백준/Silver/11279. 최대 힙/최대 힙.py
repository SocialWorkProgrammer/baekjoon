import sys
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        # 1번 인덱스부터 사용하므로 0번은 None
        self.heap = [None]

    def __str__(self):
        return str(self.heap[1:])
    def push(self, value):
        # 힙 맨 뒤 삽입
        self.heap.append(value)
        idx = len(self.heap) - 1

        # 부모와 비교하며 아래로 내리기
        while idx > 1:
            parent = idx // 2
            # 부모가 더 크거나 같으면 break
            if self.heap[parent] >= self.heap[idx]:
                break
            # 자식이 더 크면 부모가 더 클을 때까지 swap 반복
            self.heap[parent], self.heap[idx] = self.heap[idx],self.heap[parent]
            idx = parent
        return self.heap

    def pop(self):
        # 힙이 비어 있는 경우
        if len(self.heap) == 1:
            return 0
        # 원소가 하나만 있는 경우 => 바로 출력
        if len(self.heap) == 2:
            return self.heap.pop()
        # 루트값을 pop하며 최댓값에 저장
        max_value = self.heap[1]
        # 마지막 원소를 루트로 이동
        self.heap[1] = self.heap.pop()
        # 자식과 비교하며 위로 올리기
        idx = 1
        while True:
            left = idx * 2
            right = idx * 2 + 1
            largest = idx
            # 왼쪽 자식과 비교
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            # 오른쪽 자식과 비교
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            # (운 좋게도) 루트값이 최댓값이면 종료
            if largest == idx:
                break
            # 더 작은 자식과 교환
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest
        return max_value

maxheap = MaxHeap()
N = int(input())
for tc in range(N):
    x = int(input())
    if x == 0:
        print(maxheap.pop())
    else:
        maxheap.push(x)