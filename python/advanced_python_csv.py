import sys
import os
import csv

#new example code vs. problem code

list_of_emails = ['laura.fedoruk@gmail.com', 'andrew.young28@gmail.com', 'fedoruks@shaw.ca', 'test@yahoo.com']

with open ('emails.csv', 'w') as csv_file:
    emailwriter = csv.writer(csv_file)
    emailwriter.writerow(['list_of_emails'])
    for email in list_of_emails:
        emailwriter.writerow(['%s' % email])
