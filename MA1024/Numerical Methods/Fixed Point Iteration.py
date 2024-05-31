'''Fixed-Point Iteration Method'''
import numpy as np

#Enter code for special cases like g(x) going out of range

''' Enter the Data Relevent to the Equation '''
limit=0.01
x0=1.5
k=1/4 #maximum absolute value of derivative within range( |g'(x)| )

n=0
nlimit= float('inf')
x=x0

def function(x):
    ''' Enter the Equation '''
    equation = np.log(x+2)
    return equation

while nlimit>=limit:
    f =  function(x)    
    if n!=0:
        nlimit = (k**n*(abs(x1-x0)))/(1-k)

    print(f"Iteration: {n+1}, x: {x:.4f}, f: {f:.4f}, accuracy: {nlimit:.4f} " )
    
    x = f
    n += 1

    if n==1:
        x1=x
    if n > 10:
        print("Maximum iterations reached.")
        break
