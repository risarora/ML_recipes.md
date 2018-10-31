### Replace - Sed
```shell
$ sed -i 's/ugly/beautiful/g' /home/bruno/old-friends/sue.txt
```
<code>sed</code> is used to replace the found expression "ugly" with "beautiful"
* **g** stands for "global", meaning to do this for the whole line. If you leave off the g and "ugly" appears twice on the same line, only the first "ugly" is changed to "beautiful".
* **-i** option is used to edit in place on filename.
* *-e* option indicates a command to run.

$ sed -i 's/<old>/<new>/g' <filepath>

vi
:1,$ s/<old>/<new>/gc

### Replace Tabs with comma output of Hive Query
```shell
bash >> hive -e 'select * from some_Table' | sed 's/[\t]/,/g'  > outputfile.txt
```
### Replace New Line

```shell
sed ':a;N;$!ba;s/\n/ /g' (FileName) >   (FileName)
sed ':a;N;$!ba;s/\n/ /g' row.txt > newrow.txt
```
### Replace first Character of each line with <New Character>

```shell
sed -i -e 's/^/<New Character>/' /home/brockadm/monitor/out.txt
```
### Add ';' at the end of each line
```shell
sed -i -e 's/$/;/' Tableslist.list
```

### Others
```shell

sed -i '' /<PATH>/out.txt

sed -i -e 's/^/describe extended /' Tableslist.list

sed -i -e '/^$/d' myFile
```

http://stackoverflow.com/questions/1251999/how-can-i-replace-a-newline-n-using-sed
