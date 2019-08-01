#!/bin/bash

find . -type f -name "*.doc" -o -name "*.od*" -o -name "*.docx" | while read i ; do
	[ "$1" ] || { echo "You forgot search string!" ; exit 1 ; }
	unzip -ca "$i" 2>/dev/null | grep -iq "$*"
	if [ $? -eq 0 ] ; then
		echo "Found -> $i" | nl
	fi
done
