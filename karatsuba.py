"""
Created on Mon Apr  8 14:36:29 2019

@author: zeinabss

This function calculates multiplication of two number (positive or negative) using Karatsuba algorithm. 
"""
import math

def DigitCount(num):
    if num == 0:
        n = 1
    else:
        n = int(math.log10(abs(num)))+1
    return n
        

def split(num,splitlen):
    
    firsthalf=math.floor(num/(10**splitlen))
    secondhalf=num-firsthalf*10**splitlen
    return firsthalf, secondhalf
    
    
def karatsuba_multiply(num1,num2):
    digit_num1=DigitCount(num1)
    digit_num2=DigitCount(num2)
    
    if digit_num1==1 or digit_num2==1:
        return num1*num2
    
    splitlen1=int(digit_num1/2)
    splitlen2=int(digit_num2/2)
    
    firsthalf_num1, secondhalf_num1=split(num1,splitlen1)
    firsthalf_num2, secondhalf_num2=split(num2,splitlen2)
    
    # first number = ab
    # second number = cd
    
    ac=karatsuba_multiply(firsthalf_num1,firsthalf_num2)
    bd=karatsuba_multiply(secondhalf_num1,secondhalf_num2)
    
    if splitlen1==splitlen2:
        ##Gauss's trick
        # r=(a+b)*(c+d) , t=ad+bc
        r=karatsuba_multiply(firsthalf_num1+secondhalf_num1,firsthalf_num2+secondhalf_num2)
        t=r-bd-ac
        product=ac*10**(splitlen1+splitlen2)+bd+t*10**int(splitlen1)
    else:
        #future imporovement:
        #develope the Gauss's trick for this condition! 
        ad=karatsuba_multiply(firsthalf_num1,secondhalf_num2)
        cb=karatsuba_multiply(firsthalf_num2,secondhalf_num1)
        product=ac*10**(splitlen1+splitlen2)+bd+ad*10**int(splitlen1)+cb*10**int(splitlen2)
    return product


