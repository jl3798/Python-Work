#!/usr/bin/env python
# coding: utf-8

# In[13]:


# dependencies
import csv
import os


    
# file to load

file_to_load = os.path.join (".", "budget_data.csv")

file_to_output = os.path.join (".", "budget_analsyis.txt")

total_months = 0
total_net = 0

net_change_list = []
month_of_changes = []

greatest = ["", 0]
least = ["", 77777777777777]

#Read the csv and convert it to a list
with open (file_to_load) as financial_data:
    
    reader = csv.reader(financial_data)

    #Read the header row
    header = next(reader)
    
    
    #print(f"Title: {header}")
    first_row = next(reader)
    
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    
    
    for row in reader:
        
        #Track the total
        # total_months = total_months + 1
        total_months += 1 
        total_net += int(row[1])
        
        #Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)

        
        #Calculate the greatest increase
        if(net_change > 0):
            greatest[0] = row[0]
            greatest[1] = net_change
            
        #Calculate the greatest decrease
        if(net_change < least[1]):
            least[0] = row[0]
            least[1] = net_change
            
        
print(net_change_list)

print(greatest)
print(least)

net_monthly_average = sum(net_change_list)/ len(net_change_list)

output = (
    f"financial_analysis\n"
    f"----------------------------\n"
    f"Total months: {total_months})\n"
    f"Total: ${total_net}\n"
    f"Average Change ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest [0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]} (${least[1]})\n"
    
)

        
print(output)
        

    
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

with open (file_to_output, "w") as txt_file:
    txt_file.write(output)
    
    


# In[ ]:





# In[ ]:




