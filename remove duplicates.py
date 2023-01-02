def duplicate(arr,n):
  
  new=[]
  for i in range(n):
    if arr[i] in new:
      continue
    else:
      new.append(arr[i])
               
  print(new)


nums=input()
arr= nums.split(",")
print(arr)
n=len(arr)
duplicate(arr,n)

 