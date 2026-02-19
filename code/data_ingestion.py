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
url = "https://www.da.gov.ph/price-monitoring/"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Accept-Language':'en-GB,en;q=0.5',
    'Referer':'https://google.com',
    'DNT':'1'
}
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,'html.parser')

print(soup.prettify())