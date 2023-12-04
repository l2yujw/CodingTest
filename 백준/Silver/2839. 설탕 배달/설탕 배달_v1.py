n=int(input())
print([n//5+[0,2-n%5%2][n%5>0],-1][n in[4,7]])