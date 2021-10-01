print(2+3)
if 1>2:
    print("yes")
else:
    print("No")

# It is very bad for me to again start learning python

b,c,d=4, 5.6, "Gaurav Mishra"
print(d,b,c)

st= "Faltu ka kaam"

for i in range(5):
    st=st+' '+str(i);

print(st)

name="Gaurav Mishra"
age= 25
print("{} age is  {}".format(name,age))

#List in python

values = [1, 2, 3, 4, "Gaurav", "Mishra"]
for a in values:
    print(a)
print(values[-1]) #Start with the last index of list
print(values[1:3]) # [2, 3]

#Inserting in between the list let say if I have to insert at position number 5
values.insert(3,"Krips and Div")
print(values) #[1, 2, 3, 'Krips and Div', 4, 'Gaurav', 'Mishra']
values.append("waste") #it will just add waste to the last index of the list

values.insert(3,"krips") # This will only add additional value to the list at index 3 but if you have to change
#content inside the list
print(values)  # [1, 2, 3, 'krips', 'Krips and Div', 4, 'Gaurav', 'Mishra', 'waste']

#To update some index value in the list we can use assignment operator
#Let's say if you want to change index 4 value to Div
values[4]="Div"
print(values) # [1, 2, 3, 'krips', 'Div', 4, 'Gaurav', 'Mishra', 'waste']

# DELETING One of the list values

del values[0]
print(values) #[2, 3, 'krips', 'Div', 4, 'Gaurav', 'Mishra', 'waste']

#List and tuple does the same things the only difference is that tuple is immutable i.e. it cannot be changed

# Declaring tuples

tup = (1,2,3,4,5,"Div")
print(tup) #(1, 2, 3, 4, 5, 'Div')

# As tuple is immutable we'll now see if it is so or not
print(tup[0])
#tup[0]=0
print(tup) # TypeError: 'tuple' object does not support item assignment
# As you seen above that the tuples is not mutable i.e. immutable

# Dictionary{}
# A dictionary is an unordered sequence of data of key-value pair form.

Dic = {5:"Gaurav",4:"Krips",3:"Div"}
print(Dic) #{1: 'Gaurav', 4: 'Krips', 3: 'Div'}
print(Dic[5]) # In dictionary Index doesn't know instead of index you have to give key
#let's say if you want to retrive for key =5 its corresponding value then write as Dic[5] not Dic[0] index X


# How to create Dictionaries at runtime and add data into it

dic={} # create a empty dictionary
# adding data into it
dic["Firstname"]="Gaurav"
dic["Age"]= 21
print(dic)