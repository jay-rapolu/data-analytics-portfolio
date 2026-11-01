# Day 01 Learning's Documentation
## Topics Covered
- ### Spreadsheet Fundamentals
  - Rows, columns, cells and cell references.
  - Headers, records and data types.
  - Retail sales dataset.
  - Revenue calculation using multiplication.
      - SUM( ), AVERAGE( ), COUNT( ), MAX( ) and MIN( )
- ### Python Revision
  - Loops using the Nested Dictionaries
  - Revenue calculations.
  - Filtering and aggregating sales data.
- ### AI-assisted business analysis
  - Total revenue.
  - Transaction count.
  - Average order value.
  - Best-selling product by quantity.
  - Highest-revenue product.

 ## Spreadsheet Fundamentals.
- ### Rows
  Rows are the combination of all the boxes which are in the horizontal line generally it is denoted or recognized using the numbers which starts from 1.

- ### Columns
  Columns are the combination of all the boxes which in the vertical line generally these are denoted or recognized using the Capital Alphabets starting from A.

- ### Cells
  Cells are the individual boxes where both horizontal line and Vertical line intersect.

- ### Cell References
  Cells are referred using the Column alphabet and the Row number to get the single cell. for example using C1 we can get the cell from 3 column and 1 row.

- ### Headers
  In Row 1 we mention the name of the each column which defines what type of data or what data is stored in that column.

- ### Records
  Each row after row 1 is considered as record and this might be changed based on the type of data we have. for sales we call each row as transaction, employees we call each row as employee.

- ### dataset
  dataset is nothing but all the rows and columns related to one type of data is called as one dataset.

- ### data types
  - Text: Any String is considered as text.
  - Number: Any Numeric value is considered as Number.
  - Date: Any Date is considered as Date
  - Boolean: True or False
 
 - ### [retail sales dataset](https://github.com/jay-rapolu/data-analytics-portfolio/blob/main/01-spreadsheet-fundamentals/Day_01_Retail_Sales_Data_Fundamentals.ods)
   - you can download the dataset using the above link. This dataset consists of both the data and the formulas
   - Formulas that are used in this dataset are
     - Calculate the Revenue by adding new column in E, in E2 Applied C2xD2 to get the revenue and dragged to E5 to apply the formula till E5 and the formula will update the row number with respective row in E5 formula changes to C5xD5. use "*" instead of x.
     - SUM(E2:E5) in cell E6 - Adds all the numeric values from E2 to E5
     - AVERAGE(E2:E5) in E7 -Adds all the numeric values from E2 to E5 and divides it with number of cells 
     - COUNT(E2:E5) in E8 - Returns the count of cells containing numeric values from E2 to E5
     - MAX(E2:E5) in E9 - Returns the max numeric value in cells E2 to E5
     - MIN(E2:E5) in E10 - Returns the min numeric value in cells E2 to E5
  - [Note]: for all the formulas you need to add = so that it is recognized as formula by cell.

## Python Revision
-  In this Revision I calculated the data using the for loop and the dictionary and uploaded that python file you can download it from here [Day_01_Nested_Dictionary_Practice.py](https://github.com/jay-rapolu/data-analytics-portfolio/blob/main/03-python-analytics/Day_01_Nested_Dictionary_Practice.py)
-  Operations performed on this data are
  - Calculating and adding revenue using the sales dictionary
  - Total Number of transactions
  - Total revenue
  - Average of Total revenue
  - Find the product with least revenue
  - Find the product with highest revenue

## AI-assisted business analysis
- Using AI I have analyzed the major kpi's or Key Performance Indicators which are mentioned below:
  - Total Revenue of the dataset - ₹1,20,100.
  - Total number of transactions or sales - 4.
  - Average of total sales - ₹30,025.
  - Best Selling product by the quantity - Mouse – 5 units
  - Product which is having the highest revenue - Laptop – ₹90,000.
