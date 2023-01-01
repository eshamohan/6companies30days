n= int(input("Enter number of terms: "))
arr=[]
print("enter elements:")
for i in range (0,n):
  arr.append(int(input()))

for i in range(0,n):
  for k in range(i+1, n):
    if arr[i]==arr[k]:
      print("Repeated number is:",arr[i])
      break
  



