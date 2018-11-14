## Check for a String Partial match in shell

There are a few ways to find out if a string contains a substring using bash. Below are a couple of ways this can be done without invoking any other processes.


#### Star Wildcard
You can use wildcards (*) outside a case statement, too, if you use double brackets:
One very simple method is to match strings using the * character to denote any number of other characters. For example:

```shell

if [[ "$string" == *"$substring"* ]]; then
    echo "'$string' contains '$substring'";
else
    echo "'$string' does not contain '$substring'";
fi
```
If you want to find if a string begins with substring, only use the * character after substring. ie: [[ "$string" == "$substring"* ]]. Similarly, omit the first * character to match strings ending with substring.

#### Regular Expressions
More advanced pattern matching can be done using regular expressions. In it’s most basic form, we can do simple substring matching like so:

```shell
if [[ "$string" =~ $substring ]]; then
    echo "'$string' contains '$substring'";
else
    echo "'$string' does not contain '$substring'";
fi
```

This method is computationally slower than the first method, but it can be expanded with other regular expression syntax to do more powerful pattern matching, such as matching strings which contain the substring on word boundaries.
See http://linux.die.net/Bash-Beginners-Guide/sect_04_01.html#sect_04_01_02 for more details on bash regular expression syntax.
[source][link="https://timmurphy.org/2013/05/13/string-contains-substring-in-bash/"]


#### Create a function

```shell
# contains(string, substring)
#
# Returns 0 if the specified string contains the specified substring,
# otherwise returns 1.
contains() {
    string="$1"
    substring="$2"
    if test "${string#*$substring}" != "$string"
    then
        return 0    # $substring is in $string
    else
        return 1    # $substring is not in $string
    fi
}

contains "abcd" "e" || echo "abcd does not contain e"
contains "abcd" "ab" && echo "abcd contains ab"
contains "abcd" "bc" && echo "abcd contains bc"
contains "abcd" "cd" && echo "abcd contains cd"
contains "abcd" "abcd" && echo "abcd contains abcd"
contains "" "" && echo "empty string contains empty string"
contains "a" "" && echo "a contains empty string"
contains "" "a" || echo "empty string does not contain a"
contains "abcd efgh" "cd ef" && echo "abcd efgh contains cd ef"
contains "abcd efgh" " " && echo "abcd efgh contains a space"


```

https://stackoverflow.com/questions/2829613/how-do-you-tell-if-a-string-contains-another-string-in-posix-sh


**Example 1**, check for 'yes' in string (case insensitive):
```shell
if [[ "${str,,}" == *"yes"* ]] ;then
```
**Example 2**, check for 'yes' in string (case insensitive):
```shell
if [[ "$(echo "$str" | tr '[:upper:]' '[:lower:]')" == *"yes"* ]] ;then
```
**Example 3**, check for 'yes' in string (case sensitive) :
```shell

 if [[ "${str}" == *"yes"* ]] ;then
```
**Example 4**, check for 'yes' in string (case sensitive):
```shell

 if [[ "${str}" =~ "yes" ]] ;then
```
**Example 5**, exact match (case sensitive):
```shell

 if [[ "${str}" == "yes" ]] ;then
```
**Example 6**, exact match (case insensitive):
```shell
 if [[ "${str,,}" == "yes" ]] ;then
```
**Example 7**, exact match :

```shell
if [ "$a" = "$b" ] ;then
```
