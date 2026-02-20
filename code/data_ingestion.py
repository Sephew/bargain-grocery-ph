# Get Weekly Average Report from https://www.da.gov.ph/price-monitoring/
# if a unique record is detected:
#   open pdf
#   read pdf
#   extract commodity name, unit & price, clean then add to database alongside unique record (WeekRange)

# columns: date
# rows: commodity
# cell: price

# Create 2nd relational database with commodity name as the foreign key for nutritional facts table.

# columns: nutrition + unit + other specs
# rows : commodity
# cell: value


#OUTPUT: 2 correlated tables (Price & Nutrition)


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.da.gov.ph/price-monitoring/"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Accept-Language':'en-GB,en;q=0.5',
    'Referer':'https://google.com',
    'DNT':'1'
}
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.content,'html.parser')
print(soup.prettify())

print("-"*50)

#Get List of all tables in the webpage (202)
tables = soup.find_all('table')[1:5]

#Get tables with attribute ''

PDF_list = []


#For the first four tables (2026 - 2023), find <a> element with href tag, get href link that ends with .pdf then store into a list for later use.
for table in tables:
    for anchor in table.find_all('a',href=True):
        if anchor['href'].endswith('.pdf'):
            print("PDF LINK: ",anchor['href'])
            PDF_list.append(anchor['href'])



# next step: open pdf, read pdf using csv then store into sql database
# setup sql database with 2 tables: price & nutrition


#Reading the PDF_list using Camelot

import camelot

table_test = camelot.read_pdf('https://www.da.gov.ph/wp-content/uploads/2023/10/Weekly-Average-Prices-October-2-6-2023.pdf',pages='all')
df_test = table_test.df



for pdf in PDF_list:
    tables = camelot.read_pdf(pdf,pages='all')
    for table in tables:
        df = table.df
        print(df)
