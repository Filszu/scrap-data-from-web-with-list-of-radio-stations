from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from os import system

# WAIT WEB
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import saveToFile
import config


emails = []
radioStations_session = [] #name #email #tel_nr  --------get in this session
radioStations_page = [] #per 1 page
notFoundEmails = 0
# to config
currPage=None
currPageUrlTemplate=None
# ------
resultsperPage = 60




# example url https://www.fmradiofree.com/hawaiian-music-live
def inputStartDomain():
    global currPageUrlTemplate

    # "https://www.fmradiofree.com/?page="
    domains = config.getWebsites()

    print("\navaible domains: ")#\033[92m'+
    i=0
    for x in domains:   

        print(f"{i} : {x}")
        i+=1
    
    selectedDomain = ""
    try:
        num = int(input("gimmie domain index: "))
        selectedDomain = domains[num]
    except:
        selectedDomain=domains[0]
        print("u are fucking stupid")

    #-------
    title = "seraching web:: "+selectedDomain+"  [Filszu searching emails engine]"
    
    system("title " + title)
    currPageUrlTemplate = f"{selectedDomain}?page="
    #--------

    print(f'''=============================
    STARTING AT:
    {currPageUrlTemplate}\n
    =============================''')
    # \033[0m'

    
    

def inputStartingPageNum():
    global currPage
    try:

        currPage = int(input("gimmie starting page index: "))
    except:
        currPage=0
        print("u are fucking stupid")

if currPageUrlTemplate==None:
    inputStartDomain()
if currPage==None:
    inputStartingPageNum()




def findEmail():

    print("searching email...")
    el = driver.find_element(By.XPATH, "//*[contains(text(),\'@')]")
    # print(el.text)
    email = el.text
    if(email!=""):
        emails.append(email)  
        print(f"Email founded {email}")
        saveToFile.saveEmails([email," "])
        return email
    else:
        global notFoundEmails
        notFoundEmails+=1 

  

def setURL(url):
    driver.get(url)

def getStationName():
    try:
        el = driver.find_element(By.CLASS_NAME, "mdc-typography--display1")
        # print(el.text)
        return el.text
    except:
        # print("no name")
        return None

   

def getData(): # get radio station data
    data = [] #name #email #tel_nr
    email = findEmail()
    


    if(email!="" and email!=None):
        # data.append([name,])
        staionName = getStationName()

        data = [staionName, email]

        global radioStations_page, radioStations_session

        saveToFile.save(data)
        radioStations_page.append(data)
        radioStations_session.append(data)
    


def saveDataToFile_main(): #adding by 1 web
    global radioStations_page
    saveToFile.save(radioStations_page)
    print("saved to main file")
    
    radioStations_page.clear()

def saveToFile_session():
    saveToFile.saveSession(radioStations_session)
    print("saved session")

currId = 1
searchingActive = True
notFoundTimes = 0


def findRadioBox():
    # //radio_list_li_12
    global currId
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

        getData()
        # findEmail()
    except:
        print(f"{elId}not found")
        global searchingActive
        global notFoundTimes
        notFoundTimes+=1

        if(notFoundTimes>15000):
            searchingActive = False

    # global currId
    

def nextPage():
    global currPage
    currPage+=1
    print(f"\n--------NEXT PAGE-----{currPage}--------")
    print(emails)
    # saveToFile.saveEmails(emails)
    print("\n----\nThis page")
    # saveToFile.save(radioStations_page)
    # print(radioStations_page)
    # saveDataToFile_main()
    print("]\n\n***************All")
    print(radioStations_session)
    saveToFile_session()
    
    global currId
    currId=0



print("\n-------------------")

driver = webdriver.Chrome("webDriver/chromedriver.exe")
driver.implicitly_wait(30)
driver.get(currPageUrlTemplate)

while(searchingActive==True):

    try:
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
    except:
        continue
    

# page_source = driver.page_source
# print(page_source)


# findEmail()         



# driver.close()



print(emails)
print(f"\n\nENDED at: {currPage}")
input("press any key to continue...")

