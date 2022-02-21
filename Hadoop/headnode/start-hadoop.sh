#!/bin/bash

if [[ -z "${HEADNODE_HOST}" ]]; then
  tput setaf 1;echo "HEADNODE_HOST is undefined"
else
sed -i 's/\"%PATH_TO_OPENJDK8_INSTALLATION%\"/\/usr\/lib\/jvm\/java-8-openjdk-amd64/' $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
sed -i 's/\"%PATH_TO_HADOOP_INSTALLATION\"/\/usr\/local\/hadoop\/current/' $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
sed -i 's/\"%HADOOP_HEAP_SIZE%\"/'$HADOOP_HEAPSIZE_MAX'/' $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
sed -i 's/%HDFS_NAMENODE_HOSTNAME%/'$HEADNODE_HOST'/' $HADOOP_HOME/etc/hadoop/core-site.xml && \
sed -i 's/%NAMENODE_DIRS%/\/opt\/mount1\/namenode-dir\,\/opt\/mount2\/namenode-dir/' $HADOOP_HOME/etc/hadoop/hdfs-site.xml && \
sed -i 's/%DATANODE_DIRS%/\/opt\/mount1\/datanode-dir\,\/opt\/mount2\/datanode-dir/' $HADOOP_HOME/etc/hadoop/hdfs-site.xml && \
sed -i 's/%YARN_RESOURCE_MANAGER_HOSTNAME%/'$HEADNODE_HOST'/' $HADOOP_HOME/etc/hadoop/yarn-site.xml && \
sed -i 's/%NODE_MANAGER_LOCAL_DIR%/\/opt\/mount1\/nodemanager-local-dir\,\/opt\/mount2\/nodemanager-local-dir/' $HADOOP_HOME/etc/hadoop/yarn-site.xml && \
sed -i 's/%NODE_MANAGER_LOG_DIR%/\/opt\/mount1\/nodemanager-log-dir\,\/opt\/mount2\/nodemanager-log-dir/' $HADOOP_HOME/etc/hadoop/yarn-site.xml

# format namenode
tput setaf 2;echo "Formatting namenode"
$HADOOP_HOME/bin/hdfs namenode -format cluster1

# start hadoop
tput setaf 2;echo "Start namenode and resourcemanager"
$HADOOP_HOME/bin/hdfs --daemon start namenode
$HADOOP_HOME/bin/yarn --daemon start resourcemanager
fi

# keep container running
tail -f /dev/null