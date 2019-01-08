## To check if a directory exists in a shell script you can use the following:

```
if [ -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY exists.
fi
Or to check if a directory doesn't exist:

if [ ! -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
fi
```
However, subsequent commands may not work as intended if you do not take into account that a symbolic link to a directory will also pass this check. E.g. running this:

```
ln -s "$ACTUAL_DIR" "$SYMLINK"
if [ -d "$SYMLINK" ]; then
  rmdir "$SYMLINK"
fi
```
Will produce the error message:

rmdir: failed to remove `symlink`: Not a directory
So symbolic links may have to be treated differently, if subsequent commands expect directories:
```
if [ -d "$LINK_OR_DIR" ]; then
  if [ -L "$LINK_OR_DIR" ]; then
    # It is a symlink!
    # Symbolic link specific commands go here.
    rm "$LINK_OR_DIR"
  else
    # It's a directory!
    # Directory command goes here.
    rmdir "$LINK_OR_DIR"
  fi
fi

```


Other Variations

Note: Be careful, leave empty spaces on either side of both opening and closing braces.

With the same syntax you can use:

 * -e: any kind of archive 
 * -f: file 
 * -h: symbolic link 
 * -r: readable file 
 * -w: writable file 
 * -x: executable file 
 * -s: file size greater than zero 

source
https://stackoverflow.com/questions/59838/check-if-a-directory-exists-in-a-shell-script
