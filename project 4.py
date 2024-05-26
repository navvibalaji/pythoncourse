l1=list(map(int,input().split(" ")))
even=[]
odd=[]
for i in l1:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(*even)
print(*odd)