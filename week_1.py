import random
import math

def mc(number_of_interations, step):
    i = 1
    in_circle = 0
    est_pi = 0
    while(i < number_of_interations + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y <= 1):
            in_circle += 1
        if(i%step == 0):
            est_pi = 4*in_circle/ float(i)
            print(i, ": ...", est_pi)
        i += 1
    return est_pi
        
        
        
print("Monte-Carlo pi approximator.")
iter = input("Enter the total number of iterations: ")
display = input("Enter the display step: ")
est_pi = mc(int(iter), int(display))
print("The calculated final value is: ... ", est_pi)
print("Python math.pi equals: ", math.pi)