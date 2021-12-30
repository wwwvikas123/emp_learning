## 1

### 1.1

$ sudo ip address add 192.168.33.200/24 dev ens34

Checking of ssh connection btw host and vm:

<details><summary>$ sudo tcpdump -ni ens34 port 22 -v</summary>
    
```
tcpdump: listening on ens34, link-type EN10MB (Ethernet), capture size 262144 bytes
20:30:50.677919 IP (tos 0x0, ttl 64, id 2160, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [S], cksum 0xc0b5 (correct), seq 2431541708, win 64240, options [mss 1460,sackOK,TS val 1013559836 ecr 0,nop,wscale 7], length 0
20:30:50.678099 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [S.], cksum 0xc448 (incorrect -> 0xe74f), seq 3300602077, ack 2431541709, win 28960, options [mss 1460,sackOK,TS val 3108189 ecr 1013559836,nop,wscale 7], length 0
20:30:50.678298 IP (tos 0x0, ttl 64, id 2161, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0x8545 (correct), ack 1, win 502, options [nop,nop,TS val 1013559837 ecr 3108189], length 0
20:30:50.678891 IP (tos 0x0, ttl 64, id 2162, offset 0, flags [DF], proto TCP (6), length 93)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x61ec (correct), seq 1:42, ack 1, win 502, options [nop,nop,TS val 1013559837 ecr 3108189], length 41
20:30:50.679026 IP (tos 0x0, ttl 64, id 23939, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0x862e), ack 42, win 227, options [nop,nop,TS val 3108190 ecr 1013559837], length 0
20:30:50.698612 IP (tos 0x0, ttl 64, id 23940, offset 0, flags [DF], proto TCP (6), length 73)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc455 (incorrect -> 0xc254), seq 1:22, ack 42, win 227, options [nop,nop,TS val 3108210 ecr 1013559837], length 21
20:30:50.699428 IP (tos 0x0, ttl 64, id 2163, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0x84dd (correct), ack 22, win 502, options [nop,nop,TS val 1013559858 ecr 3108210], length 0
20:30:50.700283 IP (tos 0x0, ttl 64, id 2164, offset 0, flags [DF], proto TCP (6), length 1564)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0xca28 (incorrect -> 0xa912), seq 42:1554, ack 22, win 502, options [nop,nop,TS val 1013559859 ecr 3108210], length 1512
20:30:50.700389 IP (tos 0x0, ttl 64, id 23941, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0x7fef), ack 1554, win 250, options [nop,nop,TS val 3108211 ecr 1013559859], length 0
20:30:50.706889 IP (tos 0x0, ttl 64, id 23942, offset 0, flags [DF], proto TCP (6), length 1332)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc940 (incorrect -> 0x6941), seq 22:1302, ack 1554, win 250, options [nop,nop,TS val 3108218 ecr 1013559859], length 1280
20:30:50.707253 IP (tos 0x0, ttl 64, id 2166, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0x79e6 (correct), ack 1302, win 501, options [nop,nop,TS val 1013559866 ecr 3108218], length 0
20:30:50.710383 IP (tos 0x0, ttl 64, id 2167, offset 0, flags [DF], proto TCP (6), length 100)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x138c (correct), seq 1554:1602, ack 1302, win 501, options [nop,nop,TS val 1013559869 ecr 3108218], length 48
20:30:50.714653 IP (tos 0x0, ttl 64, id 23943, offset 0, flags [DF], proto TCP (6), length 416)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc5ac (incorrect -> 0xe344), seq 1302:1666, ack 1602, win 250, options [nop,nop,TS val 3108226 ecr 1013559869], length 364
20:30:50.715312 IP (tos 0x0, ttl 64, id 2168, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0x783b (correct), ack 1666, win 501, options [nop,nop,TS val 1013559873 ecr 3108226], length 0
20:30:50.717608 IP (tos 0x0, ttl 64, id 2169, offset 0, flags [DF], proto TCP (6), length 68)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x6dff (correct), seq 1602:1618, ack 1666, win 501, options [nop,nop,TS val 1013559876 ecr 3108226], length 16
20:30:50.757910 IP (tos 0x0, ttl 64, id 23944, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0x78f8), ack 1618, win 250, options [nop,nop,TS val 3108269 ecr 1013559876], length 0
20:30:50.758313 IP (tos 0x0, ttl 64, id 2170, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x1f9d (correct), seq 1618:1662, ack 1666, win 501, options [nop,nop,TS val 1013559917 ecr 3108269], length 44
20:30:50.758412 IP (tos 0x0, ttl 64, id 23945, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0x78a3), ack 1662, win 250, options [nop,nop,TS val 3108269 ecr 1013559917], length 0
20:30:50.758627 IP (tos 0x0, ttl 64, id 23946, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc46c (incorrect -> 0x44f4), seq 1666:1710, ack 1662, win 250, options [nop,nop,TS val 3108270 ecr 1013559917], length 44
20:30:50.759503 IP (tos 0x0, ttl 64, id 2171, offset 0, flags [DF], proto TCP (6), length 112)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0xaecc (correct), seq 1662:1722, ack 1710, win 501, options [nop,nop,TS val 1013559917 ecr 3108270], length 60
20:30:50.799920 IP (tos 0x0, ttl 64, id 23947, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0x7811), ack 1722, win 250, options [nop,nop,TS val 3108311 ecr 1013559917], length 0
20:31:00.775934 IP (tos 0x0, ttl 64, id 23948, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc494 (incorrect -> 0x3413), seq 1710:1794, ack 1722, win 250, options [nop,nop,TS val 3118284 ecr 1013559917], length 84
20:31:00.778436 IP (tos 0x0, ttl 64, id 2172, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x7e76 (correct), seq 1722:2222, ack 1794, win 501, options [nop,nop,TS val 1013569937 ecr 3118284], length 500
20:31:00.778579 IP (tos 0x0, ttl 64, id 23949, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0x2794), ack 2222, win 273, options [nop,nop,TS val 3118289 ecr 1013569937], length 0
20:31:00.784253 IP (tos 0x0, ttl 64, id 23950, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc494 (incorrect -> 0x04b3), seq 1794:1878, ack 2222, win 273, options [nop,nop,TS val 3118295 ecr 1013569937], length 84
20:31:00.784653 IP (tos 0x0, ttl 64, id 2173, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0xed56 (correct), seq 2222:2722, ack 1878, win 501, options [nop,nop,TS val 1013569943 ecr 3118295], length 500
20:31:00.785646 IP (tos 0x0, ttl 64, id 23951, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc494 (incorrect -> 0xeb34), seq 1878:1962, ack 2722, win 296, options [nop,nop,TS val 3118297 ecr 1013569943], length 84
20:31:00.786207 IP (tos 0x0, ttl 64, id 2174, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x099c (correct), seq 2722:3222, ack 1962, win 501, options [nop,nop,TS val 1013569945 ecr 3118297], length 500
20:31:00.787013 IP (tos 0x0, ttl 64, id 23952, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc494 (incorrect -> 0xdd13), seq 1962:2046, ack 3222, win 318, options [nop,nop,TS val 3118298 ecr 1013569945], length 84
20:31:00.787599 IP (tos 0x0, ttl 64, id 2175, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x559d (correct), seq 3222:3722, ack 2046, win 501, options [nop,nop,TS val 1013569946 ecr 3118298], length 500
20:31:00.788459 IP (tos 0x0, ttl 64, id 23953, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc494 (incorrect -> 0xf414), seq 2046:2130, ack 3722, win 341, options [nop,nop,TS val 3118299 ecr 1013569946], length 84
20:31:00.829161 IP (tos 0x0, ttl 64, id 2176, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0x1f48 (correct), ack 2130, win 501, options [nop,nop,TS val 1013569987 ecr 3118299], length 0
20:31:08.343673 IP (tos 0x0, ttl 64, id 2177, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x0c05 (correct), seq 3722:3806, ack 2130, win 501, options [nop,nop,TS val 1013577502 ecr 3118299], length 84
20:31:08.367709 IP (tos 0x0, ttl 64, id 23954, offset 0, flags [DF], proto TCP (6), length 80)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc45c (incorrect -> 0xef14), seq 2130:2158, ack 3806, win 341, options [nop,nop,TS val 3125879 ecr 1013577502], length 28
20:31:08.368105 IP (tos 0x0, ttl 64, id 2178, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0xe3c7 (correct), ack 2158, win 501, options [nop,nop,TS val 1013577527 ecr 3125879], length 0
20:31:08.368585 IP (tos 0x0, ttl 64, id 2179, offset 0, flags [DF], proto TCP (6), length 164)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0x6091 (correct), seq 3806:3918, ack 2158, win 501, options [nop,nop,TS val 1013577527 ecr 3125879], length 112
20:31:08.408584 IP (tos 0x0, ttl 64, id 23955, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0xe3ce), ack 3918, win 341, options [nop,nop,TS val 3125920 ecr 1013577527], length 0
20:31:08.627586 IP (tos 0x0, ttl 64, id 23956, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc634 (incorrect -> 0x26d7), seq 2158:2658, ack 3918, win 341, options [nop,nop,TS val 3126139 ecr 1013577527], length 500
20:31:08.627830 IP (tos 0x0, ttl 64, id 2180, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0xdf5c (correct), ack 2658, win 501, options [nop,nop,TS val 1013577786 ecr 3126139], length 0
20:31:08.627890 IP (tos 0x0, ttl 64, id 23957, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc46c (incorrect -> 0x3e03), seq 2658:2702, ack 3918, win 341, options [nop,nop,TS val 3126139 ecr 1013577786], length 44
20:31:08.628027 IP (tos 0x0, ttl 64, id 2181, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0xdf2f (correct), ack 2702, win 501, options [nop,nop,TS val 1013577787 ecr 3126139], length 0
20:31:08.628397 IP (tos 0x10, ttl 64, id 2182, offset 0, flags [DF], proto TCP (6), length 512)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [P.], cksum 0xc52b (correct), seq 3918:4378, ack 2702, win 501, options [nop,nop,TS val 1013577787 ecr 3126139], length 460
20:31:08.628468 IP (tos 0x0, ttl 64, id 23958, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [.], cksum 0xc440 (incorrect -> 0xdded), ack 4378, win 363, options [nop,nop,TS val 3126139 ecr 1013577787], length 0
20:31:08.637326 IP (tos 0x10, ttl 64, id 23959, offset 0, flags [DF], proto TCP (6), length 160)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc4ac (incorrect -> 0x2df8), seq 2702:2810, ack 4378, win 363, options [nop,nop,TS val 3126148 ecr 1013577787], length 108
20:31:08.637555 IP (tos 0x10, ttl 64, id 2183, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0xdce5 (correct), ack 2810, win 501, options [nop,nop,TS val 1013577796 ecr 3126148], length 0
20:31:08.639621 IP (tos 0x10, ttl 64, id 23960, offset 0, flags [DF], proto TCP (6), length 296)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc534 (incorrect -> 0x81d7), seq 2810:3054, ack 4378, win 363, options [nop,nop,TS val 3126151 ecr 1013577796], length 244
20:31:08.639829 IP (tos 0x10, ttl 64, id 2184, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0xdbec (correct), ack 3054, win 501, options [nop,nop,TS val 1013577798 ecr 3126151], length 0
20:31:08.902074 IP (tos 0x10, ttl 64, id 23961, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59112: Flags [P.], cksum 0xc494 (incorrect -> 0xf3d8), seq 3054:3138, ack 4378, win 363, options [nop,nop,TS val 3126413 ecr 1013577798], length 84
20:31:08.902301 IP (tos 0x10, ttl 64, id 2185, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59112 > 192.168.33.200.ssh: Flags [.], cksum 0xd98b (correct), ack 3138, win 501, options [nop,nop,TS val 1013578061 ecr 3126413], length 0
```
    
</details>

Deleting: 
$ sudo ip address del 192.168.33.200/24 dev ens34

### 1.2

$ sudo nano /etc/sysconfig/network-scripts/ifcfg-ens34

```
NM_CONTROLLED=no
DEVICE=ens34
ONBOOT=yes
BOOTPROTO=static
IPADDR0=192.168.33.118
PREFIX0=24
IPADDR1=192.168.33.200
PREFIX1=24
```

$ sudo reboot

Checking of ssh connection btw host and vm:

<details><summary>$ sudo tcpdump -ni ens34 port 22 -vv</summary>

```
[sudo] password for user: 
tcpdump: listening on ens34, link-type EN10MB (Ethernet), capture size 262144 bytes
21:16:07.927048 IP (tos 0x0, ttl 64, id 50097, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [S], cksum 0x567f (correct), seq 3324714287, win 64240, options [mss 1460,sackOK,TS val 1016277063 ecr 0,nop,wscale 7], length 0
21:16:07.927176 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [S.], cksum 0xc448 (incorrect -> 0xb5c6), seq 1946736203, ack 3324714288, win 28960, options [mss 1460,sackOK,TS val 4294762534 ecr 1016277063,nop,wscale 7], length 0
21:16:07.927388 IP (tos 0x0, ttl 64, id 50098, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0x53bc (correct), seq 1, ack 1, win 502, options [nop,nop,TS val 1016277064 ecr 4294762534], length 0
21:16:07.928144 IP (tos 0x0, ttl 64, id 50099, offset 0, flags [DF], proto TCP (6), length 93)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x3062 (correct), seq 1:42, ack 1, win 502, options [nop,nop,TS val 1016277065 ecr 4294762534], length 41
21:16:07.928246 IP (tos 0x0, ttl 64, id 13930, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0x54a4), seq 1, ack 42, win 227, options [nop,nop,TS val 4294762535 ecr 1016277065], length 0
21:16:07.952694 IP (tos 0x0, ttl 64, id 13931, offset 0, flags [DF], proto TCP (6), length 73)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc455 (incorrect -> 0x90c6), seq 1:22, ack 42, win 227, options [nop,nop,TS val 4294762559 ecr 1016277065], length 21
21:16:07.953065 IP (tos 0x0, ttl 64, id 50100, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0x534b (correct), seq 42, ack 22, win 502, options [nop,nop,TS val 1016277090 ecr 4294762559], length 0
21:16:07.953805 IP (tos 0x0, ttl 64, id 50101, offset 0, flags [DF], proto TCP (6), length 1564)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0xca28 (incorrect -> 0x082d), seq 42:1554, ack 22, win 502, options [nop,nop,TS val 1016277090 ecr 4294762559], length 1512
21:16:07.953987 IP (tos 0x0, ttl 64, id 13932, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0x4e5e), seq 22, ack 1554, win 250, options [nop,nop,TS val 4294762560 ecr 1016277090], length 0
21:16:07.962048 IP (tos 0x0, ttl 64, id 13933, offset 0, flags [DF], proto TCP (6), length 1332)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc940 (incorrect -> 0x0499), seq 22:1302, ack 1554, win 250, options [nop,nop,TS val 4294762568 ecr 1016277090], length 1280
21:16:07.962326 IP (tos 0x0, ttl 64, id 50103, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0x4852 (correct), seq 1554, ack 1302, win 501, options [nop,nop,TS val 1016277099 ecr 4294762568], length 0
21:16:07.964151 IP (tos 0x0, ttl 64, id 50104, offset 0, flags [DF], proto TCP (6), length 100)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0xd0c2 (correct), seq 1554:1602, ack 1302, win 501, options [nop,nop,TS val 1016277101 ecr 4294762568], length 48
21:16:07.967503 IP (tos 0x0, ttl 64, id 13934, offset 0, flags [DF], proto TCP (6), length 416)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc5ac (incorrect -> 0xdd1d), seq 1302:1666, ack 1602, win 250, options [nop,nop,TS val 4294762574 ecr 1016277101], length 364
21:16:07.967864 IP (tos 0x0, ttl 64, id 50105, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0x46ab (correct), seq 1602, ack 1666, win 501, options [nop,nop,TS val 1016277104 ecr 4294762574], length 0
21:16:07.970253 IP (tos 0x0, ttl 64, id 50106, offset 0, flags [DF], proto TCP (6), length 68)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x3c6f (correct), seq 1602:1618, ack 1666, win 501, options [nop,nop,TS val 1016277107 ecr 4294762574], length 16
21:16:08.010076 IP (tos 0x0, ttl 64, id 13935, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0x4768), seq 1666, ack 1618, win 250, options [nop,nop,TS val 4294762617 ecr 1016277107], length 0
21:16:08.010473 IP (tos 0x0, ttl 64, id 50107, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0xfc3f (correct), seq 1618:1662, ack 1666, win 501, options [nop,nop,TS val 1016277147 ecr 4294762617], length 44
21:16:08.010554 IP (tos 0x0, ttl 64, id 13936, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0x4714), seq 1666, ack 1662, win 250, options [nop,nop,TS val 4294762617 ecr 1016277147], length 0
21:16:08.011476 IP (tos 0x0, ttl 64, id 13937, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc46c (incorrect -> 0x50a6), seq 1666:1710, ack 1662, win 250, options [nop,nop,TS val 4294762617 ecr 1016277147], length 44
21:16:08.012060 IP (tos 0x0, ttl 64, id 50108, offset 0, flags [DF], proto TCP (6), length 112)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x6d4c (correct), seq 1662:1722, ack 1710, win 501, options [nop,nop,TS val 1016277149 ecr 4294762617], length 60
21:16:08.052152 IP (tos 0x0, ttl 64, id 13938, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0x4680), seq 1710, ack 1722, win 250, options [nop,nop,TS val 4294762659 ecr 1016277149], length 0
21:16:18.034758 IP (tos 0x0, ttl 64, id 13939, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc494 (incorrect -> 0x5273), seq 1710:1794, ack 1722, win 250, options [nop,nop,TS val 4294772639 ecr 1016277149], length 84
21:16:18.037556 IP (tos 0x0, ttl 64, id 50109, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0xa816 (correct), seq 1722:2222, ack 1794, win 501, options [nop,nop,TS val 1016287168 ecr 4294772639], length 500
21:16:18.037654 IP (tos 0x0, ttl 64, id 13940, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0xf5fc), seq 1794, ack 2222, win 273, options [nop,nop,TS val 4294772644 ecr 1016287168], length 0
21:16:18.055449 IP (tos 0x0, ttl 64, id 13941, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc494 (incorrect -> 0x2436), seq 1794:1878, ack 2222, win 273, options [nop,nop,TS val 4294772662 ecr 1016287168], length 84
21:16:18.056054 IP (tos 0x0, ttl 64, id 50110, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x4941 (correct), seq 2222:2722, ack 1878, win 501, options [nop,nop,TS val 1016287187 ecr 4294772662], length 500
21:16:18.056833 IP (tos 0x0, ttl 64, id 13942, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc494 (incorrect -> 0x1f53), seq 1878:1962, ack 2722, win 296, options [nop,nop,TS val 4294772663 ecr 1016287187], length 84
21:16:18.057473 IP (tos 0x0, ttl 64, id 50111, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x8adf (correct), seq 2722:3222, ack 1962, win 501, options [nop,nop,TS val 1016287188 ecr 4294772663], length 500
21:16:18.058117 IP (tos 0x0, ttl 64, id 13943, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc494 (incorrect -> 0x44f0), seq 1962:2046, ack 3222, win 318, options [nop,nop,TS val 4294772665 ecr 1016287188], length 84
21:16:18.058711 IP (tos 0x0, ttl 64, id 50112, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x66e8 (correct), seq 3222:3722, ack 2046, win 501, options [nop,nop,TS val 1016287189 ecr 4294772665], length 500
21:16:18.059356 IP (tos 0x0, ttl 64, id 13944, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc494 (incorrect -> 0xe05f), seq 2046:2130, ack 3722, win 341, options [nop,nop,TS val 4294772666 ecr 1016287189], length 84
21:16:18.101181 IP (tos 0x0, ttl 64, id 50113, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xed96 (correct), seq 3722, ack 2130, win 501, options [nop,nop,TS val 1016287232 ecr 4294772666], length 0
21:16:21.865102 IP (tos 0x0, ttl 64, id 50114, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x4daf (correct), seq 3722:3806, ack 2130, win 501, options [nop,nop,TS val 1016290993 ecr 4294772666], length 84
21:16:21.886407 IP (tos 0x0, ttl 64, id 13945, offset 0, flags [DF], proto TCP (6), length 80)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc45c (incorrect -> 0xa27e), seq 2130:2158, ack 3806, win 341, options [nop,nop,TS val 4294776493 ecr 1016290993], length 28
21:16:21.886716 IP (tos 0x0, ttl 64, id 50115, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xcf6c (correct), seq 3806, ack 2158, win 501, options [nop,nop,TS val 1016291015 ecr 4294776493], length 0
21:16:21.887082 IP (tos 0x0, ttl 64, id 50116, offset 0, flags [DF], proto TCP (6), length 164)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x22a8 (correct), seq 3806:3918, ack 2158, win 501, options [nop,nop,TS val 1016291015 ecr 4294776493], length 112
21:16:21.927190 IP (tos 0x0, ttl 64, id 13946, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0xcf73), seq 2158, ack 3918, win 341, options [nop,nop,TS val 4294776534 ecr 1016291015], length 0
21:16:22.267925 IP (tos 0x0, ttl 64, id 13947, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc634 (incorrect -> 0xa469), seq 2158:2658, ack 3918, win 341, options [nop,nop,TS val 4294776874 ecr 1016291015], length 500
21:16:22.268140 IP (tos 0x0, ttl 64, id 50117, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xca0e (correct), seq 3918, ack 2658, win 501, options [nop,nop,TS val 1016291396 ecr 4294776874], length 0
21:16:22.268379 IP (tos 0x0, ttl 64, id 13948, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc46c (incorrect -> 0x4e7e), seq 2658:2702, ack 3918, win 341, options [nop,nop,TS val 4294776874 ecr 1016291396], length 44
21:16:22.268592 IP (tos 0x0, ttl 64, id 50118, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xc9e1 (correct), seq 3918, ack 2702, win 501, options [nop,nop,TS val 1016291397 ecr 4294776874], length 0
21:16:22.269054 IP (tos 0x10, ttl 64, id 50119, offset 0, flags [DF], proto TCP (6), length 512)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0xd931 (correct), seq 3918:4378, ack 2702, win 501, options [nop,nop,TS val 1016291397 ecr 4294776874], length 460
21:16:22.269128 IP (tos 0x0, ttl 64, id 13949, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0xc89e), seq 2702, ack 4378, win 363, options [nop,nop,TS val 4294776875 ecr 1016291397], length 0
21:16:22.278028 IP (tos 0x10, ttl 64, id 13950, offset 0, flags [DF], proto TCP (6), length 160)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc4ac (incorrect -> 0x7ac0), seq 2702:2810, ack 4378, win 363, options [nop,nop,TS val 4294776884 ecr 1016291397], length 108
21:16:22.278426 IP (tos 0x10, ttl 64, id 50120, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xc796 (correct), seq 4378, ack 2810, win 501, options [nop,nop,TS val 1016291406 ecr 4294776884], length 0
21:16:22.283130 IP (tos 0x10, ttl 64, id 13951, offset 0, flags [DF], proto TCP (6), length 128)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc48c (incorrect -> 0x2d37), seq 2810:2886, ack 4378, win 363, options [nop,nop,TS val 4294776890 ecr 1016291406], length 76
21:16:22.283637 IP (tos 0x10, ttl 64, id 50121, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xc73e (correct), seq 4378, ack 2886, win 501, options [nop,nop,TS val 1016291412 ecr 4294776890], length 0
21:16:22.566473 IP (tos 0x10, ttl 64, id 13952, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc494 (incorrect -> 0x806c), seq 2886:2970, ack 4378, win 363, options [nop,nop,TS val 4294777173 ecr 1016291412], length 84
21:16:22.566665 IP (tos 0x10, ttl 64, id 50122, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xc4b4 (correct), seq 4378, ack 2970, win 501, options [nop,nop,TS val 1016291695 ecr 4294777173], length 0
21:16:24.786870 IP (tos 0x10, ttl 64, id 50123, offset 0, flags [DF], proto TCP (6), length 88)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x469a (correct), seq 4378:4414, ack 2970, win 501, options [nop,nop,TS val 1016293913 ecr 4294777173], length 36
21:16:24.787625 IP (tos 0x10, ttl 64, id 13953, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc46c (incorrect -> 0x2cfd), seq 2970:3014, ack 4414, win 363, options [nop,nop,TS val 4294779394 ecr 1016293913], length 44
21:16:24.788062 IP (tos 0x10, ttl 64, id 50124, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xb30b (correct), seq 4414, ack 3014, win 501, options [nop,nop,TS val 1016293915 ecr 4294779394], length 0
21:16:24.790463 IP (tos 0x10, ttl 64, id 13954, offset 0, flags [DF], proto TCP (6), length 228)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [P.], cksum 0xc4f0 (incorrect -> 0xa0a9), seq 3014:3190, ack 4414, win 363, options [nop,nop,TS val 4294779396 ecr 1016293915], length 176
21:16:24.790689 IP (tos 0x10, ttl 64, id 50125, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xb257 (correct), seq 4414, ack 3190, win 501, options [nop,nop,TS val 1016293917 ecr 4294779396], length 0
21:16:24.790994 IP (tos 0x10, ttl 64, id 50126, offset 0, flags [DF], proto TCP (6), length 88)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0x52c0 (correct), seq 4414:4450, ack 3190, win 501, options [nop,nop,TS val 1016293918 ecr 4294779396], length 36
21:16:24.791074 IP (tos 0x10, ttl 64, id 50127, offset 0, flags [DF], proto TCP (6), length 112)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [P.], cksum 0xc184 (correct), seq 4450:4510, ack 3190, win 501, options [nop,nop,TS val 1016293918 ecr 4294779396], length 60
21:16:24.791079 IP (tos 0x10, ttl 64, id 50128, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [F.], cksum 0xb1f5 (correct), seq 4510, ack 3190, win 501, options [nop,nop,TS val 1016293918 ecr 4294779396], length 0
21:16:24.793034 IP (tos 0x10, ttl 64, id 13955, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [.], cksum 0xc440 (incorrect -> 0xb27c), seq 3190, ack 4511, win 363, options [nop,nop,TS val 4294779399 ecr 1016293918], length 0
21:16:24.808169 IP (tos 0x10, ttl 64, id 13956, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.59946: Flags [F.], cksum 0xc440 (incorrect -> 0xb26b), seq 3190, ack 4511, win 363, options [nop,nop,TS val 4294779415 ecr 1016293918], length 0
21:16:24.808404 IP (tos 0x10, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.59946 > 192.168.33.200.ssh: Flags [.], cksum 0xb1d0 (correct), seq 4511, ack 3191, win 501, options [nop,nop,TS val 1016293935 ecr 4294779415], length 0
^C
60 packets captured
60 packets received by filter
0 packets dropped by kernel
```
</details>    

