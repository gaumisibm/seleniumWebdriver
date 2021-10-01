from selenium import webdriver

driver=webdriver.Firefox(executable_path="D:/AutomationScripts/selePyApplication/geckodriver.exe")
#driver=webdriver.Edge(executable_path="D:/AutomationScripts/selePyApplication/msedgedriver.exe")

driver.get("https://www.flipkart.com/")
driver.fullscreen_window()
#driver.find_element_by_class_name("_2IX_2- VJZDxU").send_keys("7903764607")
#driver.find_elements_by_class_name("_2IX_2- VJZDxU")
driver.find_element_by_css_selector("input[class='_2IX_2- VJZDxU']").send_keys("7903764607")
driver.find_element_by_xpath("//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys("9905848369")
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
# Webdriver will have many locators
# Id
# Name
# Xpath
#Customized Xpath Syntax
# //tagname[@attribute=value]
# //button[@class='_2KpZ6l _2HKlqd _3AWRsL']
# Xpath Regex //(*/tagname)[contains(@attribute,'value')]  ex. //*[contains(@class,'alert-success')]

# CSS
# Customized CSS Syntax
# tagname[attribute='value'] --- tagname is optional
# input[class='_2IX_2- VJZDxU']
# CSS Regex [attribute*='value'] ex. [class*='alert-success']

# Css selector are generally fast in locating various element
#Generating Css from ID
#tagname#ID-- Tagname is optional

#Generating Css from className
#tagname.className (make sure there are no spaces in class names)



#
# className
# linkText

# Generating Xpath based on the text
//tagname[text()='xxx'] again tagname is optional

