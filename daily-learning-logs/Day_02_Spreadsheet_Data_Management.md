# Day 02 – Spreadsheet Data Management and Quality Inspection

## 1. Objective

The objective of this file is to showcase how the data is managed using spreadsheet. In today's practice I have learned and completed the exercises on data management techniques like sorting (Ascending, Descending), Filtering (Single Condition, Multiple Conditions) and Basic data-quality issues like duplicates and missing cells.

## 2. Dataset description

The dataset is a raw data of the store where the each record contains each sale details or each transaction details. you can get the dataset from here: [Day_02_Retail_Sales_Practice.ods](https://github.com/jay-rapolu/data-analytics-portfolio/blob/main/01-spreadsheet-fundamentals/Day_02_Retail_Sales_Practice.ods)

## 3. Tools Used

Libreoffice is used to perform the analysis of this dataset, and the options or tools that are provided by that tool.

## 4. Methodology

### Sorting

Sorted the data by selecting the whole dataset and used the data option in the ribbon and selected sort option to sort the data. 
- First sorted the data in ascending order to find the product which has the least revenue. 
- Then sorted the data in descending order to find the product which has the highest revenue. Here I found that the if the data is missing that is sorted in top when using descending order

Note: We must select whole data while sorting instead of single column so that the respective rows also gets sorted.

### Filters

Applied Filters to all the columns using the headers as the reference. Performed some filter actions
- Applied Filter to Category to show only the sales records of Accessories Category.
- Applied Filter to show the records which have sales quantity more than 3.
- Applied Filter using AND condition to show the records which are related to Accessories and quantity is greater than 3.
- Applied Filter using AND condition to show the records which are related to Electronics or quantity is greater than 3.
- Applied Filter to show products whose revenue is greater than 10000.

Note: Filter hides the data which does not meet the condition It does not delete the data.

## 5. Results and Findings

As of now there is more cleaning required where we found an duplicate entry and one missing data in one cell. we need to Investigate further how the duplicate entry was done and why one cell is empty or Missing.

## 6. Data Quality Observations

We have one transaction with the one duplicate transaction where only the Id was duplicate and rest are different we need to find from where that was occured. One cell is marked as Missing we need to find why that was missing.

## 7. Business Insights

As per current data 
- Electronics Category is generating the Max Revenue even if the sales quantity are less.
- Accessories Category is generating the Min Revenue but the sales quantity is high.
- Furniture Category is in the middle with Medium Revenue and quantity of sales is also medium.
- Total Number of sales are 12 along with one duplicate and one missing record.

## 8. Learning Outcomes

Outcomes are understood how to sort the data, filter the data, inspect the data and provide the business insights which helps track the business manage the Inventory and much more.
Major things to be noted select all the dataset while sorting and filter does not deletes the data it hides the data temporarily, and how to inspect the data manually by checking the duplicates and any missing data.
