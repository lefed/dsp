import sys
import os
import csv

#new example code vs. problem code

list_of_emails = ['laura@gmail.com', 'andrew@gmail.com', 'feds@shaw.ca', 'test@yahoo.com']

with open ('emails.csv', 'w') as csv_file:
    emailwriter = csv.writer(csv_file)
    emailwriter.writerow(['list_of_emails'])
    for email in list_of_emails:
        emailwriter.writerow(['%s' % email])
