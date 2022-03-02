import os
import string

pid = os.getpid()
user_name = os.getlogin()
os_name = os.uname().sysname
os_release = os.uname().release
os_params = [os_name, os_release]
join_str = "-".join(os_params)
strip_split_str = (f'PID: {pid}. It was ran by {user_name} to work happily on {os_name}-{os_release}.')

#f-строки
print (f'PID: {pid}. It was ran by {user_name} to work happily on {os_name}-{os_release}.')
print ("PID: %s. It was ran by %s to work happily on %s-%s." %(pid,user_name,os_name,os_release))
#Конкатенация (склеивание) с помощью +
print (f'PID: {pid}.' + f' It was ran by {user_name} to work happily on {os_name}-{os_release}.')
#.join 
print (f'PID: {pid}. It was ran by {user_name} to work happily on', join_str)
#.strip
print (str(strip_split_str).strip('PI'))
#.split
print (str(strip_split_str).split('.'))
