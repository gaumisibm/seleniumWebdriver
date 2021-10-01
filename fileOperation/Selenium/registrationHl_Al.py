import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

myprofile = webdriver.FirefoxProfile()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
myprofile.set_preference("general.useragent.override", user_agent)
myprofile.update_preferences()
# options = webdriver.FirefoxOptions()
# options.headless = True # Headless mode is basically doing the operation without opening the browser, which will consume CPU usage and making process faster
# driver = webdriver.Firefox(firefox_profile=myprofile,executable_path="D:/AutomationScripts/selePyApplication/geckodriver.exe", options=options)
driver = webdriver.Firefox(firefox_profile=myprofile,executable_path="D:/AutomationScripts/selePyApplication/geckodriver.exe")
driver.get("https://temp-mail.org/en/")

# profile = webdriver.FirefoxProfile()
# profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36")
# driver = webdriver.Firefox(profile)
# driver.fullscreen_window()
time.sleep(4)



# cap=DesiredCapabilities().FIREFOX
# cap["marionette"]= True
# DesiredCapabilities capabilities = DesiredCapabilities.firefox();
# capabilities.setCapability("marionette", 'true');
# webdriver driver = new FirefoxDriver(capabilities);

capabilities = {
		"build" : "your build name",
		"name" : "your test name",
		"platform" : "Windows 10",
		"browserName" : "Chrome",
		"version" : "94.0"
	}

# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
# print(driver.find_element_by_xpath("//input[@id='mail']").get_attribute('name'))
tempmailId = driver.find_element_by_xpath("//input[@id='mail']").get_attribute('value')
print(tempmailId)
print(driver.current_window_handle)
# driver.switch_to.window("https://myaccount.acura.com/registration")
# driver.get("https://myaccount.acura.com/registration")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://myaccount.acura.com/registration")
driver.find_element_by_id("text1").send_keys(tempmailId)
driver.find_element_by_id("btnContinue").click()
confirm = driver.find_element_by_xpath("//p[@style='text-align:center;']").text
print(confirm)
assert "receive" in confirm
# driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.current_window_handle)
# profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36")
# driver.find_element_by_xpath("//span[@title='AcuraLink ']").click()
driver.find_element_by_id("click-to-delete").click()
# driver.back()
# print(driver.current_url)