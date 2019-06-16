## Hive Data Types

Hive supports different data types to be used in table columns. The data types supported by Hive can be broadly classified in Primitive and Complex data types.

The __primitive data__ types supported by Hive are listed below:
1. **Numeric Types**
	* TINYINT (1-byte signed integer, from -128 to 127)
	* SMALLINT (2-byte signed integer, from -32,768 to 32,767)
	* INT (4-byte signed integer, from -2,147,483,648 to 2,147,483,647)
	* BIGINT (8-byte signed integer, from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
	* FLOAT (4-byte single precision floating point number)
	* DOUBLE (8-byte double precision floating point number)
	* DECIMAL (Hive 0.13.0 introduced user definable precision and scale)
2. **Date/Time Types**
	* TIMESTAMP
	* DATE
3. **String Types**
	* STRING
	* VARCHAR
	* CHAR
4. **Misc Types**
	* BOOLEAN
	* BINARY

Apart from these primitive data types Hive offers some complex data types which are listed below:

5. **Complex Types**
	* arrays: ARRAY<data_type>
	* maps: MAP<primitive_type, data_type>
	* structs: STRUCT<col_name : data_type [COMMENT col_comment], ...>
	* union: UNIONTYPE<data_type, data_type, ...>


### COMPLEX DATA Types - ARRAY

```
ARRAY_Technology_Data.txt
1,Amit,4000,Java$Spring$Struts, Hyderabad
2,Manu,3000,C#$.NET$, Banglore
3,Zeenat,3000,d$f$, CHENNAI
```

```
Create table if not exists Emp_Technology_Details_ARRAY (
ID TINYINT,
Name STRING,
SALARY INT,
Technology ARRAY<String>,
Base_City STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '$'
--MAP KEYS TERMINATED BY '#'
STORED AS TEXTFILE;


LOAD DATA LOCAL INPATH 'Hive/ARRAY_Technology_Data.txt'
OVERWRITE INTO TABLE Emp_Technology_Details_ARRAY;

select * from Emp_Technology_Details_ARRAY;
hive> select * from Emp_Technology_Details_ARRAY;
OK
1       Amit    4000    ["Java","Spring","Struts"]       Hyderabad
2       Manu    3000    ["Cpp",".NET",""]         Banglore
3       Zeenat  3000    ["d","f",""]     CHENNAI
Time taken: 3.372 seconds

select Name,Technology[1] from Emp_Technology_Details_ARRAY;
hive>select Name,Technology[1] from Emp_Technology_Details_ARRAY;

OK
Amit    Spring
Manu    .NET
Zeenat  Oracle
Time taken: 11.222 seconds

drop table  Emp_Technology_Details_ARRAY;
```
### COMPLEX DATA Types - MAP
```
MAP_Technology_Data.txt
1,Amit,4000,Java$Spring$Struts,pf#1200$epf#800,Hyderabad
2,Manu,3000,C#$.NET$,pf#1150$epf#600,Banglore
3,Zeenat,3000,SQL$Oracle$,pf#1240,CHENNAI

```

```
Create table if not exists Emp_Technology_Details_MAP (
ID TINYINT,
Name STRING,
SALARY INT,
Technology ARRAY<String>,
Deduction MAP<String,INT>,
Base_City STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '$'
MAP KEYS TERMINATED BY '#';
--STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'Hive/MAP_Technology_Data.txt'
OVERWRITE INTO TABLE Emp_Technology_Details_MAP;

select * from Emp_Technology_Details_MAP;

hive> select * from Emp_Technology_Details_MAP;
OK
1       Amit    4000    ["Java","Spring","Struts"]      {"pf":1200,"epf":800}   Hyderabad
2       Manu    3000    ["C#",".NET",""]        {"pf":1150,"epf":600}   Banglore
3       Zeenat  3000    ["SQL","Oracle",""]     {"pf":1240}     CHENNAI
Time taken: 0.232 seconds
hive>

select Name,Technology[1], deduction["pf"] from Emp_Technology_Details_MAP;
OK
Amit    Spring  1200
Manu    .NET    1150
Zeenat  Oracle  1240
Time taken: 11.222 seconds
hive>
```

### COMPLEX DATA Types - STRUCT

```
STRUCT_Technology_Data.txt
1,Amit,4000,Java$Spring$Struts,pf#1200$epf#800,Hyderabad$AndhraPRADESH$220001
2,Manu,3000,C#$.NET$,pf#1150$epf#600,Banglore$Karnataka$330001
3,Zeenat,3000,SQL$Oracle$,pf#1240,CHENNAI$Tamil Nadu$440001
```

```
Create table if not exists Emp_Technology_Details_STRUCT (
ID TINYINT,
Name STRING,
SALARY INT,
Technology ARRAY<String>,
Deduction MAP<String,INT>,
ADDRESS STRUCT <City :STRING, State:STRING, PIN:BIGINT>)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '$'
MAP KEYS TERMINATED BY '#';
--STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'Hive/STRUCT_Technology_Data.txt'
OVERWRITE INTO TABLE Emp_Technology_Details_STRUCT;

select * from Emp_Technology_Details_STRUCT;

hive> select * from Emp_Technology_Details_STRUCT;
OK
1       Amit    4000    ["Java","Spring","Struts"]      {"pf":1200,"epf":800}   {"city":"Hyderabad","state":"AndhraPRADESH","pin":220001}
2       Manu    3000    ["C#",".NET",""]        {"pf":1150,"epf":600}   {"city":"Banglore","state":"Karnataka","pin":330001}
3       Zeenat  3000    ["SQL","Oracle",""]     {"pf":1240}     {"city":"CHENNAI","state":"Tamil Nadu","pin":440001}
Time taken: 3.059 seconds
hive>

select Name,Technology[1], deduction["pf"],address.city from Emp_Technology_Details_STRUCT;
OK
Amit    Spring  1200    Hyderabad
Manu    .NET    1150    Banglore
Zeenat  Oracle  1240    CHENNAI
Time taken: 11.298 seconds
hive>
```
