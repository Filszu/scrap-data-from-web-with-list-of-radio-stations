import re
validatedEmails= []

def remove(x):
  return list(dict.fromkeys(x))


# conver to array
def splitBy(x):
    # splitedList = x.split(",")
    splitedList =x.splitlines()
    return splitedList

def emailValidate(mail):
  # pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
  pat = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
  if re.match(pat,mail):
      # print (f"validated: {mail}")
      return True
  # print(f"invalid mail: {mail}")
  return False

def checkAllEmails(mailsAray):
  for mail in mailsAray:
    
      if ", " in mail:
        mail = mail[:-2]
      elif "," in mail:
        mail = mail[:-1]
      # print(f"mail to check: {mail}")

      if emailValidate(mail) == True:
        global validatedEmails
        validatedEmails.append(mail)
      
    

def start(emailList):
  global validatedEmails
  # emailList = '''
  
  # '''
  emailList = splitBy(emailList)
  mylist = remove(emailList)
  print(mylist)

  checkAllEmails(mylist)
  # print("\n")
  # print(validatedEmails)
  # validatedEmails = remove(validatedEmails) 

  print(validatedEmails)
  print('\n\n\n---------')

  # #convertto string
  stringToReturn =", \n".join(validatedEmails)
  print(stringToReturn)
  return stringToReturn




  


