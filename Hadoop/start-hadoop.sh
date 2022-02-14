#!/bin/bash

# start ssh server
/etc/init.d/ssh start

# format namenode
$HADOOP_HOME/bin/hdfs namenode -format cluster1

# start hadoop
$HADOOP_HOME/bin/hdfs --daemon start namenode
$HADOOP_HOME/bin/yarn --daemon start resourcemanager

# keep container running
tail -f /dev/null