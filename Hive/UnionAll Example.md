## UNION ALL usage in Hive

UNION ALL is used to combine the result from multiple SELECT statements into a single result set.
Duplicate records are displayed.
Each SELECT statement within the UNION ALL must have the same number of columns.
The columns must also have similar data types and similar names.
Also, the columns in each SELECT statement must be in the same order. Otherwise, a schema error is thrown.

Lets create 3 tables.

```
create table employeeX (emp_id BIGINT, emp_name STRING, dept_id STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

insert into employeeX values(001,'UserA','SER');
insert into employeeX values(002,'UserB','IT');
insert into employeeX values(003,'UserC','IT');
insert into employeeX values(004,'UserD','SER');
insert into employeeX values(005,'UserE','SER');
insert into employeeX values(006,'UserF','HR');
```


Work Information Table

```
create table workinfo (emp_id BIGINT,emp_name STRING, dept_id STRING,work_status STRING,country STRING, state STRING, emp_age INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

insert into workinfo values(001,'UserA','SER','Full Time','USA','MA',25);
insert into workinfo values(002,'UserB','IT','Full Time','USA','NJ',32);
insert into workinfo values(003,'UserC','IT','Intern','India','MUM',35);
insert into workinfo values(004,'UserD','SER','Full Time','UK','LON',29);
insert into workinfo values(005,'UserE','SER','Part Time','Swiss','Zur',25);
insert into workinfo values(006,'UserF','HR','Part Time','USA','MI',25);
```

Department Information
```
create table department (dept_id STRING, dept_name STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

insert into department values ('IT','Information Technology');
insert into department values ('SER','Service');
insert into department values ('HR','Human Resources');
```
```
select * from department;
select * from workinfo;
select * from employeeX;
```
Query to check which users are of what work status, works for which department, belongs to which country, state and what are their ages
```
select temp.emp_name,temp.dept_id,
w.work_status, w.country, w.state, w.emp_age, d.dept_name
from
(select e.emp_id,e.emp_name,e.dept_id
from employeeX e

UNION ALL

select w.emp_id,w.emp_name,w.dept_id
from workinfo w)
temp join workinfo w on (temp.emp_id = w.emp_id) join department d on (w.dept_id = d.dept_id);

```


```
select temp.emp_name,temp.dept_id,
w.work_status, w.country, w.state, w.emp_age, d.dept_name
from
(select e.emp_id,e.emp_name,e.dept_id
from employeeX e

UNION

select w.emp_id,w.emp_name,w.dept_id
from workinfo w)
temp join workinfo w on (temp.emp_id = w.emp_id) join department d on (w.dept_id = d.dept_id);
```
