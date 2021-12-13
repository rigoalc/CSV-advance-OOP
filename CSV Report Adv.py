# Rodrigo Alcover
# 4/12/2021
# CIS-216-12292 
# Python Programming
# Assignment: CSV Report OOP


from collections import Counter
from typing import List

class CSVReport:    
    def __init__(self):
        self.reading = 'read_csv' 
    def run(self):       
        header = True  
        year_data = {}
        print("Year |  Min |  Max |  Avg") #header 
        print("==== | ==== | ==== | ====")
        with open('MIGRNDRA.csv', 'r') as my_file:# Open file for reading with open(path)
            for line in my_file.readlines():#search for lines 
                line = line.strip() #   
                if not line: 
                    continue
                if header:#search for header
                    header = False#ignore the header
                    continue
                values = line.split(',')#How to read the values separated by a coma
                month = int(values[0])#read and store values
                day = int(values[1])
                year = int(values[2])
                temp = float(values[3])
                if year not in year_data:#load year 
                    year_data[year] = []# add year to the collection
                year_data[year].append(temp) #append the dictionary    
      

                continue        
           
        for year, temps in year_data.items():#read year and temps
         
            average = sum (temps) / len(temps)#calculate average
            minimun = min (temps) #calulate minimun
            maximun = max (temps)#calculate max
        
                
            print("{} | {:=4} | {:>.1f} | {:>.1f}".format (year, minimun, maximun, average))#Print the results
            
class Monthly:    
    def __init__(self):
        self.reading = 'read_csv' 
    def run(self, monthinput):       
        header = True  
        year_data = {}
        print("Year |  Min |  Max |  Avg") #header 
        print("==== | ==== | ==== | ====")
        with open('MIGRNDRA.csv', 'r') as my_file:# Open file for reading with open(path)
            for line in my_file.readlines():#search for lines 
                line = line.strip() #   
                if not line: 
                    continue
                if header:#search for header
                    header = False#ignore the header
                    continue
                values = line.split(',')#How to read the values separated by a coma
                month = int(values[0])#read and store values
                day = int(values[1])
                year = int(values[2])
                temp = float(values[3])
                if monthinput != month:
                    continue
                if year not in year_data:#load year 
                    year_data[year] = []# add year to the collection
                year_data[year].append(temp) #append the dictionary    
      

                continue        
           
        for year, temps in year_data.items():#read year and temps
         
            average = sum (temps) / len(temps)#calculate average
            minimun = min (temps) #calulate minimun
            maximun = max (temps)#calculate max
        
                
            print("{} | {:=4} | {:>.1f} | {:>.1f}".format (year, minimun, maximun, average))#Print the results
#How to read the values
menu = (" 1) See breakdown by year","2) See breakdown by year for a single month","3) Quit")
        
print(menu)

userinput = input("Please enter 1, 2, or 3.")
userinput = int(userinput)

if userinput == 1:  
             
    my_csv_instance = CSVReport()
    my_csv_instance.run()
    
elif userinput == 2:
    
    monthinput = input("Please choose the month (1-12):")
    monthinput = int(monthinput)
     
    my_csv_instance = Monthly()
    my_csv_instance.run(monthinput)
    
    

elif userinput == 3:
    print("Good Bye")
    
    
        
        


#The total development time is 3 hs.


#This program reads the data from a list of temperature data (in Fahrenheit) for Grand Rapids, MI from 1995 until 2020. 
#The program will organize, calculate and print the average, min, max temperature by year, or month.
#The user will select " 1) See breakdown by year","2) See breakdown by year for a single month","3) Quit"
