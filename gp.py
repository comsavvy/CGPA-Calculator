from cal_gp import G4
cg= G4()
print('\t\tThis Is A Program For Calculating Total CGPA')          
cg.cont()
data = input('Do you want to see the DataFrame of your Score: ').capitalize()
cg.showFrame(data)
while True:
    try:    
        con_qu= int(input('''You have come to end of the program. 
To calculate another CGPA press 1, To Quit the program press 0: '''))
        if con_qu == 1:
            cg.cont()
            data
        elif con_qu == 0:
            print('Quit🤞')
            break
        else:
            print('Not allow')
    except ValueError:
        print('Check the input')                