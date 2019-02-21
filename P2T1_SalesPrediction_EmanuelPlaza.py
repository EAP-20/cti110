# Calculating a profit percentage of an inputted total sales amount.
# 02/14/19
# CTI-110 P2T1-Sales Prediction
# Emanuel Plaza



# Get projected total sales.
total_sales=float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit=total_sales*0.23

# Display the profit.
print('The profit is $',format(profit,',.2f'),".",sep="")



#  First, with the "input" function, I made the "total_sales"
# variable and made it equal whatever the user inputs (and
# made it a float). Then, in order to calculate the profit
# percentage, I made a variable for the profit amount, and
# made it equal "total_sales" * "0.23". Finally, using a
# "print" function, I displayed the profit percentage, and
# formatted it so that it would round to the second decimal
# point.
