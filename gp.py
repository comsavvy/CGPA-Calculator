from cal_gp import G4
cg= G4()

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

if __name__ == "__main__":
    print('\t\tThis Is A Program For Calculating Total CGPA')
    cg.start()
    data = input('Do you want to see the DataFrame of your Score: ').lower()
    request(data)
    occurence= input('Do you want to see the number of Instances of your Grades occurence in CountPlot? ').lower()
    showPlot(occurence)
    while True:
        try:
            con_qu= int(input('''You have come to end of the program. 
To calculate another CGPA press 1, To Quit the program press 0: '''))
            if con_qu == 1:
                cg.start()
                data = input('Do you want to see the DataFrame of your Score: ').lower()
                request(data)
                occurence= input('Do you want to see the number of Instances of your Grades occurence in CountPlot? ').lower()
                showPlot(occurence)
            elif con_qu == 0:
                print('Quit🤞')
                break
        except ValueError:
            print('Check the input')