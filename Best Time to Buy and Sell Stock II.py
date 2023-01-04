n = int(input("Enter number of days: "))
arr=[]
print("Enter price of stock on each day: ")
for i in range (n):
  arr.append(int(input()))

profit=0
i=0
while i<n-1:
  if arr[i]==max(arr):
    i+=1
    continue
  else:
    for k in range(i+1,n):
      if arr[k]>arr[i]:
        if (k+1!=n and arr[k+1]>arr[k]):
          continue
        else:
          profit+=(arr[k]-arr[i])
          i=k+1
          break
      else:
        profit+=0
        if k==n-1:
          i+=1

print(profit)