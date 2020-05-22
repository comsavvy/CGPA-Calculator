from cal_gp import G4
cg= G4()

def showPlot(occurence):
    if occurence== "Y" or occurence == "Yes":
        cg.showcountplot()
    else:
        pass

def request(data):
    if data == "Y" or data == "Yes":
        print(cg.showdataframe(True))
    else:
        pass
    
print('\t\tThis Is A Program For Calculating Total CGPA')          
cg.start()
data = input('Do you want to see the DataFrame of your Score: ').capitalize()
request(data)
occurence= input('Do you want to see the number of Instances of your Grades occurence in CountPlot? ').capitalize()
showPlot(occurence)

while True:
    try:    
        con_qu= int(input('''You have come to end of the program. 
To calculate another CGPA press 1, To Quit the program press 0: '''))
        if con_qu == 1:
            cg.start()            
            data = input('Do you want to see the DataFrame of your Score: ').capitalize()
            request(data)
            occurence= input('Do you want to see the number of Instances of your Grades occurence in CountPlot? ').lower()
            showPlot(occurence)
        elif con_qu == 0:
            print('Quit🤞')
            break
        else:
            print('ValueError!')
    except ValueError:
        print('Check the input')                