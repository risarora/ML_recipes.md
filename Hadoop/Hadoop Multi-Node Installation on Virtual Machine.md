# Hadoop Multi-Node Installation on Virtual Machine


Hadoop installation on a multi node cluster. We are going to use Virtual Box for this purpose to utilise its VM Cloning feature.

So to start with, lets have a look at software and hardware requirement for it as follows :-
A single computer (yes, a single computer as we will will using cloning feature of Virtual Box)
Minimum 4 GB RAM. 8 GB desired.
High Speed internet connection for software downloads.
So lets get started with it in the following steps :-
Create a Single Node Hadoop installation as per my previous post.
Now we have to start creating the clones using the "cloning" feature of Oracle Virtual Box.
Lets create the first clone from the single node set up and call it hadoopmnmaster.
Once the clone is created, start this instance and and open the hosts file by entering the sudo nano /etc/hosts command.
In this file we have to enter the host and ip details of the all the nodes in the cluster (both Master and Slaves) as follows :-
192.168.56.10            hadoopmnmaster
192.168.56.11            hadoopmnslave1
192.168.56.12            hadoopmnslave2
192.168.56.13            hadoopmnslave3
 Now open the hostname file on hadoopmnmaster using sudo nano /etc/hostname command and change the hostname to hadoopmnmaster in this file.
Now open this instance's core-site.xml using the sudo nano /usr/local/hadoop/etc/hadoop/core-site.xml command. Replace the localhost to hadoopmnmaster for the namenode URL entry.
Open the interfaces file using sudo nano /etc/network/interfaces command. Change the IP in this file to 192.168.56.10
Now open this instance's hdfs-site.xml using the sudo nano /usr/local/hadoop/etc/hadoop/hdfs-site.xml command. Change the replication factor from 1 to 3.
Remove the the entry from namenode in this file. This is done temporarily so that the instance can be cloned as slaves.
 Reboot the instance using sudo reboot command.
 Remove the previously created hadoop data folder using sudo rm -rf /usr/local/hadoop/hadoop_data command.
 Make a new directory for datanodes using the sudo mkdir -p /usr/local/hadoop/hadoop_data/hdfs/datanode
Give appropriate rights to the newly created folde above by executing sudo chown -R syed:syed /usr/local/hadoop command. Close the instance now.
Your master instance is ready to be cloned now. Create 3 clones from this instance as hadoopmnslave1, hadoopmnslave2 and hadoopmnslave3.
Start hadoopmnmaster back now.  Now you need to add the master to the masters file. Open the masters file using sudo nano /usr/local/hadoop/etc/hadoop/masters command. Add hadoopmnmaster to it.
Open the hdfs-site.xml and put the entry back for namenode. Remove the hadoop_data folder from hadoop root
Make a new directory for namenode using the sudo mkdir -p /usr/local/hadoop/hadoop_data/hdfs/namenode. Give read and write rights to the hadoop folder using sudo chown -R syed:syed /usr/local/hadoop
Open the slaves file using sudo nano /usr/local/hadoop/etc/hadoop/slaves command. Add hadoopmnslave1, hadoopmnslave2, hadoopmnslave3 to it.  Reboot the master server
Start the first slave server hadoopmnslave1 now. Open the hostname file to change the name to  hadoopmnslave1. Open the interfaces file to update the IP address as 192.168.56.11. Do the same for all the other slaves and reboot them.
Very important property to set up. Go to the mapred-site.xml file of all your master and slave file and make sure that every entry of localhost is replaced by hadoopmnmaster.
Similarly, go to your yarn-site.xml of all your nodes and add the property yarn.resourcemanager.hostname and keep the value as the hadoopmnmaster. Replace all the occurrences of localhost / master node in this file with ${yarn.resourcemanager.hostname}. This will ensure that all your daemons are started properly on the masternode only.
Ensure that passwordless SSH is happening between all the nodes. Fix the keys if it is not happening. Go through this link to get the help.
Go to hadoopmnmaster and execute hstart command. This should start the namenode and resource manager at the master instance and datanode and node manager on all the slave instances.
Test your wordcount from the master machine. it should start the MRAppMaster on one slave and YARNChild on the other.
Your multinode cluster is up and running !
