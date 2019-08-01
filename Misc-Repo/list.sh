#!/bin/bash
unzip -p "File List DPA-I.docx" > TempDoc.txt
sed -e 's/<\/w:p>/\n/g; s/<[^>]\{1,\}>//g;' TempDoc.txt > TempDoc2.txt
sed '/^$/d' TempDoc2.txt > TempDoc.txt
grep -o "^AC/[0-9]*/[0-9]*/[0-9]*\|^DPA-I/[0-9]*/[0-9]*/[0-9]*" TempDoc.txt
