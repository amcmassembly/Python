# Python/Covid-19-Dashboard

This folder stores scripts related to the new RaISe Covid-19 Power BI dashboard. These scripts perform a number of functions: retrieving data through API calls and web scraping; calculating 7 day moving averages; organising data in a database; and exporting the data to .csv files. These .csv files are then used by the Power BI Covid-19 dashboard. These scripts automate the process of data gathering and analysis enabling the author to refresh the dashboard with the most recently available data in a matter of minutes. Descriptions of each of the scripts and the libraries required to run them can be found below.

## Covid-API-call.py 

> Libraries: pandas, uk_covid19

> Description: This code is designed to perform an API call to retrieve data from coronavirus.gov.uk. This code is designed to request data pertaining to case numbers, deaths, hospitalisations for England, Northern Ireland, Scotland and Wales. 7-Day Averages (mid-point) are calculated for cases, deaths...etc and the data is transformed and exported to .csv.

## Covid-API-call-2.py 

Libraries: pandas, uk_covid19

Description: This code is designed to perform an API call to retrieve data from coronavirus.gov.uk. This code is designed to request data by upper tier local authority (UTLA). The data is transformed and exported to .csv.

## Webscrape-Power-BI.py

Libraries: selenium

Description: This code is designed to scrape the Department of Health Covid-19 Power BI Dashboard. The code will wait until the page number element reads "22" as this is the page data is to be scraped from. Once that element is visible the page is scraped and the result is output to a text file. 

## Webscrape-Power-BI-2.py

Libraries: selenium

Description: This code is designed to scrape the Department of Health Covid-19 Power BI Dashboard. The code will wait until the page number element reads "30" as this is the page data is to be scraped from. Once that element is visible the page is scraped and the result is output to a text file. 

## Webscrape-Data-Clean.py

Libraries: pandas

Description: This code takes the .txt output produced by Webscrape-Power-BI.py code and organises and cleans the data to retrieve only the desired metrics and arrange them in a database which is exported as a .csv.

## Webscrape-Data-Clean-2.py

Libraries: pandas

Description: Description: This code takes the .txt output produced by Webscrape-Power-BI-2.py code and organises and cleans the data to retrieve only the desired metrics and arrange them in a database which is exported as a .csv.


