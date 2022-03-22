### 3. 
ansible all -i myhosts.ini -m user -a "user=ansi state=present password={{ 'newpassword' | password_hash('sha512') }} append=yes" -u exam -b -k

ansible all -i myhosts.ini -m shell -a "echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+O0nvkGZxp+JtulDTCEw7RSxovi/JArwICdY+P4KT5uUWA4SR1tTiI7qEkkIk8OS7O+NOGqF45qoQKamhbUYpqTVKcdx4BDcToemow6mXJ0r3s8Kh5afMMqGWAUbThBCoGlysr0vr6g6YGzKs4Oya8EbKFSnpSLybhkPjBd5O3e7XijNQzGtSe62mtLAmV4oN4l0totnyPGMIAiDbxY5f3U5FV2KuuzV+hDDvVYlHctmms8OxKf3eLX75vasRwJN9wvwBUVhqViPIaIDCDxEp0pKxUsFB810P6P1ZmhnDv8eSTRSI8WEe7GufxA+VE7Gkeogd6DOdQYAHa9NhKtzH ansi@localhost.localdomain' >> ~/.ssh/authorized_keys" -u ansi
