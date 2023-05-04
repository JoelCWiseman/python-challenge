import os
import csv

input_file = os.path.join("Resources", "election_data.csv")

output_file = os.path.join("analysis", "election_results.txt")

with open(input_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Skip the header row
    data = list(csv_reader)

#Set variables for the data
total_votes = 0
candidates = {}
winner = ""

for row in data:
    #Count of total votes
    total_votes += 1

    #Total votes for each candidate
    candidate = row[2]
    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1

#Calculate the percentage of votes for each and the winner
max_votes = 0
for candidate, votes in candidates.items():
    percentage = round(votes/total_votes*100, 3)
    candidates[candidate] = [votes, percentage]
    if votes > max_votes:
        winner = candidate
        max_votes = votes

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, values in candidates.items():
    print(f"{candidate}: {values[1]}% ({values[0]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, values in candidates.items():
        file.write(f"{candidate}: {values[1]}% ({values[0]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
