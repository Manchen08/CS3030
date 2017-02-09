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
awkFile="stateName.awk"
sedFile="stateChange.sed"
inputFile=$1
state=$2
outFile=$1.$ts.$state

# 1) Filter data by state <$2>
grep $state $inputFile |
# call sed script to modify data
sed -f $sedFile |
# Awk script to take first field(Name)
awk -f $awkFile |
# sort alphabetilcally by first name
sort |
#select unique records
uniq > $outFile
exit 0
