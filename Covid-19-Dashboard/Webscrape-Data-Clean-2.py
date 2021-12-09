import pandas as pd

f = open("C:/location/webscrape-data.txt", "r")
listofentries=[]
for line in f:
	listofentries.append(line.replace('\n',''))

icu_update_date=listofentries[1]

mask=[4,31,33,35,63,65,67]

columns=[]
for i in range(0,len(listofentries)):
	if i in mask:
		columns.append(listofentries[i])

values=[]
for i in range(0, len(listofentries)):
	if i in mask:
		values.append(listofentries[i-1])

table_two = {'%s' %columns[0]: [int(values[0])],
		'%s' %columns[1]:  [int(values[1])],
		'%s' %columns[2]:  [int(values[2])],
		'%s' %columns[3]:  [int(values[3])],
		'%s' %columns[4]:  [int(values[4])],
		'%s' %columns[5]:  [int(values[5])],
		'%s' %columns[6]:  [int(values[6])]}

table_two_panda=pd.DataFrame(table_two)

table_two_panda.to_csv('C:/location/filename_5.csv')

with open('C:/location/filename_6.txt','w') as f:
	f.write(icu_update_date)		
