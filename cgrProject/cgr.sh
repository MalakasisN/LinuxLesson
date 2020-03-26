#cleans file
sed '/^[[:space:]]*$/d' hg38_knownCanonical.exonNuc.fa>hg38_knownCanonical.exonNuc.FA

#applies cgr.py to every gene file made in.
for j in `seq 2 2 10000`
do
    head -$j hg38_knownCanonical.exonNuc.FA|tail -2>gene$j.FA
    python3 cgr.py -x gene$j.FA -k 1.5
done

#Make total coordinate output files
cat gene*.FAx-coords.txt>x-coordstotal.txt
cat gene*.FAy-coords.txt>y-coordstotal.txt

#Optional,removes outputs per gene
rm gene*.FA*

#makes final output plot
python3 cgrtotalplot.py
