import math

def solution(w, h):
    gcd = math.gcd(w, h)
    return w * h - (w + h - gcd)
