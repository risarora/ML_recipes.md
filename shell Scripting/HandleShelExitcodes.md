caller.sh 
-----------------------------------------------------
#!/bin/bash
SCRIPT_PATH="./scriptP.sh"

echo " Test Case 1"
OUTPUT=$("$SCRIPT_PATH" "Rishi" "Arora")
status=$?
echo "OUTPUT "${OUTPUT}
echo "status "${status}
if [ $OUTPUT -eq 0 ]; then
  echo "Captured Failure Successfully"
fi

# or
echo " Test Case 2"
OUTPUT=`"$SCRIPT_PATH"`
echo "OUTPUT "${OUTPUT}
echo "status "${status}

if [ $OUTPUT -eq 0 ]; then
  echo "Captured Failure Successfully"
fi

echo " Reached end of Script"
##############################################
./scriptP.sh
----------------------------------------------
#!/bin/bash
./script.sh $1 $2


##############################################
./script.sh
----------------------------------------------
#!/bin/bash
fname=$1
lname=$2
cat file.txt

if [ $? -eq 0 ]
then
echo "The script ran ok"
  exit 0
else
  echo "The script failed ${1} ${2}" #>&2
  exit 11
fi



############################################
$ ./caller.sh 
 Test Case 1
+ ./script.sh Rishi Arora
cat: file.txt: No such file or directory
OUTPUT The script failed Rishi Arora
status 11
Captured Failure Successfully
 Reached end of Script
