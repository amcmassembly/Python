# RaISe Covid-19 Dashboard

## Contents
1. [Introduction](#introduction)
2. [Scripts](#paragraph1)
    1. [Covid-API-call](#subparagraph1)
    2. [Covid-API-call-2](#subparagraph2)
    3. [Webscrape-Power-BI](#subparagraph3)
    4. [Webscrape-Power-BI-2](#subparagraph4)
    5. [Webscrape-Data-Clean](#subparagraph5)
    6. [Webscrape-Data-Clean-2](#subparagraph6)
3. [Future Updates](#future) 

## Introduction <a name="introduction"></a>
This folder contains scripts related to the new RaISe Covid-19 Power BI dashboard. These scripts perform a number of functions: 

- retrieving data through API calls and web scraping
- calculating 7 day moving averages; organising data in a database
- and exporting the data to .csv files

The .csv files output by these scripts are used by the Power BI Covid-19 dashboard. These scripts automate the process of data gathering and analysis enabling the author to refresh the dashboard with the most recently available data in a matter of minutes. Descriptions of each of the scripts and the libraries required to run them can be found below.

## Scripts <a name="paragraph1"></a>


### Covid-API-call  <a name="subparagraph1"></a>

Libraries: pandas, uk_covid19

Description: This code is designed to perform an API call to retrieve data from coronavirus.gov.uk. This code is designed to request data pertaining to case numbers, deaths, hospitalisations for England, Northern Ireland, Scotland and Wales. 7-Day Averages (mid-point) are calculated for cases, deaths...etc and the data is transformed and exported to .csv.

Last updated: 10/12/2021

### Covid-API-call-2 <a name="subparagraph2"></a>

Libraries: pandas, uk_covid19

Description: This code is designed to perform an API call to retrieve data from coronavirus.gov.uk. This code is designed to request data by upper tier local authority (UTLA). The data is transformed and exported to .csv.

Last updated: 10/12/2021

### Webscrape-Power-BI <a name="subparagraph3"></a>

Libraries: selenium

Description: This code is designed to scrape the Department of Health Covid-19 Power BI Dashboard. The code will wait until the page number element reads "22" as this is the page data is to be scraped from. Once that element is visible the page is scraped and the result is output to a text file. 

Last updated: 10/12/2021

### Webscrape-Power-BI-2 <a name="subparagraph4"></a>

Libraries: selenium

Description: This code is designed to scrape the Department of Health Covid-19 Power BI Dashboard. The code will wait until the page number element reads "30" as this is the page data is to be scraped from. Once that element is visible the page is scraped and the result is output to a text file. 

Last updated: 10/12/2021

### Webscrape-Data-Clean <a name="subparagraph5"></a>

Libraries: pandas

Description: This code takes the .txt output produced by Webscrape-Power-BI code and organises and cleans the data to retrieve only the desired metrics and arrange them in a database which is exported as a .csv.

Last updated: 10/12/2021

### Webscrape-Data-Clean-2 <a name="subparagraph6"></a>

Libraries: pandas

Description: Description: This code takes the .txt output produced by Webscrape-Power-BI-2 code and organises and cleans the data to retrieve only the desired metrics and arrange them in a database which is exported as a .csv.

Last updated: 10/12/2021

## Future Updates <a name="future"></a>

These scripts have been built as proof of concept work to show the automation potential of python scripting but these scripts will refined and combined into one much shorter programme rather than separate scripts. It is hoped that there will be an ongoing process of review and refinement with regards to these scripts and that this sub directory will be the first of many dedicated to automation and webscraping with python. 
