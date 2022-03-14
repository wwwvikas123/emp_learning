import os, sys
from pickle import TRUE
import subprocess
import time
from subprocess import PIPE, STDOUT
stringi = str("kuki")
first = subprocess.check_call("cat access.log | awk '{print $9}'  | sort -n | uniq -c | sort -rn | head > 1", shell=TRUE, stdout=PIPE)
dva = subprocess.run("cat access.log | grep '216.244.66.230' | cut -d[ -f2 | cut -d] -f1  | awk -F ':' '{print $1}' | awk -F '/' '{print 'reqs', $2, $3}'| uniq -c  > 2", shell=True)
drei = subprocess.check_call(["cat access.log | awk '{a[$1]+=$10}END {for (i in a) print a [i], 'bites_for', i}' > 3"], shell=True)
