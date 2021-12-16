# Processes

$ while true; do sleep 1;done <br/>
$ sleep 1000 <br/>
$ sleep 20000 <br/>

[user@localhost ~]$ ps -aux | grep sleep <br/>
user       2993  0.0  0.0 108052   356 pts/1    S+   23:26   0:00 sleep 1000 <br/>
user       3042  0.0  0.0 108052   356 pts/2    S+   23:26   0:00 sleep 20000 <br/>
user       3112  0.0  0.0 108052   356 pts/0    S+   23:26   0:00 sleep 1 <br/>
user       3114  0.0  0.0 112808   964 pts/3    S+   23:26   0:00 grep --color=auto sleep <br/>


------------------------
$kill -19 2993 <br/>

$ sleep 20000 <br/>
^Z <br/>
[1]+  Stopped                 sleep 20000 <br/>


$ kill -s STOP 3206
[user@localhost ~]$ ps -aux | grep sleep
user       2993  0.0  0.0 108052   356 pts/1    T    23:26   0:00 sleep 1000  <br/>
user       3206  0.0  0.0 108052   356 pts/0    T    23:27   0:00 sleep 30000 <br/>
user       3454  0.0  0.0 108052   356 pts/2    T    23:31   0:00 sleep 20000 <br/>
user       4032  0.0  0.0 112808   964 pts/3    S+   23:41   0:00 grep --color=auto sleep <br/>


---------------------
$ kill  -s TERM 2993
[user@localhost ~]$ fg
sleep 1000
Terminated

---------------------
 
$ sudo kill -s CONT 3206 <br/>
[user@localhost ~]$ ps -aux | grep sleep <br/>
user       3206  0.0  0.0 108052   356 pts/0    S    23:27   0:00 sleep 30000  <br/>
user       3454  0.0  0.0 108052   356 pts/2    T    23:31   0:00 sleep 20000 <br/>
root       4405  0.0  0.0 108052   352 ?        S    23:49   0:00 sleep 60 <br/>
user       4424  0.0  0.0 112808   964 pts/3    R+   23:49   0:00 grep --color=auto sleep <br/>

$ fg
sleep 20000


------------------

$ kill -9 3206
[user@localhost ~]$ ps -aux | grep sleep <br/> 
user       4641  0.0  0.0 112808   964 pts/3    S+   23:53   0:00 grep --color=auto sleep <br/>


$ sleep 20000
^Z
[1]+  Stopped                 sleep 20000 <br/>
[user@localhost ~]$ jobs
[1]+  Stopped                 sleep 20000 <br/>
[user@localhost ~]$ kill %1
[1]+  Terminated              sleep 20000 <br/>


# systemd

```
[Unit]
Description=a simple daemon which does sleep 10 after a start and then does echo 1

[Service]
ExecStart=/bin/sleep 10
ExecStartPost=/usr/bin/bash -c '/usr/bin/echo 1 > /tmp/homework'
TimeoutSec=0
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```
