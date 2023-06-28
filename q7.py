s1 = input("Enter string ")

consonants = [s for s in s1 if s != 'a' and s!='e' and s!='i' and s!='o' and s!='u' and s!='A' and s!='E' and s!='I' and s!='O' and s!='U']

s2=''
for x in consonants:
    s2=s2+x
 
print(consonants)
print(s2)