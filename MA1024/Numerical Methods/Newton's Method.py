'''Newton's Method'''
import numpy as np

#Need to code for special cases like f(x) going out of range

''' Enter the Data Relevent to the Equation '''
limit=0.00001
x0=0.5

n=0
nlimit= float('inf')
x=x0

def function(x):
    ''' Enter the Equation '''
    equation = x**3-4*x**2+1
    return equation

def derivative(x):
    ''' Enter the Derivative Equation '''
    d_equation = 3*x**2-8*x
    return d_equation

while nlimit>=limit:
    f =  function(x)
    f_ = derivative(x)   
    x2 = x-f/f_
    print(f"Iteration: {n}, x{n}: {x:.8f}, f: {f:.8f}, df: {f_:.8f}, x{n+1}: {x2:.8f}, accuracy: {nlimit:.8f} " )
    
    nlimit = abs((x2-x)/x2)
    x=x2
    n += 1
    

    if n > 100:
        print("Maximum iterations reached.")
        break
print(f"Iteration: {n}, x{n}: {x:.8f}, f: {f:.8f}, df: {f_:.8f}, x{n+1}: {x2:.8f}, accuracy: {nlimit:.8f} " )   
                  
