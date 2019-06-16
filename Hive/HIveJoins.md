## JOINS

* INNER JOIN

* OUTER JOIN
  * left outer join
  * right outer join
  * full outer join

* SEMI JOIN
Hive does not provide 'IN' Clause instead provides  for SEMI INNER JOIN
select * from item_details LEFT SEMI JOIN sales_details ON (sales_details.item_code= item_details.item_code);

#### Create the Tables
```
Create table if not exists Sales_Details (
Name STRING,
SALES SMALLINT,
ITEM_CODE SMALLINT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;


Create table if not exists Item_Details (
Name STRING,
ITEM_CODE SMALLINT,
Price TINYINT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

#### Create the Data Files
```
Sales_Details.txt
Raj	,3,101
Raj	,2,102
Raj	,5,103
Ajay	,4,101
Ajay	,1,102
Ajay	,6,103
Sam	,4,101
Chandan	,1,102
Sumit	,6,103
Sumit	,8,113
Sumit	,3,109
Sumit	,5,111


Item_Detail.txt
Shampoo		,101,150
ToothPaste	,102,76
ToothBrush	,103,50
Comb		,104,20
Brush		,105,55
Tie 		,110,88
```

#### Load the Data
```
LOAD DATA LOCAL INPATH '/home/training/MyDemos/Hive/Sales_Details.txt'
OVERWRITE INTO TABLE SALES_Details;

LOAD DATA LOCAL INPATH '/home/training/MyDemos/Hive/Item_Details.txt'
OVERWRITE INTO TABLE ITEM_Details;
```

### View the data
```
select name,sales,item_code from sales_details ;
select Name,item_code,Price from item_details ;
```

#### JOIN
```
select name,sales,item_code from sales_details ;
join item_details ON (sales_details.item_code = item_details.item_code);
```

##### INNER JOIN

```
 select sales_details.*, item_details.* from sales_details join item_details ON (sales_details.item_code = item_details.item_code);
```
##### OUTER JOIN

```
 select sales_details.*, item_details.* from sales_details left outer join item_details ON (sales_details.item_code = item_details.item_code);
 select sales_details.*, item_details.* from sales_details right outer join item_details ON (sales_details.item_code = item_details.item_code);
 select sales_details.*, item_details.* from sales_details full outer join item_details ON (sales_details.item_code = item_details.item_code);
```

##### SEMI JOIN

Hive does not provide 'IN' Clause instead provides  for SEMI INNER JOIN
```
select * from item_details LEFT SEMI JOIN sales_details ON (sales_details.item_code= item_details.item_code);

Shampoo                 101     150
ToothPaste              102     76
ToothBrush              103     50
```

#### Sub queries:
A Query present within a Query is known as a sub query. The main query will depend on the values returned by the subqueries.

Hive does have a support of SUB-QUERIES from version-0.13. So you can use this version. Or you can try this query:
```
select * from table1 t1 JOIN (select 100_string_column as col2 from table2 where (whatever your condition is)) t2 ON t1.<matching_column> = t2.col2
```

* Subqueries can be classified into two types
    * Subqueries in FROM clause
    * Subqueries in WHERE clause
* When to use:

To get a particular value combined from two column values from different tables
Dependency of one table values on other tables
Comparative checking of one column values from other tables

* Syntax:

```
Subquery in FROM clause
SELECT <column names 1, 2…n>From (SubQuery) <TableName_Main >
Subquery in WHERE clause
SELECT <column names 1, 2…n> From<TableName_Main>WHERE col1 IN (SubQuery);
```
* Example:

SELECT col1 FROM (SELECT a+b AS col1 FROM t1) t2

Source : https://www.guru99.com/hive-join-subquery.html
