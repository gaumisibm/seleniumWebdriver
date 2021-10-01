# before selenium was invented at that time you can access html element using DOM document
# The HTML DOM document object is the owner of all the other objects in you web page
# selenium will also help you to execute js DOM as well
# let suppose if you entered some text on the web after loading then you won't we able to access using
# .text method

from selenium import webdriver


driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Kumar Gaurav")
# driver.execute_script() # this execute_scripts will allow you to run java script or it can be also thinked as selenium is giving access to javascript to execute the commands
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script("return document.getElementsByName('name')[0].value"))
# using the above line 13 and 14 we'll get the same output one 13 line is handled via selenium webdriver
# and line number 14 is handled via javascript executor


# Selenium by default do not have ability to scroll down
# In that case we'll use javascript to handle scroll down options
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')


