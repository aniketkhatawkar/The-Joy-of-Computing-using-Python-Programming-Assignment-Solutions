S=[i for i in input().split()]
ans=0
for i in S:
  k=i.split('.')
  if len(k[1])>len(k[0]):
    ans+=1
print(ans, end="") 