$ sudo rm  /etc/sysconfig/network-scripts/ifcfg-ens34
$ sudo reboot


## 1.3


$ sudo reboot

Checking of ssh connection btw host and vm:

<details><summary>$ sudo tcpdump -ni ens34 port 22 -vv</summary>

```
tcpdump: listening on ens34, link-type EN10MB (Ethernet), capture size 262144 bytes
21:26:09.568741 IP (tos 0x0, ttl 64, id 2564, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [S], cksum 0xd5f6 (correct), seq 1402528110, win 64240, options [mss 1460,sackOK,TS val 1016878706 ecr 0,nop,wscale 7], length 0
21:26:09.568967 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [S.], cksum 0xc448 (incorrect -> 0x4a8c), seq 3933191980, ack 1402528111, win 28960, options [mss 1460,sackOK,TS val 4294798223 ecr 1016878706,nop,wscale 7], length 0
21:26:09.569206 IP (tos 0x0, ttl 64, id 2565, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xe881 (correct), seq 1, ack 1, win 502, options [nop,nop,TS val 1016878707 ecr 4294798223], length 0
21:26:09.569939 IP (tos 0x0, ttl 64, id 2566, offset 0, flags [DF], proto TCP (6), length 93)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xc528 (correct), seq 1:42, ack 1, win 502, options [nop,nop,TS val 1016878707 ecr 4294798223], length 41
21:26:09.570040 IP (tos 0x0, ttl 64, id 54434, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xe96a), seq 1, ack 42, win 227, options [nop,nop,TS val 4294798224 ecr 1016878707], length 0
21:26:09.597045 IP (tos 0x0, ttl 64, id 54435, offset 0, flags [DF], proto TCP (6), length 73)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc455 (incorrect -> 0x258b), seq 1:22, ack 42, win 227, options [nop,nop,TS val 4294798250 ecr 1016878707], length 21
21:26:09.597370 IP (tos 0x0, ttl 64, id 2567, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xe80c (correct), seq 42, ack 22, win 502, options [nop,nop,TS val 1016878735 ecr 4294798250], length 0
21:26:09.597974 IP (tos 0x0, ttl 64, id 2568, offset 0, flags [DF], proto TCP (6), length 1564)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xca28 (incorrect -> 0xc6e6), seq 42:1554, ack 22, win 502, options [nop,nop,TS val 1016878735 ecr 4294798250], length 1512
21:26:09.598077 IP (tos 0x0, ttl 64, id 54436, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xe31e), seq 22, ack 1554, win 250, options [nop,nop,TS val 4294798252 ecr 1016878735], length 0
21:26:09.610747 IP (tos 0x0, ttl 64, id 54437, offset 0, flags [DF], proto TCP (6), length 1332)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc940 (incorrect -> 0x85fc), seq 22:1302, ack 1554, win 250, options [nop,nop,TS val 4294798264 ecr 1016878735], length 1280
21:26:09.611030 IP (tos 0x0, ttl 64, id 2570, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xdd0a (correct), seq 1554, ack 1302, win 501, options [nop,nop,TS val 1016878748 ecr 4294798264], length 0
21:26:09.614211 IP (tos 0x0, ttl 64, id 2571, offset 0, flags [DF], proto TCP (6), length 100)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x079a (correct), seq 1554:1602, ack 1302, win 501, options [nop,nop,TS val 1016878752 ecr 4294798264], length 48
21:26:09.617870 IP (tos 0x0, ttl 64, id 54438, offset 0, flags [DF], proto TCP (6), length 416)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc5ac (incorrect -> 0x4caf), seq 1302:1666, ack 1602, win 250, options [nop,nop,TS val 4294798271 ecr 1016878752], length 364
21:26:09.618176 IP (tos 0x0, ttl 64, id 2572, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xdb5f (correct), seq 1602, ack 1666, win 501, options [nop,nop,TS val 1016878756 ecr 4294798271], length 0
21:26:09.622226 IP (tos 0x0, ttl 64, id 2573, offset 0, flags [DF], proto TCP (6), length 68)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xd122 (correct), seq 1602:1618, ack 1666, win 501, options [nop,nop,TS val 1016878760 ecr 4294798271], length 16
21:26:09.661944 IP (tos 0x0, ttl 64, id 54439, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xdc19), seq 1666, ack 1618, win 250, options [nop,nop,TS val 4294798316 ecr 1016878760], length 0
21:26:09.662201 IP (tos 0x0, ttl 64, id 2574, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x6647 (correct), seq 1618:1662, ack 1666, win 501, options [nop,nop,TS val 1016878800 ecr 4294798316], length 44
21:26:09.662266 IP (tos 0x0, ttl 64, id 54440, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xdbc5), seq 1666, ack 1662, win 250, options [nop,nop,TS val 4294798316 ecr 1016878800], length 0
21:26:09.662632 IP (tos 0x0, ttl 64, id 54441, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc46c (incorrect -> 0x126f), seq 1666:1710, ack 1662, win 250, options [nop,nop,TS val 4294798316 ecr 1016878800], length 44
21:26:09.663007 IP (tos 0x0, ttl 64, id 2575, offset 0, flags [DF], proto TCP (6), length 112)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xe6ac (correct), seq 1662:1722, ack 1710, win 501, options [nop,nop,TS val 1016878800 ecr 4294798316], length 60
21:26:09.705987 IP (tos 0x0, ttl 64, id 54442, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xdb31), seq 1710, ack 1722, win 250, options [nop,nop,TS val 4294798360 ecr 1016878800], length 0
21:26:29.682819 IP (tos 0x0, ttl 64, id 54443, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc494 (incorrect -> 0x7d34), seq 1710:1794, ack 1722, win 250, options [nop,nop,TS val 4294818335 ecr 1016878800], length 84
21:26:29.684849 IP (tos 0x0, ttl 64, id 2576, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xf09f (correct), seq 1722:2222, ack 1794, win 501, options [nop,nop,TS val 1016898835 ecr 4294818335], length 500
21:26:29.684948 IP (tos 0x0, ttl 64, id 54444, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0x3c84), seq 1794, ack 2222, win 273, options [nop,nop,TS val 4294818339 ecr 1016898835], length 0
21:26:29.692234 IP (tos 0x0, ttl 64, id 54445, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc494 (incorrect -> 0x9dea), seq 1794:1878, ack 2222, win 273, options [nop,nop,TS val 4294818346 ecr 1016898835], length 84
21:26:29.692603 IP (tos 0x0, ttl 64, id 2577, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x2c35 (correct), seq 2222:2722, ack 1878, win 501, options [nop,nop,TS val 1016898843 ecr 4294818346], length 500
21:26:29.693753 IP (tos 0x0, ttl 64, id 54446, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc494 (incorrect -> 0x3dd6), seq 1878:1962, ack 2722, win 296, options [nop,nop,TS val 4294818347 ecr 1016898843], length 84
21:26:29.694375 IP (tos 0x0, ttl 64, id 2578, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xa5b0 (correct), seq 2722:3222, ack 1962, win 501, options [nop,nop,TS val 1016898844 ecr 4294818347], length 500
21:26:29.695081 IP (tos 0x0, ttl 64, id 54447, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc494 (incorrect -> 0x7628), seq 1962:2046, ack 3222, win 318, options [nop,nop,TS val 4294818349 ecr 1016898844], length 84
21:26:29.695559 IP (tos 0x0, ttl 64, id 2579, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xd83d (correct), seq 3222:3722, ack 2046, win 501, options [nop,nop,TS val 1016898846 ecr 4294818349], length 500
21:26:29.696252 IP (tos 0x0, ttl 64, id 54448, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc494 (incorrect -> 0xbc17), seq 2046:2130, ack 3722, win 341, options [nop,nop,TS val 4294818350 ecr 1016898846], length 84
21:26:29.737352 IP (tos 0x0, ttl 64, id 2580, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0x3435 (correct), seq 3722, ack 2130, win 501, options [nop,nop,TS val 1016898887 ecr 4294818350], length 0
21:26:36.295990 IP (tos 0x0, ttl 64, id 2581, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x6433 (correct), seq 3722:3806, ack 2130, win 501, options [nop,nop,TS val 1016905446 ecr 4294818350], length 84
21:26:36.319079 IP (tos 0x0, ttl 64, id 54449, offset 0, flags [DF], proto TCP (6), length 80)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc45c (incorrect -> 0xc73d), seq 2130:2158, ack 3806, win 341, options [nop,nop,TS val 4294824973 ecr 1016905446], length 28
21:26:36.319472 IP (tos 0x0, ttl 64, id 2582, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0x002f (correct), seq 3806, ack 2158, win 501, options [nop,nop,TS val 1016905470 ecr 4294824973], length 0
21:26:36.319750 IP (tos 0x0, ttl 64, id 2583, offset 0, flags [DF], proto TCP (6), length 164)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0xe2a1 (correct), seq 3806:3918, ack 2158, win 501, options [nop,nop,TS val 1016905470 ecr 4294824973], length 112
21:26:36.359682 IP (tos 0x0, ttl 64, id 54450, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0x0037), seq 2158, ack 3918, win 341, options [nop,nop,TS val 4294825013 ecr 1016905470], length 0
21:26:36.628083 IP (tos 0x0, ttl 64, id 54451, offset 0, flags [DF], proto TCP (6), length 552)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc634 (incorrect -> 0xd29c), seq 2158:2658, ack 3918, win 341, options [nop,nop,TS val 4294825281 ecr 1016905470], length 500
21:26:36.628413 IP (tos 0x0, ttl 64, id 2584, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xfb61 (correct), seq 3918, ack 2658, win 501, options [nop,nop,TS val 1016905779 ecr 4294825281], length 0
21:26:36.628481 IP (tos 0x0, ttl 64, id 54452, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc46c (incorrect -> 0x22b4), seq 2658:2702, ack 3918, win 341, options [nop,nop,TS val 4294825282 ecr 1016905779], length 44
21:26:36.628608 IP (tos 0x0, ttl 64, id 2585, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xfb34 (correct), seq 3918, ack 2702, win 501, options [nop,nop,TS val 1016905779 ecr 4294825282], length 0
21:26:36.628871 IP (tos 0x10, ttl 64, id 2586, offset 0, flags [DF], proto TCP (6), length 512)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x07e4 (correct), seq 3918:4378, ack 2702, win 501, options [nop,nop,TS val 1016905779 ecr 4294825282], length 460
21:26:36.628953 IP (tos 0x0, ttl 64, id 54453, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xf9f2), seq 2702, ack 4378, win 363, options [nop,nop,TS val 4294825282 ecr 1016905779], length 0
21:26:36.639702 IP (tos 0x10, ttl 64, id 54454, offset 0, flags [DF], proto TCP (6), length 160)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc4ac (incorrect -> 0x41e2), seq 2702:2810, ack 4378, win 363, options [nop,nop,TS val 4294825293 ecr 1016905779], length 108
21:26:36.639917 IP (tos 0x10, ttl 64, id 2587, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xf8e6 (correct), seq 4378, ack 2810, win 501, options [nop,nop,TS val 1016905790 ecr 4294825293], length 0
21:26:36.644706 IP (tos 0x10, ttl 64, id 54455, offset 0, flags [DF], proto TCP (6), length 128)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc48c (incorrect -> 0xf207), seq 2810:2886, ack 4378, win 363, options [nop,nop,TS val 4294825298 ecr 1016905790], length 76
21:26:36.645209 IP (tos 0x10, ttl 64, id 2588, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xf890 (correct), seq 4378, ack 2886, win 501, options [nop,nop,TS val 1016905795 ecr 4294825298], length 0
21:26:36.900223 IP (tos 0x10, ttl 64, id 54456, offset 0, flags [DF], proto TCP (6), length 136)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc494 (incorrect -> 0xf4ea), seq 2886:2970, ack 4378, win 363, options [nop,nop,TS val 4294825554 ecr 1016905795], length 84
21:26:36.900550 IP (tos 0x10, ttl 64, id 2589, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xf63c (correct), seq 4378, ack 2970, win 501, options [nop,nop,TS val 1016906051 ecr 4294825554], length 0
21:26:40.559635 IP (tos 0x10, ttl 64, id 2590, offset 0, flags [DF], proto TCP (6), length 88)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x26fb (correct), seq 4378:4414, ack 2970, win 501, options [nop,nop,TS val 1016909710 ecr 4294825554], length 36
21:26:40.562027 IP (tos 0x10, ttl 64, id 54457, offset 0, flags [DF], proto TCP (6), length 96)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc46c (incorrect -> 0xb0bc), seq 2970:3014, ack 4414, win 363, options [nop,nop,TS val 4294829216 ecr 1016909710], length 44
21:26:40.562311 IP (tos 0x10, ttl 64, id 2591, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xd950 (correct), seq 4414, ack 3014, win 501, options [nop,nop,TS val 1016909713 ecr 4294829216], length 0
21:26:40.563177 IP (tos 0x10, ttl 64, id 54458, offset 0, flags [DF], proto TCP (6), length 228)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [P.], cksum 0xc4f0 (incorrect -> 0x2aa8), seq 3014:3190, ack 4414, win 363, options [nop,nop,TS val 4294829216 ecr 1016909713], length 176
21:26:40.563678 IP (tos 0x10, ttl 64, id 2592, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xd89f (correct), seq 4414, ack 3190, win 501, options [nop,nop,TS val 1016909714 ecr 4294829216], length 0
21:26:40.563873 IP (tos 0x10, ttl 64, id 2593, offset 0, flags [DF], proto TCP (6), length 88)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x329e (correct), seq 4414:4450, ack 3190, win 501, options [nop,nop,TS val 1016909714 ecr 4294829216], length 36
21:26:40.563888 IP (tos 0x10, ttl 64, id 2594, offset 0, flags [DF], proto TCP (6), length 112)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [P.], cksum 0x9a00 (correct), seq 4450:4510, ack 3190, win 501, options [nop,nop,TS val 1016909714 ecr 4294829216], length 60
21:26:40.563891 IP (tos 0x10, ttl 64, id 2595, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [F.], cksum 0xd83e (correct), seq 4510, ack 3190, win 501, options [nop,nop,TS val 1016909714 ecr 4294829216], length 0
21:26:40.563992 IP (tos 0x10, ttl 64, id 54459, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xd8c6), seq 3190, ack 4511, win 363, options [nop,nop,TS val 4294829218 ecr 1016909714], length 0
21:26:40.582547 IP (tos 0x10, ttl 64, id 54460, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [F.], cksum 0xc440 (incorrect -> 0xd8b3), seq 3190, ack 4511, win 363, options [nop,nop,TS val 4294829236 ecr 1016909714], length 0
21:26:40.582804 IP (tos 0x10, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xd816 (correct), seq 4511, ack 3191, win 501, options [nop,nop,TS val 1016909733 ecr 4294829236], length 0
^C
60 packets captured
60 packets received by filter
0 packets dropped by kernel   
```
    
 </details>     

