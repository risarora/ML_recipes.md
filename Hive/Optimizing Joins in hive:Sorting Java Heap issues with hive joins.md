## Optimizing Joins in hive/Sorting Java Heap issues with hive joins
In hadoop we tend to use hive extensively since it is SQL like language and easier in framing our jobs with stored structured data. (Even Pig is great but still needs a little time to get comfortable with Pig Latin). But as beginners we often get struck with hive joins in large data sets. It is a common scenario running into out of memory/java heap space errors on joins with huge hive tables. We can avoid these bottlenecks to a greater extent utilizing a few smarter options available with hive. Let us look into a few of them.

 1.       Enable map joins
It is a pretty good approach to enable map joins in hive when you are trying to do a join with multiple tables and if one or more of them has a smaller data volume. With this enabled the smaller tables would be distributed on the distributed cache as a hash table by a local map reduce task before the actual map reduce job. This could save considerable time as it turns to be map side join compared to running a common map reduce side join (normal hive join). You need to set the following at hive CLI before running the join Query
               set hive.auto.convert.join = true;

The point to be noted here is that, hive is intelligent enough with map side joins and if the data volume is larger not to fit into map side joins it executes the backup task, ie the common  join(full map reduce execution) to accomplish the job. So when you are taking performance into consideration the time to check on the executablity of map  join is an overhead, so if you are sure the data in the tables that you try to join is always huge then better not enabling the same for your job.
We were mentioning the term ‘small tables’ a lot here. But how small this table has to be? By default the small table size is 25 Mb. So if the table is larger than 25 Mb then the hive common join would be triggered. However 25Mb is conservative and you can modify the same to a desirable value by setting the following configuration variable.
                set hive.smalltable.filesize = 40000000;

 2.       Exploiting EQUI Join support in hive
Hive supports only Equi joins and we need to exploit the same in our hive query to get rid of OOM errors as well another common scenario of hive queries running infinitely. It is relatively straight forward, if your join query has a few where clauses with equality then include them inside the ON clause in your joins. It’d considerably reduce the number of records chosen to join and hence lesser number of records in sort phase.

                For eg: let us consider a query like this
Select Table1.Column1, Table2.Column2 FROM Table1 JOIN Table2 ON (Table1.Column5 = Table2.Column7 AND Table1.Column9=Table2.Column3) WHERE Table1.Column1 = ‘1024’ AND Table2.Column2 > 5;

This Query has an equality expression in the where clause involving one of the tables in join, we can optimize our hive query by including the equality filter condition as part of join as

Select Table1.Column1, Table2.Column2 FROM Table1 JOIN Table2 ON (Table1.Column5 = Table2.Column7 AND Table1.Column9=Table2.Column3 AND Table1.Column1 = ‘1024’) WHERE Table2.Column2 > 5;

The difference it creates in execution is that in first query after the join the filter condition is applied which means there would be more records involved in join but in the second query the filter condition is done before/on joining hence less records in join.

 3.       Increase the heap Size
Definitely this has to be one of the options if your hive query is already optimized and satisfies the first two checks and still the execution halts due to heap size issues. You can increase the heap size for the map reduce child tasks by setting the property ‘mapred.child.java.opts’ to a higher value.  Like for 1GB set it as
mapred.child.java.opts =  -Xmx1024m


Definitely there are many other options to deal with these issues like working on io.sort.mb deciding on the maximum number of mappers/reducers etc. Left up to your choice to google on and hit the bulls eye based on your use case/hive query
