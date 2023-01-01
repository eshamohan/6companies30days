def color_sort(arr,n):
  
  for i in range(n):
    temp=i
    for k in range(i+1,n):
      if arr[k]<arr[temp]:
        temp=k

    (arr[i],arr[temp]) = (arr[temp],arr[i])
  
  print("Sorted colors: \n")
  print(arr)

n = int(input("Enter number of terms: "))
arr=[]
print("enter elements:")
for i in range (0,n):
  arr.append(int(input()))
color_sort(arr,n)

