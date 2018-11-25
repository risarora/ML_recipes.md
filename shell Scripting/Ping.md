## Ping

Using the <code>ping</code> connection to a machine/server/website is checked . The <code>ping</code> will ping the destination  till the user stops it by pressing <code>ctrl-C</code>.

```shell
$ ping google.com
PING google.com (172.217.4.238) 56(84) bytes of data.
64 bytes from ord30s31-in-f238.1e100.net (172.217.4.238): icmp_seq=1 ttl=49 time=14.3 ms
64 bytes from ord30s31-in-f238.1e100.net (172.217.4.238): icmp_seq=2 ttl=49 time=14.3 ms
64 bytes from ord30s31-in-f238.1e100.net (172.217.4.238): icmp_seq=3 ttl=49 time=14.3 ms
^C
--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2001ms
rtt min/avg/max/mdev = 14.339/14.343/14.350/0.138 ms
```


## Ping a machine predetermined number of times
<code>-c <COUNT> </code> terminates the ping command after the specified number of pings are done.

```shell
$ ping -c 5 google.com
PING google.com (172.217.4.238) 56(84) bytes of data.
64 bytes from ord30s31-in-f14.1e100.net (172.217.4.238): icmp_seq=1 ttl=49 time=14.3 ms
64 bytes from ord30s31-in-f14.1e100.net (172.217.4.238): icmp_seq=2 ttl=49 time=14.3 ms
64 bytes from ord30s31-in-f14.1e100.net (172.217.4.238): icmp_seq=3 ttl=49 time=14.4 ms
64 bytes from ord30s31-in-f14.1e100.net (172.217.4.238): icmp_seq=4 ttl=49 time=15.0 ms
64 bytes from ord30s31-in-f14.1e100.net (172.217.4.238): icmp_seq=5 ttl=49 time=14.3 ms

--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4003ms
rtt min/avg/max/mdev = 14.363/14.502/15.000/0.281 ms
```
