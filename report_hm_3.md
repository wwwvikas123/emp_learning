# AWK.

## 1.
[user@centos_2 Documents]$  cat access.log.txt | awk '{print $12}'  |  sort -n | uniq -c | sort -rn | head
```
363959 "Mozilla/4.0
 259926 "Mozilla/5.0
   7564 "python-requests/2.25.1"
   2720 "curl/7.68.0"
   2360 "-"
   1693 "AHC/2.1"
   1250 "Apache-HttpClient/4.5.2
   1148 "libwww-perl/6.05"
    949 "python-requests/2.25.0"
    851 "'Mozilla/5.0
```

## 2. 
[user@centos_2 Documents]$ cat access.log.txt | grep "216.244.66.230"  | cut -d[ -f2 | cut -d] -f1 | awk -F "/" '{print $2" " "reqs"}'  | sort -n | uniq -c

```
     34 Apr reqs
    108 Aug reqs
      6 Dec reqs
     14 Feb reqs
     43 Jan reqs
     23 Jul reqs
      3 Jun reqs
      2 Mar reqs
     27 May reqs
    106 Nov reqs
     23 Oct reqs
      7 Sep reqs
```      
## 3. 
[user@centos_2 Documents]$ cat access.log.txt | awk '{a[$1]+=$10} END {for (i in a) print a [i] " " "bites for" " "  i}'

```
668197537 bites for 109.146.137.238
2022488 bites for 31.40.226.9
75393 bites for 157.55.39.145
11863 bites for 213.226.113.93
11863 bites for 5.183.60.18
81982479 bites for 157.33.1.197
24897504 bites for 73.45.141.120
13020 bites for 204.15.145.39
10184644 bites for 157.55.39.148
34198293 bites for 159.89.187.19
10466 bites for 94.154.220.93
26209910 bites for 145.253.118.26
....
``` 
# SED.

## 1.

## 2.
[user@centos_2 Documents]$  head -n 5 access.log | sed 's/^[0-9]*.[0-9]*.[0-9]*.[0-9]*.[0-9]*/**/'

```**- - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"
**- - [19/Dec/2020:14:08:06 +0100] "GET /apache-log/access.log HTTP/1.1" 200 233 "-" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
**- - [19/Dec/2020:14:08:08 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "http://www.almhuette-raith.at/apache-log/access.log" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
**- - [19/Dec/2020:14:14:26 +0100] "GET /robots.txt HTTP/1.1" 200 304 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)" "-"

```
## or 

[user@centos_2 Documents]$ head -n 100 access.log | sed 's/^[[:digit:]]...........[[:digit:]]*/**/'

```

**- - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"
** - - [19/Dec/2020:14:08:06 +0100] "GET /apache-log/access.log HTTP/1.1" 200 233 "-" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
** - - [19/Dec/2020:14:08:08 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "http://www.almhuette-raith.at/apache-log/access.log" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
** - - [19/Dec/2020:14:14:26 +0100] "GET /robots.txt HTTP/1.1" 200 304 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)" "-"

```

