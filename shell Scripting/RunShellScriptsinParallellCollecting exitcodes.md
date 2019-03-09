### Collect exit codes for background scripts in parallel

```
script3 will be executed only if script1 and script2 are successful and script1 and script2 will be executed in parallel:

./script1 &
process1=$!

./script2 &
process2=$!

wait $process1
rc1=$?

wait $process2
rc2=$?

if [[ $rc1 -eq 0 ]] && [[ $rc2 -eq 0  ]];then
./script3
fi

```


source :https://unix.stackexchange.com/questions/344360/collect-exit-codes-of-parallel-background-processes-sub-shells#344367
