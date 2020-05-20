import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
class G4:
    def __init__(self):
        self.gradde= {'Grade': [],
             'GradePoint': [],
             'Unit': []}
    def advice(self, gp):
        if gp >= 4.5:
            print('Weldone, You Are In First Class 👍')
        elif gp >= 3.5:
            print('Work Hard, You Are In Second Class Upper')
        elif gp >= 2.4:
            print('Nothing is impossible, You are in Second Class Lower')
        elif gp >= 2.39:
            print('Work Hard, You are in Third Class')
        else:
            print('You pass through school')

    def score(self, total_unit, total_courses):
            result= 0
            course= 0
            unit_counter=0
            increment= 1
            if total_unit != 0:
                try:
                    while increment <= total_courses:
                        grade= (input(f"Grade_{increment}: ").upper())
                        self.gradde['Grade'].append(grade)
                        unit= int(input(f"Course_{increment} unit: "))
                        self.gradde['Unit'].append(unit)
                        print("\n")
                        if grade == 'A':
                            point= 5
                            self.gradde['GradePoint'].append(point)
                            course= point * unit
                        elif grade == 'B':
                            point= 4
                            self.gradde['GradePoint'].append(point)
                            course= point * unit
                        elif grade == 'C':
                            point= 3
                            self.gradde['GradePoint'].append(point)
                            course= point * unit 
                        elif grade == 'D':
                            point= 2
                            self.gradde['GradePoint'].append(point)
                            course= point * unit
                        elif grade == 'E':
                            point= 1
                            self.gradde['GradePoint'].append(point)
                            course= point * unit
                        elif grade == 'F':
                            point= 0
                            self.gradde['GradePoint'].append(point)
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
                        self.advice(gp)    
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

    def cont(self):
        try:
            total_unit= int(input("Total Unit: "))
            total_courses= int(input("Total Courses: "))
            print("\n")
            self.score(total_unit, total_courses)
        except ValueError:
            print('Value Error')
            
    def dataFrame(self):
        df= pd.DataFrame(self.gradde)
        return df
    
    def showFrame(self, data):
        if data == 'Y':
            self.dataFrame()
        else: 
            pass