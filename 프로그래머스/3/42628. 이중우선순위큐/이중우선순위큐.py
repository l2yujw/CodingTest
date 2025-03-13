import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry = {}

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry[num] = entry.get(num, 0) + 1

        elif cmd == "D":
            if num == 1:
                while max_heap and entry.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_value = -heapq.heappop(max_heap)
                    entry[max_value] -= 1

            elif num == -1:
                while min_heap and entry.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_value = heapq.heappop(min_heap)
                    entry[min_value] -= 1

    while min_heap and entry.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and entry.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]
