para=input().split()
n=int(input())
S=list(set(para))
d={}
for i in S:
  d[i]=para.count(i)
if n in d.values():
  print(1,end="")
else:
  print(0,end="")