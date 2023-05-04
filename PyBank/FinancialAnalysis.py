import os
import csv

# Path to input file
input_file = os.path.join("Resources", "budget_data.csv")

# Path to output file
output_file = os.path.join("analysis", "budget_analysis.txt")

# Open the CSV file and read in the data
with open(input_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Skip the header row
    data = list(csv_reader)

# Initialize variables to store the data points we want to calculate
total_months = 0
total_profit_loss = 0
change_list = []
last_profit_loss = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Loop through the data to calculate the data points
for row in data:
    # Count the total number of months
    total_months += 1

    # Calculate the net total amount of profit/losses
    total_profit_loss += int(row[1])

    # Calculate the change in profit/losses from the previous month
    if last_profit_loss != 0:
        change = int(row[1]) - last_profit_loss
        change_list.append(change)

        # Update the greatest increase and decrease if necessary
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        elif change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

    last_profit_loss = int(row[1])

# Calculate the average change in profit/losses
average_change = round(sum(change_list)/len(change_list), 2)

# Print out the results to the terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the results to a text file in the analysis folder
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
