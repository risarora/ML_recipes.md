### <code>grep</code> command  

grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p, which has the same effect: doing a global search with the regular expression and printing all matching lines.




```shell

$ cat myFile.txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
```

### Arguments

#### FILES WITHOUT-MATCH
-L, --files-without-match

```shell
grep -L veniam myFile.txt
```

#### FILES WITH-MATCHES
-l, --files-with-matches
```shell
grep -l veniam myFile.txt

```

#### INVERT MATCH
-v, --invert-match
```shell
grep -l veniam myFile.txt

```
#### IGNORE CASE
-i, --ignore-case
```shell
grep -l VENIAM myFile.txt

```
#### WITH FILENAME
-H, --with-filename

```shell
grep -H veniam myFile.txt

```
#### NO FILENAME
-h, --no-filename
```shell
grep -h veniam myFile.txt

```
#### COUNT OF Matching records
<code>grep -c, --count
```shell
grep -c veniam myFile.txt
1
```
#### Line Number
-n, --line-number
```shell
```

#### Pipes and Filter

#### cat
cat HIVE_plan_limit_2018_11_14.log  | grep "map 100%"
2020-11-13 08:09:58.460 [main] [INFO ] mapreduce.Job:  map 100% reduce 0%

#### Others Options


#### Matching the lines that start with a string :
The ^ regular expression pattern specifies the start of a line. This can be used in grep to match the lines which start with the given string or pattern.

$ grep "^unix" geekfile.txt
Output:

unix is great os. unix is opensource. unix is free os.


#### Matching the lines that end with a string :
The $ regular expression pattern specifies the end of a line. This can be used in grep to match the lines which end with the given string or pattern.

$ grep "os$" geekfile.txt
