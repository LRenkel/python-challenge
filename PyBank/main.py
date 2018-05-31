import csv

with open('budget_data_1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip header row
    data = list(reader)
    # now data is a list of rows

total_revenue = 0
revenue_change = 0
revenue_change_list = []
month_list = []
previous_revenue = None

for row in data:
   month_list.append(row[0]) #create list of all months in dataset (for later count calculations)
   revenue = eval(row[1]) #define revenue as in column 2
   total_revenue += revenue #increase total revenue for each iteration
   if previous_revenue != None: #if statement leaves out first row of data since there is no change to calculate
       revenue_change = eval(row[1]) - previous_revenue  #calculate revenue change using current row revenue and defined previous revenue
       revenue_change_list.append(revenue_change) #add current revenue change to revenue change list for later analysis
   previous_revenue = revenue #define new previous_revenue value for use in next iteration's revenue change calculation

total_months = len(month_list)
greatest_increase = (max(revenue_change_list))
greatest_decrease = (min(revenue_change_list))
greatest_increase_month = month_list[(revenue_change_list.index(greatest_increase)) + 1] 
#determine corresponding month for greatest incrase utilizing revenue increase's index position in list, add 1 to account for the additional month at the front of the list not included in rev change
greatest_decrease_month = month_list[(revenue_change_list.index(greatest_decrease)) + 1]
average_revenue_change = sum(revenue_change_list) / len(revenue_change_list)

print("Financial Analysis")
print("------------------------")
print("Total Months: {}".format(total_months))
print("Total Revenue: ${}".format(total_revenue))
print("Average Revenue Change: ${}".format(average_revenue_change))
print("Greatest Increase in Revenue: {} (${})".format(greatest_increase_month, greatest_increase))
print("Greatest Decrease in Revenue: {} (${})".format(greatest_decrease_month, greatest_decrease))

with open('Financial Analysis.txt', 'w') as f:
    f.write("Financial Analysis \n") 
    f.write("------------------------ \n")
    f.write("Total Months: {} \n".format(total_months))
    f.write("Total Revenue: ${} \n".format(total_revenue))
    f.write("Average Revenue Change: ${} \n".format(average_revenue_change))
    f.write("Greatest Increase in Revenue: {} (${}) \n".format(greatest_increase_month, greatest_increase))
    f.write("Greatest Decrease in Revenue: {} (${}) \n".format(greatest_decrease_month, greatest_decrease))