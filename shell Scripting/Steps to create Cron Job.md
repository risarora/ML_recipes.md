## Steps to create Cron Jobs
### What is a cron job

### 1. Add user to /etc/cron.allow file

	sudo echo "<UserName>" >> /etc/cron.allow

	Eg.
	sudo echo "root" >> /etc/cron.allow
	sudo echo "admin" >> /etc/cron.allow
	sudo echo "user1" >> /etc/cron.allow


### 2. Schedule the cron job

* Min(0-59)
* Hr(0-23)  
* DOM(1-31)
* Mon(1-12)
* DOW(0-6)



```shell
0 * * * 2,3,4,5,6 ./MemoryMonitor.sh > /dev/null 2>&1
```

### 3. Guidelines for using cronjobs
* Check for duplicate process.
* Use fully qualified directory names.
* Avoid bash
* cron shell is recomended
* Start script file with #!/bin/ksh
* Redirect the errors to null
>/dev/null 2>&1



	5,35 * * * * /mapr/datalake/uhg_admin/bin/bdp_zk_monitor -monitor > /dev/null 2>&1 # Monitor Zookeeper
	* * * * * /script >/dev/null 2>&1



# Min(0-59) Hr(0-23) DOM(1-31) Mon(1-12) DOW(0-6) Comman
5,35 * * * * /mapr/datalake/uhg_admin/bin/bdp_zk_monitor -monitor > /dev/null 2>&1 # Monitor Zookeeper

Check for duplicate process.

HOWMANYRUN=`ps -ef |grep $0 |grep -v grep |wc -l | awk '{print $1}'`
  if [ ${HOWMANYRUN} -gt ${HMCONCURR} ] ; then
     dtm; echo "${DT} ${HN}  _main[WARN] concurrent exec:[${HOWMANYRUN}], -aborting current instance ${THISSCRIPT}" >> ${LF}
     exit 1
else dtm ; echo "${DT} ${HN} _main concurrent:${HOWMANYRUN} limit:${HMCONCURR}" >> ${LF}
     _cleanup
     _logmaintenance
     _listenprep
     _channelfill
     _mon_cust_scrpts
     _buildhtml  # This will send alert email if necessary, always leave uncommented.
     dtm ; echo "${DT} ${HN} _main.${SCRPTNM}:automation end" >> ${LF}
 fi
exit 0



http://serverfault.com/questions/449651/why-is-my-crontab-not-working-and-how-can-i-troubleshoot-it
http://kvz.io/blog/2007/07/29/schedule-tasks-on-linux-using-crontab/
https://help.ubuntu.com/community/CronHowto


###############################################################
