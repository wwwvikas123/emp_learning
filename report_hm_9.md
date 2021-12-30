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
