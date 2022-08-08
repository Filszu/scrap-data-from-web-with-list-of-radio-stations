emails = []
def findEmail():
    el = driver.find_element(By.XPATH, "//*[contains(text(),\'@')]")
    # print(el.text)
    email = el.text
    emails.append(email)       



print("\n-------------------")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("webDriver/chromedriver.exe")
driver.get("https://www.fmradiofree.com/hd-radio-classic-rock")
# driver.get("https://www.ciac.me")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)






page_source = driver.page_source
# print(page_source)



  
# driver.get('https://www.fmradiofree.com/love-songs')



findEmail()         



driver.close()



print(emails)
input("press any key to continue...")

