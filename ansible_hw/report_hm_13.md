### 3. 
ansible all -i myhosts.ini -m user -a "user=ansi state=present password={{ 'newpassword' | password_hash('sha512') }} append=yes" -b -k
