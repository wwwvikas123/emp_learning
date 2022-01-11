## Boot process
​
1. enable recovery options for grub, update main configuration file and find new item in grub2 config in /boot.

```

GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=false
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="crashkernel=auto rhgb quiet"
GRUB_DISABLE_RECOVERY="false"
```
$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
![images] (./images/recovery_on_10.png)

3. modify option vm.dirty_ratio:
   - using echo utility
   - using sysctl utility
   - 
![images] (./images/utility_10.png)

   - using sysctl configuration files

```
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
vm.dirty_ratio = 10
```
$ sudo sysctl --system

* extra
1. Inspect initrd file contents. Find all files that are related to XFS filesystem and give a short description for every file.
2. Study dracut utility that is used for rebuilding initrd image. Give an example for adding driver/kernel module for your initrd and recreating it.
3. Explain the difference between ordinary and rescue initrd images.
