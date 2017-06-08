# Hint:  use Google to find python function
#Start of answer work

#import module datetime
from datetime import datetime

####a)

#these are strings that represent dates to me but not to python
date_start = '01-02-2013'  
date_stop = '07-28-2015'

#need to convert strings to datetime format

date_starttime = datetime.strptime(date_start, '%m-%d-%Y')
date_stoptime = datetime.strptime(date_stop, '%m-%d-%Y')

#compute time difference and print to screen

print(date_stoptime - date_starttime)

####b)  
date_startb = '12312013'  
date_stopb = '05282015'

#similar to a above, we first need to convert these strings to dates

date_starttimeb = datetime.strptime(date_startb, '%m%d%Y')
date_stoptimeb = datetime.strptime(date_stopb, '%m%d%Y')

#compute time difference and print to screen

print(date_stoptimeb - date_starttimeb)

####c)  
date_startc = '15-Jan-1994'  
date_stopc = '14-Jul-2015'

#similar to a above, we first need to convert these strings to dates

date_starttimec = datetime.strptime(date_startc, '%d-%b-%Y')
date_stoptimec = datetime.strptime(date_stopc, '%d-%b-%Y')

#compute time difference and print to screen

print(date_stoptimec - date_starttimec)
