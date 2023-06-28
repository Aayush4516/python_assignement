array = []
n = int(input("Enter the list size "))


for i in range(0, n):
    temp = int(input())
    array.append(temp)

for x in range(len(array)):
    array[x]=array[x]*array[x]

print(array)