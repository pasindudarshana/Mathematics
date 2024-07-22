'''Jacobi Method (For 3x3 matrix)'''
import numpy as np

#Need to code for special cases like f(x) going out of range

''' Enter the Data Relevent to the Equation '''
##a1,b1,c1= map(int,input("Enter a1 b1 c1: ").split())
##a2,b2,c2= map(int,input("Enter a2 b2 c2: ").split())
##a3,b3,c3= map(int,input("Enter a3 b3 c3: ").split())
##d1,d2,d3= map(int,input("Enter d1 d2 d3: ").split())
x,y,z= map(int,input("Enter initial values of x,y,z (x1,x2,x3): ").split())

k = int(input("Enter the number of iterations: "))

print("\n"+"1st Approximation" +"\n" + "x0 :"+str(x)+"\n" +"y0 :"+str(y)+"\n" +"z0 :"+str(z)+"\n")

#for i in range(k):
    