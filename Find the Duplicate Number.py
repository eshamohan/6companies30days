# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
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
  



