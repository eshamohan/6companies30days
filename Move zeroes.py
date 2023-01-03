n = int(input("Enter number of terms: "))
arr=[]
print("enter elements:")
for i in range (n):
  arr.append(int(input()))
count=0

for i in range(n):
  if arr[i]==0:
    count=count+1
    for j in range(i,n-1):
      arr[j]=arr[j+1]
for i in range(n-count,n):
  arr[i]=0
  
print(count)
print(arr)
