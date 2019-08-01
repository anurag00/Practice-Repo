#!/bin/bash
unzip -p "File List DPA-I.docx" > TempDoc.txt
echo "--------------------------------------------------"
sed -e 's/<\/w:p>/\n/g; s/<[^>]\{1,\}>//g;' TempDoc.txt > TempDoc2.txt
echo "--------------------------------------------------"
sed '/^$/d' TempDoc2.txt > TempDoc.txt
echo "--------------------------------------------------"
if [ $# -eq 1 ]; then
	grep -in -B1 "$1" TempDoc.txt
fi
if [ $# -eq 2 ]; then
	grep -in -A1 "$1" TempDoc.txt
fi
echo "--------------------------------------------------"
