# Hadoop Single Node Installation on Virtual Machine

Below are the steps to setup hadoop single node cluster on Virtual Box

1. Start VirtualBox
* Ensure that the latest version of Ubuntu LTS is installed on your VM software.  You can use link such as this.
 Once installed, login to your Ubuntu installation with your credentials. Open a terminal command.
* . Change the hostname to _hadoosn_ in the hostname and _/etc/hostname_ file. Given the IP to this VM as 192.168.56.9. Make the change accordingly in _/etc/hosts_ file.
* Enable the network adapters in the VM. Make the first adapter as "Internal Network" and second to "NAT". This will ensure that the internet access is working in your VMs.Reboot the VM for changed to take into effect.
* Execute sudo apt-get update command to update your Ubuntu installation
* Now is the time to make static IP. Open the /etc/network/interfaces file on the VMs and add the following :
```shell
#The primary network interface
  auto eth0
             iface eth0 inet static
                    address 192.168.56.9
                    netmask 255.255.255.0
  auto eth1
             iface eth1 inet dhcp
```
* Now to ensure that your ssh is working, check ssh immediately after the below commands by executing whereis ssh and whereis sshd commands. If any one of these commands return a blank response that means your SSH is not properly installed. Install it now the following 3 steps and check the ssh and sshd again:

```shell
  sudo apt-get remove openssh-client
  sudo apt-get update
  sudo apt-get install openssh-server
```
Reboot once for all the above changes to take into effect.

* Now enable root access executing the following steps
```    
sudo nano /etc/ssh/sshd_config
```

comment line PermitRootLogin without-password
Just below the commented line, add PermitRootLogin yes

* Restart ssh by executing sudo service ssh restart
* Change the root password by using the command “sudo passwd root”. Change the password to reflect a new password
* Log in to root user using “su root” command to check if the new password is working.

### Let create ssh keys on this host as follows :-
Ensure that you are into your user log in (not root log in).
Remove any keys that have been created on this VM before by executing rm -rf .ssh/ command.
Now let us first create the keys by executing ssh-keygen -t rsa command
Now log into your root and just run the following command.
```
cat /home/hadoopuser/.ssh/id_rsa.pub | ssh root@hadoopsn 'cat >> /root/.ssh/authorized_keys'
```
Now run the same on localhost
```
cat /home/hadoopuser/.ssh/id_rsa.pub | ssh root@localhost 'cat >> /root/.ssh/authorized_keys'
```
This command will ensure that the .ssh folder is created in root location and also the public key created by the syed user is copied to the authorised_keys file in the root location.

Now you need to give the required right to .ssh folder and authorised_keys file in ssh location. Execute chmod 700 /root/.ssh, chmod 600 /root/.ssh/authorized_keys, chmod 640 /root/.ssh/authorized_keys
Now try to ssh in your root log in using ssh root@hadoopsn. You should be able to ssh in without password. Doing the same with syed user in root login will ask you for a password, which is fine. Doing the same with syed user in syed log will also ask for a password. This should also be fine.
If you get “Agent admitted failure to sign using the key” issue, just run ssh-add from syed log in and you should be fine.

### Install Java


Type the __sudo apt-get install openjdk-7-jdk__ command to install java

Type the java -version command to check if java is installed. This should return some valid version of Java 7 installed.

### Install Apache Hadoop

Get latest version of hadoop binary using the wget http://mirrors.sonic.net/apache/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz command.
Extract the downloaded binary using the tar -xvzf hadoop-2.7.3.tar.gz command
Copy the extracted folder to /usr/local directory using sudo mv hadoop-2.7.3 /usr/local/hadoop command.
Go to /usr/local folder
Give read and write permissions to hadoop folder using the following command
```
sudo chown -R <username>:<groupname>  /usr/local/hadoop.
```

So if you have created a user by the "syed", by default it will get created in "syed" group. Hence the command would look like sudo chown -R syed:syed /usr/local/hadoop
Log into your root user. Open the bashrc file using the sudo nano $HOME/.bashrc command
Add the following 3 lines to above bashrc file and save and quit
```
export HADOOP_HOME=/usr/local/hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export PATH=$PATH:$HADOOP_HOME/bin
```
Use source $HOME/.bashrc command for the above changes to take into affect
Execute hadoop version command to check if the latest version is installed. Process if you see the latest version is installed.
Now create a temporary directory to save intermediate output emitted by the mappers as follows and give it required permissions
```
      sudo mkdir -p /usr/local/hadoop/tmp
      sudo chown <username> /usr/local/hadoop/tmp
      sudo chmod 750 /usr/local/hadoop/tmp
```

