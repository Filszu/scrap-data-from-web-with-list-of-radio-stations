
import csv
def saveToFile(data=[0,0,0],pageNo=None):
    with open('generated_files/data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(["NAME", "EMAIL", "TEL"])
        # writer.writerow(["NAME", "EMAIL", "TEL"])
        
        if pageNo!=None:
            writer.writerow(['---', '---', '---',pageNo])
        
            writer.writerow(data)
        
        

    print("saved")

saveToFile(["Filszu","filip@ciac.me",11111111111], 5)