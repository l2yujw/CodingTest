N, M = map(int, input().split())
heights = list(map(int, input().split()))

def binary_search(target):
    left, right = 0, max(heights)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for h in heights:
            if h > mid:
                total += h - mid

        if total >= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


print(binary_search(M))