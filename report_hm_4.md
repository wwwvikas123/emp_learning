## Task 1: Users and groups

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

\# chage -M 15 -W 10 bob

chage -l bob

```
Last password change			: Dec 13, 2021
Password expires					: Jan 12, 2022
Password inactive					: never
Account expires						: never
Minimum number of days between password change		: 0
Maximum number of days between password change		: 30
Number of days of warning before password expires	: 25
```

\# chage -E `date -d "90 days" +"%Y-%m-%d"` eve
\# chage -E `date -d "90 days" +"%Y-%m-%d"` alice

chage -l eve
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
