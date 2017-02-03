#!/bin/bash - 
#===============================================================================
#
#          FILE: hw3.sh
# 
#         USAGE: ./hw3.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 02/01/2017 05:31
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

help()
{
	echo "Usage $0 [-c customerDataFolder] [-f dataFile]"
	echo "Both arguments are required"
}

if [[ $1 == "--help" ]]
then
	help
	exit 0
fi

while getopts ":c:f:" opt
do
	case $opt in
		c) dataFolder=$OPTARG
			;;
		f) dataFile=$OPTARG
			;;
		/?)
			help
			;;
	esac
done

if [[ ! -d $dataFolder ]]
then
	echo "Customer $dataFolder is missing"
	echo "Creating folder"
	mkdir -p $dataFolder/{01..12}
fi


echo "Getting file from customer server"

scp jw01126@icarus.cs.weber.edu:/home/hvalle/submit/cs3030/files/FRED.csv ./$dataFolder/`date +%m`/$dataFile.`date +%Y-%m-%d`

echo "File located at ./$dataFolder/`date +$m`/$dataFile"
exit 0


