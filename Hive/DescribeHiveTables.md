## Describe Hive Table
There are three ways to describe a table in Hive.

#### 1. To see table primary info of Hive table, use describe table_name; command

```
hive> describe employeeX;
OK
emp_id              	bigint
emp_name            	string
dept_id             	string
Time taken: 0.503 seconds, Fetched: 3 row(s)

```
#### 2. To view detailed information about the table, use describe extended table_name; command

```
hive> describe extended employeeX;
OK
emp_id              	bigint
emp_name            	string
dept_id             	string
Detailed Table Information	Table(tableName:employeex, dbName:test, owner:lakeowner, createTime:1556883898, lastAccessTime:0, retention:0, sd:StorageDescriptor(cols:[FieldSchema(name:emp_id, type:bigint, comment:null), FieldSchema(name:emp_name, type:string, comment:null), FieldSchema(name:dept_id, type:string, comment:null)], location:maprfs:/mydatalake/hive/warehouse/test.db/employeex, inputFormat:org.apache.hadoop.mapred.TextInputFormat, outputFormat:org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat, compressed:false, numBuckets:-1, serdeInfo:SerDeInfo(name:null, serializationLib:org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, parameters:{serialization.format=,, line.delim=
, field.delim=,}), bucketCols:[], sortCols:[], parameters:{}, skewedInfo:SkewedInfo(skewedColNames:[], skewedColValues:[], skewedColValueLocationMaps:{}), storedAsSubDirectories:false), partitionKeys:[], parameters:{totalSize=69, numRows=6, rawDataSize=63, COLUMN_STATS_ACCURATE={"BASIC_STATS":"true"}, numFiles=6, transient_lastDdlTime=1556884179}, viewOriginalText:null, viewExpandedText:null, tableType:MANAGED_TABLE)
Time taken: 0.799 seconds, Fetched: 6 row(s)

```

#### 3. To see code in a clean manner use describe formatted table_name; command to see all information.
also describe all details in a clean manner.

```
hive> describe formatted  employeeX;
OK
# col_name            	data_type           	comment

emp_id              	bigint
emp_name            	string
dept_id             	string

# Detailed Table Information
Database:           	test
Owner:              	lakeowner
CreateTime:         	Fri May 03 06:44:58 CDT 2019
LastAccessTime:     	UNKNOWN
Retention:          	0
Location:           	maprfs:/mydatalake/hive/warehouse/test.db/employeex
Table Type:         	MANAGED_TABLE
Table Parameters:
	COLUMN_STATS_ACCURATE	{\"BASIC_STATS\":\"true\"}
	numFiles            	6
	numRows             	6
	rawDataSize         	63
	totalSize           	69
	transient_lastDdlTime	1556884179

# Storage Information
SerDe Library:      	org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe
InputFormat:        	org.apache.hadoop.mapred.TextInputFormat
OutputFormat:       	org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat
Compressed:         	No
Num Buckets:        	-1
Bucket Columns:     	[]
Sort Columns:       	[]
Storage Desc Params:
	field.delim         	,
	line.delim          	\n
	serialization.format	,
Time taken: 0.64 seconds, Fetched: 34 row(s)
hive>
```

#### 4. View Table Create Query

```
hive>
    > show create table employeeX;
OK
CREATE TABLE `employeeX`(
  `emp_id` bigint,
  `emp_name` string,
  `dept_id` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'field.delim'=',',
  'line.delim'='\n',
  'serialization.format'=',')
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'maprfs:/mydatalake/hive/warehouse/test.db/employeex'
TBLPROPERTIES (
  'COLUMN_STATS_ACCURATE'='{\"BASIC_STATS\":\"true\"}',
  'numFiles'='6',
  'numRows'='6',
  'rawDataSize'='63',
  'totalSize'='69',
  'transient_lastDdlTime'='1556884179')
Time taken: 0.468 seconds, Fetched: 23 row(s)
hive>

```
