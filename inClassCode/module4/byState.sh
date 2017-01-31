#!/bin/bash - 
#===============================================================================
#
#          FILE: byState.sh
# 
#         USAGE: ./byState.sh 
# 
#   DESCRIPTION: Call sed script to modify data
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/31/2017 19:34
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error
ts=`date +%m%d`
sedFile="stateChange.sed"
inputFile=$1
outFile=$1.$ts

sed -f $sedFile $inputFile > $outFile

if [[ $? -eq 0 ]]
then
	echo "Processed $inputFile"
	echo "Output is $outFile"
fi

exit 0
