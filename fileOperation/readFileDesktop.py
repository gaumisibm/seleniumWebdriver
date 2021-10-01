file = open('C:/Users/KumarGaurav/Desktop/notes.txt')
#print(file.read())
#file.read()
#lines=file.readline()
#while lines!="":
#    print(lines)
 #   lines=file.readline()

# the above while loop will print lines one by one and it will end when it will find empty line

list1= file.readlines() # it will read all the one by one and store it into a list
for a in list1:
    print(a)