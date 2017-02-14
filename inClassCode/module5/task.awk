#!/user/bin/awk -f
BEGIN { FS=":"}# delimiter
{
	print $1" " $6
}

