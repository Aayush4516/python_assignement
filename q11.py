array = []
n = int(input("Enter the list size "))


for i in range(0, n):
    temp = int(input())
    array.append(temp)

target = int(input("Enter the integer "))

k=0

for i in range(0,n):
    if(array[i]!=target):
     array[k]=array[i]
     k=k+1

for i in range (k,n):
   array[i]=target

print(array)