## 1

$ sudo ip address add 192.168.33.200/24 dev ens34

Проверка соединения 

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

Deleting: $ sudo ip address del 192.168.33.200/24 dev ens34
