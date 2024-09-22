n=[int(i) for i in input().split()]
mid=len(n)/2
left=sum(n[:len(n)//2])
right=sum(n[len(n)//2:])
#print(f"left is {left} and right is {right}")
if left>right:
  print(-1,end="")
elif right>left:
  print(1,end="")
else:
  print(0,end="")