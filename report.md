preparation
----
[user@localhost ~]$ hostnamectl set-hostname centos_1
[user@centos_1 ~]$ userssh-keygen 
[user@centos_1 ~]$ ssh-copy-id user@192.168.18.139
[user@centos_1 ~]$ su
[root@centos_1 user]# chmod -G user wheel
[root@centos_1 user]# usermod -g user wheel
[root@centos_1 user]# usermod -G wheel user
[root@centos_1 user]# init 6
[user@centos_1 ~]$ ssh user@192.168.18.139

Last login: Mon Nov 29 14:00:22 2021 from 192.168.18.138

- 1 задание

[user@centos_2 ~]$ ls -Rl /usr/share/man/man*/*config*  
[user@centos_2 ~]$ ls -dl /usr/share/man/man1/*system* /usr/share/man/man7/*system*

- 2 задание

[user@centos_2 ~]$ find /usr/share/man/ -type f -iname "*help*"
[user@centos_2 ~]$ find /usr/share/man/ -type f -iname "help*"

- 3 задание

[user@centos_2 ~]$ head -n 7 /etc/yum.conf
[user@centos_2 ~]$ tail -2  /etc/fstab

[user@centos_2 ~]$ cat /etc/fstab | wc -l
11
[user@centos_2 ~]$ head -n 15 /etc/fstab | wc -l
11

- 4 задание

[user@centos_2 ~]$ touch file_name{1..3}.md
[user@centos_2 ~]$ ls -p | grep -v /
> file_name1.md
> file_name2.md
> file_name3.md

- 5 задание

[user@centos_2 ~]$ cd /mnt/
[user@centos_2 mnt]$
>>>>>>>>>>>>>
[user@centos_2 mnt]$ cd -
/home/user
>>>>>>>>>>>>>
[user@centos_2 mnt]$ cd ~
[user@centos_2 ~]$
>>>>>>>>>>>>>
[user@centos_2 mnt]$ cd
[user@centos_2 ~]$
>>>>>>>>>>>>>
[user@centos_2 mnt]$ pushd ~
~ /mnt
>>>>>>>>>>>>>
[user@centos_2 etc]$ cd /home/user/
[user@centos_2 ~]$ 
>>>>>>>>>>>>>
[user@centos_2 etc]$ cd ../home/user/
[user@centos_2 ~]$
>>>>>>>>>>>>>
[user@centos_2 etc]$ cd $HOME
[user@centos_2 ~]$

- 6 задание

[user@centos_2 test]$ mkdir -p {new,in-process/tread{0..2},processed}
[user@centos_2 test]$ ls
in-process  new  processed
[user@centos_2 test]$ tree .
.
├── in-process
│   ├── tread0
│   ├── tread1
│   └── tread2
├── new
└── processed






