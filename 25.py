i=int(input())
j=list(map(int,input().split()))
j.sort()
med=j[int(i/2)]
print(med)
