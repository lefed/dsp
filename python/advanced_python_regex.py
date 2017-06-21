import csv
import sys
import os

facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""

with open('faculty.csv', 'w') as f:
    f.write(facultycsv)

csv_f = open ('faculty.csv')
degree_read_list = list()
csv_f.readline()

for line in csv_f:
    data = line.strip()
    degree_read_list.append(data.split(','))

csv_f.close()    

#Test commented out - print (degree_read_list)                 

#Q1 Code:

new_degrees = []

for row  in degree_read_list:
    new_degrees.append(row[1])

def count_degrees(csv_file_name):
     #Find number of times ' Ph.D' or ' PhD' occurs in degree_read_list:    
    PHD_count = (sum(x.count('Ph.D') for x in new_degrees))+ (sum(x.count('PhD') for x in new_degrees)) + (sum(x.count('PHD') for x in new_degrees)) 

    #Find number of times other degrees occur
    MD_count = (sum(x.count(' MD') for x in new_degrees))+ (sum(x.count(' M.D.') for x in new_degrees))

    MA_count = (sum(x.count(' MA') for x in new_degrees))+ (sum(x.count(' M.A.') for x in new_degrees))

    SCD_count = (sum(x.count(' SCD') for x in new_degrees))+ (sum(x.count(' ScD') for x in new_degrees))+ (sum(x.count(' Sc.D.') for x in new_degrees))

    zero_count = (sum(x.count('0') for x in new_degrees))

    JD_count = (sum(x.count(' JD') for x in new_degrees))+ (sum(x.count(' J.D.') for x in new_degrees))

    MS_count = (sum(x.count(' MS') for x in new_degrees))+ (sum(x.count(' M.S.') for x in new_degrees))

    MPH_count = (sum(x.count(' MPH') for x in new_degrees))+ (sum(x.count(' M.Ph.') for x in new_degrees))

    BSED_count = (sum(x.count(' BSED') for x in new_degrees))+ (sum(x.count(' B.S.Ed.') for x in new_degrees))

    degree_count_dict = {"BSED": BSED_count, "MPH": MPH_count, "MS": MS_count, "JD": JD_count, "0": zero_count, "SCD": SCD_count, "MA": MA_count, "MD": MD_count, "PHD": PHD_count}

    print(degree_count_dict)
    return(degree_count_dict)

count_degrees('faculty.csv')
        
#Q2 Code:

faculty_titles = []

for row  in degree_read_list:
    faculty_titles.append(row[2])

def count_titles(csv_file_name):
     #Find number of times 'professor', 'associate' or 'assistant' occurs degree_read_list:    
    Professor_count = (sum(x.count('Professor') for x in faculty_titles)) - (sum(x.count('Associate') for x in faculty_titles)) - (sum(x.count('Assistant') for x in faculty_titles))

    Associate_count = (sum(x.count('Associate') for x in faculty_titles))

    Assistant_count = (sum(x.count('Assistant') for x in faculty_titles))

    title_count_dict = {"Professor": Professor_count, "Associate": Associate_count, "Assistant": Assistant_count}

    print(title_count_dict)
    return(title_count_dict)

count_titles('faculty.csv')
        
#Q3 Code - Made up example code vs. problem code:


list_of_emails = ['laura@gmail.com', 'andrew@gmail.com', 'feds@shaw.ca', 'test@yahoo.com']

with open ('emails.csv', 'w') as csv_file:
    emailwriter = csv.writer(csv_file)
    emailwriter.writerow(['list_of_emails'])
    for email in list_of_emails:
        emailwriter.writerow(['%s' % email])


with open('emails.csv', 'r') as csv_file:
    csv_file.readline()
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

#Q4 Code - Made up example code vs. problem code:

emails = ['laura@gmail.com', 'andrew@gmail.com', 'me@yahoo.com', 'latebloomer@hotmail.com', 'fedoruks@shaw.ca', 'andrew.young28@gmail.com']

single = 'laura.fedoruk@gmail.com'

end = single[single.find('@'):]    

domains = [x.split('@', 1)[-1] for x in emails]

#THIS CODE WORKS!!!

index_domains = [x[x.find('@'):] for x in emails]

#Then turn into set

unique_domains = set(index_domains)

#print(end)
#print(single)
#print(domains)
print(index_domains)
print(unique_domains)
