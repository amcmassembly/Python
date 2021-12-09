# Python
A repository to store scripts relating to automation and webscraping with python.

## Covid-API-call.py 

Libraries: pandas, uk_covid19

Description: This code is designed to perform an API call, retrieving data from coronavirus.gov.uk. This code is designed to request data pertaining to case numbers, deaths, hospitalisations for England, Northern Ireland, Scotland and Wales. 7-Day Averages (mid-point) are calculated for cases, deaths...etc and the data is transformed and exported to .csv.

## Covid-API-call-2.py 

Libraries: pandas, uk_covid19

Description: This code is designed to perform an API call, retrieving data from coronavirus.gov.uk. This code is designed to request data by upper tier local authority (UTLA). The data is transformed and exported to .csv.

## Webscrape-Power-BI.py

Libraries: selenium

Descrpiption: This code is designed to scrape the Department of Health Covid-19 Power BI Dashboard. The code will wait until the page number element reads "22" as this is the page data is to be scraped from. Once that element is visible the page is scraped and the result is output to a text file. 


