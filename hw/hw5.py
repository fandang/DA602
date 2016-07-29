import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Do the following:

Download the new data set on the Lesson 5 page called brainandbody.csv.  
This file is a small set of average brain weights and average body weights for a number of animals.  
We want to see if a relationship exists between the two. (This data set acquired from here).

Perform a linear regression using the least squares method on the relationship of brain weight [br] to body weight [bo].  
Do this using just the built in Python functions (this is really easy using scipy, but we're not there yet).  
We are looking for a model in the form bo = X * br + Y.  Find values for X and Y and print out the entire model to the console.

NOTES:
A linear regression line has an equation of the form Y = a + bX, where X is the explanatory variable and Y is the dependent variable. 
The slope of the line is b, and a is the intercept (the value of y when x = 0).
correlation coefficient....The r^2 value is 0.726 (the square of the correlation coefficient), indicating that 72.6% of the variation in one variable may be explained by the other


**** Note: had some problem with dates: http://stackoverflow.com/questions/27630114/matplotlib-issue-on-os-x-importerror-cannot-import-name-thread
**** Just in case it comes up when running code...

'''
def least_squares(df, x_label, y_label):	

	print('***********************************************')
	print('*** Linear Regression with Least Squares: ')
	print('***********************************************')

	# Use the logic from: https://en.wikipedia.org/wiki/Simple_linear_regression
	# col sums: axis=0
	x_data = df[x_label]
	y_data = df[y_label]
	
	x_sum = np.sum(x_data, axis=0)
	y_sum = np.sum(y_data, axis=0)
	x_sq_sum = np.sum(x_data * x_data, axis=0)
	y_sq_sum = np.sum(y_data * y_data, axis=0)
	x_y_sum = np.sum(x_data * y_data, axis=0)
	
	n = len(x_data) # or use len(y_data)

	print "LOG: x_sum: %s y_sum: %s x_sq_sum: %s y_sq_sum: %s x_y_sum: %s " % (x_sum, y_sum, x_sq_sum, y_sq_sum, x_y_sum)

	# From: https://en.wikipedia.org/wiki/Simple_linear_regression
	# "These quantities would be used to calculate the estimates of the regression coefficients, and their standard errors."

	beta_hat = (n * x_y_sum - x_sum * y_sum) / (n * x_sq_sum - x_sum * x_sum)
	alpha_hat = (1.0 / n) * y_sum - (1.0 / n) * beta_hat * x_sum
	print "alpha_hat: %s beta_hat: %s " % (alpha_hat, beta_hat)

	df[y_label + '_projected'] = df[x_label] * beta_hat + alpha_hat

	print "-----------------------------------------------------------------------------------------------------"
	print("RESULTS:")
	print "-----------------------------------------------------------------------------------------------------"

	print(df)

	# Just to double check my result:
	plt.scatter(df[x_label], df[y_label])

	# draw diagonal line with supplied x values and their corresponding least squares y values...
	plt.plot(x_data, (x_data * beta_hat + alpha_hat), 'k-')

	plt.show() # Depending on whether you use IPython or interactive mode, etc.

if __name__ == "__main__":
	
	print "-----------------------------------------------------------------------------------------------------"
	print "CHANGE THE FOLLOWING FLAG TO TRUE IF YOU WANT TO SEE THE WIKIPEDIA LEAST SQUARES CALCULATION + CHART"
	print "-----------------------------------------------------------------------------------------------------"

	#show_wiki_example = True
	show_wiki_example = False

	if(show_wiki_example):
		x_height_array = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
		y_mass_array = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]
		df = pd.DataFrame({ 'X_Height' : x_height_array, 'Y_Mass' : y_mass_array })
		least_squares(df, 'X_Height', 'Y_Mass')
	else:	
		df = pd.read_csv('brainandbody.csv')
		df = df.rename(columns = {'Unnamed: 0':'animal_name'})
		least_squares(df, 'body', 'brain')

	
	