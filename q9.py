words = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    item = input("Enter Word ")
    words.append(item)

print("User list is ", words)

dict1={}

for x in words:
 dict1={'name':x,
        'size':len(x)}
 
 print(dict1)