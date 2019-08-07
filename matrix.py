#Arrange the 2D matrix
r=int(input("\nEnter the Row: "))
c=int(input("\nEnter the Column: "))

mat=[]
sum1=[]


for i in range(r):
    mat.append([0]*c)

print("\nEnter the value:\n")
for i in range(len(mat)):
    for j in range(len(mat[0])):
                   mat[i][j]=int(input())

for i in range(len(mat)):
    add=0
    for j in range(len(mat[0])):
                   print(mat[i][j],end=' ')
                   add=add+mat[i][j]
    sum1.append(add)
    print("\n")


