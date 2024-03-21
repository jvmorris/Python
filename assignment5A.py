# Jevaughn Morris
# Assignment 5 Problem A
# COP2500
# July 26th, 2022

# import math for functions

import math

# create functions for discriminant and roots

def determinant(a, b, c):
    return b ** 2 - 4 * a * c

def root1(a, b, c):
    return (-b + math.sqrt(determinant(a, b, c)))/(2 * a)
    

def root2(a, b, c):
    return (-b - math.sqrt(determinant(a, b, c)))/(2 * a)
    
#gather coefficients by using float

a = float(input("Enter the coefficient a:"))
b = float(input("Enter the coefficient b:"))
c = float(input("Enter the coefficient c:"))

D = determinant(a, b, c)

# create if statements for the outcome of the variable D signifying the discriminant

if D == 0:
    print ("That quadratic has one root:", root1(a, b, c))
elif D > 0:
    print("That quadratic has two real roots:", root1(a, b, c), "and", root2(a, b, c))
else:
    print ("Sorry, that quadratic has complex roots.")
