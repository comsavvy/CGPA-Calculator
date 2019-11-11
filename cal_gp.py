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

def gp_visual(display, total_courses):
    A= 5
    B= 4
    C= 3
    D= 2
    E= 1
    F= 0
    plt.plot(display, total_courses)
    plt.xlabel(['A', 'B', 'C', 'D', 'E', 'F'])
    plt.ylabel(0, 1, 2, 3, 4, 5)
    


def gp_bar(grade):
    output = []
    output.append(grade)
    return output
    
    
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
                    gp_bar(grade)
                    increment+= 1  
                    unit_counter += unit
                    result += course
                if total_unit == unit_counter:
                    gp = result / total_unit
                    print(f"Grade: {round(gp, 3)}")
                    display= gp_bar(grade)
                    Advice(gp)
                    gp_visual(display, total_courses)
                                  
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