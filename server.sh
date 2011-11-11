#!/bin/bash

PROJDIR="/var/www/z-gu.ru/_tea"
PIDFILE="$PROJDIR/server.pid"
METHOD="threaded" #prefork for bigmem

cd $PROJDIR

case "$1" in
 "start")
<<<<<<< HEAD
   exec python ./manage.py runfcgi method=$METHOD host=127.0.0.1 port=8881 pidfile=$PIDFILE
 ;;
 "stop")
   kill -9 `cat -- $PIDFILE`
   rm -f -- $PIDFILE
=======
 #./manage.py runfcgi method=prefork host=127.0.0.1 port=8881 pidfile=H:/teahouse/ninjapirate.pid
 ./manage.py runfcgi method=threaded host=127.0.0.1 port=8881 pidfile=H:/teahouse/ninjapirate.pid
 ;;
 "stop")
 kill -9 `cat H:/teahouse/server.pid`
>>>>>>> eebcb97632489b66eaf90ccd983178408fb17fd3
 ;;
 "restart")
   $0 stop
   sleep 1
   $0 start
 ;;
   *) echo "Usage: ./server.sh {start|stop|restart}";;
esac
