n = int(input("Enter number of days: "))
arr=[]
print("Enter price of stock on each day: ")
for i in range (n):
  arr.append(int(input()))

profit=[]

for i in range(n):
  for k in range(i+1,n):
    profit.append(arr[k]-arr[i])
  
if max(profit)<0:
  print("0")
else:
  print("Profit:",max(profit))