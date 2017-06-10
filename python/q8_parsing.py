# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

goals_difference = []

with open('football.csv') as csvfile:
    readfootballcsv = csv.reader(csvfile)   
    next(readfootballcsv, None)
    
    for row in readfootballcsv:
        difference = abs(int(row[5]) - int(row[6]))
        goals_difference.append(difference)

    print(row[goals_difference.index(min(goals_difference))-1][0])

    print(goals_difference)

#above code works, still need to figure out why this next code does not - it seems to stop the above code from working properly as well
    
    listfootballcsv = list(csv.reader(csvfile))

    print(readfootballcsv[0][goals_difference.index(min(goals_difference))-1]])






    


