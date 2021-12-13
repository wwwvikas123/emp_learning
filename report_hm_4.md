## Task 1: Users and groups

# groupadd -g 4000 sales


# useradd -s /bin/bash -G sales bob
# useradd -s /bin/bash -G sales alice
# useradd -s /bin/bash -G sales eve


# passwd bob
# passwd alice 
# passwd eve



# chage -M 30 -W 25 bob
# chage -M 30 -W 25 alice
# chage -M 30 -W 25 eve

# chage -l alice 

```
Last password change					: Dec 13, 2021
Password expires					: Jan 12, 2022
Password inactive					: never
Account expires						: never
Minimum number of days between password change		: 0
Maximum number of days between password change		: 30
Number of days of warning before password expires	: 25
```

