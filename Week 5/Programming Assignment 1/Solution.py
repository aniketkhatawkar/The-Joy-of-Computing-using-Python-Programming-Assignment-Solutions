L = input().split(' ')
L = [int(num) for num in L]
x = int(input())
 
first_pos = 0
last_pos = len(L)-1
flag=0
count = 0
while(first_pos<=last_pos and flag==0):
  count+=1
  mid = (first_pos+last_pos)//2
  if (x==L[mid]):
    flag = 1
    print(mid,end ='')
    break
  else:
    if (x < L[mid]):
      last_pos = mid-1
    else:
      first_pos = mid+1
else:
  print('-1',end ='')