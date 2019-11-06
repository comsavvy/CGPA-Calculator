import cal_gp as cg
print('\t\tThis Is A Program For cgculating Total cgPA')          
cg.cont()
while True:
    try:    
        con_qu= int(input('''You have come to end of the program. 
To calculate another CGPA press 1, To Quit the program press 0: '''))
        if con_qu is 1:
            cg.cont()
        elif con_qu is 0:
            print('Quit🤞')
            break
        else:
            print('Not allow')
    except ValueError:
        print('Check the input')                