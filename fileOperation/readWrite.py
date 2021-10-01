file = open('demoText.txt')

#print(file.read())
#file.close()
print(file.read(5)) # read n numbers of problems
file.close()
res=file.read()

file.readline() # This will read a single linen
for ra in res:
    print(ra)
    print("HI")

file.close()