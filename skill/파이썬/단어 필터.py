import re

paragraph = "Bob hit a ball, the hit BALL flew far after ir was hit."
banned = ['hit']

# 단어 문자 아닌 것은 ' ' (공백으로 치환) 하고 소문자로 변경후 , banned가 아닌 것이 리스트로 반환
words = [ word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
          if word not in banned]

print(words)