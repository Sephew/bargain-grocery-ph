# Bargain Grocery PH
Recommend Grocery to Purchase based on DOA price monitoring fluctuations (discourage purchasing higher-priced vegetables, recommend cheaper vegetables and meals to make from them)

Input:

Given a Weekly Average of prices in pdf every week
Extract "Commodity", "Unit" and "Weekly Average Price"

Create Time Series database with primary identifier of "WeekRange"
Correlate features (correlation changes per months (seasonal) & price correlation between features)

Create Optimization algorithm -> (Protien + calories) with penalty for items that are higher-priced than before

OUTPUT:
List of Ingredients


FUTURE: Recommender Sys + Website Up in the cloud


NEED TO DOs:
Folder Structure
Ingestion 
