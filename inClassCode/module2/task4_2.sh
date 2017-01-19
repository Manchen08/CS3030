#!/bin/bash - 
#===============================================================================
#
#          FILE: task4_2.sh
# 
#         USAGE: ./task4_2.sh 
# 
#   DESCRIPTION: Ask user for directory name, if it exists, prompt message.
#				If it does not, create it, then prompt message.
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/19/2017 19:49
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

echo "Please enter directory"
read dir

if [[  -d $dir ]]
then
	echo "Directory exists"
	echo "Do you want to remove it?(y)"
	read answer
	if [[ $answer == "y" ]]
	then	
		echo "$dir removed"
		rmdir $dir
	fi	
else
	echo "Directory does not exist"
	mkdir $dir
fi


exit 0
