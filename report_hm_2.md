## 1.

$ man awk 

/ENVIRONMENT

$ man awk | grep ENVIRONMENT VARIABLES -a 20 > env_path.txt

## 2.                                                                           
```
#!/bin/bash
touch ../task2.txt 2>err.log || echo "ERROR."
```

## 2*.

```
#!/bin/bash
[ -w ../ ]
right=$?
if [ -f ../task2.txt ];
then echo 'file exist'; 
elif [ $right -eq 1 ];
then echo "you don't have permissions";
else touch task2.txt 2>err.log ||echo "ERROR.";
fi
```
## 3.
$ echo $PWD > dir.txt

$ cat dir.txt

```
/home/vika/EPAM/script
```

```
#!/bin/bash
cat dir.txt | xargs ls -al
```

## 3*.

 $ cat script.sh
```
#!/bin/bash
cat dir.txt | xargs ls -alp && ls -p |grep / | echo directory $(wc -l) && ls -p | grep -v / | echo files $(wc -l)
```

## 3**.

 $ cat dir.txt
```
/home/vika/EPAM/script
/home/vika/EPAM
/etc/nginx/sites-available/
/var
```

```
#!/bin/bash
cat dir.txt | xargs -n1 -I DIR bash -c 'ls -alp "DIR" &&  ls -p "DIR" | grep / | echo directory $(wc -l) && ls -p "DIR" | grep -v / | echo files $(wc -l)'
