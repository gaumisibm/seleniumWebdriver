from selenium import webdriver
from selenium.webdriver import ActionChains

driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
actions = ActionChains(driver) # create a object for ActionChains class and using that object we will do various operation
actions.move_to_element(driver.find_element_by_id("mousehover")).perform()
actions.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()
# after only you will assign perform to action it will work

# Now we'll perform double click
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
actions = ActionChains(driver)
# If you want to right click then there is an method called context_click
actions.context_click(driver.find_element_by_id("double-click")).perform()
actions.double_click(driver.find_element_by_id("double-click")).perform()

alerts = driver.switch_to.alert
text = alerts.text
assert "You double clicked me!!!, You got to be kidding me" == text
alerts.accept()