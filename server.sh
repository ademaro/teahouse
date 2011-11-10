#!/bin/bash

PROJDIR="/var/www/z-gu.ru/_tea"
PIDFILE="$PROJDIR/server.pid"

cd $PROJDIR

case "$1" in
 "start")
   exec python ./manage.py runfcgi method=prefork host=127.0.0.1 port=8881 pidfile=$PIDFILE
 ;;
 "stop")
   kill -9 `cat -- $PIDFILE`
   rm -f -- $PIDFILE
 ;;
 "restart")
   $0 stop
   sleep 1
   $0 start
 ;;
   *) echo "Usage: ./server.sh {start|stop|restart}";;
esac
