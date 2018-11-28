### Install Elastic Search
1.  Download elasticsearch zip file from https://www.elastic.co/downloads/elasticsearch and unzip the file
2.  Set JAVA_HOME
3.  Run the elasticsearch.bat file present in the bin folder
4.  Check whether the it has started by visiting http://localhost:9200/ in the browser
5.  Now we are ready to index document and search them via CURL commands in command window
6.  For more user friendly requests install Head Plugin for elasticsearch  by running below in command window
    + **cd elasticsearch/bin/**
    + **plugin install mobz/elasticsearch-head**  
Check the plugin from http://localhost:9200/_plugin/head


### Install Elastic Search


curl -L -O https://download.elasticsearch.org/kibana/kibana/kibana-
4.1.1-linux-x64.tar.gz

curl –L –O https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.2.zip


curl -L -O https://download.elasticsearch.org/kibana/kibana/kibana-4.1.1-windows.zip
unzip kibana-4.1.1-windows.zip


## Testing Machine
SERVER
http://SERVER:9200/_plugin/kopf/

##### Elastic URL
http://localhost:9200

##### Kibana URL
http://localhost:5601/#/settings/indices/?_g=%28%29




#### Shutting down Elasticsearch
GET http://localhost:9000/: This command retrieves basic information
about Elasticsearch
• GET http://localhost:9200/_cluster/state/nodes/: This command
retrieves the information about the nodes in the cluster
• POST http://localhost:9200/_cluster/nodes/_shutdown: This
command sends a shutdown request to all the nodes in the cluster



#### Automatic identifier creation
curl -XPUT http://localhost:9200/blog/article/1 -d '{"title": "New version of Elasticsearch released!", "content": "Version 1.0 released today!", "tags": ["announce", "elasticsearch", "release"] }'

curl -XGET http://localhost:9200/blog/article/1

Importing a JSON file into Elasticsearch

sudo curl --silent --location https://deb.nodesource.com/setup_0.12 | sudo bash -



#### Elastic Notes

**Field**: This is the smallest single unit of data stored in Elasticsearch. It is similar to a column in a traditional relational database. Every document contains key-value pairs, which are referred to as fields. Values in a field can contain a single value, such as integer [27] ,  string ["Kibana"] , or multiple values, such as  array [1, 2, 3, 4, 5] . The field type is responsible for specifying which type of data can be stored in
a particular field, for example,  integer ,  string ,  date , and so on.

**Document**: This is the simplest unit of information stored in Elasticsearch. It is a collection of fields. It is considered similar to a row of a table in a traditional relational database. A document can contain any type of entry, such as a document for a single restaurant, another document for a single cuisine, and yet another for a single order. Documents are in JavaScript Object Notation (JSON), which is a language-independent data interchange format. JSON contains key-value pairs. Every document that is stored in Elasticsearch is indexed. Every document contains a type and an ID.

**Type**: This is similar to a table in a traditional relational database. It contains a list of fields, which is defined for every document. A type is a logical segregation of indexes, whose interpretation/semantics entirely depends on you. For example, you have data about the world and you put all your data into an index. In this index, you can define a type for continent-wise data, another type for country-wise data, and a third type for region-wise data. Types are used with a mapping API; it specifies the type of its field.

**Index**: This is a collection of documents (one or more than one). It is similar to a database in the analogy with traditional relational databases. For example, you can have an index for user information, transaction information, and product type. An index has a mapping; this mapping is used to define multiple types. In other words, an index can contain single or multiple types. An index is defined by a name, which is always used whenever referring to an index to perform search, update, and delete operations for documents. You can define any number of indexes you require. Indexes also act as logical namespaces that map documents to primary shards, which contain zero or more replica shards for replicating data. With respect to traditional databases, the basic analogy is similar to the following:

    MySQL => Databases => Tables => Columns/Rows
    Elasticsearch => Indexes => Types => Documents with Fields

Note :-
    The combination of index, type, and ID must be unique for each document.

## Other Key words
 - Mapping :
 - Node
 - Cluster
 - Sharding
     + Primary Shard
     + Replica Shard
 - Inverted Index




### Create Index :
*URL*: http://localhost:9200/schools
*Request Type* POST
*Body*:

     <index specific setting >

*Response :*

    {"acknowledged": true}


###Create Mapping and Add data
*URL*: http://localhost:9200/schools/_bulk
*Request Type* POST
*Body*:

    {"index":{"_index":"schools","_type":"school", "_id":"1"}}
    {"name":"Central School", "description":"CBSE Affiliation","street":"Nagan", "city":"paprola","state":"HP","zip":"176115",  "location":[31.8955385,76.8380405], "fees":2000, "tags":["Senior Secondary","beautiful campus"],"rating":"3.5"}
    {"index":{"_index":"schools","_type":"school","_id":"2"}}
    {"name":"Saint Paul School","description":"ICSE Afiliation","street":"Dawarka","city":"Delhi","state":"Delhi","zip":"110075","location":[28.5733056,77.0122136],"fees":5000, "tags":["Good Faculty","Great Sports"],"rating":"4.5"}
    {"index":{"_index":"schools","_type":"school","_id":"3"}}
    {"name":"Crescent School","description":"State Board Affiliation","street":"Tonk Road","city":"Jaipur","state":"RJ","zip":"176114","location":[26.8535922,75.7923988],"fees":2500,"tags":["Well equipped labs"],"rating":"4.5"}

*Response :*

    {"acknowledged": true}



###Search Index :

*URL* http://localhost:9200/schools/_search
*Request Type* POST
*Body*:

    {
    "query":{
    "match_all":{}
    }
    }

##### Crete another Index

*URL* http://localhost:9200/schools_gov  
*Request Type* POST  
*Body*:  

    Body Here

##### Add Elements

*URL* http://localhost:9200/schools_guv/bulk  
*Request Type* POST  
*Body*:  

    {"index":{"_index":"schools_gov", "_type":"school", "_id":"1"}}
    {"name":"Model School", "description":"CBSE Affiliation",
    "street":"silk city", "city":"Hyderabad", "state":"AP", "zip":"500030",
    "location":[17.3903703,78.4752129], "fees":200,
    "tags":["Senior Secondary", "beautiful campus"],"rating":"3"}

    {"index":{"_index":"schools_gov", "_type":"school", "_id":"2"}}
    {"name":"Government School", "description":"State Board Affiliation",
    "street":"Hinjewadi", "city":"Pune", "state":"MH", "zip":"411057",
    "location": [18.599752, 73.6821995],"fees":500,"tags":["Great
    Sports"],"rating":"4"}

*Response*:

    Response Body Here



##### Action

*URL*http://localhost:9200/
*Request Type* POST
*Body*:

    Body Here

*Response*:

    Response Body Here


##### Action

*URL*http://localhost:9200/
*Request Type* POST
*Body*:

    Body Here

*Response*:

    Response Body Here


##### Action

*URL*  http://localhost:9200/  
*Request Type* POST  
*Body*:

    Body Here

*Response*:

    Response Body Here


##### Action

*URL* http://localhost:9200/  
*Request Type* POST  
*Body*:  

    Body Here

*Response*:

    Response Body Here
