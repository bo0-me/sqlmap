#!/bin/bash
logs=~/.sqlmap/output/
#find $logs -iregex .+result.+\.csv -size +38c  -print
#rm -f $logs/all.out
#find $logs -iregex "$logs/result.+\.csv" -size +38crm all.out
#for f in $logs$(find $logs -iregex .+result.+\.csv -size +38c -printf "%P\n")

for f in $(find -E $logs -iregex .+result.+\.csv -size +38c)
do
sed '1d' "$f" | sed 's/^\(.*\),.*,.*,.*/\1/' >> all.out
done
# " --techniqie=\2/