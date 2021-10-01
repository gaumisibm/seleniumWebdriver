# Instead of writing file = open('text.txt') and then closing with file.close(). We can write a single
# line to do both these task.

# read the lines into list objective 1
# reverse the list and then write into the file objective 2

with open('C:/Users/KumarGaurav/Desktop/seleText.txt','r') as reader:
    #print(reader.read())
    list8 = reader.readlines()
    #for a in list8:
    #   print(a)
    with open('C:/Users/KumarGaurav/Desktop/seleText.txt','w') as writer:
        for a in reversed(list8):
            writer.write(a)
    #print(reader.read())


