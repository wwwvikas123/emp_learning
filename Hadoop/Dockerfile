FROM ubuntu:16.04

# set environment vars
ENV HADOOP_HOME /usr/local/hadoop/current
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# install packages
RUN \
  apt-get update && apt-get install -y \
  ssh \
  rsync \
  nano \
  tar \
  openjdk-8-jdk

USER root
WORKDIR /root
# download and extract hadoop, set JAVA_HOME in hadoop-env.sh, update path
RUN \
  wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz && \
  tar -xzf hadoop-3.1.2.tar.gz -C /opt && \
  mkdir -p /usr/local/hadoop && \
  ln -sT /opt/hadoop-3.1.2/ $HADOOP_HOME && \ 
  echo "PATH=$PATH:$HADOOP_HOME/bin" >> ~/.bashrc

# create ssh keys
RUN \
  ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
  cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
  chmod 0600 ~/.ssh/authorized_keys

# copy hadoop configs
ADD configs/* $HADOOP_HOME/etc/hadoop/

#ENV HADOOP_HOME /usr/local/hadoop/current
#ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
#ENV HADOOP_HEAPSIZE_MAX 512
#ENV HOSTNAME $HOSTNAME
#ENV HADOOP_CONF_DIR /usr/local/hadoop
RUN mkdir /opt/mount1 && \
    mkdir /opt/mount2 && \
    mkdir -p /opt/mount1/namenode-dir && \
    mkdir -p /opt/mount2/namenode-dir

RUN sed -i 's/\"%PATH_TO_OPENJDK8_INSTALLATION%\"/\/usr\/lib\/jvm\/java-8-openjdk-amd64/' $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
sed -i 's/\"%PATH_TO_HADOOP_INSTALLATION\"/\/usr\/local\/hadoop\/current/' $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
sed -i 's/\"%HADOOP_HEAP_SIZE%\"/512M/' $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
sed -i 's/%HDFS_NAMENODE_HOSTNAME%/localhost/' $HADOOP_HOME/etc/hadoop/core-site.xml && \
sed -i 's/%NAMENODE_DIRS%/\/opt\/mount1\/namenode-dir\,\/opt\/mount2\/namenode-dir/' $HADOOP_HOME/etc/hadoop/hdfs-site.xml && \
sed -i 's/%DATANODE_DIRS%/\/opt\/mount1\/datanode-dir\,\/opt\/mount2\/datanode-dir/' $HADOOP_HOME/etc/hadoop/hdfs-site.xml && \
sed -i 's/%YARN_RESOURCE_MANAGER_HOSTNAME%/localhost/' $HADOOP_HOME/etc/hadoop/yarn-site.xml && \
sed -i 's/%NODE_MANAGER_LOCAL_DIR%/\/opt\/mount1\/nodemanager-local-dir\,\/opt\/mount2\/nodemanager-local-dir/' $HADOOP_HOME/etc/hadoop/yarn-site.xml && \
sed -i 's/%NODE_MANAGER_LOG_DIR%/\/opt\/mount1\/nodemanager-log-dir\,\/opt\/mount2\/nodemanager-log-dir/' $HADOOP_HOME/etc/hadoop/yarn-site.xml

# copy script to start hadoop
ADD start-hadoop.sh start-hadoop.sh

# expose various ports
EXPOSE 8088 8031 9870 8020

# start hadoop
CMD bash start-hadoop.sh