## 2 

As we see from previous captured dump, that first couple segments are SYN and ACK. <br/>
(Из предыдущего захваченного трафика видно,что первые два пакета - это Syn Ack запросы.)

A client - 192.168.33.1 - send SYN to server (192.168.33.200) with values of seq and win (buffer size - how much packages is he ready to recive without approvement) <br/>
(Клиент - 192.168.33.1 - отправляет SYN серверу - 192.168.33.200 -  со значениями seq и win.)

```
tcpdump: listening on ens34, link-type EN10MB (Ethernet), capture size 262144 bytes
21:26:09.568741 IP (tos 0x0, ttl 64, id 2564, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [S], cksum 0xd5f6 (correct), seq 1402528110, win 64240, options [mss 1460,sackOK,TS val 1016878706 ecr 0,nop,wscale 7], length 0
21:26:09.568967 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [S.], cksum 0xc448 (incorrect -> 0x4a8c), seq 3933191980, ack 1402528111, win 28960, options [mss 1460,sackOK,TS val 4294798223 ecr 1016878706,nop,wscale 7], length 0
```
Third fragment shows us that client has approved receving of segment <br/>
(В третем пакете видно, что клиент подтверждает получение сегмента от сервера.)

```
21:26:09.569206 IP (tos 0x0, ttl 64, id 2565, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xe881 (correct), seq 1, ack 1, win 502, options [nop,nop,TS val 1016878707 ecr 4294798223], length 0
```

The connection is established,  Flags [P.] approves it. <br/>
(Далее соединение в состоянии Established, Flags [P.] тому подтверждение.)

## 3

Flags [F.] is a sign of connection finishing. <br/>
(Знаком завершения TCP является фрагмент с Flags [F.].)

The client had inisilized the clousing of connection. The client and server are exchanging with last fragments. <br/>
(Клиент инициировал завершение соединения. Клиент и серрвер обменияваются заключительными пакетами и подтвержениями их получения.)

```
192.168.33.1.60114 > 192.168.33.200.ssh: Flags [F.], cksum 0xd83e (correct), seq 4510, ack 3190, win 501, options [nop,nop,TS val 1016909714 ecr 4294829216], length 0
21:26:40.563992 IP (tos 0x10, ttl 64, id 54459, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [.], cksum 0xc440 (incorrect -> 0xd8c6), seq 3190, ack 4511, win 363, options [nop,nop,TS val 4294829218 ecr 1016909714], length 0
21:26:40.582547 IP (tos 0x10, ttl 64, id 54460, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.200.ssh > 192.168.33.1.60114: Flags [F.], cksum 0xc440 (incorrect -> 0xd8b3), seq 3190, ack 4511, win 363, options [nop,nop,TS val 4294829236 ecr 1016909714], length 0
21:26:40.582804 IP (tos 0x10, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.33.1.60114 > 192.168.33.200.ssh: Flags [.], cksum 0xd816 (correct), seq 4511, ack 3191, win 501, options [nop,nop,TS val 1016909733 ecr 4294829236], length 0
```

## 4 


Capturing of requests

```
[user@localhost ~]$ sudo tcpdump -ni ens33 port http and src host 192.168.0.17 -XX
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens33, link-type EN10MB (Ethernet), capture size 262144 bytes
22:36:14.930067 IP 192.168.0.17.38930 > 93.184.220.29.http: Flags [.], ack 788752898, win 241, options [nop,nop,TS val 4036288 ecr 1904324565], length 0
	0x0000:  749d 7914 1f16 000c 291b f1b4 0800 4500  t.y.....).....E.
	0x0010:  0034 f490 4000 4006 4ba4 c0a8 0011 5db8  .4..@.@.K.....].
	0x0020:  dc1d 9812 0050 0c52 af19 2f03 6a02 8010  .....P.R../.j...
	0x0030:  00f1 fab5 0000 0101 080a 003d 96c0 7181  ...........=..q.
	0x0040:  afd5                                     ..
22:36:18.770081 IP 192.168.0.17.49478 > 64.233.165.156.http: Flags [.], ack 3318564460, win 878, options [nop,nop,TS val 4040128 ecr 3211561325], length 0
	0x0000:  749d 7914 1f16 000c 291b f1b4 0800 4500  t.y.....).....E.
	0x0010:  0034 787c 4000 4006 1b09 c0a8 0011 40e9  .4x|@.@.......@.
	0x0020:  a59c c146 0050 18aa 3adf c5cd 466c 8010  ...F.P..:...Fl..
	0x0030:  036e a765 0000 0101 080a 003d a5c0 bf6c  .n.e.......=...l
	0x0040:  896d                                     .m
```

Capturing of responses

<details><summary>$ sudo tcpdump -ni ens33 port http and dst host 192.168.0.17 -XX</summary>

```
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens33, link-type EN10MB (Ethernet), capture size 262144 bytes
22:37:58.122196 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [S.], seq 1263248687, ack 4170606059, win 28960, options [mss 1452,sackOK,TS val 170991537 ecr 4139298,nop,wscale 7], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  003c 0000 4000 3806 b9d2 adf9 1a37 c0a8  .<..@.8......7..
	0x0020:  0011 0050 c802 4b4b a52f f896 65eb a012  ...P..KK./..e...
	0x0030:  7120 e35a 0000 0204 05ac 0402 080a 0a31  q..Z...........1
	0x0040:  1fb1 003f 2922 0103 0307                 ...?)"....
22:38:01.813196 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [.], ack 905, win 241, options [nop,nop,TS val 170995332 ecr 4143098], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 8bb4 4000 3806 2e26 adf9 1a37 c0a8  .4..@.8..&...7..
	0x0020:  0011 0050 c802 4b4b a530 f896 6973 8010  ...P..KK.0..is..
	0x0030:  00f1 611b 0000 0101 080a 0a31 2e84 003f  ..a........1...?
	0x0040:  37fa                                     7.
22:38:02.312691 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [P.], seq 1:738, ack 905, win 241, options [nop,nop,TS val 170995806 ecr 4143098], length 737: HTTP: HTTP/1.1 302 Moved Temporarily
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0315 8bb5 4000 3806 2b44 adf9 1a37 c0a8  ....@.8.+D...7..
	0x0020:  0011 0050 c802 4b4b a530 f896 6973 8018  ...P..KK.0..is..
	0x0030:  00f1 ca60 0000 0101 080a 0a31 305e 003f  ...`.......10^.?
	0x0040:  37fa 4854 5450 2f31 2e31 2033 3032 204d  7.HTTP/1.1.302.M
	0x0050:  6f76 6564 2054 656d 706f 7261 7269 6c79  oved.Temporarily
	0x0060:  0d0a 4461 7465 3a20 5468 752c 2033 3020  ..Date:.Thu,.30.
	0x0070:  4465 6320 3230 3231 2031 393a 3338 3a30  Dec.2021.19:38:0
	0x0080:  3120 474d 540d 0a53 6572 7665 723a 2041  1.GMT..Server:.A
	0x0090:  7061 6368 650d 0a56 6172 793a 2041 6363  pache..Vary:.Acc
	0x00a0:  6570 742d 456e 636f 6469 6e67 2c43 6f6f  ept-Encoding,Coo
	0x00b0:  6b69 650d 0a58 2d56 6172 792d 4f70 7469  kie..X-Vary-Opti
	0x00c0:  6f6e 733a 2041 6363 6570 742d 456e 636f  ons:.Accept-Enco
	0x00d0:  6469 6e67 3b6c 6973 742d 636f 6e74 6169  ding;list-contai
	0x00e0:  6e73 3d67 7a69 702c 436f 6f6b 6965 3b73  ns=gzip,Cookie;s
	0x00f0:  7472 696e 672d 636f 6e74 6169 6e73 3d73  tring-contains=s
	0x0100:  656f 6d61 7374 655f 7275 7377 696b 6964  eomaste_ruswikid
	0x0110:  625f 7275 735f 775f 546f 6b65 6e3b 7374  b_rus_w_Token;st
	0x0120:  7269 6e67 2d63 6f6e 7461 696e 733d 7365  ring-contains=se
	0x0130:  6f6d 6173 7465 5f72 7573 7769 6b69 6462  omaste_ruswikidb
	0x0140:  5f72 7573 5f77 5f4c 6f67 6765 644f 7574  _rus_w_LoggedOut
	0x0150:  3b73 7472 696e 672d 636f 6e74 6169 6e73  ;string-contains
	0x0160:  3d73 656f 6d61 7374 655f 7275 7377 696b  =seomaste_ruswik
	0x0170:  6964 625f 7275 735f 775f 5f73 6573 7369  idb_rus_w__sessi
	0x0180:  6f6e 0d0a 4578 7069 7265 733a 2054 6875  on..Expires:.Thu
	0x0190:  2c20 3031 204a 616e 2031 3937 3020 3030  ,.01.Jan.1970.00
	0x01a0:  3a30 303a 3030 2047 4d54 0d0a 4361 6368  :00:00.GMT..Cach
	0x01b0:  652d 436f 6e74 726f 6c3a 2070 7269 7661  e-Control:.priva
	0x01c0:  7465 2c20 6d75 7374 2d72 6576 616c 6964  te,.must-revalid
	0x01d0:  6174 652c 206d 6178 2d61 6765 3d30 0d0a  ate,.max-age=0..
	0x01e0:  436f 6e74 656e 742d 456e 636f 6469 6e67  Content-Encoding
	0x01f0:  3a20 677a 6970 0d0a 4c6f 6361 7469 6f6e  :.gzip..Location
	0x0200:  3a20 6874 7470 3a2f 2f77 7777 2e73 6275  :.http://www.sbu
	0x0210:  702e 636f 6d2f 7769 6b69 2f25 4430 2539  p.com/wiki/%D0%9
	0x0220:  4525 4430 2542 3125 4431 2538 3125 4431  E%D0%B1%D1%81%D1
	0x0230:  2538 3325 4430 2542 3625 4430 2542 3425  %83%D0%B6%D0%B4%
	0x0240:  4430 2542 3525 4430 2542 4425 4430 2542  D0%B5%D0%BD%D0%B
	0x0250:  3825 4430 2542 355f 2544 3125 3833 2544  8%D0%B5_%D1%83%D
	0x0260:  3125 3837 2544 3025 4230 2544 3125 3831  1%87%D0%B0%D1%81
	0x0270:  2544 3125 3832 2544 3025 4244 2544 3025  %D1%82%D0%BD%D0%
	0x0280:  4238 2544 3025 4241 2544 3025 4230 3a57  B8%D0%BA%D0%B0:W
	0x0290:  696b 6953 7973 6f70 0d0a 436f 6e74 656e  ikiSysop..Conten
	0x02a0:  742d 4c65 6e67 7468 3a20 3230 0d0a 4b65  t-Length:.20..Ke
	0x02b0:  6570 2d41 6c69 7665 3a20 7469 6d65 6f75  ep-Alive:.timeou
	0x02c0:  743d 332c 206d 6178 3d36 300d 0a43 6f6e  t=3,.max=60..Con
	0x02d0:  6e65 6374 696f 6e3a 204b 6565 702d 416c  nection:.Keep-Al
	0x02e0:  6976 650d 0a43 6f6e 7465 6e74 2d54 7970  ive..Content-Typ
	0x02f0:  653a 2074 6578 742f 6874 6d6c 3b20 6368  e:.text/html;.ch
	0x0300:  6172 7365 743d 7574 662d 380d 0a0d 0a1f  arset=utf-8.....
	0x0310:  8b08 0000 0000 0000 0303 0000 0000 0000  ................
	0x0320:  0000 00                                  ...
22:38:02.392893 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [.], ack 1774, win 255, options [nop,nop,TS val 170995912 ecr 4143682], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 8bb6 4000 3806 2e24 adf9 1a37 c0a8  .4..@.8..$...7..
	0x0020:  0011 0050 c802 4b4b a811 f896 6cd8 8010  ...P..KK....l...
	0x0030:  00ff 563b 0000 0101 080a 0a31 30c8 003f  ..V;.......10..?
	0x0040:  3a42                                     :B
