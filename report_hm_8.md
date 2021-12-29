# 1
Attaching of a new vd

![images](./images/new_disk.png)

## 1.1
sudo fdisk /dev/sdb -l
parted /dev/sdb
(parted) p
(parted) mklable gpt
(parted) mkpart primary 0 2048
(parted) q
sudo mkfs.ext4 /dev/sbd1

```
\# fdisk /dev/sdb1
[...]
Command (m for help): t
Partition number (1-3, default 3): 3
Hex code (type L to list all codes): L

Partition type (type L to list all types): 20
Changed type of partition 'Microsoft basic data' to 'Linux filesystem'

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
[user@localhost ~]$  sudo fdisk /dev/sdb -l
WARNING: fdisk GPT support is currently new, and therefore in an experimental phase. Use at your own discretion.

Disk /dev/sdb: 5368 MB, 5368709120 bytes, 10485760 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: gpt
Disk identifier: 5FB21CC7-9405-4892-8A7A-A59024A83D50


#         Start          End    Size  Type            Name
 1           34      3906250    1.9G  Linux filesyste primary
```


## 1.2

parted /dev/sdb
(parted) p
(parted) mkpart primary 2048 2560MB
(parted) q
sudo mkfs.ext4 /dev/sbd2

...

```
Partition type (type L to list all types): 19
Changed type of partition 'Microsoft basic data' to 'Linux swap'

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
[user@localhost ~]$  sudo fdisk /dev/sdb -l
WARNING: fdisk GPT support is currently new, and therefore in an experimental phase. Use at your own discretion.

Disk /dev/sdb: 5368 MB, 5368709120 bytes, 10485760 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: gpt
Disk identifier: 0F0E87A6-24DB-48CB-92CC-E9B5FC133983


#         Start          End    Size  Type            Name
 1           34      4000000    1.9G  Linux filesyste primary
 2      4000001      5000000  488.3M  Linux swap      primary
```


## 1.3

parted /dev/sdb
(parted) p
(parted) mkpart primary 2560 4608MB
(parted) q
sudo mkfs.xfs /dev/sdb3

![images] (./images/list_parted_1_3.png)

## 1.4

swapon --show
sudo mkswap /dev/sdb2
sudo swapon /dev/sdb2


## 1.5

![images] (./images/1_5_mount.png)

$ sudo blkid /dev/sdb3

```
/dev/sdb3: UUID="71f77eaa-f2e3-47ec-ae31-a52d785ae12f" TYPE="xfs" PARTLABEL="primary" PARTUUID="1bfff556-f273-4804-a7d2-6ac5d1a3bd03" 
```

nano /etc/fstab

```
sudo blkid /dev/sdb3
[sudo] password for user: 
/dev/sdb3: UUID="71f77eaa-f2e3-47ec-ae31-a52d785ae12f" TYPE="xfs" PARTLABEL="primary" PARTUUID="1bfff556-f273-4804-a7d2-6ac5d1a3bd03" 
```

## 1.6

echo '/dev/sdb2 none swap 0 0' | sudo tee -a /etc/fstab

## 1.7 

![images] (./images/result.png)

# 2

