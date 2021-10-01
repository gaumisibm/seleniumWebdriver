from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
# iframes, frameset, frame when we have some thing inside these tags then our general locator might not work at that place
driver.switch_to.frame("mce_0_ifr") # frame id or frame name or index value.
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("Right now I'm able to edit the text")
# Now suppose if we want to work on the HTML page then we have to switch from frame to html control
driver.switch_to.default_content()
print(driver.find_element_by_tag_name('h3').text)

