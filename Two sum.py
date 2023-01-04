def sos(n,m,arr):
  if n==0 and m==0:
    return(True)
  elif n!=0 and m==0:
    return(True)
  elif n==0 and m!=0:
    return(False)
  else:
    for i in range(n-1):
      if arr[i]>m:
        continue
      else:
        for j in range (i+1,n):
          if arr[i]+arr[j]==m:
            print(i,j)
            break     

n = int(input("Enter number of elements: "))
arr=[]
print("Enter elements: ")
for i in range (n):
  arr.append(int(input()))
m=int(input("Enter target: "))
sos(n,m,arr)
