#!/bin/bash

ts=`date`
tmd=`date +%m%d`
tm=`date +%m`
home="/home/student1"
logdir="$home/log/$tm"
log="hello".$tmd

# log structure should be long/MM

echo "Hello Jon. It is: $ts"

if [[ ! -d $logdir ]]
then
	# create dir
	mkdir -p $logdir
fi

# run program
echo "Hello Jon. It is: $ts" >> $logdir/$log

exit 0
