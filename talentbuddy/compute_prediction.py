from __future__ import division
import math
def compute_prediction(n, w):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    
    prev_week = n
    while w:
        cur_week = prev_week + (prev_week*7/100)
        prev_week = cur_week
        w=w-1
        
    print int(prev_week)

def compute_prediction_tb(n, w):
    print int(n * pow(1.07, w))
    
compute_prediction(100,4)
compute_prediction_tb(100,4)