from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.title)
driver.find_element_by_xpath("//a[text()='Click Here']").click()
handles = driver.window_handles # this will returns all the handle values of opened browser window
# for this case handles will contains (parent handle id, child handle id)
# driver.current_window_handle
driver.switch_to.window(handles[1])
print(driver.title)

