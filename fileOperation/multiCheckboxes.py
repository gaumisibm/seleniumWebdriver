from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.fullscreen_window()
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
st="option1"
for checkbox in checkboxes:
    if st == checkbox.get_attribute("value"):
        checkbox.click()
        assert checkbox.is_selected()

radio = driver.find_elements_by_name("radioButton")
radio[2].click()



