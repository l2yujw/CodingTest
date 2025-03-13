import heapq

def solution(operations):
    heap = []
    for oper in operations:
        arr = list(oper.split())
        command = arr[0]
        num = int(arr[1])
        
        if command == 'I': 
            heapq.heappush(heap, num)
        elif command == 'D':
            if heap:
                if num == 1:
                    heap.sort()
                    heap.pop()
                else:
                    heapq.heappop(heap)
    
    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else: 
        return [0, 0]