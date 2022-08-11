import uniq_and_validated as uv
import csv


# uv.start(tab)



def saveUniqEmails(data):
    try:
        with open('generated_files/uniq_emails.csv', 'w', newline='') as file:
            # writer = csv.writer(file)
            
            
            
            # writer.writerow(data)
            file.write(data)
        
        print("Data saved")
    except:
        print("ERROR with saving")


def readFile():
    try:
        f = open("generated_files/emails.csv", "r")
        # print(f.read())
        data = uv.start(f.read())

        
        saveUniqEmails(data)
    except:
        print("error with reading")


readFile()

input("...")