FROM ubuntu:16.04

# set environment vars
ENV HADOOP_HOME=/usr/local/hadoop/current \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    HADOOP_HEAPSIZE_MAX=512 \
    TERM=xterm-256color
ARG USER=hadoop

# install packages
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
  ssh \
  tar \
  wget \ 
  openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/* && \
groupadd --gid 2000 $USER \ 
&& useradd --uid 2000 \
           --gid $USER \
           --shell /bin/bash \
           --create-home $USER && \
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz && \
     tar -xzf hadoop-3.1.2.tar.gz -C /opt && \
     rm -rf hadoop-3.1.2.tar.gz && \
     mkdir -p /usr/local/hadoop && \
     ln -sT /opt/hadoop-3.1.2/ $HADOOP_HOME && \ 
     echo "PATH=$PATH:$HADOOP_HOME/bin" >> ~/.bashrc && \
     chown -R $USER:$USER $HADOOP_HOME/ && \
     chmod 750 $HADOOP_HOME/ && \
     wget https://gist.githubusercontent.com/rdaadr/2bedf24fd2721bad276e416b57d63e38/raw/640ee95adafa31a70869b54767104b826964af48/hdfs-site.xml && \
     wget https://gist.githubusercontent.com/rdaadr/64b9abd1700e15f04147ea48bc72b3c7/raw/2d416bf137cba81b107508153621ee548e2c877d/core-site.xml && \
     wget https://gist.githubusercontent.com/rdaadr/2f42f248f02aeda18105805493bb0e9b/raw/6303e424373b3459bcf3720b253c01373666fe7c/hadoop-env.sh && \
     wget https://gist.githubusercontent.com/Stupnikov-NA/ba87c0072cd51aa85c9ee6334cc99158/raw/bda0f760878d97213196d634be9b53a089e796ea/yarn-site.xml && \
     cp core-site.xml hadoop-env.sh hdfs-site.xml yarn-site.xml $HADOOP_HOME/etc/hadoop/ && \  
install -d --group=$USER --owner=$USER /opt/mount1/datanode-dir && \
install -d --group=$USER --owner=$USER /opt/mount2/datanode-dir && \
install -d --group=$USER --owner=$USER /opt/mount1/nodemanager-local-dir && \
install -d --group=$USER --owner=$USER /opt/mount2/nodemanager-log-dir && \
install -d --group=$USER --owner=$USER /opt/mount1/nodemanagerlog-dir && \
install -d --group=$USER --owner=$USER /opt/mount2/nodemanager-local-dir

# expose various ports
EXPOSE 8088 8031 9870 8020

# copy script to start hadoop
COPY --chown=$USER:$USER start-hadoop.sh /home/$USER/start-hadoop.sh
RUN chmod +x /home/$USER/start-hadoop.sh

# switch user
USER $USER

WORKDIR /home/$USER
# start hadoop
CMD bash start-hadoop.sh