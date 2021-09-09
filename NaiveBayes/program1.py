# -*- coding: utf-8 -*-
"""

The Script is written using the basic Naïve Bayes program, one related to the
Congressional Voting Records. The data consists of the voting record of U.S. Congressional
representatives. The attributes are how that representative voted in 16 different bills. The first
attribute is the Class attribute.

The data set is available in the folder as “votes”. The module imports the Classifer
class defined in naiveBayesBasic.py.

The following instances are classified based on the voting records to make probabilistic guesses about
whether the person is a democrat or a republican. 16 votes must be provided,
(either ‘y’ or ‘n’) for somebody that you want to classify whether they are likely to be a
Republican or Democrat.

conditions: 
    
1) Alternate ‘y’ and ‘n’ votes starting with ‘y’
2) 4 ‘y’ votes followed by 4 ‘n’ notes followed by 8 ‘n’ votes
3) All ‘n’ votes
4) All ‘y’ votes
5) 3 ‘n’ votes followed by 3 ‘y’ votes followed by 3 ‘n’ votes followed by 1 ‘y’ vote followed
by 6 ‘n’ votes

@author: amith
"""

from naiveBayesBasic import *

c = Classifier("votes.txt","class\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr")
print(c.prior,'\n')

print(c.conditional,'\n')

print(c.classify(['y','n','y','n','y','n','y','n','y','n','y','n','y','n','y','n']))

print(c.classify(['y','y','y','y','n','n','n','n','n','n','n','n','n','n','n','n']))

print(c.classify(['n','n','n','n','n','n','n','n','n','n','n','n','n','n','n','n']))

print(c.classify(['y','y','y','y','y','y','y','y','y','y','y','y','y','y','y','y']))

print(c.classify(['n','n','n','y','y','y','n','n','n','y','n','n','n','n','n','n']))