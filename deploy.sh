#!/usr/bin/env bash

id=`netstat -nlp | grep :5000 | awk '{print $7}' | awk -F"/" '{ print $1 }'`
if [ ! -z $id ]; then
   echo "kill process $id"
   kill $id
fi
nohup python app.py >/dev/null 2>&1 &
echo "start server"