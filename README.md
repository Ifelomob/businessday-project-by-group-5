# Businessday-project-by-group-5
## AIM:To determine the emotional tone of articles in businessday.ng
# Project overview 
## This research is focused on understanding the opinions and emotional tones expressed in Articles related to Nigeria’s Economy from 2021 to present.
## The outcome is to provide insights into how the Economic narrative of Nigeria has evolved over time through media coverage.
## Datasource "businessday_final3.csv" file contains all the details scraped from the analysis.
# Methodology
### Web scrapping (Extract structured data like Title, Author, Date, content and url)
### Data cleaning (Ensures the scraped data is constituent and ready for analysis)
### Data storage (Save the scraped data either in csv or excel for further analysis)
### Sentiment Analysis (Analyze the sentiment of the article content)
# Tools and Libraries used
### 1.	Selenium used for automating web scraping by interacting with dynamic web pages
### 2.	Undetected-chrome driver: used to by passanti-bot mechanisms like cloudflare challenges.
### 3.	Pandas  : used to handle and manipulate the scraped data.
### 4.	JSON:  used to save and load checkpoint data for resuming the scraping data.
### 5.	Python standard libraries  : os was used to manage file paths and directories, time was used to introduce delays for human like behavior and timestamp checkpoint data, while timestamp was used to generate random delays for scrolling and navigation.
### 6.	Web driver-manager : was used to automatically manage and update the chrome webdriver
### 7.	Exception handling : Ensures the script continues to run even if errors occurs.
### Pre_processing,sentiment and polarity scoring and sentiment visualization were using Textblob
