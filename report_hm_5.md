## Processes

$ while true; do sleep 1;done
$ sleep 1000
$ sleep 20000

[user@localhost ~]$ ps -aux | grep sleep
user       2993  0.0  0.0 108052   356 pts/1    S+   23:26   0:00 sleep 1000
user       3042  0.0  0.0 108052   356 pts/2    S+   23:26   0:00 sleep 20000
user       3112  0.0  0.0 108052   356 pts/0    S+   23:26   0:00 sleep 1
user       3114  0.0  0.0 112808   964 pts/3    S+   23:26   0:00 grep --color=auto sleep


------------------------
$kill -19 2993

$ sleep 20000
^Z
[1]+  Stopped                 sleep 20000


$ kill -s STOP 3206
[user@localhost ~]$ ps -aux | grep sleep
user       2993  0.0  0.0 108052   356 pts/1    T    23:26   0:00 sleep 1000
user       3206  0.0  0.0 108052   356 pts/0    T    23:27   0:00 sleep 30000
user       3454  0.0  0.0 108052   356 pts/2    T    23:31   0:00 sleep 20000
user       4032  0.0  0.0 112808   964 pts/3    S+   23:41   0:00 grep --color=auto sleep


---------------------
$ kill  -s TERM 2993
[user@localhost ~]$ fg
sleep 1000
Terminated

---------------------

$ sudo kill -s CONT 3206
[user@localhost ~]$ ps -aux | grep sleep
user       3206  0.0  0.0 108052   356 pts/0    S    23:27   0:00 sleep 30000
user       3454  0.0  0.0 108052   356 pts/2    T    23:31   0:00 sleep 20000
root       4405  0.0  0.0 108052   352 ?        S    23:49   0:00 sleep 60
user       4424  0.0  0.0 112808   964 pts/3    R+   23:49   0:00 grep --color=auto sleep

$ fg
sleep 20000


------------------

$ kill -9 3206
[user@localhost ~]$ ps -aux | grep sleep
user       4641  0.0  0.0 112808   964 pts/3    S+   23:53   0:00 grep --color=auto sleep


$ sleep 20000
^Z
[1]+  Stopped                 sleep 20000
[user@localhost ~]$ jobs
[1]+  Stopped                 sleep 20000
[user@localhost ~]$ kill %1
[1]+  Terminated              sleep 20000


## systemd
