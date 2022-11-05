from cal_gp import G4
cg= G4()

"""
The main program starts in this module, which comprises all the usable functions for the program to work perfectly. 
All the structure for the order of execution were all compiled here.

"""

def showPlot(occurence):
    if occurence.startswith('y'):
        try:
            cg.showcountplot()
        except Exception as e:
            print(f"Error occur because: {e}")
    else:
        pass


def request(data):
    if data.startswith('y'):
        print(cg.showdataframe(True))
    else:
        pass


def printingTask():
    data = input('Do you want to see the DataFrame of your Score: ').lower()
    request(data)
    occurrence= input('Do you want to see the number of Instances of your Grades occurence in CountPlot? ').lower()
    showPlot(occurrence)


if __name__ == "__main__":
    print('\t\tThis Is A Program For Calculating Total CGPA')
    cg.start()
    printingTask()
    while True:
        try:
            con_qu= int(input('''You have come to end of the program. 
To calculate another CGPA press 1, To Quit the program press 0: '''))
            if con_qu == 1:
                cg.start()
                printingTask()
            elif con_qu == 0:
                print('Quit🤞')
                break
        except ValueError:
            print('Check the input')