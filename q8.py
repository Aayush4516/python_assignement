s = input("Enter string")

temp = s.split()

result = [w for w in temp if len(w)<=4]

print(result)

