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
import re #for store_link
url = "https://www.da.gov.ph/price-monitoring/"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Accept-Language':'en-GB,en;q=0.5',
    'Referer':'https://google.com',
    'DNT':'1'
}
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.content,'html.parser')


tables_WeeklyReport = soup.find_all("table")[1:4]


def dictionary_link_insert(dictionary,url):
    """
    Stores the .pdf link for later viewing by the OCR bot to extract data from the unstructed .pdf
    Input: dictionary object & Link URL
    Output: Dictionary of Values (HashMap) with FileName (Date of Report) & Link URL
    """
    # regex split to get date of report e.g. August-21-25-2023
    # Attempt 1: date_of_report = re.split(r"Weekly-Average-Prices-|\.pdf",url)[2]
    # Attempt 2: error because someone in DOA misspelled weekly... have to put l & s as optional
    match = re.search(r"Weekl?y-Average-Prices?-(.*?)\.pdf",url)
    if match:
        date_of_report = match.group(1)
    else:
        raise ValueError(f"Could not extract date of report from URL {url}")
    
    dictionary[date_of_report] = url

    print("dictionary inserted",date_of_report,"with",url)
    return dictionary




pdf_links = dict()
for table in tables_WeeklyReport:
    for anchor in table.find_all("a"):
        link = anchor["href"]
        print("PDF LINK:", link)
        dictionary_link_insert(pdf_links,link)
    print("-"*50)   

# #get <table> tag
# iterate through tr then tc, get all values (name & anchor tag for pdf link) and store in a list of dicts

# next step: open pdf, read pdf using csv then store into sql database
# setup sql database with 2 tables: price & nutrition
