letters = ['let1 art can','let2 own kit dig', 'let3 art zero']

#2번째 절을 정렬, 같을경우 맨앞 기준으로 정렬
print(letters[1].split()[1:])
letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
print(letters)

letters.sort(key=lambda x : (x.split()[1:], x.split()[0]),reverse=True)
print(letters)