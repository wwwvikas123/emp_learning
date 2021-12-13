# AWK.

## 1.
[user@centos_2 Documents]$  cat access.log | awk -F\" '{print $6}' | sort -n | uniq -c | sort -rn | head

```
 340874 Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)
  42635 Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko
  17036 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
  16086 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)
   9497 Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.45
   7823 Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0
   7564 python-requests/2.25.1
   4607 Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0
   4592 Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108               baidu.sogo.uc.UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN
   4209 Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)

```

## 2. 
[user@centos_2 Documents]$ cat access.log | grep "216.244.66.230" | cut -d[ -f2 | cut -d] -f1 | awk -F ":" '{print $1}'| awk -F "/" '{print "reqs "sort"", $2,$3}'|  uniq -c

```
      1 reqs  Dec 2020
     43 reqs  Jan 2021
     14 reqs  Feb 2021
      2 reqs  Mar 2021
     34 reqs  Apr 2021
     27 reqs  May 2021
      3 reqs  Jun 2021
     23 reqs  Jul 2021
    108 reqs  Aug 2021
      7 reqs  Sep 2021
     23 reqs  Oct 2021
    106 reqs  Nov 2021
      5 reqs  Dec 2021


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
[user@centos_2 Documents]$ tail access.log | sed 's/"[[:alpha:]]*\/[[:digit:]]*.[[:digit:]]/lynx/'

```
107.150.89.123 - - [10/Dec/2021:18:30:06 +0100] "GET /apache-log/access.log HTTP/1.1" 200 53141504 "http://www.almhuette-raith.at/" lynx (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1" "-"
107.150.89.123 - - [10/Dec/2021:18:31:10 +0100] "GET /apache-log/access.log HTTP/1.1" 200 53174272 "http://www.almhuette-raith.at/" lynx (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1" "-"
107.150.89.123 - - [10/Dec/2021:18:31:10 +0100] "GET /index.php?option=com_easyblog&view=dashboard&layout=write HTTP/1.1" 404 1397 "http://www.almhuette-raith.at/" lynx (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1" "-"
51.178.216.7 - - [10/Dec/2021:18:32:46 +0100] "GET /apache-log/access.log HTTP/1.1" 200 2247000 "http://www.almhuette-raith.at/" lynx (X11; Fedora; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0" "-"
45.130.60.19 - - [10/Dec/2021:18:32:46 +0100] "GET /index.php?option=com_easyblog&view=dashboard&layout=write HTTP/1.1" 404 1397 "http://www.almhuette-raith.at/" lynx (X11; Fedora; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0" "-"

```
## 2.
[user@centos_2 Documents]$ sed 's/^[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}\b/**/' access.log

```**- - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"
**- - [19/Dec/2020:14:08:06 +0100] "GET /apache-log/access.log HTTP/1.1" 200 233 "-" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
**- - [19/Dec/2020:14:08:08 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "http://www.almhuette-raith.at/apache-log/access.log" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
**- - [19/Dec/2020:14:14:26 +0100] "GET /robots.txt HTTP/1.1" 200 304 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)" "-"

```
## or 

[user@centos_2 Documents]$ sed -i's/^[[:digit:]]...........[[:digit:]]*/**/'  access.log

```

**- - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"
** - - [19/Dec/2020:14:08:06 +0100] "GET /apache-log/access.log HTTP/1.1" 200 233 "-" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
** - - [19/Dec/2020:14:08:08 +0100] "GET /favicon.ico HTTP/1.1" 404 217 "http://www.almhuette-raith.at/apache-log/access.log" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
** - - [19/Dec/2020:14:14:26 +0100] "GET /robots.txt HTTP/1.1" 200 304 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)" "-"

```

## Extra (только небольшую часть удалось придумать)

[user@centos_2 Documents]$ grep  "GET / HTTP" access.log.txt | awk '{print $1,$4,$7}'
