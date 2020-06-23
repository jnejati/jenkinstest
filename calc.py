form math import pi

#Calculates a cirecle's area
def calct_area(r):
    return pi * r **2

def calc_divide(a, b):
    if b == 0:
	raise ValueError('Division by Zero')
    return a/b

def subtract(a, b):
    return a - b
