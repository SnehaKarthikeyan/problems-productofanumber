Coding:
  
n, k= map(int,input().split())
x = [1]*k
n -= k
i = 0
while i<k and n:
  while x[i]<=n:
   n-=x[i]
   x[i]*=2
  i+=1
if n:
 print('NO')
else:
 print('YES')
