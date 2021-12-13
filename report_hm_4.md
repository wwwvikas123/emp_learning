# Task 1: Users and groups

\# groupadd -g 4000 sales


\# useradd -s /bin/bash -G sales bob
\# useradd -s /bin/bash -G sales alice
\# useradd -s /bin/bash -G sales eve


\# passwd bob
\# passwd alice 
\# passwd eve


\# sudo nano /etc/login.defs

```
PASS_MAX_DAYS 30
```

\# chage -M 15 -W 10 bob <br/>

\# chage -l bob

```
Last password change			: Dec 13, 2021
Password expires					: Jan 12, 2022
Password inactive					: never
Account expires						: never
Minimum number of days between password change		: 0
Maximum number of days between password change		: 30
Number of days of warning before password expires	: 25
```

\# chage -E `date -d "90 days" +"%Y-%m-%d"` eve <br/>
\# chage -E `date -d "90 days" +"%Y-%m-%d"` alice <br/>

\# chage -l eve 

````
Last password change					: Dec 13, 2021
Password expires					: never
Password inactive					: never
Account expires						: Mar 13, 2022
Minimum number of days between password change		: 0
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7
````

{не нашла где настроить политику паролей для все пользователей конкретной группы}

## Дополнительно:

\# chage -d 0 alice <br/>
\# chage -d 0 bob <br/>
\# chage -d 0 eve <br/>
\# su eve

```
Password: 
You are required to change your password immediately (root enforced)
Changing password for eve.
(current) UNIX password: 
```


# Task 2: Controlling access to files with Linux file system permissions
\# groupadd students               <br/>
\# useradd -G students glen<br/>
\# useradd -G students antony<br/>
\# useradd -G students lesly<br/>
\# mkdir  /home/students<br/>
\# chown :students /home/students/<br/>


\# chmod -R ug+rwx /home/students/<br/>
\# chmod -R o-rwx /home/students/ <br/>
\# chmod g+s  /home/students/ <br/>

# Task3: ACL

\# mkdir -p /share/casescd
\# cd /share/cases/
\# touch murders.txt  moriarty.txt

\# groupadd bakerstreet
\# useradd -G bakerstreet holmes
\# useradd -G bakerstreet watson
\# groupadd scotlandyard
\# useradd -G scotlandyard lestrade
\# useradd -G scotlandyard gregson
\# useradd -G scotlandyard jones
\#  passwd <user>