Open /usr/local/hadoop/etc/hadoop/core-site.xml add the following properties to it :-
```
<configuration>
<property>
<name>hadoop.tmp.dir</name>
<value>/usr/local/hadoop/tmp</value>
<description>A base for other temporary directories.</description>
</property>
<property>
<name>fs.defaultFS</name>
<value>hdfs://localhost:54310</value>
<description>The name of the default file system.  A URI whose
scheme and authority determine the FileSystem implementation.  The
uri's scheme determines the config property (fs.SCHEME.impl) naming
the FileSystem implementation class.  The uri's authority is used to
determine the host, port, etc. for a filesystem.</description>
</property>
</configuration>
```
Open  /usr/local/hadoop/etc/hadoop/yarn-site.xml add the following properties to it :-

``` <configuration>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
<value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>
<property>
<name>yarn.resourcemanager.address</name>
<value>localhost:9003</value>
</property>
<property>
<name>yarn.resourcemanager.resource-tracker.address</name>
<value>localhost:9001</value>
</property>
<property>
<name>yarn.resourcemanager.scheduler.address</name>
<value>localhost:9002</value>
</property>
<property>
<name>yarn.log-aggregation-enable</name>
<value>true</value>
</property>
</configuration>
```
Open  /usr/local/hadoop/etc/hadoop/hdfs-site.xml add the following properties to it :-
```
 <configuration>
 <property>
 <name>dfs.replication</name>
 <value>1</value>
 <description>default replication factor for the cluster.
 </description>
 </property>
 <property>
 <name>dfs.namenode.name.dir</name>
 <value>file:/usr/local/hadoop/hadoop_data/hdfs/namenode</value>
 <description>default replication factor for the cluster.
 </description>
 </property>
 <property>
 <name>dfs.datanode.data.dir</name>
 <value>file:/usr/local/hadoop/hadoop_data/hdfs/datanode</value>
 <description>default replication factor for the cluster.
 </description>
 </property>
 </configuration>
```
Open  /usr/local/hadoop/etc/hadoop/mapred-site.xml add the following properties to it :-
```
<configuration>
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
<property>
<name>mapreduce.jobhistory.address</name>
<value>localhost:10020</value>
</property>
<property>
<name>mapreduce.jobhistory.webapp.address</name>
<value>localhost:19888</value>
</property>
</configuration>
```
Make the directories

```
mkdir -p /usr/local/hadoop/hadoop_data/hdfs/namenode
```
and
```
mkdir -p /usr/local/hadoop/hadoop_data/hdfs/datanode
```
for the above configuration changes.
Give these newly created directories the proper right using sudo chown username:usergroup -R /usr/local/hadoop command. For mac set ups, run sudo chown -R syedrizvi:staff /usr/local/Cellar/hadoop to give the write access to the folders. Do a sudo chmod 750 to /usr/local/hadoop folder if the namenode does not start the first time.
Use the hdfs namenode –format command to format the namenode. Make sure that the dfs folder inside /usr/local/hadoop/ has the proper access after this command. Run the chown command again if the access is not there.
Now log into your root user. Use the hadoop/sbin/start-dfs.sh command to start HDFS Services
Use the hadoop/sbin/start-yarn.sh command to start YARN Services
Set JAVA_HOME explicitly if hadoop-env.sh if start up gives messages with respect to it.

Check if all the services are running using jps command.
Create your aliases as below. This will ensure that you can start and stop the cluster in one shot
```
alias hstart="/usr/local/hadoop/sbin/start-dfs.sh;/usr/local/hadoop/sbin/start-yarn.sh"
alias hstop="/usr/local/hadoop/sbin/stop-yarn.sh;/usr/local/hadoop/sbin/stop-dfs.sh"
```
Once the services are running, your single node hadoop server is up and running with the latest version.
