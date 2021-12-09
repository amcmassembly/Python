# This code was written to perform a second API call requesting data at UTLA level, rather than regional.

from uk_covid19 import Cov19API
import pandas as pd 


def main():
	# Built from documentation: https://publichealthengland.github.io/coronavirus-dashboard-api-python-sdk/pages/getting_started.html
	all_utlas = ["areaType=utla"]
	cases_and_deaths = {
		"Date": "date",
		"UTLA": "areaName",
		"Daily cases by publish date": "newCasesByPublishDate",
		"Cumulative cases by publish date": "cumCasesByPublishDate",
		"Daily deaths within 28 days of positive test by death date": "newDeaths28DaysByDeathDate",
		"Cumulative deaths within 28 days of positive test by death date": "cumDeaths28DaysByDeathDate",
	}

	api = Cov19API(
		filters=all_utlas,
		structure=cases_and_deaths
	)

	data = api.get_dataframe()

	LGDs= ['Antrim and Newtownabbey',
       'Ards and North Down',
       'Armagh City, Banbridge and Craigavon',
       'Belfast',
       'Causeway Coast and Glens',
       'Derry City and Strabane',
       'Fermanagh and Omagh',
       'Lisburn and Castlereagh',
       'Mid and East Antrim',
       'Mid Ulster',
       'Newry, Mourne and Down']


	newdata = data[data.UTLA.isin(LGDs)]

	# Export to csv
	newdata.to_csv('C:/Users/Aaron/OneDrive/Documents/assembly/covid_dashboards/LGD_covid_data.csv') 

if __name__ == "__main__":
	main()
