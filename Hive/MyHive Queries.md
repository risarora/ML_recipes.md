## Create Hive Table


```
Create table  Item_Details (
Name STRING,
ITEM_CODE SMALLINT,
Price TINYINT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

insert into Item_Details values ('Pullover'	,201,150);
insert into Item_Details values ('Socks'		,202,76);
insert into Item_Details values ('jacket'		,203,50);
insert into Item_Details values ('Shirt'		,2023423,20);
insert into Item_Details values ('Trousers'	,305,5AA);
insert into Item_Details values ('Frock' 		,410,88);

Item_Details.txt

Pullover,201,150
Socks,202,76
jacket,203,50
Shirt,2023423,20
Trousers,305,5AA
Frock,410,88


hive> LOAD DATA LOCAL INPATH '/home/training/MyDemos/Hive/Item_Details.txt'
OVERWRITE INTO TABLE ITEM_Details;
Copying data from file:/home/training/MyDemos/Hive/Item_Details.txt
Copying file: file:/home/training/MyDemos/Hive/Item_Details.txt
Loading data to table default.item_details
Deleted hdfs://localhost/user/hive/warehouse/item_details
OK
Time taken: 0.59 seconds
hive> select * from item_details;
OK
Pullover                201     NULL
Socks                   202     76
jacket                  203     50
Shirt                   NULL    20
Trousers                305     NULL
Frock                   410     88
Time taken: 0.159 seconds
hive>
```


#### ALTER Table
```
alter table <OLD NAME> rename to <NEW NAME>;

eg.
alter table SALES_rep rename to sales_details;
alter table SALES_ITEM rename to item_details;

```
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

select name,sales,item_code from sales_details ;
select Name,item_code,Price from item_details ;

#### FILTER
```
select sales_details.* from sales_details where item_code >103;
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

##################################################################

### View Table Details

DESCRIBE <TABLE_NAME>
DESCRIBE EXTENDED <TABLE_NAME>
DESCRIBE FORMATTED <TABLE_NAME>

EXPLAIN <HQL Query>
ILLUSTRATE <HQL Query>

##################################################################

OUTPUT TO DATA FILE/ TABLE
Insert overwrite table Items_used
select * from item_details LEFT SEMI JOIN sales_details ON (sales_details.item_code= item_details.item_code);

--Create table if not exists Items_used (
Create table  Items_used (
Name STRING,
ITEM_CODE SMALLINT,
Price TINYINT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

hive> Insert overwrite table Items_used
select * from item_details LEFT SEMI JOIN sales_details ON (sales_details.item_code= item_details.item_code);
Total MapReduce jobs = 1
Launching Job 1 out of 1
Number of reduce tasks not specified. Estimated from input data size: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
...................
Ended Job = job_201408150957_0021
Loading data to table default.items_used
Deleted hdfs://localhost/user/hive/warehouse/items_used
Table default.items_used stats: [num_partitions: 0, num_files: 1, num_rows: 0, total_size: 55]
3 Rows loaded to items_used
OK
Time taken: 20.923 seconds
hive> select * from items_used;
OK
Shampoo                 101     NULL
ToothPaste              102     76
ToothBrush              103     50
Time taken: 0.228 seconds
hive>

select item_code from item_details LEFT SEMI JOIN sales_details ON (sales_details.item_code= item_details.item_code);
101
102
103

########################################################

Hive does have a support of SUB-QUERIES from version-0.13. So you can use this version. Or you can try this query:

select * from table1 t1 JOIN (select 100_string_column as col2 from table2 where (whatever your condition is)) t2 ON t1.<matching_column> = t2.col2
########################################################

Sub Query
TBD

### UDF - User Defined Functions in Hive

Create UDF
A hive UDF must satisfy two conditions
1. UDF must be subclass of org.apache.hadoop.hive.ql.exec.UDF
2. UDF must implement atleast one evaluate methord.

```
%> hive
hive> ADD JAR <jar file path>;
hive> create temporary function <alias> as '<class package>';
hive> select alias(firstname) from <Table Name> <Condition>;
```
```
import org.apache.hadoop.hive.ql.exec.UDF;
import org.apache.hadoop.io.Text;

public class UpperCase extends UDF {

	private Text result = new Text();

	public Text evaluate(Text string) {
		if (string == null)
			return null;
		result.set(string.toString().toUpperCase());
		return result;
	}
}
```


* Create jar toUpperCase.jar

* Add jar /home/training/MyDemos/Hive/toUpperCase.jar

* CREATE TEMPORARY FUNCTION toUpper AS 'UpperCase';

```
 select toUpper(Name) from item_Details;
```
