"""
This module can be used to calculate the total CGPA of a student per each semester
"""
# Importing the necessary Libraries to use  
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class G4:
    """
    This contains alot of fuctions such as:
    o _advice
    o _Score
    o start (This is where other methods are executed)
    o _dataFrame(This will create the DataFrame of all the data you've inputted)    
    o showdataframe (This allows you to see the DataFrame of the data)
    
    Out of all the listed functions, those that're mearnt to be call are:
    - start
    - Showdataframe
    _ Showcountplot
    
    """
    def __init__(self):
        self.holder= {'Grade': [],
             'GradePoint': [],
             'Unit': []}
    def _advice(self, gp):
        """
        This is going to return Advice on the performance of the Student
        
        """
        if gp >= 4.5:
            print('Weldone, You Are In First Class 👍')
        elif gp >= 3.5:
            print('Work Hard, You Are In Second Class Upper')
        elif gp >= 2.4:
            print('Nothing is impossible, You are in Second Class Lower')
        elif gp >= 2.39:
            print('Work Hard, You are in Third Class')
        else:
            print('Certificate of attendance')

    def _score(self, total_unit, total_courses):
        """
        You don't need to call this function, it a special method to be call only 
        by `Start' method
        
        """
        result= 0
        course= 0
        unit_counter=0
        increment= 1
        if total_unit != 0:
            try:
                while increment <= total_courses:
                    grade= (input(f"Grade_{increment}: ").upper())
                    self.holder['Grade'].append(grade)
                    unit= int(input(f"Course_{increment} unit: "))
                    self.holder['Unit'].append(unit)
                    print("\n")
                    if grade == 'A':
                        point= 5
                        self.holder['GradePoint'].append(point)
                        course= point * unit
                    elif grade == 'B':
                        point= 4
                        self.holder['GradePoint'].append(point)
                        course= point * unit
                    elif grade == 'C':
                        point= 3
                        self.holder['GradePoint'].append(point)
                        course= point * unit 
                    elif grade == 'D':
                        point= 2
                        self.holder['GradePoint'].append(point)
                        course= point * unit
                    elif grade == 'E':
                        point= 1
                        self.holder['GradePoint'].append(point)
                        course= point * unit
                    elif grade == 'F':
                        point= 0
                        self.holder['GradePoint'].append(point)
                        course= point
                    else:
                        print('Invalid Grade')
                        break
                    increment+= 1  
                    unit_counter += unit
                    result += course
                if total_unit == unit_counter:
                    gp = result / total_unit
                    print(f"Grade: {round(gp, 3)}")
                    self._advice(gp)    
                else:
                    print('Unit not balance')
            except ValueError:
                print('Wrong input!')
            except UnboundLocalError:
                print('Check Input')
            except ZeroDivisionError:
                print('Undefine')
        else:
            print('Total Unit can not be zero!')

    def start(self):
        try:
            total_unit= int(input("Total Unit: "))
            total_courses= int(input("Total Courses: "))
            print("\n")
            self._score(total_unit, total_courses)
        except ValueError:
            print('Value Error')
            
    def _dataFrame(self):
        """
        You don't need to call this function it going to generate dataframe
        for showdataframe method
        """
        df= pd.DataFrame(self.holder)
        return df
    
    def showdataframe(self, show= False):
        """
        This method allow you to view the DataFrame of your inputted data
        """
        df= self._dataFrame()
        return df
        
    def showcountplot(self):
        """
        This method is going to generate the number of instances a grade occur.
        But plot will only generate when you close the program.
        """
        df= self._dataFrame()
        sns.countplot(data= df, x= 'Grade')
        plt.show()