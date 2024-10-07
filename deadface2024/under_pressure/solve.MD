uname -a
Linux f48779bc8382 6.1.0-26-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.112-1 (2024-09-30) x86_64 Linux

~ $ whoami
deephax

~ $ id
uid=1000(deephax) gid=1000(deephax) groups=1000(deephax)

~ $ cat /etc/passwd
root:x:0:0:root:/root:/bin/sh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
deephax:x:1000:1000:Linux User,,,:/home/deephax:/bin/sh
lilith:x:1001:1001:Linux User,,,:/home/lilith:/bin/sh

~ $ ps -ef
PID   USER     TIME  COMMAND
    1 root      0:00 {start.sh} /bin/sh /usr/local/bin/start.sh
    9 root      0:00 crond -b -l 5 -L /dev/null
   10 root      0:00 /usr/local/bin/usrv
   12 deephax   0:00 /bin/sh
   47 deephax   0:00 ps -ef
~ $ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin