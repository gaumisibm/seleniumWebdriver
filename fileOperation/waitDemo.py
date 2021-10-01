# when we are manually testing we can see when the previous step is completed and next should be started
# but our automation scripts will not know
# to acheive this there are two wait time 1. Explicit wait and 2. Implicit wait
# and they will pause the test for few seconds using Time class
# Implicit wait time applies to each and every instances of driver object
import time

from selenium import webdriver
options =webdriver.ChromeOptions()
options.headless = True
driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.implicitly_wait(5) # wait until 5 seconds if object is not displayed and suppose if object found in 2 sec then it will not wait further
                            # and will not wait for another 3 sec instead it will resume it's application

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
itemList = driver.find_elements_by_xpath("//h4[@class='product-name']")
print(len(itemList))
list1=[]
for items in itemList:
    list1.append(items.text)
    # print(list1,"hi")
print(list1)
list2=[]
print("\n")
for a in list1:
    print(a,end='')
    list2.append(a.split()[0])
print('\n')
list3=[]
print(list1)
for a in list1:
    list3.append(a.split())

print("list 2 is ",list2)
list4=[]
# print(len(list3))
# for a in list3:
#     if len(a)<=2:
#         continue
#     list4.append(a[2])
#     print(list4)
# print(list4)
# res = [int(sub.split('.')[1]) for sub in test_list]
list4 = [ (sub.split('-'))for sub in list1]
print(list4)
for i,sub in enumerate(list4):
    if len(sub)<2:
        print(i)
        del list4[i]
print(list4)
button = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# button[0].click()
del button[8]
del list2[8]
print(list2)
print(len(button))
print(len(list2))

required = ['Brocolli', 'Carrot', 'Tomato', 'Brinjal', 'Potato']
quantity = [3,5,4,2,3]
list5=[]
for two in list4:
    list5.append(two[1])

print(list5)
list6=[(aub.split(' ')[1])for aub in list5]
# for aub in list

print(list6)
print(len(list6))
# j=0
# for i,a in enumerate(list2):
#     if a in required:
#         for j in range(quantity[j]):
#             button[i].click()
#             time.sleep(2)
#         j=j+1

quan = driver.find_elements_by_xpath("//input[@class='quantity']")
del quan[8]
print(len(quan))
print("List",list2)
j=0
for i,a in enumerate(list2):
    if a in required:
        print(a,i,j)
        time.sleep(4)
        quan[i].clear() # clear methods help to remove the pre existing text and new text can be entered
        # quan[i].send_keys('4')
        quan[i].send_keys(quantity[j])
        time.sleep(2)
        button[i].click()
        j=j+1

#list2 -> name of all the vegetables
# button -> has the list of all button
# list6 -> quantity


