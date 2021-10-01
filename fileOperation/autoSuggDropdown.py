import time

from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.fullscreen_window()
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")
# for country in countries:
#     print(country.text())
# I think we cannot write driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a").text
# because it will have many web tags and we cannot put operation of text in those tags
# instead we can extract one web elements and then we can apply text operation
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

# Here when we'll try to get that if India is being selected or not, then we can't do it via normal way
# as the DOM is not being updated instead we have to do it by following ways

print(driver.find_element_by_id("autosuggest").text) # it will not work because the DOM will not work

assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India" # DOM has something called Value which will
# update every value everytime it is being called


