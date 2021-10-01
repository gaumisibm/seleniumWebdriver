import time

from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
driver.fullscreen_window()
driver.find_element_by_id("firstName").send_keys("Honda")
time.sleep(1)
driver.find_element_by_id("lastName").send_keys("America_1")
time.sleep(1)
driver.find_element_by_id("username").send_keys("hondaamerica1testing")
time.sleep(1)
driver.find_element_by_name("Passwd").send_keys("Hondaisgreat1")
time.sleep(1)
driver.find_element_by_name("ConfirmPasswd").send_keys("Hondaisgreat1")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/span').click()
time.sleep(1)