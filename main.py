from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# WAIT WEB
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


emails = []
radioStations = [] #name #email #tel_nr
notFoundEmails = 0
MAIN_PAGE_URL = "https://www.fmradiofree.com/"
currPage =1
currPageUrlTemplate="https://www.fmradiofree.com/?page="
resultsperPage = 60


driver = webdriver.Chrome("webDriver/chromedriver.exe")
driver.implicitly_wait(30)

# example url https://www.fmradiofree.com/hawaiian-music-live



def findEmail():

    print("searching email...")
    el = driver.find_element(By.XPATH, "//*[contains(text(),\'@')]")
    # print(el.text)
    email = el.text
    if(email!=""):
        emails.append(email)  
        print(f"Email founded {email}")
    else:
        global notFoundEmails
        notFoundEmails+=1 

  

def setURL(url):
    driver.get(url)

allRadioBoxes =""
def newPage():
    global allRadioBoxes

    try:
        allRadioBoxes = driver.find_elements(By.CLASS_NAME, "mdc-grid-tile__secondary")
    except:
        time.sleep(1)
        newPage()

    # mdc-grid-tile__primary mdc-elevation--z4

currId = 1
searchingActive = True
notFoundTimes = 0


def findRadioBox():
    # //radio_list_li_12
    global currId, allRadioBoxes
    elId=f"radio number {currId}"
    currId+=1 
    
    try:
        
        # radioSlectBox = driver.find_element(By.ID, elId)
        # radioSlectBox.click()
        
        # radioSlectBox = allRadioBoxes[currId]
        radioSlectBox = driver.find_elements(By.CLASS_NAME, "mdc-grid-tile")[currId]
        print(elId + "founded")
        radioSlectBox.click()
        time.sleep(1)

        findEmail()
    except:
        print(f"{elId}not found")
        global searchingActive
        global notFoundTimes
        notFoundTimes+=1

        if(notFoundTimes>150):
            searchingActive = False

    # global currId
    

def nextPage():
    global currPage
    currPage+=1
    print(f"\n--------NEXT PAGE-----{currPage}--------")
    print(emails)
    global currId
    currId=0



print("\n-------------------")


driver.get(MAIN_PAGE_URL)

while(searchingActive==True):

    if(currId>resultsperPage):
        nextPage()
        
        
    setURL(f"{currPageUrlTemplate}{currPage}")
    # time.sleep(1)
    # newPage()
    # myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))

    # myElem = WebDriverWait(Driver, 3).until(EC.presence_of_element_located((By.TAG_NAME,'body')))
    time.sleep(1)
    findRadioBox()
    time.sleep(1)
    

# page_source = driver.page_source
# print(page_source)


# findEmail()         



# driver.close()



print(emails)
input("press any key to continue...")

