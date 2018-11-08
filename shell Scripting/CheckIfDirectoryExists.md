#### To check if a directory exists

```shell
if [ -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY exists.
fi
Or to check if a directory doesn't exist:

if [ ! -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
fi
```


To check more than one directory use this code:

```shell
if [ -d "$DIRECTORY1" ] && [ -d "$DIRECTORY2" ] then
    # Things to do
fi
```

##### Other options

```shell
-e: any kind of archive 
-f: file 
-h: symbolic link 
-r: readable file 
-w: writable file 
-x: executable file 
-s: file size greater than zero 
```


Source : https://stackoverflow.com/questions/59838/check-if-a-directory-exists-in-a-shell-script