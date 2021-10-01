# For most of the Api's for dropdown in selenium would be select tag which is used to select static options
# select class provide the methods to handle the options in dropdown
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.fullscreen_window()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1")) # we are creating obj of select class

dropdown.select_by_visible_text("Male")# using these two methods any one of them can be selected
dropdown.select_by_index(1)
#dropdown.select_by_value() # if there is any options present inside the tags
WebDriverWait(driver,10000)
#driver.close()
driver.find_element_by_xpath("//input[@value='Submit']").click()
messsage=driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

print(messsage)

assert "Success" in message
#Important note this select class can be only used if there is tag with select
#  if there is any other tag such as div,input then you won't be able to use this


# Handling Auto suggestive Dynamic dropdown
