m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))
matrix=[]
store=[]
sm=0
sn=0

for i in range (m):
  a=[]
  for j in range(n):
    el=int(input())
    a.append(el)
    if el==0:
      store.append([i,j])
      sm+=1
      sn+=1


  matrix.append(a)

for i in range(m):
  for j in range(n):
    if [i,j] in store:
      for a in range(n):
        matrix[i][a]=0
      for b in range(m):
        matrix[b][j]=0

print(matrix)
