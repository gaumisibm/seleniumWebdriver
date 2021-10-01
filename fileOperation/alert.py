from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.fullscreen_window()
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()