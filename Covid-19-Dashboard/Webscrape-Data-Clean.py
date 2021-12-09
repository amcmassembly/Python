import pandas as pd

#open the text doc
f = open("C:/location/webscraped-data.txt", "r")

# make a list from each sentence in the text doc
listofentries=[]
for line in f:
	listofentries.append(line.replace('\n','').replace(',',''))

# name variables
admissions_updated=listofentries[3]
total_admissions=listofentries[35]
total_discharged=listofentries[37]
total_inpatients=listofentries[39]
columns=listofentries[123:128]
locations=listofentries[128:133]
admissions_7=listofentries[133:138]
discharges_7=listofentries[138:143]
admissions_14=listofentries[143:148]
discharges_14=listofentries[148:153]
columns_2=listofentries[86:90]
dates=listofentries[90:98]
admissions_cumulative=listofentries[98:106]
discharged_culumative=listofentries[106:114]
inpatients_cumulative=listofentries[114:122]

#make a data table for pandas
table_one = {'Date':dates,
		'Cumulative Admissions': admissions_cumulative,
		'Cumulative Discharged': discharged_culumative,
		'Cumulative Inpatients:': inpatients_cumulative}

# make a data table for pandas using the column names retrieved from the list earlier
table_two = {'%s' %columns[0]: locations,
		'%s' %columns[1]: admissions_7,
		'%s' %columns[2]: discharges_7,
		'%s' %columns[3]: admissions_14,
		'%s' %columns[4]: discharges_14}

#another data table, removing commas so values can be changed from strings to ints.
KPIs = {'Admissions': [int(total_admissions.replace(',',''))],
			'Discharges': [int(total_discharged.replace(',',''))],
			'Inpatients': [int(total_inpatients.replace(',',''))]}

# make pandas data frame
table_one_panda=pd.DataFrame(table_one)
table_two_panda=pd.DataFrame(table_two)
kpis_pandas=pd.DataFrame(KPIs)

# send the data frame to a csv output
table_one_panda.to_csv('C:/Users/location/filename_1.csv')
table_two_panda.to_csv('C:/Users/location/filename_2.csv')
kpis_pandas.to_csv('C:/Users/location/filename_3.csv')

# output the admissions update data as a text since it's just once sentence and not a list of variables
with open('C:/Users/location/filename.txt','w') as f:
	f.write(admissions_updated)		
