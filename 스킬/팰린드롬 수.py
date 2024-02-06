import re
def isPallindrome(s : str) -> bool:
    s= s.lower()
    print(s)
    s= re.sub('[^a-z0-9]','',s)
    print(s)
    return s == s[::-1]
print(isPallindrome("race A car"))
# race a car
# raceacar
# False

