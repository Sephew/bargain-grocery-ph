

2/18/2026 - Transitioned from Sentiment Analytics Stock trader to Price Watch Grocery Ingredients Recommendation System. Because it's practical and can help me practice multiple backend disciplines

2/19/2026 - Created file structures & listed the requirements needed, did simple webscraping tests with requests & beautifulsoup4

2/20/2026 - Understood AJAX & Jquery, tried to look for AJAX requests we can use, or hidden APIs to no success. Concluded the best scenario is to look for <table> and iterate for each tr then tc to get the <a> link of the pdf
Next Step: Iterate through <tables> get the anchor links, open PDFs (test with 1), build backend sql for data storage then CSV read using Tesseract then write it down to DB.
Mistakes Made: Spent time trying different methods to find hidden APIs or requests for simpler implementation, however it seems like the data does not call from a backend because no XHR or fetch requests where made. Most likely, files are stored directly to wordpress.

NOTE: If you will experiment, use ipynb to document exploration.


2/21/2026 - Progress: I was able to get the .pdf list of links ready for the Weekly Average Report, However a slight ego inside me is telling me I can organize the messy data of the "Daily Report" to maybe increase accuracy and further the decision-power possible. But for now, the weekly report will do to not over scope my needs.
- Problem arised when only more recent years are able to use "Tabula-py", 2023 dataset are not text-based and are unstructed data, we will have to use OCR or Machine Learning to extract data from this.

Next Step: setup OCR to iterate from PDF_list and get tabularized data (pandas dataframe preferably), then store into database (mySQL)


2/21/2026 - I did not push my commit from my desktop, so now I have to redo progress from yesterday. This should be easy because I now know how to do it, all I need to do is recollect the process from memory.

2/24/2026 - 
1) Build these tables

commodities (manual/semi-auto)

commodity_nutrition (manual)

weekly_prices (automated)

optional but highly recommended: raw_weekly_rows (raw extraction log)

2) Ingestion logic each week (structured data)

Extract all rows into raw_weekly_rows (OCR)

Try to match each raw row to a commodity_id

If matched → insert into weekly_prices

If not matched → flag as “needs mapping” (you update commodities to intervene)


Add a column in commodities like:

canonical_name

aliases (or a separate table commodity_aliases)

Because government PDFs will name the same thing 3 different ways across time.

3) Ingestion logic each week (unstructured data)

from dataset of structured, fine-tune a model, reduce loss function, test then deploy.