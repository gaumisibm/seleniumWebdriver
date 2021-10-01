import urllib
import OCR
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:/Automation Testing/chromedriver.exe")
driver.get("https://myaccount.honda.com/forgotpassword/default.aspx?cc=US&lc=en&app=ct&pgm=HL&ru=https%3A%2F%2Fhondalink.honda.com&tgt=mobile")

while driver.current_url != "https://myaccount.honda.com/forgotpassword/forgotpassword-questions":
    driver.find_element_by_id("text-firstName").send_keys("biqocygy@acrossgracealley.com")
    captchaEle = driver.find_element_by_id("CaptchaImage")
    captchaEle.screenshot('C:/Users/KumarGaurav/Desktop/screenTest/captcha12.png')
    str1, a = OCR.ocrconvertor()
    time.sleep(5)
    print('{} {}'.format(str1, a))
    driver.find_element_by_id("CaptchaInputText").send_keys(str1)
    driver.find_element_by_id("btn-next").click()


driver.find_element_by_id("AnswerOne").send_keys("Bangalore")
driver.find_element_by_id("AnswerTwo").send_keys("Priyanka")
driver.find_element_by_id("btn-next").click()
driver.find_element_by_id("text-password").send_keys("Hondaisgreat2022")
driver.find_element_by_id("text-password2").send_keys("Hondaisgreat2022")
driver.find_element_by_id("btn-next").click()
text1 = driver.find_element_by_id("titleDiv").text
print(text1)
assert text1 == "CONFIRMATION"
# print(src)

# urllib.urlretrive(src,"captcha1.png")
# actions = ActionChains(driver)
# actions.context_click(driver.find_element_by_id("CaptchaImage")).perform()

