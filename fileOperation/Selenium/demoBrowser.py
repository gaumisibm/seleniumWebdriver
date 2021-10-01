from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://gd.mail.ibm.com/verse")
driver.fullscreen_window()
print(driver.title) #It will print title of the web page
print(driver.current_url) # It will get you the current link of the webpage you are in
                            # Many a times hacker will re direct you to a different web page
#driver.close() # It will only close only the current working window
# driver.quit() # It will close all the window

driver.get("https://hondaweb.com/hra_jira/browse/CVPSO-16149")
driver.back()
driver.refresh()