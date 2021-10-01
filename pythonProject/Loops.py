greetings = "Good Morning"
if greetings == "good morning":
    print("Voila!")
else:
    print("Oh no oh no")

arr=[1,2,3,4,"Gaurav", "div", "Krips"]

for a in arr:
    if (str(a).isalpha()):
        a="gaurav"
        print(a)
    else:
        a="pooja"
        print("nope")
print(arr)

#Here in the above form of for loop we don't have access for the index in the list
#to solve this their is a inbuild function in python to enumerate i.e enumerate();
print(list(enumerate(arr))) #[(0, 1), (1, 2), (2, 3), (3, 4), (4, 'Gaurav'), (5, 'div'), (6, 'Krips')]
# so this will contains index along with the corresponding value for the index

for i,a in enumerate(arr):
    print("Element is {} and it's index is {}".format(a,i))

# Enumerate will return object in (Index,value) form

for i in range(1,6): #So it will iterate from 1 till 5(including 5) and excluding(6)
    #print(i) # 1,2,3,4,5
    print(i,end=' ') # printing in the same line

print("")

#Summation of first 10 numbers
summation=0
for i in range(1,11):
    summation+=i

print(summation)

#If we want some other increment other than 1.

for i in range(1,6,2): #so it will jump two indices at a time
    print(i)

for i in range(2,8,2):
    print(i)

for i in range(10):
    print(i,end='') #0123456789

# while loops

i=0
while i<4:
    print(i)
    i+=1    # i-- and i++ are not working in IBM.

