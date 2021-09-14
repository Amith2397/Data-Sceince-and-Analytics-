# -*- coding: utf-8 -*-
"""
Linear Regression using two models:

There are few data files each of them having a set of values for two variables (say x & y) in the folder, one
pair per line in the data file. We are trying to determine if there is a linear relationship between
them.

• Regression functions are in a module called regression_functions.py.

• The two techniques used in the program are (1) Method of Least Squares that gives us a
Coefficient of Determination about the linearity of the relationship and also allows us try and fit a
line along a possible linear path (2) Pearson technique which gives us a Correlation Coefficient
about the linearity of the relationship


• The four data files are in1, in2, in3 and in4. Run the program against a data file and observe the
results

conditions:
    
• In order to plot the relationship of x and y, do the following:
• (1) Plot x vs y as a scatter plot (2) Plot x vs f(x) as a line plot
• Apply appropriate text in the plot for axes, title, as well as the coefficient of determination
(from Least Squares) and Pearson coefficient (from Pearson). Your plots should also
include meaningful information infer whether or not the visualization and numerical results agree with each
other.

@author: amith
"""
import regression_functions as regress
import matplotlib.pyplot as plt
import numpy as np

file1 = open('in1.txt', 'r')
r_file1 = file1.readlines()

file2 = open('in2.txt', 'r')
r_file2 = file2.readlines()

file3 = open('in3.txt', 'r')
r_file3 = file3.readlines()

file4 = open('in4.txt', 'r')
r_file4 = file4.readlines()

file_list = [r_file1, r_file2, r_file3, r_file4]

def main():
    
    for f in file_list:
        print ('Input File: ')
        x, y = np.loadtxt(f, delimiter=",", unpack=True, encoding="utf-8-sig")
        m, b = regress.compute_m_and_b(x, y)
        fx, residual = regress.compute_fx_residual(x, y, m, b)
        least_squares_r = regress.compute_sum_of_squared_residuals(residual)
        sum_squares = regress.compute_total_sum_of_squares(y)
        print()
    
        print("Data points: ", len(x))
        print("Least Squares Method")
        print("--------------------")
        print("Coefficients: m =", "%8.6f" % m, "\tb =", "%8.6f" % b)
    
        print("Sum of Squared Residuals: %12.6f" % least_squares_r)
        print("Total Sum of Squares: %12.6f" % sum_squares)
        coeff_of_determination = (1 - (least_squares_r/sum_squares))
        print("Coefficient of determination: %12.6f" % coeff_of_determination)
        print()
        pearson_r = regress.compute_pearson_coefficient(x, y)
        print("Pearson Method")
        print("--------------")
        print("Pearson Correlation Coefficient: %12.6f" % pearson_r)
        print("Predicted value of y (for x=80): %8.2f" % (m*80 + b))
        plt.figure()
        plt.scatter(x, y, color='red')
        plt.plot(x, fx, 'b')
            
        
    return
            

    
main()
plt.show()