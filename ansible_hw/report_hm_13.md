### 3. 
ansible all -i myhosts.ini -m user -a "user=ansi state=present password={{ 'newpassword' | password_hash('sha512') }} append=yes" -u exam -b -k

 ansible all -i myhosts.ini -m shell -a "echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCpoS6Ih5DvgDHzjyNZcr6Idsd3YnLHmmMyU9W15w0TFJOYpEslJWBrlvtWcZ60n62FnfEFyeCdUv5BmNWqIdVbsBb24QZr2EQR5pnIYvtSDIL34qzEaerDucFyW2iiYmJBI05wtBAO7bx1Kfqhl77UOJWc+ZFiC+znBv0U7xCihOt5ejtm+0fc6RdQPd8aKClYBYgAfkxRJIGzD3LL4KMdNGzxn7Yde708tbEBz4Q5bjIGJ7BSwS/t7sD7VAsG1qzWxJlQXsrQdu7Gktd0gMfitPIDSp7E/9bwqTglky+eranFdfLngfEzZ6zkKLr9H2y1loxvh5j5wYqgG9TcWpEt ansi@localhost.localdomain' > ~/.ssh/authorized_keys & chmod -R 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys" -u ansi -k
 
 ansible]$ ansible all -i myhosts.ini -m shell -a "usermod -aG wheel ansi" -b -u exam -k
