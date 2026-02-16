def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

inputs = [input().strip() for _ in range(3)]

answer_val = None

for idx, s in enumerate(inputs):
    if s.isdigit():
        answer_val = int(s) + (3 - idx)
        break

print(fizzbuzz(answer_val))
