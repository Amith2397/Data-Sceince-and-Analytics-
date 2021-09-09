# -*- coding: utf-8 -*-
"""
The Script is written Using the Naïve Bayes Density program with the Pima Indian Diabetes data set (pimaSmall) provided
in the folder and is used to classify a few instances with varying values for the numeric attributes (values
should be relevant to each attribute). 

The program uses naiveBayesDensity.py classifier.

@author: amith
"""
from naiveBayesDensity import *

c = Classifier("pimaSmall.txt","num\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tclass")
print(c.prior,'\n')

print(c.conditional,'\n')

print(c.classify([],[1,180,95,40,190,27.5,1.120,42]))
print(c.classify([],[5,120,92,42,200,30.5,1.223,54]))
print(c.classify([],[9,160,94,44,230,39.5,0.020,37]))



