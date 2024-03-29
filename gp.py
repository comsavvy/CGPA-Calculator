#!/usr/bin/env python

from cal_gp import G4
import pandas as pd


"""
The main program starts in this module, which comprises all the usable functions for the program to work perfectly. 
All the structure for the order of execution were all compiled here.

"""


class Flow:
    def __init__(self):
        self.cg = G4()

    def showPlot(self, occurence):
        if occurence.startswith("y"):
            try:
                self.cg.showcountplot()
            except Exception as e:
                print(f"Error occur because: {e}")
        else:
            pass

    def request(self, data):
        if data.startswith("y"):
            print(self.cg.showdataframe(True))
        else:
            pass

    def printingTask(self):
        data = input("Do you want to see the DataFrame of your Score: ").lower()
        self.request(data)
        occurrence = input(
            "Do you want to see the number of Instances of your Grades occurence in CountPlot? "
        ).lower()
        self.showPlot(occurrence)

    def execute(self):
        self.cg.start()
        self.printingTask()

    def executeRepeat(self):
        self.execute()
        while True:
            try:
                con_qu = int(
                    input(
                        """You have come to end of the program.
To calculate another CGPA press 1, To Quit the program press 0: """
                    )
                )
                if con_qu == 1:
                    self.cg.start()
                    self.printingTask()
                elif con_qu == 0:
                    print("Quit🤞")
                    break
            except ValueError:
                print("Check the input")


class Users:
    def __init__(self):
        self.names = {}

    def differentUsers(self):
        next = True
        while next:
            user = input("Enter username: ").title()
            flow = Flow()
            flow.execute()
            self.names[user] = flow.cg.gp
            next = input("Next user [y/n]: ").lower().startswith("y")

    def usersGP(self):
        return pd.DataFrame(self.names.items(), columns=["Username", "Gp"])


def main():
    print("\t\tThis Is A Program For Calculating Total CGPA")
    users = Users()
    users.differentUsers()
    print(users.usersGP())


if __name__ == "__main__":
    main()
