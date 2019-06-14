a,b=map(int,input().split())
for x in range (a+1,b):
  temp=x
  sum=0
  while(temp>0):
    remainder=temp%10
    sum=sum+remainder**3
    temp=temp//10
  if(x==sum):
    print(x,end=' ')
  
