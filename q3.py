
import pickle
 

data = [
    {'Hospital':'Fortis','Address':'Sector 62 Noida'},{'Hospital': 'Max','Address':'Sector 112 Noida' },{'Hospital':'Apollo','Address':'Sector 18 Noida'}],
    


with open('datafile.txt', 'wb') as fh:
   pickle.dump(data, fh)

temp = open ("datafile.txt", "rb")
emp = pickle.load(temp)
print(emp)
