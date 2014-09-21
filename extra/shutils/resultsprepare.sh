rm all.out
for f in *.csv
do
sed '1d' "$f" | sed 's/^\(.*\),.*,.*,.*/\1/' >> all.out
done
# " --techniqie=\2/