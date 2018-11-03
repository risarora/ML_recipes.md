## File Permissions


File permissions of a linux are <code>read</code>, <code>write</code> and/or <code>execute</code> and the allocated to <code>user</code>, <code>group</code> and <code>everyone</code> respectively.

### How not to forget file permissions
permission code | r/w/x | decimal number | permissions
---|---|---| ---
000|---|0 | No permissions
001|--x|1 | execute
010|-w-|2 |write
011|-wx|3 |write and execute
100|r--|4 |read
101|r-x|5 |read and execute
110|rw-|6 |read and write
111|rwx|7 |read, write, and execute

### View File Permissions

User can view a files permissions using <code>ls -l </code> command.

**Example :**

```
$ ls -l x
-rw-r--r--. 1 rarora17 dce 0 Nov  2 07:04 userdataFile.csv
```

Permission Code | Permission For | permissions
---|---|---
rw- |Owner| Read and Write
r--|Group |Read only
r--|Everyone |Read only

### Change File permissions
To change the permissions of a file or directory we use the <code>chmod</code> command. chmod takes three digits, each one representing the permissions for the user, group, and everyone. Thus, 741 would mean:

permission code | r/w/x | Decimal number | Permissions| For
---|---|---|---|---
111|rwx|7 |read, write, and execute |owner
100|r--|4 |read | group
001|--x|1 |execute | everyone

```shell
$ ls -l x
-rw-r--r--. 1 rarora17 dce 0 Nov  2 07:04 userdataFile.csv
$ chmod 741 userdataFile.csv
$ ls -l userdataFile.csv
-rwxr----x. 1 rarora17 dce 0 Nov  2 07:24 userdataFile.csv
$
```
