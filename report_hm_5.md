# Processes

$ sleep 30000 <br/>
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
[1]+  Stopped                 sleep 20000  <br/>


$ kill -s STOP 3206 <br/>
[user@localhost ~]$ ps -aux | grep sleep <br/>
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


```
[Unit]
Description=a simple daemon which does does echo 2

[Service]
Type=oneshot
ExecStart=/usr/bin/bash -c '/usr/bin/echo 2 >> /tmp/homework'
```
---------------
```
[Unit]
Description=a simple daemon which does sleep 10 after a start and then does ech$
Before=epam_second_demon.service

[Service]
ExecStart=/bin/sleep 10
ExecStartPost=/usr/bin/bash -c '/usr/bin/echo 1 >> /tmp/homework'

[Install]
WantedBy=multi-user.target
```


```
[Unit]
Description=a simple daemon which does does echo 2
After=epam_first_demon.service
Requires=epam_first_demon.service

[Service]
Type=oneshot
ExecStart=/usr/bin/bash -c '/usr/bin/echo 2 >> /tmp/homework'

[Install]
WantedBy=multi-user.target
```
--------------

```

[Unit]
Description=Do epam_second_demon.service on 01.01.2019 at 00:00

[Timer]
OnCalendar=2019-01-01 00:00:00
Persistent=true

[Install]
WantedBy=timers.target
```
$ sudo systemctl list-timers  <br/>

```
NEXT                         LEFT                LAST                         PASSED       UNIT                         ACTIVATES 
n/a                          n/a      Fri 2021-12-17 01:15:41 MSK  4min 39s ago epam_second_demon.timer      epam_second_demon.service
Sat 2021-12-18 00:00:00 MSK  22h left Fri 2021-12-17 00:00:01 MSK  1h 20min ago unbound-anchor.timer         unbound-anchor.service
Sat 2021-12-18 01:14:02 MSK  23h left Fri 2021-12-17 01:14:02 MSK  6min ago     systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
```
This is screen ![image](./images/screen%20_%20hw_5.png)

# cron/anacron
- script
```
#!/bin/bash
echo Hello > /opt/hello
```
- tabs

```
0 0 2 * * /home/user/tabs/script_one.sh
@reboot sleep 60; /home/user/tabs/script_one.sh
```
# lsof

$ sleep 10000 0>in.txt 1>out.txt  ### запуск

![image](./images/sleep_ex_5.png)

- 1

$ sudo lsof | grep "in.txt"

```
sleep     3565                root    0w      REG                8,3         0  101431902 /home/user/in.txt
```

$ sudo lsof | grep "out.txt"

```
sleep     3565                root    1w      REG                8,3         0  100705868 /home/user/out.txt
```

- 2

sudo lsof -c sleep   #### время sleep истекло, пришлось перезапустить команду, поэтому PID изменился

$ sudo lsof -d0 -a -f | grep sleep

```
sleep     4653           root    0w   REG                8,3        0 101431902 /home/user/in.txt
sleep     5055           root    0r   CHR                1,3      0t0      7516 /dev/null
```

- 3

sudo lsof -iTCP

```
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
rpcbind  624    rpc    8u  IPv4  18691      0t0  TCP *:sunrpc (LISTEN)
rpcbind  624    rpc   11u  IPv6  18694      0t0  TCP *:sunrpc (LISTEN)
cupsd   1083   root   10u  IPv6  28678      0t0  TCP localhost:ipp (LISTEN)
cupsd   1083   root   11u  IPv4  28679      0t0  TCP localhost:ipp (LISTEN)
master  1406   root   13u  IPv4  27474      0t0  TCP localhost:smtp (LISTEN)
master  1406   root   14u  IPv6  27475      0t0  TCP localhost:smtp (LISTEN)
dnsmasq 1450 nobody    6u  IPv4  28438      0t0  TCP localhost.localdomain:domain (LISTEN)
```
