itemsInCart=0
#2 items will be added in the cart

if itemsInCart !=2:
    pass
    #raise Exception("2 items should have added into the cart but it is not")

#assertion in an another way of checking if the conditions meet
# assertion will break the code execution if it receives false conditions

assert(itemsInCart==0)


# If we don't want to fail our test execution and upon error also it should execute then (Try , catch )
# comes into the picture

#try:
    # some logic

#catch:(Instead of catch in python we have except)
    # handle error

try:
    with open('C:/Users/KumarGaurav/Desktop/selemonText.txt', 'r') as reader: # no such file exist
        reader.read()
except:
    print("failure occur in try block ")

# now the quesition arises where we can use this try except in our Automation

# suppose you landed on some page on websites and sometimes pop up will come and sometimes it won't come
# In this scenario you will write logic to handle pop up in try and if it won't come the except block
# will execute



#here instead of printing customized string in except block if we want to catch that exception and then
# print it can be done by catching the exception in except block as
try:
    with open('C:/Users/KumarGaurav/Desktop/selemonText.txt', 'r') as reader:  # no such file exist
        reader.read()
except Exception as e:
    print("failure occur in try block {}".format(e))

finally:
    print("This block will always execute irrespective of error catched in try block or not")
    #In automation finally is generally used whenever we have setted up the data and we want to be cleaned
    #after we have used the data 