# RaISe Covid-19 Dashboard

## Contents
1. [Introduction](#introduction)
    1. [Benefits](#benefits)
    2. [Risks](#risks)
2. [Videos](#videos)
    1. [Automated Covid-19 Dashboard](#sub1)  
3. [Scripts](#paragraph1)
    1. [Covid-API-call](#subparagraph1)
    2. [Covid-API-call-2](#subparagraph2)
    3. [Webscrape-Power-BI](#subparagraph3)
    4. [Webscrape-Power-BI-2](#subparagraph4)
    5. [Webscrape-Data-Clean](#subparagraph5)
    6. [Webscrape-Data-Clean-2](#subparagraph6)
4. [Future Updates](#future) 

## Introduction <a name="introduction"></a>
This folder contains scripts related to the new automated RaISe Covid-19 Power BI dashboard. These scripts perform a number of functions: 

- retrieving data through API calls and web scraping
- calculating 7 day moving averages; organising data in a database
- and exporting the data to .csv files

The .csv files output by these scripts are used by the Power BI Covid-19 dashboard. These scripts automate the process of data gathering and analysis enabling the author to refresh the dashboard with the most recently available data in a matter of minutes. Descriptions of each of the scripts and the libraries required to run them can be found below.

This folder also contains a video demonstrating the use of these scripts to gather data and refresh the Covid-19 dashboard.

### Benefits <a name="benefits"></a>

There are a number of benefits to using these scripts:

1. Speed

It takes approximately 5-10 minutes for one person to run these scripts and update the dashboard with the latest data. Previously several people were involved in updating mapping data and 7-day moving averages. 

2. Labour

This process eliminates the need to manually trawl through the coronavirus.gov.uk website downloading multiple .csvs and eliminates the need to transform the data contained in those .csvs and perform calculations in Excel. This process also eliminates the need to trawl through Power BI dashboards recording data. These tasks are all performed by the scripts. 

3. Error

The use of these scripts reduces human error as the code will always operate in the same way. It can't make incorrect moving average calculations and it can't misread a number or a data label. The calculations will be performed the same way every time as they are hard coded and the API calls request data straight from the source rather than reading it from a screen. Similarly the webscraping scripts collect data from the underlying source code of the website being scraped.

### Risks <a name="risks"></a>

For all the benefits there are some downsides:

1. Novel Process

This is the first time a script has been written to scrape a Power BI dashboard. If the dashboard being scraped undergoes significant changes the webscraping scripts may not be able to scrape them. If the webscraping fails however it will not crash or destroy the dashboard as the scripts and the dashboard are independent. The scripts would simply fail to update the existing .csv data on ICU beds and hospitalisations and this data would need to be collected manually again until the code is updated to reflect the changes on the dashboard being scraped. 

2. Dependencies

These scripts rely on several libraries (selenium, pandas and Cov19API) and these libraries could be updated. Typically warnings are produced in the command console when using functions which are scheduled to be changed as most developers recognise that library users require advanced notice of changes, so there would be advanced warning of changes and the code could be updated accordingly.

3. Skills/Experience

There are only several people with experience in Python and as far as I know I may be the only person who has scraped a Power BI dashboard, not just in our assembly but more widely throughout parliaments. I can produce documentation to guide people through the process of running the scripts and updating the data but unfortunately if I am not here there's no support.

## Videos <a name="videos"></a>

### Automated Covid-19 Dashboard-low2.mp4 <a name="sub1"></a>

Description: A downloadable video (20Mb) showing these scripts being used to refresh the Covid-19 dashboard. 

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
