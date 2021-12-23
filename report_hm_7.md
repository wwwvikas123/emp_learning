## Repositories and Packages

- Use rpm for the following tasks:
1. 
wget http://mirror.centos.org/centos/7/os/x86_64/Packages/sysstat-10.1.5-19.el7.x86_64.rpm

2. 
rpm -qip sysstat-10.1.5-19.el7.x86_64.rpm
rpm -ql sysstat
 
3.
sudo rpm -ivh sysstat-10.1.5-19.el7.x86_64.rpm


- Add NGINX repository (need to find repository config on https://www.nginx.com/) and complete the following tasks using yum:
1.
yum repolist all nginx repo

2. 
sudo yum install nginx
 
3.
yum history 

```
Loaded plugins: fastestmirror, langpacks
ID     | Login user               | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
     3 | Vika <user>              | 2021-12-24 02:12 | Install        |    1 EE
     2 | Vika <user>              | 2021-12-16 18:56 | I, U           |  301 EE
     1 | System <unset>           | 2021-11-25 12:53 | Install        | 1407   
history list
```
sudo yum history undo 3

4. 
sudo yum-config-manager --enable nginx repo
 
5.
sudo yum remove sysstat.x86_64 

11. Install EPEL repository and get information about it.

13. Find how much packages provided exactly by EPEL repository.
14. Install ncdu package from EPEL repo.
​
*Extra task:
    Need to create an rpm package consists of a shell script and a text file. The script should output words count stored in file.
​
## Work with files
​
1. Find all regular files below 100 bytes inside your home directory.
2. Find an inode number and a hard links count for the root directory. The hard link count should be about 17. Why?
3. Check what inode numbers have "/" and "/boot" directory. Why?
4. Check the root directory space usage by du command. Compare it with an information from df. If you find differences, try to find out why it happens.
5. Check disk space usage of /var/log directory using ncdu
