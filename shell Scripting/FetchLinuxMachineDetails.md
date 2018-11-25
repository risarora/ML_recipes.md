$ cat /proc/version
rishi@machine1:/home/rishi/

$ lsb_release
LSB Version:    :xxxxxxxxxxxxxxxxxxxxx
rishi@machine1:/home/rishi/

$ lsb_release -a
LSB Version:    :xxxxxxxxxxxxxxxxxxxxxxxx
Distributor ID: RedHatEnterpriseServer
Description:    Red Hat Enterprise Linux Server release 7.4 (Maipo)
Release:        7.4
Codename:       Maipo
rishi@machine1:/home/rishi/


#### RAM Usage

```shell

$ cat /proc/meminfo
MemTotal:       313932336 kB
MemFree:         3112300 kB
MemAvailable:   316292324 kB
Buffers:           31312 kB
Cached:         314052324 kB
SwapCached:        31364 kB
Active:         318522324 kB
Inactive:       31132320 kB
Active(anon):   31002316 kB
Inactive(anon):  3102376 kB
Active(file):   31512308 kB
Inactive(file): 31332344 kB
Unevictable:        3168 kB
Mlocked:            3168 kB
SwapTotal:       3192300 kB
SwapFree:        3162344 kB
Dirty:              3180 kB
Writeback:          31 0 kB
AnonPages:      311522372 kB
Mapped:          3162356 kB
Shmem:           3132332 kB
Slab:            3142328 kB
SReclaimable:    3102360 kB
SUnreclaim:       312368 kB
KernelStack:      312360 kB
PageTables:       312308 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    17816126 kB
Committed_AS:   27879522 kB
VmallocTotal:   3785973827 kB
VmallocUsed:      77826 kB
VmallocChunk:   3782249524 kB
HardwareCorrupted:     0 kB
AnonHugePages:  2677376 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:      10808 kB
DirectMap2M:     609120 kB
DirectMap1G:    38998272 kB
rishi@machine1:/home/rishi/
```

### CPU Information
```shell
$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 62
model name      : Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz
stepping        : 4
microcode       : 0x42c
cpu MHz         : 2600.000
cache size      : 20480 KB
physical id     : 0
siblings        : 16
core id         : 0
cpu cores       : 8
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu ......... pts
bogomips        : 5186.96
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:

processor       : 1
......
processor       : nth
```