22:38:02.878076 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [.], seq 738:3618, ack 1774, win 255, options [nop,nop,TS val 170996390 ecr 4143682], length 2880: HTTP: HTTP/1.1 404 Not Found
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0b74 8bb7 4000 3806 22e3 adf9 1a37 c0a8  .t..@.8."....7..
	0x0020:  0011 0050 c802 4b4b a811 f896 6cd8 8010  ...P..KK....l...
	0x0030:  00ff 9450 0000 0101 080a 0a31 32a6 003f  ...P.......12..?
	0x0040:  3a42 4854 5450 2f31 2e31 2034 3034 204e  :BHTTP/1.1.404.N
	0x0050:  6f74 2046 6f75 6e64 0d0a 4461 7465 3a20  ot.Found..Date:.
	0x0060:  5468 752c 2033 3020 4465 6320 3230 3231  Thu,.30.Dec.2021
	0x0070:  2031 393a 3338 3a30 3220 474d 540d 0a53  .19:38:02.GMT..S
	0x0080:  6572 7665 723a 2041 7061 6368 650d 0a43  erver:.Apache..C
	0x0090:  6f6e 7465 6e74 2d6c 616e 6775 6167 653a  ontent-language:
	0x00a0:  2072 750d 0a56 6172 793a 2041 6363 6570  .ru..Vary:.Accep
	0x00b0:  742d 456e 636f 6469 6e67 2c43 6f6f 6b69  t-Encoding,Cooki
	0x00c0:  650d 0a58 2d56 6172 792d 4f70 7469 6f6e  e..X-Vary-Option
	0x00d0:  733a 2041 6363 6570 742d 456e 636f 6469  s:.Accept-Encodi
	0x00e0:  6e67 3b6c 6973 742d 636f 6e74 6169 6e73  ng;list-contains
	0x00f0:  3d67 7a69 702c 436f 6f6b 6965 3b73 7472  =gzip,Cookie;str
	0x0100:  696e 672d 636f 6e74 6169 6e73 3d73 656f  ing-contains=seo
	0x0110:  6d61 7374 655f 7275 7377 696b 6964 625f  maste_ruswikidb_
	0x0120:  7275 735f 775f 546f 6b65 6e3b 7374 7269  rus_w_Token;stri
	0x0130:  6e67 2d63 6f6e 7461 696e 733d 7365 6f6d  ng-contains=seom
	0x0140:  6173 7465 5f72 7573 7769 6b69 6462 5f72  aste_ruswikidb_r
	0x0150:  7573 5f77 5f4c 6f67 6765 644f 7574 3b73  us_w_LoggedOut;s
	0x0160:  7472 696e 672d 636f 6e74 6169 6e73 3d73  tring-contains=s
	0x0170:  656f 6d61 7374 655f 7275 7377 696b 6964  eomaste_ruswikid
	0x0180:  625f 7275 735f 775f 5f73 6573 7369 6f6e  b_rus_w__session
	0x0190:  0d0a 4578 7069 7265 733a 2054 6875 2c20  ..Expires:.Thu,.
	0x01a0:  3031 204a 616e 2031 3937 3020 3030 3a30  01.Jan.1970.00:0
	0x01b0:  303a 3030 2047 4d54 0d0a 4361 6368 652d  0:00.GMT..Cache-
	0x01c0:  436f 6e74 726f 6c3a 2070 7269 7661 7465  Control:.private
	0x01d0:  2c20 6d75 7374 2d72 6576 616c 6964 6174  ,.must-revalidat
	0x01e0:  652c 206d 6178 2d61 6765 3d30 0d0a 436f  e,.max-age=0..Co
	0x01f0:  6e74 656e 742d 456e 636f 6469 6e67 3a20  ntent-Encoding:.
	0x0200:  677a 6970 0d0a 4b65 6570 2d41 6c69 7665  gzip..Keep-Alive
	0x0210:  3a20 7469 6d65 6f75 743d 332c 206d 6178  :.timeout=3,.max
	0x0220:  3d35 390d 0a43 6f6e 6e65 6374 696f 6e3a  =59..Connection:
	0x0230:  204b 6565 702d 416c 6976 650d 0a54 7261  .Keep-Alive..Tra
	0x0240:  6e73 6665 722d 456e 636f 6469 6e67 3a20  nsfer-Encoding:.
	0x0250:  6368 756e 6b65 640d 0a43 6f6e 7465 6e74  chunked..Content
	0x0260:  2d54 7970 653a 2074 6578 742f 6874 6d6c  -Type:.text/html
	0x0270:  3b20 6368 6172 7365 743d 5554 462d 380d  ;.charset=UTF-8.
	0x0280:  0a0d 0a31 6531 300d 0a1f 8b08 0000 0000  ...1e10.........
	0x0290:  0000 03ed 5d7b 6f1b d795 ff3b fa14 53ee  ....]{o....;..S.
	0x02a0:  3ab6 130f 2959 916d c9a2 02bd 9cb8 481c  :...)Y.m......H.
	0x02b0:  2152 ea16 8661 8cc8 9138 3639 c3ce 0c2d  !R...a...869...-
	0x02c0:  2b45 81c4 d934 58a4 9b6c d362 b7d8 471f  +E...4X..l.b..G.
	0x02d0:  e8fe b140 ffa8 e3c4 7939 7180 7c02 ea2b  ...@....y9q.|..+
	0x02e0:  ec17 d8af b0bf 73ce 9d3b 7786 3324 2551  ......s..;w.3$%Q
	0x02f0:  758b 6e1e 436a e6ce 7d9c 7bee 79fc ceb9  u.n.Cj..}.{.y...
	0x0300:  97ff fbf8 dbc5 efad bdb6 baf5 a38d 75ab  ..............u.
	0x0310:  1577 dad6 c61b 2baf 5c5d b52a 76ad 767d  .w....+.\].*v.v}
	0x0320:  76b5 565b db5a b37e f8f2 d6ab af58 33d5  v.V[.Z.~.....X3.
	0x0330:  696b 2b74 fcc8 8bbd c077 dab5 dafa b58a  ik+t.....w......
	0x0340:  5569 c571 77a1 56db dbdb abee cd56 8370  Ui.qw.V......V.p
	0x0350:  b7b6 f57a ed1e d535 432f abaf 766c bc59  ...z...5C/..vl.Y
	0x0360:  6dc6 cdca d2d4 2237 d876 fcdd 7a25 ec55  m....."7.v..z%.U
	0x0370:  ac7b 9db6 1fd5 0b2a 9c99 9f9f 977a b8d0  .{.....*.....z..
	0x0380:  42fa 4afa ade9 85f5 4a3b 0e51 ef33 8b2d  B.J.....J;.Q.3.-
	0x0390:  d769 e2f3 99c5 8e1b 3b96 ef74 dc7a e5ae  .i......;..t.z..
	0x03a0:  e7ee 7583 30ae 588d c08f 5d3f ae57 f6bc  ..u.0.X...]?.W..
	0x03b0:  66dc aa37 ddbb 5ec3 b5f9 8f73 96e7 6378  f..7..^....s..cx
	0x03c0:  4edb 8e1a 4edb adcf 9cb3 3ace 3daf d3eb  N...N.....:.=...
	0x03d0:  2437 2ab5 b462 1aba edfe b8e7 ddad 5756  $7*..b........WV
	0x03e0:  a552 7b6b bfeb 1a4d c4ee bdb8 463d bf6c  .R{k...M....F=.l
	0x03f0:  355a 4e18 b971 fd8d ad2b f6a5 8a35 a29e  5ZN..q...+...5..
	0x0400:  cd78 bfed 16d6 d688 a2cc db32 bc5d d777  .x.........2.].w
	0x0410:  4327 0e42 a3f1 57dd a6e7 5cf7 ee78 98bb  C'.B..W...\..x..
	0x0420:  99b9 ea4c c16b 61b0 1dc4 a84f d3c4 0f3c  ...L.ka....O...<
	0x0430:  bfe9 de3b e707 3b41 bb1d ec15 bc73 c7dd  ...;..;A.....s..
	0x0440:  df0b c2a6 f956 ff37 fd8f 0fde 3e78 a7ff  .....V.7....>x..
	0x0450:  59ff d3fe a3fe 37fd 2ffa 8fac 8377 0ede  Y.....7./....w..
	0x0460:  eb3f c0ed fb7c e3ab fe83 05ea cce6 7e14  .?...|........~.
	0x0470:  7493 6adb 9e7f c70a dd76 bd12 b530 398d  t.j......v...09.
	0x0480:  5e6c 79e8 4bc5 6a85 ee4e bd52 db71 3039  ^ly.K.j..N.R.q09
	0x0490:  815f c5a5 e015 d709 1bad 8a15 83e6 f58a  ._..............
	0x04a0:  d3ed b6bd 8643 cc59 0bba ae1f f1d3 a61b  .....C.Y........
	0x04b0:  3542 af4b 779f 07ef e88a f78c 32b7 a850  5B.Kw.......2..P
	0x04c0:  b5db 42af 622f c6b4 5736 ddc0 62c2 d956  ..B.b/..W6..b..V
	0x04d0:  ffb7 fd27 fd2f 0ede 46ff 9ff4 1f62 3c1f  ...'./..F....b<.
	0x04e0:  5a18 edb7 18d4 17fd aff1 ffe7 b8f5 3314  Z.............3.
	0x04f0:  c0ed 2f50 f8e0 2d14 fb04 d707 788a e7fc  ../P..-.....x...
	0x0500:  375e 5334 3913 f6ce 0e0e c469 c76e e83b  7^S49......i.n.;
	0x0510:  3138 6770 2c61 1449 cf4f ba6f fff3 d6af  18gp,a.I.O.o....
	0x0520:  acd7 3737 edfe 639a 420c f081 412d e60a  ..77..c.B...A-..
	0x0530:  a2d1 8bd2 8d53 6bd3 a796 67e8 bab2 726a  .....Sk...g...rj
	0x0540:  6de6 d4a5 59fe 7e81 af73 7c95 a76b 7c9d  m...Y.~..s|..k|.
	0x0550:  e632 5716 5e77 1b58 25ab 2d2c 7a37 7ad6  .2W.^w.X%.-,z7z.
	0x0560:  e974 2fef b86e b38e 311e 922a 60f5 ce9f  .t/..n..1..*`...
	0x0570:  852c dffd 8ee8 b28c e69e 0661 6898 0965  .,.........ah..e
	0x0580:  98f0 4b87 5e6a 8b35 7991 e4a1 b1dc 48be  ..K.^j.5y.....H.
	0x0590:  442d d785 4054 6b6d af16 ddf1 fca8 d608  D-..@Tkm........
	0x05a0:  3a1d aca1 08f2 ca6d 5621 6e5e 3c3f 7d31  :......mV!n^<?}1
	0x05b0:  e14c 1668 2c82 3a24 5db0 6e1b a1eb 62c1  .L.h,.:$].n...b.
	0x05c0:  8a3c 3b4c 03d2 ce46 e8f9 f1c8 56ba 54ea  .<;L...F....V.T.
	0x05d0:  508d a06a c8b6 e04e ade3 78fe c8fa b3a3  P..j...N..x.....
	0x05e0:  f89e 6ddf f076 ac76 6c5d 5db7 e6aa 73d3  ..m..v.vl]]...s.
	0x05f0:  d3d3 3797 c61b 9b6e f6ea fadc f415 ef9e  ..7....n........
	0x0600:  1b1d a2ed c5ef dd70 fda6 b773 d3b6 999a  .......p...s....
	0x0610:  aa1f c7ea c4dc e43a 71e1 0844 b830 4122  .......:q..D.0A"
	0x0620:  5c3c 42fb 178f ddfe 0896 ce0b 46ad 7417  \<B.........F.t.
	0x0630:  5699 bf69 fa59 d0f5 22b7 13ed 369c 46cb  V..i.Y.."...6.F.
	0x0640:  adef 2be1 d760 714f 6bea d4f9 2b49 c108  ..+..`qOk...+I..
	0x0650:  2687 b30b e3e3 12f8 8e5f 751a a4bf eaa1  &........_u.....
	0x0660:  b3c7 7f9a cf07 d7e5 580b b1bc d77a 3dfe  ........X....z=.
	0x0670:  593b ad84 c961 9679 f910 5e55 4bff af83  Y;...a.y..^UK...
	0x0680:  f4f6 a829 e6e7 b0ef ea2c 76c5 4048 c5b0  ...).....,v.@H..
	0x0690:  4c77 4662 d13a 11ab c72c 7ddb b9eb c8dd  LwFb.:...,}.....
	0x06a0:  8a15 850d 1857 3981 7f75 5d44 c56d 11f8  .....W9..u]D.m..
	0x06b0:  4b8b 3529 5e6c f07a 1df0 681c 04ed 6dc7  K.5)^l.z..h...m.
	0x06c0:  b439 7db6 d332 828c fa67 76c7 92de 1bfd  .9}..2...gv.....
	0x06d0:  59aa 3d87 3756 d796 b796 6f3c 5743 f9bb  Y.=.7V....o<WC..
	0x06e0:  4e68 9132 b2ea 5625 91a8 95cb c903 525d  Nh.2..V%......R]
	0x06f0:  5d27 6ed1 d364 10fa e9de ee72 187b 8db6  ]'n..d.....r.{..
	0x0700:  bba1 4bc0 90ab fdfd 8c51 6293 c795 1618  ..K......Qb.....
	0x0710:  78a4 6ad6 2c66 14f8 8113 7a8e 1f67 1bd9  x.j.,f....z..g..
	0x0720:  71da 919b f40f 3de0 f54a f547 a8e9 273f  q.....=..J.G..'?
	0x0730:  4d9f 6cba e15d 37a4 ea0d bf29 daee 75ab  M.l..]7....)..u.
	0x0740:  d086 462b ab8e 1ff8 b066 dbd7 60dd 475d  ..F+.....f..`.G]
	0x0750:  a7e1 d23b 6f44 6e78 2b76 da77 8a4a 6e76  ...;oDnx+v.w.Jnv
	0x0760:  dd06 3c97 0d4c 0bbd 84f2 b95e e9aa aef5  ..<..L.....^....
	0x0770:  3adb dc89 d9b4 63c6 6b95 2213 e3d6 506b  :.....c.k."...Pk
	0x0780:  3ead 678b 6c0d ea6b 6aea e7e9 424f c91b  >.g.l..kj...BO..
	0x0790:  1b9c b2ab 4d3c 9b4e cb5f 8d14 9971 3b0e  ....M<.N._...q;.
	0x07a0:  7b06 8589 126a 947e afdd 4e5f a107 2f85  {....j.~..N_../.
	0x07b0:  41af 4b94 1f7c f40a 0ccf 1e28 447d 80cf  A.K..|.....(D}..
	0x07c0:  99be a7fc b7d2 e72b a1eb dcb9 12d2 6c0c  .......+......l.
	0x07d0:  5276 b517 be0e 2f32 c2a4 e787 f003 37a4  Rv..../2......7.
	0x07e0:  dbd4 9e72 c2d2 36d7 7d67 bbed 2e6f 5c1d  ...r..6.}g...o\.
	0x07f0:  189e 3cb9 1e7a 71e1 e34d b03f 3b7b ec8f  ..<..zq..M.?;{..
	0x0800:  ef04 6167 8bca a39a 1b95 73cf 542b e7ac  ..ag......s.T+..
	0x0810:  ca77 bf7b e65c e566 dad6 9ab7 ebc5 05c5  .w.{.\.f........
	0x0820:  a9ac 59ee 7537 8a43 8ff9 77bd e9c5 54a5  ..Y.u7.C..w...T.
	0x0830:  518b f1f4 d5e0 2e37 c84f 6bcf ddbc b9f4  Q......7.Ok.....
	0x0840:  5c2d 9518 f935 3fb0 e48b 45d0 1e96 eab6  \-...5?...E.....
	0x0850:  171b 3208 82cd 4aee 5ab7 230b 9651 462e  ..2...J.Z.#..QF.
	0x0860:  d1f3 97e1 ee5b b2a6 b9c0 111b 776e 3bf7  .....[......wn;.
	0x0870:  8a85 df78 c234 af90 0a05 3bc9 f1db da20  ...x.4....;.....
	0x0880:  2019 57d7 020e 6213 a301 bee2 0e8c 3411  ..W...b.......4.
	0x0890:  a004 7810 ffd6 2ba6 3837 74c2 a094 97ce  ..x...+.87t.....
	0x08a0:  47b5 dd20 d86d bb0e 909b 7dc8 4722 7146  G....m....}.G"qF
	0x08b0:  c42f d604 3559 dc0e 9afb 56a3 ed44 c062  ./..5Y....V..D.b
	0x08c0:  582d 13f9 610b 8796 1fd9 b374 2109 6475  X-..a......t!.du
	0x08d0:  d10b 7b4c 4971 4b0b 0396 ea76 3a62 8035  ..{LIqK....v:b.5
	0x08e0:  4def aee5 3581 60b4 836d a77d 3d84 1fef  M...5.`..m.}=...
	0x08f0:  328c 933e 6a04 ed5e c7b7 1548 c110 4ff2  2..>j..^...H..O.
	0x0900:  9671 ef99 c504 eb89 0960 a03a e90b f8c5  .q.......`.:....
	0x0910:  a1da 444b 5a2f 3119 2c41 07ac ed7d f831  ..DKZ/1.,A...}.1
	0x0920:  399e 3906 8daf b97b 42e6 5ebc 9327 b034  9.9....{B.^..'.4
	0x0930:  bfee 3787 75a1 35c3 fdde f1c2 2826 b6f6  ..7.u.5.....(&..
	0x0940:  fc5d 8033 3219 999b 47f1 035b 3319 aad2  .].32...G..[3...
	0x0950:  442b b1c7 e406 6e36 cbad 1307 6ef6 b62b  D+....n6....n..+
	0x0960:  4bfd ff00 b871 bfff 0820 c617 8030 1e03  K....q.......0..
	0x0970:  e2e8 7f6e 9d14 3802 0e9c 957e e426 97fb  ...n..8....~.&..
	0x0980:  b258 c35d 9947 fe47 17ba ddeb 74ed 38b0  .X.].G.G....t.8.
	0x0990:  7de7 2e7a fc5b eeed a3fe 9704 d058 fdaf  }..z.[.......X..
	0x09a0:  162c 7085 38b8 7fa7 d828 f05d 14fc 0603  .,p.8....(.]....
	0x09b0:  7a88 f17c 92e0 37c4 26e7 8cd2 c221 57fd  z..|..7.&....!W.
	0x09c0:  6e2f 46f1 6f13 1488 8a49 5f12 8e8a 6227  n/F.o....I_...b'
	0x09d0:  8c13 044d f192 744f 4d9c 1fa0 0099 2464  ...M..tOM.....$d
	0x09e0:  f710 f0d9 5dea 7f64 510f 181c 7b72 f0e1  ....]..dQ...{r..
	0x09f0:  c13f a227 5f5a 008c 9ee0 7f46 5f2c 227c  .?.'_Z.....F_,"|
	0x0a00:  ff2b 2ac1 452d 206b 8422 7d83 225f 5a74  .+*.E-.k."}."_Zt
	0x0a10:  9b41 2620 6b80 9f1e 59a8 e53e 2170 7cbd  .A&.k...Y..>!p|.
	0x0a20:  df7f 082c eed1 c1fd ea54 ffa3 83f7 a5de  ...,.....T......
	0x0a30:  cfe8 064a 6a7a d468 61d7 8e08 e46c 3275  ...Jjz.ha....l2u
	0x0a40:  6a06 a0a7 e0a9 feef fb8f 1908 7cd4 ff98  j...........|...
	0x0a50:  87f8 e1c2 4059 a1be 4c11 ca12 6d09 4aa3  ....@Y..L...m.J.
	0x0a60:  9b02 1d1a 63fd a4ff 84c7 0fa0 4dc1 6807  ....c.......M.h.
	0x0a70:  1fd2 1c58 fd87 2876 f016 deff 0434 7897  ...X..(v.....4x.
	0x0a80:  4942 ec7a f073 d0f3 dd73 538b 309b fc64  IB.z.s...sS.0..d
	0x0a90:  0aba 6da0 00e4 c991 d04b 18a2 c004 8339  ..m......K.....9
	0x0aa0:  3921 a4eb 9560 970d 7792 938c 96cd af27  9!...`..w......'
	0x0ab0:  a818 9030 6063 39cc ec05 0339 13cc ec92  ...0`c9....9....
	0x0ac0:  dc79 3e29 8a17 2e1a 609a 5471 de00 d9e4  .y>)....`.Tq....
	0x0ad0:  8565 5566 76d9 981c c589 e03f 021a db16  .eUfv......?....
	0x0ae0:  7362 8228 fe0d d101 4b15 5e4b bd72 6b1b  sb.(....K.^K.rk.
	0x0af0:  52fe 8e12 038a 11df 061b 6215 81cd b050  R.........b....P
	0x0b00:  9255 74f0 01af 4db0 2480 5e70 2a21 c190  .Ut...M.$.^p*!..
	0x0b10:  2b9f 61a5 bdc5 6cf9 98f0 5d96 1d53 28f7  +.a...l...]..S(.
	0x0b20:  180f 17b7 8fc2 6247 658f 5b47 638f 148a  ......bGe.[Gc...
	0x0b30:  37dd 4fa8 7b0a 9088 be39 2eb3 fc05 8d28  7.O.{....9.....(
	0x0b40:  3fed 98c4 2798 5048 5492 1739 697a f00e  ?...'.PHT..9iz..
	0x0b50:  6e90 f87d 00cc 1f20 7f4e fc40 b07d 2d4a  n..}.....N.@.}-J
	0x0b60:  607b a93a f56c 3bbe 4cda e0d9 ddf8 320c  `{.:.l;.L.....2.
	0x0b70:  5388 1cc8 f75a 972e acaf a658 eb4f c130  S....Z.....X.O.0
	0x0b80:  d8d8                                     ..
22:38:02.879361 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [.], seq 3618:5058, ack 1774, win 255, options [nop,nop,TS val 170996390 ecr 4143682], length 1440: HTTP
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  05d4 8bb9 4000 3806 2881 adf9 1a37 c0a8  ....@.8.(....7..
	0x0020:  0011 0050 c802 4b4b b351 f896 6cd8 8010  ...P..KK.Q..l...
	0x0030:  00ff a081 0000 0101 080a 0a31 32a6 003f  ...........12..?
	0x0040:  3a42 b0da 5e07 2675 e852 1c6a 6a03 9f61  :B..^.&u.R.jj..a
	0x0050:  d070 a328 8069 1534 5da8 909e 1f2f 58b3  .p.(.i.4]..../X.
	0x0060:  b5f3 007e a6a7 a736 8228 b6dd 7ba8 b389  ...~...6.(..{...
	0x0070:  b854 a3dd 4399 c87b d35d b0a6 5164 fee2  .T..C..{.]..Qd..
	0x0080:  ccdc 7918 30b1 1b4d 6db9 1d48 38d8 8d60  ..y.0..Mm..H8..`
	0x0090:  ef5e 0708 7b49 b9f5 7b14 18f1 60b9 c381  .^..{I..{...`...
	0x00a0:  80a7 64ed f47c b6f5 93b6 a76b 3368 986c  ..d..|.....k3h.l
	0x00b0:  6853 8131 2cb3 1304 101e 505f fd5f 2bb5  hS.1,.....P_._+.
	0x00c0:  f59e c475 2c02 c8bf fbe3 70b1 9aa8 9aa7  ...u,.....p.....
	0x00d0:  c614 95a5 4231 f7d4 fb45 acf4 dde3 8c75  ....B1...E.....u
	0x00e0:  c336 d076 b834 f56c d309 c3cb d670 3007  .6.v.4.l.....p0.
	0x00f0:  5305 169b 22c8 e496 d3f0 1af5 9f34 9dd8  S..."........4..
	0x0100:  d908 83bb 5ed3 0d17 66a6 7f7a f94c 32cd  ....^...f..z.L2.
	0x0110:  67ce fe84 cab9 f566 d060 3ea9 02bd 07df  g......f.`>.....
	0x0120:  acb7 5dfa eb0c a1f9 0410 9dbd ec56 8b9d  ..]..........V..
	0x0130:  0a3c 70a2 7dbf 5167 7fdc ad32 9244 948d  .<p.}.Qg...2.D..
	0x0140:  5410 185d 40b5 be1b d7f0 8d6c e0cb d462  T..]@......l...b
	0x0150:  9cb6 08f9 ab9a 8b56 f6b7 9c5d 72e3 d386  .......V...]r...
	0x0160:  6f4c dfbc 1c57 c19d e8ce 352c 8a2a 2212  oL...W....5,.*".
	0x0170:  6e18 afb8 f072 dd33 eeb9 f8ec 4fcf 9e39  n....r.3....O..9
	0x0180:  3b55 ab31 8f26 0815 5160 e6d2 fcc5 f317  ;U.1.&..Q`......
	0x0190:  2e5e 989b b974 e105 3cb5 f81f f833 217f  .^...t..<....3!.
	0x01a0:  a54f d095 694b 4b12 407b de66 4bac 4a25  .O..iKK.@{.fK.J%
	0x01b0:  ffe0 d0f7 9cf6 2a7c 2670 bd9e a0f4 8be1  ......*|&p......
	0x01c0:  4d2c 372d c451 11ab 99b4 4321 b58e 7425  M,7-.Q....C!..t%
	0x01d0:  0adb 2fe8 726a 58b3 43c5 96b0 e14c 756d  ../.rjX.C....Lum
	0x01e0:  c0d3 240e 28b6 2b4a 8044 150c 57f1 c75a  ..$.(.+J.D..W..Z
	0x01f0:  7330 b029 a209 f909 9392 4cd0 83f7 61b6  s0.)......L...a.
	0x0200:  cf69 bf22 796b 05be 8572 2a7a 6de5 7db5  .i."yk...r*zm.}.
	0x0210:  bda4 d256 d041 c310 1889 cdf8 2bb6 0061  ...V.A......+..a
	0x0220:  d826 c1a8 d2b5 0ae7 83bd 4971 eb16 6b6d  .&........Iq..km
	0x0230:  0fb5 b357 6021 40c3 ee4b c3b1 7dd8 e4db  ...W`!@..K..}...
	0x0240:  3610 7782 2665 203e 00a7 542f 97d9 7988  6.w.&e.>..T/..y.
	0x0250:  628e 6b66 956b 50d6 a888 9d91 bd59 47d4  b.kf.kP......YG.
	0x0260:  3d19 25fb 26ac 7ad8 7038 f8b9 d8c7 7963  =.%.&.z.p8....yc
	0x0270:  fe41 41e4 dcba d1b8 59b1 9c06 a90b c4df  .AA.....Y.......
	0x0280:  3148 d82e 7fc8 c6d7 0d82 e4c8 c190 6142  1H............aB
	0x0290:  88c8 6dbb 8dd8 6d5a 6351 e4a9 c9eb bc59  ..m...mZcQ.....Y
	0x02a0:  5246 d4c2 cc03 a231 1211 c0aa 9f29 1f29  RF.....1.....).)
	0x02b0:  4f65 7845 37e2 2c49 c9cd 2ba8 4d93 95c4  OexE7.,I..+.M...
	0x02c0:  434d b839 595a fad3 f0f6 9215 c3bc d8b5  CM.9YZ..........
	0x02d0:  0166 4494 2e93 aea0 7f87 1109 d579 f03e  .fD..........y.>
	0x02e0:  5995 f07a c497 831f a33c bfb1 97d4 117a  Y..z.....<.....z
	0x02f0:  d30e 7603 e989 6345 84a3 d72b db4e e3ce  ..v...cE...+.N..
	0x0300:  2e10 53bf 6933 a6bf 60f5 c2f6 997c 7080  ..S.i3..`....|p.
	0x0310:  1f45 ec32 56bb feee d9cb 69d8 9854 a85e  .E.2V.....i..T.^
	0x0320:  969a d9ff 1584 ff04 f630 79d9 256c 7ee3  .........0y.%l~.
	0x0330:  cdec 04bc 9960 359a ac43 81b7 250b 31da  .....`5..C..%.1.
	0x0340:  337b f0d7 82bd aa17 bdba 8990 ebdc 596b  3{............Yk
	0x0350:  c7bb e7b4 bb2d e7cc 5968 ce34 8461 d833  .....-..Yh.4.a.3
	0x0360:  a755 b28c dbb4 23e8 4804 302c 3569 a769  .U....#.H.0,5i.i
	0x0370:  d24e 7709 4bf0 7639 95e4 b416 7cff 3908  .Nw.K.v9....|.9.
	0x0380:  180c 08be d35d 127c fcce 338b a6e0 235e  .....].|..3...#^
	0x0390:  00ee 0527 9471 3323 2b25 2394 32a4 5cea  ...'.q3#+%#.2.\.
	0x03a0:  8fa6 6176 cd27 12d0 b743 ceb3 40ca 11e5  ..av.'...C..@...
	0x03b0:  590c 3471 449f 3f93 bc91 8ab5 df2b b7e8  Y.4qD.?......+..
	0x03c0:  094c 41f2 e521 e128 83e4 53c6 26de 65cc  .LA..!.(..S.&.e.
	0x03d0:  4858 5b65 067d 69dd 08b3 130f fd0a d800  HX[e.}i.........
	0x03e0:  7e17 962b fb5a df32 b6f1 90ec efd2 11c2  ~..+.Z.2........
	0x03f0:  2a0e 3a44 cd89 0d8f 6b34 c5b5 a1e7 d827  *.:D....k4.....'
	0x0400:  244f 81d0 0d92 bbfd 2fb1 72df 39f8 60d0  $O....../.r.9.`.
	0x0410:  79b8 712f 3bba 7b3c 3ae3 352d f413 b8a2  y.q/;.{<:.5-....
	0x0420:  6c8c 2db7 4df8 6582 570c 0036 5758 5b21  l.-.M.e.W..6WX[!
	0x0430:  b746 326c 7015 3840 4100 0bc6 3c8f 289a  .F2lp.8@A...<.(.
	0x0440:  994d 45fc 2724 a5d8 c0a7 5995 4979 c298  .ME.'$....Y.Iy..
	0x0450:  d47d b848 dffd f1a4 70c0 ef1e 33c1 521e  .}.H....p...3.R.
	0x0460:  7890 a14f 99d4 53b6 9d12 19c7 0071 296b  x..O..S......q)k
	0x0470:  a4e3 8477 0620 7269 2145 1ebb b660 84a5  ...w..ri!E...`..
	0x0480:  c6d2 62db d976 db16 4c57 80aa 1938 5127  ..b..v..LW...8Q'
	0x0490:  95c1 82a1 32b0 640c 61c2 202c 9767 3b4a  ....2.d.a..,.g;J
	0x04a0:  db62 8655 4541 1fd8 039c 1740 41d0 3454  .b.UEA.....@A.4T
	0x04b0:  2910 2ebf 4d85 c03f 1a38 5d84 f841 861d  )...M..?.8]..A..
	0x04c0:  5bf6 a75b 5eb3 e9fa a755 7a24 db28 15eb  [..[^....Uz$.(..
	0x04d0:  aed3 ee41 2794 8278 92fe 081a 484d 6953  ...A'..x....HMiS
	0x04e0:  8293 aaca 12b2 a42e 44ca 5f70 1e29 1550  ........D._p.).P
	0x04f0:  56d3 3f11 fcc9 8b8a b3e4 9e58 3776 b26b  V.?........X7v.k
	0x0500:  6747 7749 25ff e8a6 6510 516f 1b2e 7532  gGwI%...e.Qo..u2
	0x0510:  08e8 b6d4 ca61 f2f5 603e 2339 29ed e74b  .....a..`>#9)..K
	0x0520:  81ba 8718 b30c 3583 18e7 8c35 0348 1e80  ......5....5.H..
	0x0530:  5ccf 9164 835c 6384 0880 3301 928c e6d2  \..d.\c...3.....
	0x0540:  aa81 e410 7453 5004 2c9b 0114 8106 f4ac  ....tSP.,.......
	0x0550:  bf1d 7529 8036 7458 3b88 700a 60a7 6c59  ..u).6tX;.p.`.lY
	0x0560:  c51b c6e0 3a7b 8a17 9311 27a3 23ad c5f8  ....:{....'.#...
	0x0570:  563a 327d 2b2f bade 3f47 5361 584e 0afa  V:2}+/..?GSaXN..
	0x0580:  8269 8219 6300 0cf8 33ec 16e0 cf1a 9c4e  .i..c...3......N
	0x0590:  e645 74f6 628d 786e 8489 345a ff6e aebf  .Et.b.xn..4Z.n..
	0x05a0:  76ab ba36 53bd 3453 5d9b aeae ccf1 f769  v..6S.4S]......i
	0x05b0:  fe7e 9eaf 9792 a7b8 bfa2 7534 5ea3 1190  .~........u4^...
	0x05c0:  dd07 681f 5350 e49c 8cd0 d154 fdbc d9ac  ..h.SP.....T....
	0x05d0:  7cbf c2d7 15be a223 6856 3ab2 c6df e5fe  |......#hV:.....
	0x05e0:  9c8d                                     ..
22:38:02.882329 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [P.], seq 5058:9019, ack 1774, win 255, options [nop,nop,TS val 170996390 ecr 4143682], length 3961: HTTP
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0fad 8bba 4000 3806 1ea7 adf9 1a37 c0a8  ....@.8......7..
	0x0020:  0011 0050 c802 4b4b b8f1 f896 6cd8 8018  ...P..KK....l...
	0x0030:  00ff 9889 0000 0101 080a 0a31 32a6 003f  ...........12..?
	0x0040:  3a42 0ed8 49ff f443 5420 c565 0cb8 ce72  :B..I..CT..e...r
	0x0050:  99d5 646c baa4 9459 3145 3e44 e12f 30a0  ..dl...Y1E>D./0.
	0x0060:  b721 8261 4b51 2a2d db8d 34d2 32db 51bb  .!.aKQ*-..4.2.Q.
	0x0070:  45c4 55ca 27f2 b95b cbd2 1521 a449 4e8c  E.U.'..[...!.IN.
	0x0080:  42c8 2c5d 1102 f388 92d7 f40b f3c6 e0d7  B.,]............
	0x0090:  6546 ccfe 52ec 0881 3a28 e6d0 83dd cb59  eF..R...:(.....Y
	0x00a0:  b590 e64a a524 2600 56c3 ef15 632a f454  ...J.$&.V...c*.T
	0x00b0:  7972 035d 9e17 5a49 d7d6 85b8 9a70 c220  yr.]..ZI.....p..
	0x00c0:  7a2e a43b 3253 f25d e645 be5f 281d e3d5  z..;2S.].E._(...
	0x00d0:  0da9 5728 f282 4123 613c e180 6973 985e  ..W(..A#a<..is.^
	0x00e0:  d76e 113a 47c9 d776 3b40 da71 10aa b1fe  .n.:G..v;@.q....
	0x00f0:  12c2 00da 9224 0347 7738 bc41 f28d 4222  .....$.Gw8.A..B"
	0x0100:  12de b8ba 6161 f408 5ef0 cc66 d55b 6eca  ....aa..^..f.[n.
	0x0110:  e631 1c3d 658a de03 6b62 593a 28a3 3039  .1.=e...kbY:(.09
	0x0120:  152f 989c 2ab4 c851 ed92 bc26 7580 6078  ./..*..Q...&u.`x
	0x0130:  2c85 2e1a 0453 9cc9 f789 2934 554c 0a67  ,....S....)4UL.g
	0x0140:  1841 6589 c3d4 a51d 03fb 3607 9edf 7413  .Ae.......6...t.
	0x0150:  2a49 a234 41ed 6f91 7021 1303 34e2 54f1  *I.4A.o.p!..4.T.
	0x0160:  4476 e2fe 6308 d7f7 40b6 8707 ef73 8427  Dv..c...@....s.'
	0x0170:  45db 4bf9 c59c 7e2d 2568 7c26 7564 808a  E.K...~-%h|&ud..
	0x0180:  a90c ee90 17d2 019a eb56 3388 5e20 787a  .........V3.^.xz
	0x0190:  c164 8a66 4f32 d05d 9b8d fc1d d2c9 7abc  .d.fO2.]......z.
	0x01a0:  49fc 504c e477 991f 92b0 551a c92b b304  I.PL.w....U..+..
	0x01b0:  afb7 82ab 593b be15 7891 701c 3f2b 7b91  ....Y;..x.p.?+{.
	0x01c0:  0657 c043 b2aa 6424 c255 176d 4a01 7a9d  .W.C..d$.U.mJ.z.
	0x01d0:  a322 a9c5 4903 418e c91d bb0b 3c43 d242  ."..I.A.....<C.B
	0x01e0:  149b ab4c 778e 477e 6e25 ef0e ed86 c814  ...Lw.G~n%......
	0x01f0:  59bd 4269 91a1 a63c 9599 c9b0 b2f4 2f33  Y.Bi...<....../3
	0x0200:  9746 bf4b 39d3 5411 d28e ccf7 6a46 5cb1  .F.K9.T.....jF\.
	0x0210:  9d64 bbfe aee7 bb76 d425 c814 6eb0 171b  .d.....v.%..n...
	0x0220:  0bfa d79c c7cf b145 ccdc 5b3c 81e9 8e80  .......E..[<....
	0x0230:  8433 49dd 9052 54b1 01c6 a5ca 0103 65ac  .3I..RT.......e.
	0x0240:  a6b0 c168 9d78 2508 7b1d a83a c135 2d4b  ...h.x%.{..:.5-K
	0x0250:  e171 ff45 7d22 f040 2c48 e3a9 5179 e296  .q.E}".@,H..Qy..
	0x0260:  264f 8d62 e2a7 a6af 993a 0316 becd cd66  &O.b.....:.....f
	0x0270:  4916 d850 f2bd 8e61 732e 912f d037 ba92  I..P...as../.7..
	0x0280:  e8a0 b27a 99ea eb42 f5d7 b03b a3e3 bdc9  ...z...B...;....
	0x0290:  eef6 8886 5e6c d421 648a b664 40cc 0e6e  ....^l.!d..d@..n
	0x02a0:  c948 b971 8c7e 6496 5784 91e7 0689 b667  .H.q.~d.W......g
	0x02b0:  f36d b32e a688 6032 f914 6ca7 b403 6616  .m....`2..l...f.
	0x02c0:  090e 223a 3daa 1f6b 1efc 7568 102f ebab  ..":=..k..uh./..
	0x02d0:  1777 e205 ea04 4b0c 3862 b2af 06d1 ffc1  .w....K.8b......
	0x02e0:  e18f 6e76 33a0 8441 fb55 f83a 6e4c 9926  ..nv3..A.U.:nL.&
	0x02f0:  c6c2 2f6e 7b8e 3db3 27b4 e125 4130 05c6  ../n{.=.'..%A0..
	0x0300:  22ff fe53 baa9 875a c46a 866e 9346 11b4  "..S...Z.j.n.F..
	0x0310:  6a64 fcf7 e266 2165 afbb db16 0ffa 73be  jd...f!e......s.
	0x0320:  7ecc ba02 431f 45da 15b4 70c7 7ed9 89c9  ~...C.E...p.~...
	0x0330:  361b 3d40 a4bd f67f c7b6 2ee9 6fb2 ebd5  6.=@........o...
	0x0340:  5e26 a869 b6a3 33e6 4a31 57ad 0064 0363  ^&.i..3.J1W..d.c
	0x0350:  8f41 ce4b dc1a 3c6a c6c9 bea6 8904 f3e0  .A.K..<j........
	0x0360:  9395 22a5 6b50 52c4 27a3 c608 dab0 d9b5  ..".kPR.'.......
	0x0370:  e646 deae 0f4d dbb4 5f42 1a55 0b59 5ea3  .F...M.._B.U.Y^.
	0x0380:  473c 5fe1 c54b 483e cbf2 afc6 68cd 5e6e  G<_..KH>....h.^n
	0x0390:  76b0 510e 9982 632e da99 19c5 b443 f646  v.Q...c......C.F
	0x03a0:  15b6 2bce be21 d424 aaaa 6fa4 7133 7d8f  ..+..!.$..o.q3}.
	0x03b0:  833d c747 01da ee4e cc68 6736 4f2e 6999  .=.G...N.hg6O.i.
	0x03c0:  2570 2646 aa02 250a f68d 91b2 9484 4c7e  %p&F..%.......L~
	0x03d0:  7d0c 8c57 2f99 d8de 6b39 31a7 b0b4 dc70  }..W/...k91....p
	0x03e0:  62a0 d775 54fa 0a55 fa32 2ae5 64a0 a786  b..uT..U.2*.d...
	0x03f0:  f897 208a 0fd9 a393 fc9e d450 82f7 0db7  ...........P....
	0x0400:  5a34 b292 c2e4 efb1 93f4 01a7 6f60 431e  Z4..........o`C.
	0x0410:  a54d 11c6 c011 7df3 6ddc b871 3b8b 34dc  .M....}.m..q;.4.
	0x0420:  6637 45aa 00ec 482f 7c40 0902 295b 26be  f7E...H/|@..)[&.
	0x0430:  54cc 8988 a1b7 dd93 50d9 1080 ee30 5be3  T.......P....0[.
	0x0440:  2815 4f57 5a9c 5825 e927 84b3 8e20 468a  (.OWZ.X%.'....F.
	0x0450:  b91e 7c88 b43d c159 28a7 2cb7 2513 63fe  ..|..=.Y(.,.%.c.
	0x0460:  4849 9f4f 0ba2 4e45 6387 701b 238e 76f8  HI.O..NEc.p.#.v.
	0x0470:  9d81 49be 1405 edea 69e6 d252 ff5f d254  ..I.....i..R._.T
	0x0480:  1bf2 e713 cb22 9d8d 4812 dfc9 549d d864  ....."..H...T..d
	0x0490:  18c9 f4b4 e742 7685 1228 69cc 8099 e7a6  .....Bv..(i.....
	0x04a0:  ac40 93c7 ac1b 3fce 72d8 8f05 d604 33ff  .@....?.r.....3.
	0x04b0:  2cc7 8dc6 b018 0a52 4e7b 0cab 9bb6 bd8d  ,......RN{......
	0x04c0:  0c5b 3eb5 252b 196e d449 ca3f a76d 4d15  .[>.%+.n.I.?.mM.
	0x04d0:  d9cd 6bee 6855 c4fb 4845 3f79 abec a720  ..k.hU..HE?y....
	0x04e0:  1e3e 8818 b447 98a1 3266 d281 dc46 0ad4  .>...G..2f...F..
	0x04f0:  75b3 8424 4461 446d 870c da8d b6be d98f  u..$DaDm........
	0x0500:  12af 4983 4084 7d24 7e54 0a02 01b8 d2ee  ..I.@.}$~T......
	0x0510:  b4e9 d988 f721 5528 2f27 716c c8bd 4903  .....!U(/'ql..I.
	0x0520:  4dbf 4ca2 6662 5a89 2df9 0876 2444 1d16  M.L.fbZ.-..v$D..
	0x0530:  36ac c9c3 c69d 1227 503b 7b43 9c29 ed8f  6......'P;{C.)..
	0x0540:  5d11 8759 832a da5d cbb9 71e4 3b1a 6e9c  ]..Y.*.]..q.;.n.
	0x0550:  c02c d2c0 9542 d938 9f64 28a6 f98b b261  .,...B.8.d(....a
	0x0560:  58b6 1023 4d52 0735 90d1 c8db 8659 2f21  X..#MR.5.....Y/!
	0x0570:  8421 8f25 3752 b228 75b4 43ee 4bfc 43ed  .!.%7R.(u.C.K.C.
	0x0580:  3646 6a9c 7e41 e21f f258 f224 578d ef66  6Fj.~A...X.$W..f
	0x0590:  5ea5 6c61 562d 1fc9 d930 d770 0abc 6968  ^.laV-...0.p..ih
	0x05a0:  4660 a68c 1baa 3371 8f48 1bb5 135b 2824  F`....3q.H...[($
	0x05b0:  9120 d4cf d206 76e5 286c 601c b630 404e  ......v.(l`..0@N
	0x05c0:  03fd 29f5 b107 81cc e30e 71dc e9c7 2c43  ..).......q...,C
	0x05d0:  eb52 e2ac 6446 0a8f 687e d14c 202c 0726  .R..dF..h~.L.,.&
	0x05e0:  a017 c6f0 ebca 8828 fb09 26c5 e849 6df2  .......(..&..Im.
	0x05f0:  39bc 4d5e 9f84 ed08 b4a1 5142 1134 2299  9.M^......QB.4".
	0x0600:  64f5 0aa4 29ab 5456 eff2 4087 a545 5e32  d...).TV..@..E^2
	0x0610:  8ad4 a090 5e88 422d 593e b2d2 90af ac33  ....^.B-Y>.....3
	0x0620:  6554 e271 6549 6dae d031 1584 7400 73be  eT.qeIm..1..t.s.
	0x0630:  475e ea30 265c 9641 081c 85ce 6aac 06a0  G^.0&\.A....j...
	0x0640:  2421 8d93 a22e c743 6591 488a b599 740d  $!.....Ce.H...t.
	0x0650:  a944 ec02 56f8 130c 473a c602 c9f7 65bd  .D..V...G:....e.
	0x0660:  fe51 d0db ea6d 0f4e bbbe afbe 1c67 d432  .Q...m.N.....g.2
	0x0670:  bf82 cbca 3c0a 7426 c412 2962 6291 c5d2  ....<.t&..)bb...
	0x0680:  f670 e3b5 faff 8629 fb9a e506 85ef 39d5  .p.....)......9.
	0x0690:  be14 6b15 ec4d 074b 740f 452c 983d 1445  ..k..M.Kt.E,.=.E
	0x06a0:  a854 8a1e 8084 4272 8a45 8694 41db 8f2d  .T....Br.E..A..-
	0x06b0:  3bc0 b85a 14e8 85af c582 08cc cc41 15a2  ;..Z.........A..
	0x06c0:  3ab4 3c95 5cfd 9c02 512f 9031 422e 8a3a  :.<.\...Q/.1B..:
	0x06d0:  ed43 725d 8880 b419 4376 358c 22a2 e6f7  .Cr]....Cv5."...
	0x06e0:  190d 52e7 307f 2193 19b8 115e 30c1 5479  ..R.0.!....^0.Ty
	0x06f0:  6ac6 0872 3c42 cd4c 7229 cd8b 3c50 a77d  j..r<B.Lr)..<P.}
	0x0700:  d809 c9b4 d010 4121 8433 9314 44f3 6afd  ......A!.3..D.j.
	0x0710:  9b2b af55 b89e 13b5 1142 acbe fec7 4926  .+.U.....B....I&
	0x0720:  42e9 292b 8720 f7f9 eac4 192d a5c8 2dae  B.)+.......-..-.
	0x0730:  5d75 1adf 0fd1 af81 e986 f0ce 3180 2c3b  ]u..........1.,;
	0x0740:  33c2 a3c2 4027 3ac5 b9a9 84e1 94bb 23fa  3...@':.......#.
	0x0750:  568c b84c 364a 4209 7b38 8c37 683c cd9b  V..L6JB.{8.7h<..
	0x0760:  e8bd 5a21 a224 4497 69eb 13df 119d 24a9  ..Z!.$D.i.....$.
	0x0770:  78a2 24d0 7a43 f852 db8e f83e 2f92 440f  x.$.zC.R...>/.D.
	0x0780:  9531 518a 9b23 5968 e8ec cb64 9ac1 3471  .1Q..#Yh...d..4q
	0x0790:  1480 1016 a4ff 1cd1 4a9c d75e b9d6 e262  ........J..^...b
	0x07a0:  7213 0ef9 8b41 b03a 3b15 7408 d8a4 7a23  r....A.:;.t...z#
	0x07b0:  75d1 b58c 2a3f 9c5c 635c 152e 4327 a050  u...*?.\c\..C'.P
	0x07c0:  cd62 c541 c0ea 80a8 e643 53b9 e50d 63b3  .b.A.....CS...c.
	0x07d0:  9019 501f 0c48 ab19 3e81 7916 074b c4af  ..P..H..>.y..K..
	0x07e0:  8859 717f c4da 35d7 a669 e341 9fe5 8d67  .Yq...5..i.A...g
	0x07f0:  2de0 f140 c4bc 283d a95a ec6c 2de5 459f  -..@..(=.Z.l-.E.
	0x0800:  2a76 5266 0436 e301 8de3 28af 242e f01f  *vRf.6....(.$...
	0x0810:  ef32 d2ac 8223 e529 7ee5 f6cf 5126 c6cc  .2...#.)~...Q&..
	0x0820:  e950 4924 9362 6736 9a27 4674 59a5 3233  .PI$.bg6.'FtY.23
	0x0830:  ca61 c5fa 2c25 28a1 a3b0 33c6 88bc 4aae  .a..,%(...3...J.
	0x0840:  8a88 4e13 8110 23c2 c42a 9493 7002 9698  ..N...#..*..p...
	0x0850:  7088 b09a 58df a6bf 2fcc 2aee bbe9 ab2b  p...X.../.*....+
	0x0860:  c400 6420 2cfd 1f18 09a1 3089 8a7f 8d21  ..d.,.....0....!
	0x0870:  5ac5 1412 2dba 2256 9610 c2b4 9174 320f  Z...-."V.....t2.
	0x0880:  2501 4c94 3964 4ec5 0812 9db9 2226 a6d0  %.L.9dN....."&..
	0x0890:  c0b4 40f5 32a4 35c7 8299 825e 882b aafd  ..@.2.5....^.+..
	0x08a0:  bf04 350e 752b 98d1 9759 ba48 22d3 3c42  ..5.u+...Y.H".<B
	0x08b0:  8693 d322 8235 2cb3 e610 8d42 f503 6bf8  ...".5,....B..k.
	0x08c0:  03ba faab 5158 c35f 855d 6b26 cb4e de88  ....QX._.]k&.N..
	0x08d0:  1d71 46e0 4429 6866 7848 3297 7210 ca32  .qF.D)hfxH2.r..2
	0x08e0:  dc04 4830 537f 32f9 6093 6424 8219 0ee5  ..H0S.2.`.d$....
	0x08f0:  2b98 ba87 d01d ad7c 4c89 29df c573 1319  +......|L.)..s..
	0x0900:  2a06 9aa9 be52 8722 3f17 a497 6833 3d02  *....R."?...h3=.
	0x0910:  cc92 7447 f8b4 0a02 8fe1 cb2b f922 108b  ..tG.......+."..
	0x0920:  28f6 13f5 e826 8db1 2ab0 4049 28a6 9b88  (....&..*.@I(...
	0x0930:  de4b da21 3ed4 8c09 ec26 d22d 07d0 6a5b  .K.!>....&.-..j[
	0x0940:  2245 5aff 4472 8e83 6f2a d7bc c4c3 1b8e  "EZ.Dr..o*......
	0x0950:  4a28 30a9 782a 723e 94f0 b999 4f28 9681  J(0.x*r>....O(..
	0x0960:  9abb 4972 fb50 d20e 7a55 da72 33ed 0035  ..Ir.P..zU.r3..5
	0x0970:  170c 5125 a412 6f8a d315 2821 62b8 1dc0  ..Q%..o...(!b...
	0x0980:  46e8 bc5c 270b ce9b 871b 4837 65c1 09aa  F..\'.....H7e...
	0x0990:  669e 52b0 2e40 410e e637 57a8 a9fc 47b2  f.R..@A..7W...G.
	0x09a0:  4f81 5038 ac5c 1993 4ba9 8b20 fd6f f0ef  O.P8.\..K....o..
	0x09b0:  6f47 2b60 e221 cd6d 624f 492a a709 ccea  oG+`.!.mbOI*....
	0x09c0:  e435 8266 24ad 52c0 b102 ee9d 2833 eac8  .5.f$.R.....(3..
	0x09d0:  89a6 afc8 4433 4ca2 176c de2b 10e1 5a20  ....D3L..l.+..Z.
	0x09e0:  24d8 0cf8 8aa3 5494 8d85 5c19 b1f9 3f4c  $.....T...\...?L
	0x09f0:  b875 14d9 7218 b6e0 d664 ae0d aedb 31d1  .u..r....d....1.
	0x0a00:  90c9 3ad0 a6f5 6a82 5f26 c635 0e37 15b8  ..:...j._&.5.7..
	0x0a10:  5a72 9c87 884a 593a 82b0 939d 7864 d085  Zr...JY:....xd..
	0x0a20:  1c7b cabd 4672 162c c802 e065 a8b8 5816  .{..Fr.,...e..X.
	0x0a30:  b615 0b79 10a1 50d6 7299 8213 e757 5681  ...y..P.r....WV.
	0x0a40:  99b4 3f12 a69c b852 9359 13d2 0e42 206a  ..?....R.Y...B.j
	0x0a50:  2eca 14dc a018 1b67 8253 a5f6 df9c ad46  .......g.S.....F
	0x0a60:  be2e 1ce0 cc26 aaec e1d0 e54a edfb 38b8  .....&.....J..8.
	0x0a70:  514e 379b 9408 306b 4cbf 972d ce8d fdb8  QN7...0kL..-....
	0x0a80:  95cd cc3c 0e1e 9fd4 269f a56d bebc 31a9  ...<....&..m..1.
	0x0a90:  c16e 5055 b894 36e5 86d8 9c3b 19ff 6883  .nPU..6....;..h.
	0x0aa0:  eba2 eb50 2b5e 5c6d d9ba 3018 3d31 579a  ...P+^\m..0.=1W.
	0x0ab0:  8aeb 4daa 7fec ad89 7b2d f246 5bce dade  ..M.....{-.F[...
	0x0ac0:  3017 8842 8720 44fe 1919 2b12 e320 5e06  0..B..D...+...^.
	0x0ad0:  9c53 3abe 6beb 5b36 9f93 8833 e233 a9e4  .S:.k.[6...3.3..
	0x0ae0:  c761 9a2a 6abd 65d4 4a7f 5bfa efd2 997d  .a.*j.e.J.[....}
	0x0af0:  6df3 ea0f 2745 ba0d a98c 3fca 1aa4 b534  m...'E....?....4
	0x0b00:  a9f6 a42e ba96 b5b6 5a3d bf82 ff26 d5e0  ........Z=...&..
	0x0b10:  eaa9 f32b f8af b2b4 fafc f387 7575 cc6d  ...+........uu.m
	0x0b20:  4213 d5b8 4556 f389 bb22 dc80 4aa9 200d  B...EV..."..J...
	0x0b30:  aa8c 6dda b354 aa2f 97bf bf3c 3156 93ba  ..m..T./...<1V..
	0x0b40:  e85a 360f 6bd8 18dc a233 3006 b706 1f21  .Z6.k....30....!
	0x0b50:  3690 d426 9f65 6dbe 716d 728b 49ea a26b  6..&.em.qmr.I..k
	0x0b60:  e9da c559 c574 68c2 6446 684c a819 fe95  ...Y.th.dFhL....
	0x0b70:  ef08 da68 7928 469d ca73 10cb abcc da55  ...hy(F..s.....U
	0x0b80:  e6f1 c973 e386 2285 7c8e 1dc5 7861 70c3  ...s..".|...xap.
	0x0b90:  93b9 59ce c43d cd98 7106 b650 b178 31c0  ..Y..=..q..P.x1.
	0x0ba0:  2506 cd9e 09e1 8a64 d60d 9b1f 9526 3248  %......d.....&2H
	0x0bb0:  1fb1 8d04 9531 0d6a 8588 ea34 afdc a498  .....1.j...4....
	0x0bc0:  18a9 8925 6400 0a15 93cf 1d8a 36c3 4025  ...%d.......6.@%
	0x0bd0:  b995 0a48 ff54 1d54 c09b 3408 f3e1 a306  ...H.T.T..4.....
	0x0be0:  54c2 3072 640f 7e71 707f 28a1 c585 56e8  T.0rd.~qp.(...V.
	0x0bf0:  aa5d 5d3d 5f5d e6e0 ddbc b9a9 53be 0fe6  .]]=_]......S...
	0x0c00:  fa09 e957 e8ad 9512 f1cd 034c d0d5 5ba7  ...W.......L..[.
	0x0c10:  56cf 9f5a e668 cbbc 20e4 2613 0f3a d242  V..Z.h....&..:.B
	0x0c20:  a915 7a8b ea87 bf0a 6016 1bf6 719c 2769  ..z.....`...q.'i
	0x0c30:  7049 23c4 e614 3a76 6ac8 66d1 1149 3955  pI#...:vj.f..I9U
	0x0c40:  1eaf b6ec 35a0 ae76 d515 a745 8f48 bea9  ....5..v...E.H..
	0x0c50:  f218 4de4 dfcc d059 cfe6 e654 1159 ff82  ..M....Y...T.Y..
	0x0c60:  1375 9e4c 28f8 a173 1735 4c2a 0b40 2d03  .u.L(..s.5L*.@-.
	0x0c70:  9dc3 a2cd b621 f96f e438 152f 0f7d 5283  .....!.o.8./.}R.
	0x0c80:  c639 cc48 dd60 f043 af94 31b1 904c f6e3  .9.H.`.C..1..L..
	0x0c90:  f8f1 169d f7a8 b13a 594c f9bc 186d 350e  .......:YL...m5.
	0x0ca0:  c9a9 2377 6b20 5843 9b86 e8e8 a3e4 3498  ..#wk.XC......4.
	0x0cb0:  74d7 d4f0 0c19 dab5 2ce8 8984 fc35 f545  t.......,....5.E
	0x0cc0:  6cd1 c6ce 21b8 8992 6d4f 0786 cde4 659a  l...!...mO....e.
	0x0cd0:  39ab 32e3 cb7f 191a 4665 8aea bd05 095c  9.2.....Fe.....\
	0x0ce0:  03b1 7864 2456 3201 b1b7 ac3b 9893 af52  ..xd$V2....;...R
	0x0cf0:  0de5 994a 19a4 3f0e 9b1f a3f6 6533 17a8  ...J..?.....e3..
	0x0d00:  6de9 c52b 2e9f a7a4 5958 96a2 1800 a41b  m..+....YX......
	0x0d10:  38bf c8a6 3dd9 b4d9 6b94 0f27 191b 128b  8...=...k..'....
	0x0d20:  ce89 3fdd b51c 4c55 9299 9248 6c15 a417  ..?...LU...Hl...
	0x0d30:  f047 cb79 1d3c cce1 406b b7ce 1898 86ac  .G.y.<..@k......
	0x0d40:  74d3 7d93 3bb9 70bf 86f4 a7cf 925f c7c7  t.}.;.p......_..
	0x0d50:  9091 0cfd 9877 9d41 1b1e 09a3 332d 0bb5  .....w.A....3-..
	0x0d60:  a957 569c 991a 2ec9 397a e76f 1a89 159c  .WV.....9z.o....
	0x0d70:  699c f0b4 29a1 8b1d 0d5a 7285 409a b200  i...)....Zr.@...
	0x0d80:  0c03 6f5a 6c13 33f9 5b12 7864 a54a d2a0  ..oZl.3.[.xd.J..
	0x0d90:  b24a 8e26 474d fc8d 8f65 a62d 7ef4 8b61  .J.&GM...e.-~..a
	0x0da0:  3853 167b 4568 b368 269e 4d22 7238 2437  8S.{Eh.h&.M"r8$7
	0x0db0:  5a16 0a56 67f2 9dd8 6e7a 32cc 5c61 251d  Z..Vg...nz2.\a%.
	0x0dc0:  87ed 6112 955d 2cbc 84e1 4cb6 c477 c929  ..a..],...L..w.)
	0x0dd0:  d251 b7bc d6ca 491b fc70 1cd8 0e1b 983f  .Q....I..p.....?
	0x0de0:  e72c 9151 c741 986b 5ef1 d631 a2f9 b9b0  .,.Q.A.k^..1....
	0x0df0:  3ca9 ad43 85e5 8d63 b907 c2f2 a5e7 14a9  <..C...c........
	0x0e00:  9352 9243 2883 1d2b 6eb9 16ed 37b4 cee0  .R.C(..+n...7...
	0x0e10:  3cfa a6bb e3f4 f0d3 534e 8c7b 4e14 9fc5  <.......SN.{N...
	0x0e20:  3195 745a 63d1 c9e2 c547 54a6 2714 e933  1.tZc....GT.'..3
	0x0e30:  5b33 e716 edd8 dd60 0fdb fd9a dbfb f4bb  [3.....`........
	0x0e40:  7a86 8fc5 e906 c5a7 8de4 cf55 81e1 8813  z..........U....
	0x0e50:  3553 f70c af16 fc52 5ee1 b66c dae5 ca93  5S.....R^..l....
	0x0e60:  8e93 8068 efba ece4 a57d d4b2 c756 e5cb  ...h.....}...V..
	0x0e70:  26c7 1661 83ba 1c8a 6fb7 b1e5 544e 954c  &..a....o...TN.L
	0x0e80:  3749 61f7 d15d a781 c326 739e 6272 22dd  7Ia..]...&s.br".
	0x0e90:  2ddb cc69 17bd 3bfe ee11 b5b3 ea88 bb47  -..i..;........G
	0x0ea0:  8497 2476 7ae8 68f7 9830 3369 89c1 fd31  ..$vz.h..03i...1
	0x0eb0:  929a a5e5 98f6 b454 228d 74cc cc58 3233  .......T".t..X23
	0x0ec0:  7244 d6e5 0e24 c732 362d c441 8da5 0371  rD...$.26-.A...q
	0x0ed0:  39bf 0dbf 7579 c2bf 5cb8 c09c 87a3 b7d3  9...uy..\.......
	0x0ee0:  fdf0 74e4 1225 0a89 7ff0 8db9 613d 395f  ..t..%......a=9_
	0x0ef0:  4431 ec61 5fcb aa47 bd57 cfd9 0ee8 7702  D1.a_..G.W....w.
	0x0f00:  fee6 9950 16d8 a0ce 30bd f724 fde2 e4f9  ...P....0..$....
	0x0f10:  023f d4c9 1b36 d5ef 0ab0 2f9c b973 823f  .?...6..../..s.?
	0x0f20:  6661 7ad6 9a4d 9a5e 8433 bcbc 0e1d a4fd  faz..M.^.3......
	0x0f30:  ffbc 3298 242e a683 ceed 212b 2cf3 8761  ..2.$.....!+,..a
	0x0f40:  bde9 c488 42f0 ce4c f779 9a92 e937 a2dc  ....B..L.y...7..
	0x0f50:  7044 0e6f c0ce ffc0 00e7 16e9 238f 883f  pD.o........#..?
	0x0f60:  0f53 3e23 8b72 f646 72fe 7cee c7d7 067f  .S>#.r.Fr.|.....
	0x0f70:  7bcd 3844 35ec f9af f9ed c069 be8c 2310  {.8D5......i..#.
	0x0f80:  cf5a 993f 719c 6a7a 9a2a 1faa cdbf 6546  .Z.?q.jz.*....eF
	0x0f90:  27d3 5bd3 d5d9 d90b f849 1dfc aa10 9fb3  '.[......I......
	0x0fa0:  8d53 b76b f4eb 3274 aa21 7efb 7869 eaff  .S.k..2t.!~.xi..
	0x0fb0:  007d 07be 0468 7a00 000d 0a              .}...hz....
22:38:02.897484 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [P.], seq 9019:9024, ack 1774, win 255, options [nop,nop,TS val 170996414 ecr 4143682], length 5: HTTP
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0039 8bbd 4000 3806 2e18 adf9 1a37 c0a8  .9..@.8......7..
	0x0020:  0011 0050 c802 4b4b c86a f896 6cd8 8018  ...P..KK.j..l...
	0x0030:  00ff efc4 0000 0101 080a 0a31 32be 003f  ...........12..?
	0x0040:  3a42 300d 0a0d 0a                        :B0....
22:38:03.199259 IP 46.4.114.109.http > 192.168.0.17.56204: Flags [S.], seq 1078162829, ack 1354319993, win 65160, options [mss 1452,sackOK,TS val 3174548701 ecr 4144463,nop,wscale 7], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  003c 0000 4000 3706 e291 2e04 726d c0a8  .<..@.7.....rm..
	0x0020:  0011 0050 db8c 4043 758d 50b9 4879 a012  ...P..@Cu.P.Hy..
	0x0030:  fe88 fdc0 0000 0204 05ac 0402 080a bd37  ...............7
	0x0040:  c4dd 003f 3d4f 0103 0307                 ...?=O....
22:38:03.200049 IP 46.4.114.109.http > 192.168.0.17.56202: Flags [S.], seq 1084873565, ack 3300599812, win 65160, options [mss 1452,sackOK,TS val 3174548704 ecr 4144463,nop,wscale 7], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  003c 0000 4000 3706 e291 2e04 726d c0a8  .<..@.7.....rm..
	0x0020:  0011 0050 db8a 40a9 db5d c4bb 2804 a012  ...P..@..]..(...
	0x0030:  fe88 43fc 0000 0204 05ac 0402 080a bd37  ..C............7
	0x0040:  c4e0 003f 3d4f 0103 0307                 ...?=O....
22:38:03.241762 IP 88.212.201.216.http > 192.168.0.17.43482: Flags [S.], seq 448420288, ack 2347697250, win 65535, options [mss 1452,nop,wscale 4,sackOK,TS val 3092166405 ecr 4144579], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  003c 0000 4000 3806 5f56 58d4 c9d8 c0a8  .<..@.8._VX.....
	0x0020:  0011 0050 a9da 1aba 59c0 8bef 0462 a012  ...P....Y....b..
	0x0030:  ffff 0848 0000 0204 05ac 0103 0304 0402  ...H............
	0x0040:  080a b84e b705 003f 3dc3                 ...N...?=.
22:38:03.305571 IP 46.4.114.109.http > 192.168.0.17.56204: Flags [.], ack 409, win 506, options [nop,nop,TS val 3174548773 ecr 4144558], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 058b 4000 3706 dd0e 2e04 726d c0a8  .4..@.7.....rm..
	0x0020:  0011 0050 db8c 4043 758e 50b9 4a11 8010  ...P..@Cu.P.J...
	0x0030:  01fa 26d5 0000 0101 080a bd37 c525 003f  ..&........7.%.?
	0x0040:  3dae                                     =.
22:38:03.308198 IP 46.4.114.109.http > 192.168.0.17.56204: Flags [P.], seq 1:346, ack 409, win 506, options [nop,nop,TS val 3174548774 ecr 4144558], length 345: HTTP: HTTP/1.1 302 Moved Temporarily
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  018d 058c 4000 3706 dbb4 2e04 726d c0a8  ....@.7.....rm..
	0x0020:  0011 0050 db8c 4043 758e 50b9 4a11 8018  ...P..@Cu.P.J...
	0x0030:  01fa 2133 0000 0101 080a bd37 c526 003f  ..!3.......7.&.?
	0x0040:  3dae 4854 5450 2f31 2e31 2033 3032 204d  =.HTTP/1.1.302.M
	0x0050:  6f76 6564 2054 656d 706f 7261 7269 6c79  oved.Temporarily
	0x0060:  0d0a 5365 7276 6572 3a20 6f70 656e 7265  ..Server:.openre
	0x0070:  7374 790d 0a44 6174 653a 2054 6875 2c20  sty..Date:.Thu,.
	0x0080:  3330 2044 6563 2032 3032 3120 3139 3a33  30.Dec.2021.19:3
	0x0090:  383a 3033 2047 4d54 0d0a 436f 6e74 656e  8:03.GMT..Conten
	0x00a0:  742d 5479 7065 3a20 7465 7874 2f68 746d  t-Type:.text/htm
	0x00b0:  6c0d 0a43 6f6e 7465 6e74 2d4c 656e 6774  l..Content-Lengt
	0x00c0:  683a 2031 3432 0d0a 436f 6e6e 6563 7469  h:.142..Connecti
	0x00d0:  6f6e 3a20 6b65 6570 2d61 6c69 7665 0d0a  on:.keep-alive..
	0x00e0:  4c6f 6361 7469 6f6e 3a20 6874 7470 733a  Location:.https:
	0x00f0:  2f2f 7777 772e 6163 696e 742e 6e65 742f  //www.acint.net/
	0x0100:  6d63 2f3f 6470 3d31 300d 0a0d 0a3c 6874  mc/?dp=10....<ht
	0x0110:  6d6c 3e0d 0a3c 6865 6164 3e3c 7469 746c  ml>..<head><titl
	0x0120:  653e 3330 3220 466f 756e 643c 2f74 6974  e>302.Found</tit
	0x0130:  6c65 3e3c 2f68 6561 643e 0d0a 3c62 6f64  le></head>..<bod
	0x0140:  793e 0d0a 3c63 656e 7465 723e 3c68 313e  y>..<center><h1>
	0x0150:  3330 3220 466f 756e 643c 2f68 313e 3c2f  302.Found</h1></
	0x0160:  6365 6e74 6572 3e0d 0a3c 6872 3e3c 6365  center>..<hr><ce
	0x0170:  6e74 6572 3e6f 7065 6e72 6573 7479 3c2f  nter>openresty</
	0x0180:  6365 6e74 6572 3e0d 0a3c 2f62 6f64 793e  center>..</body>
	0x0190:  0d0a 3c2f 6874 6d6c 3e0d 0a              ..</html>..
22:38:03.308526 IP 46.4.114.109.http > 192.168.0.17.56202: Flags [.], ack 991, win 502, options [nop,nop,TS val 3174548777 ecr 4144558], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 86f7 4000 3706 5ba2 2e04 726d c0a8  .4..@.7.[...rm..
	0x0020:  0011 0050 db8a 40a9 db5e c4bb 2be2 8010  ...P..@..^..+...
	0x0030:  01f6 6acd 0000 0101 080a bd37 c529 003f  ..j........7.).?
	0x0040:  3dae                                     =.
22:38:03.315158 IP 46.4.114.109.http > 192.168.0.17.56202: Flags [P.], seq 1:1018, ack 991, win 502, options [nop,nop,TS val 3174548777 ecr 4144558], length 1017: HTTP: HTTP/1.1 302 Moved Temporarily
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  042d 86f8 4000 3706 57a8 2e04 726d c0a8  .-..@.7.W...rm..
	0x0020:  0011 0050 db8a 40a9 db5e c4bb 2be2 8018  ...P..@..^..+...
	0x0030:  01f6 dc3e 0000 0101 080a bd37 c529 003f  ...>.......7.).?
	0x0040:  3dae 4854 5450 2f31 2e31 2033 3032 204d  =.HTTP/1.1.302.M
	0x0050:  6f76 6564 2054 656d 706f 7261 7269 6c79  oved.Temporarily
	0x0060:  0d0a 5365 7276 6572 3a20 6f70 656e 7265  ..Server:.openre
	0x0070:  7374 790d 0a44 6174 653a 2054 6875 2c20  sty..Date:.Thu,.
	0x0080:  3330 2044 6563 2032 3032 3120 3139 3a33  30.Dec.2021.19:3
	0x0090:  383a 3033 2047 4d54 0d0a 436f 6e74 656e  8:03.GMT..Conten
	0x00a0:  742d 5479 7065 3a20 7465 7874 2f68 746d  t-Type:.text/htm
	0x00b0:  6c0d 0a43 6f6e 7465 6e74 2d4c 656e 6774  l..Content-Lengt
	0x00c0:  683a 2031 3432 0d0a 436f 6e6e 6563 7469  h:.142..Connecti
	0x00d0:  6f6e 3a20 6b65 6570 2d61 6c69 7665 0d0a  on:.keep-alive..
	0x00e0:  4c6f 6361 7469 6f6e 3a20 6874 7470 733a  Location:.https:
	0x00f0:  2f2f 7777 772e 6163 696e 742e 6e65 742f  //www.acint.net/
	0x0100:  6869 742f 3f76 3d30 2e34 2e30 2675 6964  hit/?v=0.4.0&uid
	0x0110:  3d32 3661 3166 6138 322d 3961 6564 2d34  =26a1fa82-9aed-4
	0x0120:  3662 382d 6163 6463 2d38 3133 6533 6634  6b8-acdc-813e3f4
	0x0130:  3665 3734 6426 6470 3d31 3026 747a 3d25  6e74d&dp=10&tz=%
	0x0140:  3242 3033 2533 4130 3026 6e63 3d39 3636  2B03%3A00&nc=966
	0x0150:  3732 3132 3226 753d 6874 7470 2533 4125  72122&u=http%3A%
	0x0160:  3246 2532 4677 7777 2e73 6275 702e 636f  2F%2Fwww.sbup.co
	0x0170:  6d25 3246 7769 6b69 2532 4625 3235 4430  m%2Fwiki%2F%25D0
	0x0180:  2532 3539 4525 3235 4430 2532 3542 3125  %259E%25D0%25B1%
	0x0190:  3235 4431 2532 3538 3125 3235 4431 2532  25D1%2581%25D1%2
	0x01a0:  3538 3325 3235 4430 2532 3542 3625 3235  583%25D0%25B6%25
	0x01b0:  4430 2532 3542 3425 3235 4430 2532 3542  D0%25B4%25D0%25B
	0x01c0:  3525 3235 4430 2532 3542 4425 3235 4430  5%25D0%25BD%25D0
	0x01d0:  2532 3542 3825 3235 4430 2532 3542 355f  %25B8%25D0%25B5_
	0x01e0:  2532 3544 3125 3235 3833 2532 3544 3125  %25D1%2583%25D1%
	0x01f0:  3235 3837 2532 3544 3025 3235 4230 2532  2587%25D0%25B0%2
	0x0200:  3544 3125 3235 3831 2532 3544 3125 3235  5D1%2581%25D1%25
	0x0210:  3832 2532 3544 3025 3235 4244 2532 3544  82%25D0%25BD%25D
	0x0220:  3025 3235 4238 2532 3544 3025 3235 4241  0%25B8%25D0%25BA
	0x0230:  2532 3544 3025 3235 4230 2533 4157 696b  %25D0%25B0%3AWik
	0x0240:  6953 7973 6f70 2672 3d68 7474 7025 3341  iSysop&r=http%3A
	0x0250:  2532 4625 3246 7777 772e 7362 7570 2e63  %2F%2Fwww.sbup.c
	0x0260:  6f6d 2532 4677 696b 6925 3246 2532 3544  om%2Fwiki%2F%25D
	0x0270:  3025 3235 4133 2532 3544 3125 3235 3837  0%25A3%25D1%2587
	0x0280:  2532 3544 3025 3235 4230 2532 3544 3125  %25D0%25B0%25D1%
	0x0290:  3235 3831 2532 3544 3125 3235 3832 2532  2581%25D1%2582%2
	0x02a0:  3544 3025 3235 4244 2532 3544 3025 3235  5D0%25BD%25D0%25
	0x02b0:  4238 2532 3544 3025 3235 4241 2533 4157  B8%25D0%25BA%3AW
	0x02c0:  696b 6953 7973 6f70 2672 733d 3138 3436  ikiSysop&rs=1846
	0x02d0:  7839 3532 2674 3d25 4430 2539 4525 4430  x952&t=%D0%9E%D0
	0x02e0:  2542 3125 4431 2538 3125 4431 2538 3325  %B1%D1%81%D1%83%
	0x02f0:  4430 2542 3625 4430 2542 3425 4430 2542  D0%B6%D0%B4%D0%B
	0x0300:  3525 4430 2542 4425 4430 2542 3825 4430  5%D0%BD%D0%B8%D0
	0x0310:  2542 3525 3230 2544 3125 3833 2544 3125  %B5%20%D1%83%D1%
	0x0320:  3837 2544 3025 4230 2544 3125 3831 2544  87%D0%B0%D1%81%D
	0x0330:  3125 3832 2544 3025 4244 2544 3025 4238  1%82%D0%BD%D0%B8
	0x0340:  2544 3025 4241 2544 3025 4230 2533 4157  %D0%BA%D0%B0%3AW
	0x0350:  696b 6953 7973 6f70 266f 453d 3126 6f50  ikiSysop&oE=1&oP
	0x0360:  3d31 2664 543d 3230 3231 2d31 322d 3330  =1&dT=2021-12-30
	0x0370:  5432 3225 3341 3338 2533 4130 332e 3039  T22%3A38%3A03.09
	0x0380:  3726 6675 3d39 3561 3265 6265 372d 6332  7&fu=95a2ebe7-c2
	0x0390:  3762 2d34 6430 352d 6135 3038 2d32 6363  7b-4d05-a508-2cc
	0x03a0:  3438 3862 6435 6664 340d 0a0d 0a3c 6874  488bd5fd4....<ht
	0x03b0:  6d6c 3e0d 0a3c 6865 6164 3e3c 7469 746c  ml>..<head><titl
	0x03c0:  653e 3330 3220 466f 756e 643c 2f74 6974  e>302.Found</tit
	0x03d0:  6c65 3e3c 2f68 6561 643e 0d0a 3c62 6f64  le></head>..<bod
	0x03e0:  793e 0d0a 3c63 656e 7465 723e 3c68 313e  y>..<center><h1>
	0x03f0:  3330 3220 466f 756e 643c 2f68 313e 3c2f  302.Found</h1></
	0x0400:  6365 6e74 6572 3e0d 0a3c 6872 3e3c 6365  center>..<hr><ce
	0x0410:  6e74 6572 3e6f 7065 6e72 6573 7479 3c2f  nter>openresty</
	0x0420:  6365 6e74 6572 3e0d 0a3c 2f62 6f64 793e  center>..</body>
	0x0430:  0d0a 3c2f 6874 6d6c 3e0d 0a              ..</html>..
22:38:03.327858 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [.], ack 2501, win 269, options [nop,nop,TS val 170996843 ecr 4144613], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 8bbe 4000 3806 2e1c adf9 1a37 c0a8  .4..@.8......7..
	0x0020:  0011 0050 c802 4b4b c86f f896 6faf 8010  ...P..KK.o..o...
	0x0030:  010d 2bb2 0000 0101 080a 0a31 346b 003f  ..+........14k.?
	0x0040:  3de5                                     =.
22:38:03.331021 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [P.], seq 9024:10456, ack 2501, win 269, options [nop,nop,TS val 170996845 ecr 4144613], length 1432: HTTP: HTTP/1.1 200 OK
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  05cc 8bbf 4000 3806 2883 adf9 1a37 c0a8  ....@.8.(....7..
	0x0020:  0011 0050 c802 4b4b c86f f896 6faf 8018  ...P..KK.o..o...
	0x0030:  010d 713a 0000 0101 080a 0a31 346d 003f  ..q:.......14m.?
	0x0040:  3de5 4854 5450 2f31 2e31 2032 3030 204f  =.HTTP/1.1.200.O
	0x0050:  4b0d 0a44 6174 653a 2054 6875 2c20 3330  K..Date:.Thu,.30
	0x0060:  2044 6563 2032 3032 3120 3139 3a33 383a  .Dec.2021.19:38:
	0x0070:  3033 2047 4d54 0d0a 5365 7276 6572 3a20  03.GMT..Server:.
	0x0080:  4170 6163 6865 0d0a 4c61 7374 2d4d 6f64  Apache..Last-Mod
	0x0090:  6966 6965 643a 2057 6564 2c20 3230 2041  ified:.Wed,.20.A
	0x00a0:  7567 2032 3031 3420 3131 3a32 303a 3036  ug.2014.11:20:06
	0x00b0:  2047 4d54 0d0a 4163 6365 7074 2d52 616e  .GMT..Accept-Ran
	0x00c0:  6765 733a 2062 7974 6573 0d0a 436f 6e74  ges:.bytes..Cont
	0x00d0:  656e 742d 4c65 6e67 7468 3a20 3131 3530  ent-Length:.1150
	0x00e0:  0d0a 4361 6368 652d 436f 6e74 726f 6c3a  ..Cache-Control:
	0x00f0:  206d 6178 2d61 6765 3d33 3630 302c 2070  .max-age=3600,.p
	0x0100:  7562 6c69 630d 0a4b 6565 702d 416c 6976  ublic..Keep-Aliv
	0x0110:  653a 2074 696d 656f 7574 3d33 2c20 6d61  e:.timeout=3,.ma
	0x0120:  783d 3538 0d0a 436f 6e6e 6563 7469 6f6e  x=58..Connection
	0x0130:  3a20 4b65 6570 2d41 6c69 7665 0d0a 436f  :.Keep-Alive..Co
	0x0140:  6e74 656e 742d 5479 7065 3a20 696d 6167  ntent-Type:.imag
	0x0150:  652f 782d 6963 6f6e 0d0a 0d0a 0000 0100  e/x-icon........
	0x0160:  0100 1010 0000 0100 2000 6804 0000 1600  ..........h.....
	0x0170:  0000 2800 0000 1000 0000 2000 0000 0100  ..(.............
	0x0180:  2000 0000 0000 0004 0000 0000 0000 0000  ................
	0x0190:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01a0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01b0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01c0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01d0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x01e0:  0000 0000 0000 0000 0000 1a58 d4d4 1a58  ...........X...X
	0x01f0:  d4d4 0000 0000 0000 0000 0000 0000 0000  ................
	0x0200:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0210:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0220:  0000 0000 0000 0000 0000 0000 0000 1a58  ...............X
	0x0230:  d4d4 1a58 d4d4 0000 0000 0000 0000 0000  ...X............
	0x0240:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0250:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0260:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0270:  0000 1956 d3ff 1a58 d4d4 215c d0e7 0000  ...V...X..!\....
	0x0280:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0290:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x02a0:  0000 0000 0000 0000 0000 0000 0000 1a58  ...............X
	0x02b0:  d4d4 1d5d e01b 1b5b ddff 1a58 d4d4 1a58  ...]...[...X...X
	0x02c0:  d4ff 1a58 d4ff 0000 0000 0000 0000 0000  ...X............
	0x02d0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x02e0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x02f0:  0000 1c5b dbb3 0000 0000 1e5f e5ff 1e5e  ...[......._...^
	0x0300:  e4ff 1a58 d4d4 1a58 d4ff 0000 0000 0000  ...X...X........
	0x0310:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0320:  0000 0000 0000 0000 0000 0000 0000 1a58  ...............X
	0x0330:  d4d4 0000 0000 0000 0000 1f60 e7ff 1e5f  ...........`..._
	0x0340:  e3ff 3b74 e9ff 1a58 d4d4 0000 0000 0000  ..;t...X........
	0x0350:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0360:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0370:  0000 1a58 d4d4 1c5b dd0b 1a58 d4d4 1d5d  ...X...[...X...]
	0x0380:  deff 1f5d d9ff 1a58 d4d4 1a58 d4ff 0000  ...]...X...X....
	0x0390:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x03a0:  0000 0000 0000 0000 0000 0000 0000 1a58  ...............X
	0x03b0:  d4d4 0000 0000 1a58 d4d4 1a58 d4d4 1a58  .......X...X...X
	0x03c0:  d4ff 1653 c8ff 1753 c5ff 346b d5ff 1734  ...S...S..4k...4
	0x03d0:  6d15 0000 0000 0000 0000 0000 0000 0000  m...............
	0x03e0:  0000 1a58 d4d4 0000 0000 1a58 d4d4 709a  ...X.......X..p.
	0x03f0:  f604 1a58 d4d4 c6d7 fc04 1a58 d4ff 1a58  ...X.......X...X
	0x0400:  d4ff 1b5a d9ff 2763 dfff 0e46 acff 134f  ...Z..'c...F...O
	0x0410:  bfff 0000 0000 7f7f 7f16 0000 0000 0000  ................
	0x0420:  0000 0000 0000 1a58 d4d4 0000 0000 1a58  .......X.......X
	0x0430:  d4d4 0000 0000 1a58 d4d4 1450 c3ff 1d5c  .......X...P...\
	0x0440:  dfff 0717 3804 040c 1c04 1a58 d4ff 1a58  ....8......X...X
	0x0450:  d4d4 0e46 adff 0816 301c 1a58 d4d4 1a58  ...F....0..X...X
	0x0460:  d4d4 4476 dcff 2861 ceb1 2f6c e74d 1c5d  ..Dv..(a../l.M.]
	0x0470:  e087 2145 9045 134e beff 1650 c1ff 0000  ..!E.E.N...P....
	0x0480:  0000 0000 0000 0000 0000 0000 0000 3a69  ..............:i
	0x0490:  c055 3643 5f36 081f 4b0c 0000 0000 0000  .U6C_6..K.......
	0x04a0:  0000 0000 0000 1c5c dfcf 235f dbff 134d  .......\..#_...M
	0x04b0:  bdff 124c baff 1753 c8ff 1036 8445 0000  ...L...S...6.E..
	0x04c0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x04d0:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x04e0:  0000 0000 0000 0000 0000 0000 0000 1a58  ...............X
	0x04f0:  d4a9 1a58 d4a9 1a58 d419 0000 0000 0000  ...X...X........
	0x0500:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0510:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0520:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0530:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0540:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0550:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0560:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0570:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0580:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0590:  0000 0000 0000 0000 0000 ffff 0000 f3ff  ................
	0x05a0:  0000 f9ff 0000 fc7f 0000 fa1f 0000 fd0f  ................
	0x05b0:  0000 fb0f 0000 fd07 0000 fa07 0000 d503  ................
	0x05c0:  0000 ea31 0000 0a7f 0000 e0ff 0000 f9ff  ...1............
	0x05d0:  0000 ffff 0000 ffff 0000                 ..........
22:38:03.361047 IP 88.212.201.216.http > 192.168.0.17.43482: Flags [P.], seq 1:674, ack 657, win 4174, options [nop,nop,TS val 3092166521 ecr 4144613], length 673: HTTP: HTTP/1.1 302 Moved Temporarily
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  02d5 0000 4000 3806 5cbd 58d4 c9d8 c0a8  ....@.8.\.X.....
	0x0020:  0011 0050 a9da 1aba 59c1 8bef 06f2 8018  ...P....Y.......
	0x0030:  104e 295f 0000 0101 080a b84e b779 003f  .N)_.......N.y.?
	0x0040:  3de5 4854 5450 2f31 2e31 2033 3032 204d  =.HTTP/1.1.302.M
	0x0050:  6f76 6564 2054 656d 706f 7261 7269 6c79  oved.Temporarily
	0x0060:  0d0a 4461 7465 3a20 5468 752c 2033 3020  ..Date:.Thu,.30.
	0x0070:  4465 6320 3230 3231 2031 393a 3338 3a30  Dec.2021.19:38:0
	0x0080:  3320 474d 540d 0a53 6572 7665 723a 2030  3.GMT..Server:.0
	0x0090:  572f 302e 3863 0d0a 436f 6e74 656e 742d  W/0.8c..Content-
	0x00a0:  5479 7065 3a20 7465 7874 2f68 746d 6c0d  Type:.text/html.
	0x00b0:  0a4c 6f63 6174 696f 6e3a 2068 7474 7073  .Location:.https
	0x00c0:  3a2f 2f63 6f75 6e74 6572 2e79 6164 726f  ://counter.yadro
	0x00d0:  2e72 752f 6869 743f 7268 7474 7025 3341  .ru/hit?rhttp%3A
	0x00e0:  2f2f 7777 772e 7362 7570 2e63 6f6d 2f77  //www.sbup.com/w
	0x00f0:  696b 692f 2532 3544 3025 3235 4133 2532  iki/%25D0%25A3%2
	0x0100:  3544 3125 3235 3837 2532 3544 3025 3235  5D1%2587%25D0%25
	0x0110:  4230 2532 3544 3125 3235 3831 2532 3544  B0%25D1%2581%25D
	0x0120:  3125 3235 3832 2532 3544 3025 3235 4244  1%2582%25D0%25BD
	0x0130:  2532 3544 3025 3235 4238 2532 3544 3025  %25D0%25B8%25D0%
	0x0140:  3235 4241 2533 4157 696b 6953 7973 6f70  25BA%3AWikiSysop
	0x0150:  3b73 3138 3436 2a39 3532 2a32 343b 7568  ;s1846*952*24;uh
	0x0160:  7474 7025 3341 2f2f 7777 772e 7362 7570  ttp%3A//www.sbup
	0x0170:  2e63 6f6d 2f77 696b 692f 2532 3544 3025  .com/wiki/%25D0%
	0x0180:  3235 3945 2532 3544 3025 3235 4231 2532  259E%25D0%25B1%2
	0x0190:  3544 3125 3235 3831 2532 3544 3125 3235  5D1%2581%25D1%25
	0x01a0:  3833 2532 3544 3025 3235 4236 2532 3544  83%25D0%25B6%25D
	0x01b0:  3025 3235 4234 2532 3544 3025 3235 4235  0%25B4%25D0%25B5
	0x01c0:  2532 3544 3025 3235 4244 2532 3544 3025  %25D0%25BD%25D0%
	0x01d0:  3235 4238 2532 3544 3025 3235 4235 5f25  25B8%25D0%25B5_%
	0x01e0:  3235 4431 2532 3538 3325 3235 4431 2532  25D1%2583%25D1%2
	0x01f0:  3538 3725 3235 4430 2532 3542 3025 3235  587%25D0%25B0%25
	0x0200:  4431 2532 3538 3125 3235 4431 2532 3538  D1%2581%25D1%258
	0x0210:  3225 3235 4430 2532 3542 4425 3235 4430  2%25D0%25BD%25D0
	0x0220:  2532 3542 3825 3235 4430 2532 3542 4125  %25B8%25D0%25BA%
	0x0230:  3235 4430 2532 3542 3025 3341 5769 6b69  25D0%25B0%3AWiki
	0x0240:  5379 736f 703b 302e 3835 3733 3234 3135  Sysop;0.85732415
	0x0250:  3832 3130 3432 3331 0d0a 436f 6e74 656e  82104231..Conten
	0x0260:  742d 4c65 6e67 7468 3a20 3332 0d0a 4578  t-Length:.32..Ex
	0x0270:  7069 7265 733a 2054 7565 2c20 3239 2044  pires:.Tue,.29.D
	0x0280:  6563 2032 3032 3020 3231 3a30 303a 3030  ec.2020.21:00:00
	0x0290:  2047 4d54 0d0a 5072 6167 6d61 3a20 6e6f  .GMT..Pragma:.no
	0x02a0:  2d63 6163 6865 0d0a 4361 6368 652d 636f  -cache..Cache-co
	0x02b0:  6e74 726f 6c3a 206e 6f2d 6361 6368 650d  ntrol:.no-cache.
	0x02c0:  0a0d 0a3c 6874 6d6c 3e3c 626f 6479 3e4d  ...<html><body>M
	0x02d0:  6f76 6564 3c2f 626f 6479 3e3c 2f68 746d  oved</body></htm
	0x02e0:  6c3e 0a                                  l>.
22:38:03.378063 IP 64.233.162.157.http > 192.168.0.17.48638: Flags [S.], seq 238693577, ack 1730200340, win 65535, options [mss 1430,sackOK,TS val 64406225 ecr 4144616,nop,wscale 8], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  003c d79a 0000 3a06 04e2 40e9 a29d c0a8  .<....:...@.....
	0x0020:  0011 0050 bdfe 0e3a 2cc9 6720 c314 a012  ...P...:,.g.....
	0x0030:  ffff 7b77 0000 0204 0596 0402 080a 03d6  ..{w............
	0x0040:  c2d1 003f 3de8 0103 0308                 ...?=.....
22:38:03.406840 IP 173.249.26.55.http > 192.168.0.17.51202: Flags [F.], seq 10456, ack 2502, win 269, options [nop,nop,TS val 170996920 ecr 4144613], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 8bc0 4000 3806 2e1a adf9 1a37 c0a8  .4..@.8......7..
	0x0020:  0011 0050 c802 4b4b ce07 f896 6fb0 8011  ...P..KK....o...
	0x0030:  010d 25cb 0000 0101 080a 0a31 34b8 003f  ..%........14..?
	0x0040:  3de5                                     =.
22:38:03.444680 IP 2.20.254.18.http > 192.168.0.17.52846: Flags [S.], seq 2703081362, ack 1421173907, win 28960, options [mss 1452,sackOK,TS val 2574024324 ecr 4144765,nop,wscale 7], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  003c 0000 4000 3a06 7fdc 0214 fe12 c0a8  .<..@.:.........
	0x0020:  0011 0050 ce6e a11d bf92 54b5 6493 a012  ...P.n....T.d...
	0x0030:  7120 d692 0000 0204 05ac 0402 080a 996c  q..............l
	0x0040:  7e84 003f 3e7d 0103 0307                 ~..?>}....
22:38:03.485515 IP 2.20.254.18.http > 192.168.0.17.52846: Flags [.], ack 414, win 235, options [nop,nop,TS val 2574024364 ecr 4144804], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 e94c 4000 3a06 9697 0214 fe12 c0a8  .4.L@.:.........
	0x0020:  0011 0050 ce6e a11d bf93 54b5 6630 8010  ...P.n....T.f0..
	0x0030:  00eb 73a0 0000 0101 080a 996c 7eac 003f  ..s........l~..?
	0x0040:  3ea4                                     >.
22:38:03.491538 IP 2.20.254.18.http > 192.168.0.17.52846: Flags [P.], seq 1:890, ack 414, win 235, options [nop,nop,TS val 2574024366 ecr 4144804], length 889: HTTP: HTTP/1.1 200 OK
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  03ad e94d 4000 3a06 931d 0214 fe12 c0a8  ...M@.:.........
	0x0020:  0011 0050 ce6e a11d bf93 54b5 6630 8018  ...P.n....T.f0..
	0x0030:  00eb 018b 0000 0101 080a 996c 7eae 003f  ...........l~..?
	0x0040:  3ea4 4854 5450 2f31 2e31 2032 3030 204f  >.HTTP/1.1.200.O
	0x0050:  4b0d 0a53 6572 7665 723a 206e 6769 6e78  K..Server:.nginx
	0x0060:  0d0a 436f 6e74 656e 742d 5479 7065 3a20  ..Content-Type:.
	0x0070:  6170 706c 6963 6174 696f 6e2f 6f63 7370  application/ocsp
	0x0080:  2d72 6573 706f 6e73 650d 0a43 6f6e 7465  -response..Conte
	0x0090:  6e74 2d4c 656e 6774 683a 2035 3033 0d0a  nt-Length:.503..
	0x00a0:  4554 6167 3a20 2241 3546 4143 4642 3245  ETag:."A5FACFB2E
	0x00b0:  4144 4345 3746 4141 4234 4235 4633 4634  ADCE7FAAB4B5F3F4
	0x00c0:  3631 4232 4346 3035 3944 3831 4339 3530  61B2CF059D81C950
	0x00d0:  4237 4337 4638 4138 3432 3330 4532 3033  B7C7F8A84230E203
	0x00e0:  3145 4345 3032 3922 0d0a 4c61 7374 2d4d  1ECE029"..Last-M
	0x00f0:  6f64 6966 6965 643a 2057 6564 2c20 3239  odified:.Wed,.29
	0x0100:  2044 6563 2032 3032 3120 3132 3a30 303a  .Dec.2021.12:00:
	0x0110:  3030 2055 5443 0d0a 4361 6368 652d 436f  00.UTC..Cache-Co
	0x0120:  6e74 726f 6c3a 2070 7562 6c69 632c 206e  ntrol:.public,.n
	0x0130:  6f2d 7472 616e 7366 6f72 6d2c 206d 7573  o-transform,.mus
	0x0140:  742d 7265 7661 6c69 6461 7465 2c20 6d61  t-revalidate,.ma
	0x0150:  782d 6167 653d 3130 3439 330d 0a45 7870  x-age=10493..Exp
	0x0160:  6972 6573 3a20 5468 752c 2033 3020 4465  ires:.Thu,.30.De
	0x0170:  6320 3230 3231 2032 323a 3332 3a35 3620  c.2021.22:32:56.
	0x0180:  474d 540d 0a44 6174 653a 2054 6875 2c20  GMT..Date:.Thu,.
	0x0190:  3330 2044 6563 2032 3032 3120 3139 3a33  30.Dec.2021.19:3
	0x01a0:  383a 3033 2047 4d54 0d0a 436f 6e6e 6563  8:03.GMT..Connec
	0x01b0:  7469 6f6e 3a20 6b65 6570 2d61 6c69 7665  tion:.keep-alive
	0x01c0:  0d0a 0d0a 3082 01f3 0a01 00a0 8201 ec30  ....0..........0
	0x01d0:  8201 e806 092b 0601 0505 0730 0101 0482  .....+.....0....
	0x01e0:  01d9 3082 01d5 3081 bea1 3430 3231 0b30  ..0...0...4021.0
	0x01f0:  0906 0355 0406 1302 5553 3116 3014 0603  ...U....US1.0...
	0x0200:  5504 0a13 0d4c 6574 2773 2045 6e63 7279  U....Let's.Encry
	0x0210:  7074 310b 3009 0603 5504 0313 0252 3318  pt1.0...U....R3.
	0x0220:  0f32 3032 3131 3232 3931 3233 3630 305a  .20211229123600Z
	0x0230:  3075 3073 304b 3009 0605 2b0e 0302 1a05  0u0s0K0...+.....
	0x0240:  0004 1448 dac9 a0fb 2bd3 2d4f f0de 68d2  ...H....+.-O..h.
	0x0250:  f567 b735 f9b3 c404 1414 2eb3 17b7 5856  .g.5..........XV
	0x0260:  cbae 5009 40e6 1faf 9d8b 14c2 c602 1204  ..P.@...........
	0x0270:  fcd0 b3a8 af0a f353 1e0a 9e3b 8ef6 9120  .......S...;....
	0x0280:  e280 0018 0f32 3032 3131 3232 3931 3230  .....20211229120
	0x0290:  3030 305a a011 180f 3230 3232 3031 3035  000Z....20220105
	0x02a0:  3131 3539 3538 5a30 0d06 092a 8648 86f7  115958Z0...*.H..
	0x02b0:  0d01 010b 0500 0382 0101 0095 6fa3 92de  ............o...
	0x02c0:  7ee2 a2e2 27f1 a6e7 9683 c83e b1ab d8a7  ~...'......>....
	0x02d0:  63c5 7aea 15ab d0f8 a56b 7b79 42e2 7bbc  c.z......k{yB.{.
	0x02e0:  7f3d 1b6d 9001 a554 61e6 ba0a 1584 d8c3  .=.m...Ta.......
	0x02f0:  6c6b b0a9 b8b8 65ed 68e4 6030 9462 0aa5  lk....e.h.`0.b..
	0x0300:  fa27 5726 4d12 92db fd31 f4bf ba19 48f3  .'W&M....1....H.
	0x0310:  0220 ad91 0e32 e688 974d 929f 11ce daab  .....2...M......
	0x0320:  fd82 5dfc 1521 8e1a 0588 0faf 13d0 2ce9  ..]..!........,.
	0x0330:  b4a2 8a01 e5b9 1033 96f2 8610 3983 7c65  .......3....9.|e
	0x0340:  2836 3dbe 7e17 8dd7 a871 e4f7 cfc0 eb0c  (6=.~....q......
	0x0350:  9177 3eea 234a 7f6b bd92 5c8f 7df5 b7b1  .w>.#J.k..\.}...
	0x0360:  59bf 2f8e 7543 47e3 eedc d995 490b d434  Y./.uCG.....I..4
	0x0370:  cbf9 5715 9116 06c4 b4b5 e59e db31 56d9  ..W..........1V.
	0x0380:  9894 6ded a7c7 f093 c8ed 764a 40cf d26b  ..m.......vJ@..k
	0x0390:  8f6e a57c 1166 12ba 029d b874 96d1 fe48  .n.|.f.....t...H
	0x03a0:  c594 1f89 6379 7dff bbba 8b54 546a 9319  ....cy}....TTj..
	0x03b0:  a08f e816 222a e563 cdb7 b1              ...."*.c...
22:38:04.329063 IP 173.249.26.55.http > 192.168.0.17.51216: Flags [S.], seq 2817254051, ack 1511191838, win 28960, options [mss 1452,sackOK,TS val 170997850 ecr 4145571,nop,wscale 7], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  003c 0000 4000 3906 b8d2 adf9 1a37 c0a8  .<..@.9......7..
	0x0020:  0011 0050 c810 a7eb e2a3 5a12 f51e a012  ...P......Z.....
	0x0030:  7120 275f 0000 0204 05ac 0402 080a 0a31  q.'_...........1
	0x0040:  385a 003f 41a3 0103 0307                 8Z.?A.....
22:38:04.549804 IP 2.20.254.18.http > 192.168.0.17.52846: Flags [F.], seq 890, ack 414, win 235, options [nop,nop,TS val 2574025386 ecr 4144849], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 e94e 4000 3a06 9695 0214 fe12 c0a8  .4.N@.:.........
	0x0020:  0011 0050 ce6e a11d c30c 54b5 6630 8011  ...P.n....T.f0..
	0x0030:  00eb 6bfb 0000 0101 080a 996c 82aa 003f  ..k........l...?
	0x0040:  3ed1                                     >.
22:38:04.626665 IP 2.20.254.18.http > 192.168.0.17.52846: Flags [.], ack 415, win 235, options [nop,nop,TS val 2574025450 ecr 4145908], length 0
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  0034 e94f 4000 3a06 9694 0214 fe12 c0a8  .4.O@.:.........
	0x0020:  0011 0050 ce6e a11d c30d 54b5 6631 8010  ...P.n....T.f1..
	0x0030:  00eb 6797 0000 0101 080a 996c 82ea 003f  ..g........l...?
	0x0040:  42f4                                     B.
22:38:06.176032 IP 46.4.114.109.http > 192.168.0.17.56204: Flags [P.], seq 346:799, ack 835, win 503, options [nop,nop,TS val 3174551678 ecr 4147462], length 453: HTTP: HTTP/1.1 302 Moved Temporarily
	0x0000:  000c 291b f1b4 749d 7914 1f16 0800 4500  ..)...t.y.....E.
	0x0010:  01f9 058d 4000 3706 db47 2e04 726d c0a8  ....@.7..G..rm..
	0x0020:  0011 0050 db8c 4043 76e7 50b9 4bbb 8018  ...P..@Cv.P.K...
	0x0030:  01f7 46c6 0000 0101 080a bd37 d07e 003f  ..F........7.~.?
	0x0040:  4906 4854 5450 2f31 2e31 2033 3032 204d  I.HTTP/1.1.302.M
	0x0050:  6f76 6564 2054 656d 706f 7261 7269 6c79  oved.Temporarily
	0x0060:  0d0a 5365 7276 6572 3a20 6f70 656e 7265  ..Server:.openre
	0x0070:  7374 790d 0a44 6174 653a 2054 6875 2c20  sty..Date:.Thu,.
	0x0080:  3330 2044 6563 2032 3032 3120 3139 3a33  30.Dec.2021.19:3
	0x0090:  383a 3036 2047 4d54 0d0a 436f 6e74 656e  8:06.GMT..Conten
	0x00a0:  742d 5479 7065 3a20 7465 7874 2f68 746d  t-Type:.text/htm
	0x00b0:  6c0d 0a43 6f6e 7465 6e74 2d4c 656e 6774  l..Content-Lengt
	0x00c0:  683a 2031 3432 0d0a 436f 6e6e 6563 7469  h:.142..Connecti
	0x00d0:  6f6e 3a20 6b65 6570 2d61 6c69 7665 0d0a  on:.keep-alive..
	0x00e0:  4c6f 6361 7469 6f6e 3a20 6874 7470 733a  Location:.https:
	0x00f0:  2f2f 7777 772e 6163 696e 742e 6e65 742f  //www.acint.net/
	0x0100:  7069 6e67 2f3f 763d 302e 342e 3026 7569  ping/?v=0.4.0&ui
	0x0110:  643d 3236 6131 6661 3832 2d39 6165 642d  d=26a1fa82-9aed-
	0x0120:  3436 6238 2d61 6364 632d 3831 3365 3366  46b8-acdc-813e3f
	0x0130:  3436 6537 3464 2664 703d 3130 2674 7a3d  46e74d&dp=10&tz=
	0x0140:  2532 4230 3325 3341 3030 266e 633d 3137  %2B03%3A00&nc=17
	0x0150:  3130 3732 3235 2664 543d 3230 3231 2d31  107225&dT=2021-1
	0x0160:  322d 3330 5432 3225 3341 3338 2533 4130  2-30T22%3A38%3A0
	0x0170:  362e 3039 390d 0a0d 0a3c 6874 6d6c 3e0d  6.099....<html>.
	0x0180:  0a3c 6865 6164 3e3c 7469 746c 653e 3330  .<head><title>30
	0x0190:  3220 466f 756e 643c 2f74 6974 6c65 3e3c  2.Found</title><
	0x01a0:  2f68 6561 643e 0d0a 3c62 6f64 793e 0d0a  /head>..<body>..
	0x01b0:  3c63 656e 7465 723e 3c68 313e 3330 3220  <center><h1>302.
	0x01c0:  466f 756e 643c 2f68 313e 3c2f 6365 6e74  Found</h1></cent
	0x01d0:  6572 3e0d 0a3c 6872 3e3c 6365 6e74 6572  er>..<hr><center
	0x01e0:  3e6f 7065 6e72 6573 7479 3c2f 6365 6e74  >openresty</cent
	0x01f0:  6572 3e0d 0a3c 2f62 6f64 793e 0d0a 3c2f  er>..</body>..</
	0x0200:  6874 6d6c 3e0d 0a                        html>..
^C
27 packets captured
27 packets received by filter
0 packets dropped by kernel
    
 </details>  
