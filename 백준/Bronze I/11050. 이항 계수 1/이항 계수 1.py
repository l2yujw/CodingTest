N, K = map(int, input().split())

result = 1
div = 1
for x in range(K):
    result *= (N - x)
for k in range(1, K + 1):
    div *= k

print(result//div)