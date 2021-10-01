
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
# driver.get("https://uat_user:AHM1020@qa.acuralink.acura.com/")
driver.get("https://tempmailo.com/")
list2 = []
value=driver.find_element_by_id("i-email").get_attribute('value')
with open('C:/Users/KumarGaurav/Desktop/AccountforTest.txt','a') as writer:
    if(value):
        writer.write("Email id - "+value)
        writer.write("      ")
        writer.write("Password -  Hondaisgreat1")
        writer.write('\n')

print(value)
driver.implicitly_wait(20)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
# driver.get("https://myaccount.acura.com/registration")
driver.get("https://uat_user:AHM1020@qa.acuralink.acura.com/")
# driver.save_screenshot('first.png')

driver.find_element_by_xpath("//a[contains(text(),'MY ACCOUNT')]").click()
driver.find_element_by_link_text("Don't have an AcuraLink ID?").click()
driver.find_element_by_id("text1").send_keys(value)
driver.find_element_by_id("btnContinue").click()
driver.close()
driver.switch_to.window(driver.window_handles[0])

wait = WebDriverWait(driver,10)
driver.find_element_by_xpath("//span[text()='Refresh']").click()
driver.find_element_by_xpath("//span[text()='Refresh']").click()
driver.find_element_by_xpath("//span[text()='Refresh']").click()
driver.find_element_by_xpath("//span[text()='Refresh']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '''//div[text()='"AcuraLink" <myacuralinkaccount@email.acura.com>']''')))
driver.find_element_by_xpath('''//div[text()='"AcuraLink" <myacuralinkaccount@email.acura.com>']''').click()
driver.switch_to.frame('fullmessage')

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@target='_blank']")))
driver.find_element_by_xpath("//a[@target='_blank']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id("text-firstName").send_keys("Tamesh")
driver.find_element_by_id("text-lastName").send_keys("raj")
driver.find_element_by_id("text-password").send_keys("Hondaisgreat1")
driver.find_element_by_id("text-password2").send_keys("Hondaisgreat1")
driver.find_element_by_id("btn-create").click()
driver.find_element_by_xpath("//option[@value='In which city were you born? Enter city name only.']").click()
driver.find_element_by_id("text-answer1").send_keys("Bangalore")
driver.find_element_by_xpath("//option[@value='What is the first name of your oldest niece?']").click()
driver.find_element_by_id("text-answer2").send_keys("Priyanka")
driver.find_element_by_id("btn-create").click()

# LOGIN

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
# driver.get("https://myaccount.acura.com/registration")
# driver.get("https://qa.hondalink.honda.com/#/signin")
driver.get("https://acuralink.acura.com/#/signin")
driver.find_element_by_id("username").send_keys(value)
driver.find_element_by_id("password").send_keys("Hondaisgreat1")
driver.find_element_by_id("signin_button").click()
signout= driver.find_element_by_xpath("//a[text()='SIGN OUT']").text
assert "SIGN OUT" == signout
print("Login Successfully")
driver.find_element_by_xpath("//a[text()='SIGN OUT']").click()
print("Sign out Success")
print("Everythings is completed for Acuralink in qa")


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get("https://myaccount.acura.com/forgotpassword/default.aspx?cc=US&lc=en&app=ct&pgm=HL&ru=https%3A%2F%2Facuralink.acura.com&tgt=mobile")
#Forgot Password Implementation

# driver.switch_to.window((driver.window_handles[0]))
# driver.get("https://qa.hondalink.honda.com/")
# driver.switch_to.alert.send_keys("uat_userinIndia")