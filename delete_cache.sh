#!/bin/sh

##I look for directories with the name '__pycache__'
directories=$(find $PWD -type d -name "__pycache__")

#I go through the list and delete each directory and the contents of each directory
for x in $directories; do
	rm -r $x
done
