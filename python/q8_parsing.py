# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('football.csv') as csvfile:
    readfootballcsv = csv.reader(csvfile)   
    next(readfootballcsv, None)

    #define function
    def read_data(filename):
        """Returns a list of lists representing the rows of the csv file data.

        Arguments: filename is the name of a csv file (as a string)
        Returns: list of lists of strings, where every line is split into a list of values. 
       	 ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
   	    """
        #open file    
        file = open(filename)
        #create blank list for items to be returned to    
        return_list = list()
        #read lines in file    
        file.readline()

        #iterate over lines in file and strip each line to not include extra characters, then append each data between commas to return_list    
        for line in file:
            data = line.strip()
            return_list.append(data.split(','))

        #close file        
        file.close()

        #return list of values after printing list of values
        print(return_list)
        return return_list

    #define function
    def get_index_with_min_abs_score_difference(goals):
        """Returns the index of the team with the smallest difference
        between 'for' and 'against' goals, in terms of absolute value.

        Arguments: parsed_data is a list of lists of cleaned strings
        Returns: integer row index
        """
        #initialize goal_diff to be blank list    
        goal_diff = list()

        #iterate over entries in goals and append difference between column 5 and 6 as goals_diff     
        for entry in goals:
            goal_diff.append(int(entry[5]) - int(entry[6])) -1

        #use abs value of goals_diff and map to list of abs_diff of values        
        abs_diff = list(map(abs,goal_diff))

        #return index of minimum of abs_diff after printing
        print(abs_diff.index(min(abs_diff)))
        return abs_diff.index(min(abs_diff))   

    #define function
    def get_team(index_value, parsed_data):
        """Returns the team name at a given index.
    
        Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
        Returns: the team name
        """
        #team should be teh parsed data at index value, then return first column which should be the name of the team    
        team = parsed_data[index_value]
        return team[0]

    #test the functions
    read_data('football.csv')
    get_index_with_min_abs_score_difference('football.csv')




    


