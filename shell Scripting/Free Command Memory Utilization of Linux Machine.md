### Memory Utilization of Linux Machine

<code>Free</code> command is used to view the memory details of the machine.

```shell
$ free
              total        used        free      shared  buff/cache   available
Mem:      263934836   100673952    19698488     1231508   143562396   160307796
Swap:       4194300      536100     3658200
rarora17@dbsls0324:/home/rishi
$

$ free | grep Mem | awk '{print $3/$2 * 100.0}'
37.8405
rarora17@rishiMachine:/home/rishi
$
rarora17@rishiMachine:/home/rishi
```

### This will report the percentage of memory that's free

```
rarora17@rishiMachine:/home/rishi
$ free | grep Mem | awk '{print $4/$2 * 100.0}'
7.87074
rarora17@rishiMachine:/home/rishi
$
rarora17@rishiMachine:/home/rishi
$ free | grep Mem | awk '{ printf("free: %.4f %\n", $4/$2 * 100.0) }'
free: 7.8707 %
rarora17@rishiMachine:/home/rishi
$
```

### View the free memory in the machine in Gigabytes.

```shell
$ free -g
              total        used        free      shared  buff/cache   available
Mem:            251          98          16           1         137         150
Swap:             3           0           3
rarora17@dbsls0324:/home/rarora17/e2e/automatedcirrusLoads
$
```


### Clear the cache memory

``` shell
$ sudo su -
root@rishiMachine:/root
# sudo sync; echo 3 > /proc/sys/vm/drop_caches
root@rishiMachine:/root
sudo sync; echo 3 > /proc/sys/vm/drop_caches
# exit
logout
```
