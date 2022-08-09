
import csv
def save(data=[0,0,0]):
    try:
        with open('generated_files/data.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(["NAME", "EMAIL", "TEL"])
            # writer.writerow(["NAME", "EMAIL", "TEL"])
            
            
            
            writer.writerow(data)
        
        print("Data saved")
    except:
        print("ERROR with saving")
    


def greet():
    print('hello')

def saveEmails(data=[0,0,0]):
    try:
        with open('generated_files/emails.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            
            
            
            writer.writerow(data)
        
        print("Data saved")
    except:
        print("ERROR with saving")
    
def saveSession(data=[0,0,0]):
    try:
        with open('generated_files/zapasData.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            
            
            
            writer.writerow(data)
        
        print("Data saved")
    except:
        print("ERROR with saving")
    
