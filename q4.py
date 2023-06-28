l1 = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    item = int(input())
    l1.append(item)

print("User list is ", l1)

k= int(input("Enter target sum "))

dict1={}

for i in range(len(l1)):
 if k-l1[i] in dict1:
    print(l1[i],k-l1[i])
    break
 else:
    dict1[l1[i]]=i



 