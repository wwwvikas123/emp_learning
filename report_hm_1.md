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

[user@centos_2 ~ ]$ touch file_name{1..3}.md

[user@centos_2 ~]$ ls -p | grep -v /
file_name1.md
file_name2.md
file_name3.md
[user@centos_2 ~]$ f=file_name1.md && ext=.textdoc && mv -- "$f" "${f%.md}$ext"
[user@centos_2 ~]$ ls -p | grep -v /
file_name1.textdoc
file_name2.md
file_name3.md
[user@centos_2 ~]$ f=file_name2.md && ext= && mv -- "$f" "${f%.md}$ext"
[user@centos_2 ~]$ ls -p | grep -v /
file_name1.textdoc
file_name2
file_name3.md
[user@centos_2 ~]$ f=file_name3.md && ext=.md.latest && mv -- "$f" "${f%.md}$ext"
[user@centos_2 ~]$ ls -p | grep -v /
file_name1.textdoc
file_name2
file_name3.md.latest
[user@centos_2 ~]$ f=file_name1.textdoc && ext=txt && mv -- "$f" "${f%.md}$ext"
[user@centos_2 ~]$ ls -p | grep -v /
file_name1.textdoctxt
file_name2
file_name3.md.latest
[user@centos_2 ~]$ 

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
>>>>>>>>>>>>>>>
[user@centos_2 mnt]$ cd $OLDPWD
[user@centos_2 ~]$

- 6 задание

[user@centos_2 test]$ mkdir -p {new,in-process/tread{0..2},processed}
[user@centos_2 test]$ ls
in-process  new  processed
[user@centos_2 test]$ tree .
.
- ├── in-process
- │   ├── tread0
- │   ├── tread1
- │   └── tread2
- ├── new
- └── processed

[user@centos_2 new]$ touch data:"$(date +"%M")":{1..100}   #создаем файлы <br/>
$ cp *:*:{1..34} ../in-process/tread0                      #копируем 34 файла в tread0/ <br/>
$ cp *:*:{1..33} ../in-process/tread1                      #копируем 33 файла в tread1/ <br/>
$ cp *:*:{1..33} ../in-process/tread2                      #копируем 33 файла в tread2/ <br/>
$ ls -laRht ../in-process/                                 #смотрим содержимое папки in-process/ <br/>
$ mv -t ../processed/ ../in-process/tread*/*               #перемещаем всё из папок tread* в processed/ <br/> 
$ ls -R ../in-process/ ../processed/                       #смотрим содержимое папок in-process/ и /processed/ <br/>
$ a=$(ls |wc -l) && b=$(ls ../processed/ | wc -l) && if [[ $a -eq $b ]];then rm -r ./* ;else echo "in /processes=$b, in /new=$a";fi <br/>
in /processes=34, in /new=100

- 7 задание <br/>
[user@centos_2 test]$ eval echo -E file{$a..$b} <br/>
file1 file2 file3
