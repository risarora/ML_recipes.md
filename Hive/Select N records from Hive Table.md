## Select Top N records from Hive Table

### Create a Hive table and insert some records
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

### Hive Select all rows
```
hive> select * from employeeX;
OK
3	UserC	IT
1	UserA	SER
4	UserD	SER
2	UserB	IT
6	UserF	HR
5	UserE	SER
Time taken: 4.132 seconds, Fetched: 6 row(s)
```

### Hive Select N rows

```
Time taken: 1.222 seconds
hive> select * from employeeX limit 3;
OK
3	UserC	IT
1	UserA	SER
4	UserD	SER
Time taken: 0.506 seconds, Fetched: 3 row(s)
hive>
```
### Select Top N rows ordered by Ascending (default)

```
hive> select * from employeeX order by emp_id limit 3;
WARNING: Hive-on-MR is deprecated in Hive 2 and may not be available in the future versions. Consider using a different execution engine (i.e. spark, tez) or using Hive 1.X releases.
Query ID = lakeuser_20190510083822_3123123-ase-232224asdf
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_1553616708_4572234, Tracking URL = https://mylake:8090/proxy/application_1556300316708_657139/
Kill Command = /user/hadoop/hadoop-2.7.0/bin/hadoop job  -kill job_1553616708_4572234
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
2019-05-10 08:38:47,694 Stage-1 map = 0%,  reduce = 0%
2019-05-10 08:39:18,119 Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 14.78 sec
2019-05-10 08:39:43,890 Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 19.28 sec
MapReduce Total cumulative CPU time: 19 seconds 280 msec
Ended Job = job_1553616708_4572234
MapReduce Jobs Launched:
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 19.28 sec   MAPRFS Read: 0 MAPRFS Write: 0 SUCCESS
Total MapReduce CPU Time Spent: 19 seconds 280 msec
OK
1	UserA	SER
2	UserB	IT
3	UserC	IT
Time taken: 82.633 seconds, Fetched: 3 row(s)
```

### Select Top N rows ordered by Descending
```
hive> select * from employeeX order by emp_id desc limit 3;
WARNING: Hive-on-MR is deprecated in Hive 2 and may not be available in the future versions. Consider using a different execution engine (i.e. spark, tez) or using Hive 1.X releases.
Query ID = lakeuser_20190510084222_3123123-ase-232224asdf
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks determined at compile time: 1
In order to change the average load for a reducer (in bytes):
  set hive.exec.reducers.bytes.per.reducer=<number>
In order to limit the maximum number of reducers:
  set hive.exec.reducers.max=<number>
In order to set a constant number of reducers:
  set mapreduce.job.reduces=<number>
Starting Job = job_15533313440_657429, Tracking URL = https://mylake:8090/proxy/application_1556300316708_657429/
Kill Command = /user/hadoop/hadoop-2.7.0/bin/hadoop job  -kill job_15533313440_657429
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 1
2019-05-10 08:42:52,843 Stage-1 map = 0%,  reduce = 0%
2019-05-10 08:43:21,950 Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 10.46 sec
2019-05-10 08:43:44,994 Stage-1 map = 100%,  reduce = 100%, Cumulative CPU 15.44 sec
MapReduce Total cumulative CPU time: 15 seconds 440 msec
Ended Job = job_15533313440_657429
MapReduce Jobs Launched:
Stage-Stage-1: Map: 1  Reduce: 1   Cumulative CPU: 15.44 sec   MAPRFS Read: 0 MAPRFS Write: 0 SUCCESS
Total MapReduce CPU Time Spent: 15 seconds 440 msec
OK
6	UserF	HR
5	UserE	SER
4	UserD	SER
Time taken: 85.132 seconds, Fetched: 3 row(s)
```
