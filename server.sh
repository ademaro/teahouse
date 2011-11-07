#!/bin/bash

case "$1" in
 "start")
 #./manage.py runfcgi method=prefork host=127.0.0.1 port=8881 pidfile=H:/teahouse/ninjapirate.pid
 ./manage.py runfcgi method=threaded host=127.0.0.1 port=8881 pidfile=H:/teahouse/ninjapirate.pid
 ;;
 "stop")
 kill -9 `cat H:/teahouse/server.pid`
 ;;
 "restart")
 $0 stop
 sleep 1
 $0 start
 ;;
 *) echo "Usage: ./server.sh {start|stop|restart}";;
esac
