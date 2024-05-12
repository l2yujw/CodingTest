def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[0]
	tail = arr[1:]

	left = [x for x in tail if x <= pivot]
	right = [x for x in tail if x > pivot]

	return quick_sort(left) + [pivot] + quick_sort(right)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    print("#%d" % (test_case), end=" ")
    print(*quick_sort(arr))
