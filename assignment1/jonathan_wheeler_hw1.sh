#!/bin/bash - 
#===============================================================================
#
#          FILE: hw1.sh
# 
#         USAGE: ./hw1.sh 
# 
#   DESCRIPTION: Homework number 1
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/19/2017 22:36
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

help()
{
	echo "Usage $0 [--help] [-w]"
	echo "--help Print this help message"
	echo "-w Print name three times"
	echo "With no arguments it provides a menu to test the system"
}

userCheck()
{
	case "$UID" in
	0)
		echo "Welcome great and almighty root"
		;;
	*)
		echo "Current user: $UID"
		;;
esac
}

osCheck()
{
	os=`uname -s`
	if [[ $os == "Linux" ]]
	then
		echo "Current operating system: $os"
	else
		echo "We are not on Linux but, $os"
	fi
}

if [[ $1 == "--help" ]]
then
	help
	exit 0
fi

echo "My name is Jonathan Wheeler"
echo "You are running this script in  $HOSTNAME"

echo "This script can do three things:"
echo "1. Check to see if the user is the root user"
echo "2. Check to see if the script is running on Linux OS"
echo "3. Check to see if the -w argument was given"
echo "What would you like to do? (1, 2, 3): "

read answer

if [[ $answer == 1 ]]
then
	userCheck
fi

if [[ $answer == 2 ]]
then
	osCheck
fi

if [[ $answer == 3 ]]
then
	if [[ $1 == "-w" ]]
	then
		if [[ $# == 2 ]]
		then
			echo "$2 $2 $2"
			exit 0
		else
			echo "-w requires a 2nd parameter"
			exit 1
		fi
	else
		echo "requires param -w and 2nd param to be repeated. "
	fi
fi


exit 0

