import matplotlib.pyplot as plt
import numpy as np

def Advice(gp):
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

        
def gp_bar(course, total_courses):
    output = []
    output.append(course)
    return output
    
    
def gp_visual(total_courses):
    visual= gp_bar()
    plt.bar(visual, np.arange(1, total_courses), color= 'b')

    
def Score(total_unit, total_courses):
        result= 0
        course= 0
        unit_counter=0
        increment= 1
        if total_unit is not 0:
            try:
                while increment <= total_courses:
                    grade= (input(f"Grade_{increment}: ").upper())
                    unit= int(input(f"Course_{increment} unit: "))
                    print("\n")
                    if grade == 'A':
                        course= 5 * unit
                    elif grade == 'B':
                        course= 4 * unit
                    elif grade == 'C':
                        course= 3 * unit 
                    elif grade == 'D':
                        course= 2 * unit
                    elif grade == 'E':
                        course= 1 * unit
                    elif grade == 'F':
                        course= 0
                    else:
                        print('Invalid Grade')
                        break
                    gp_bar(course, total_courses)
                    increment+= 1  
                    unit_counter += unit
                    result += course
                if total_unit == unit_counter:
                    gp = result / total_unit
                    print(f"Grade: {round(gp, 3)}")
                    Advice(gp)
                    gp_visual(total_courses)
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
        
def cont():
    try:
        total_unit= int(input("Total Unit: "))
        total_courses= int(input("Total Courses: "))
        print("\n")
        Score(total_unit, total_courses)
    except ValueError:
        print('Value Error')