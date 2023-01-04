n = int(input("Enter number of packets: "))
arr=[]
print("Enter no of chocolates in each packet: ")
for i in range (n):
  arr.append(int(input()))
m=int(input("Enter number of students: "))
diff=[]

arr.sort()
min_diff=max(arr)-min(arr)

for i in range(n-m+1):
  min_diff=min(min_diff,(arr[i+m-1]-arr[i]))

print(min_diff)