bases=("A" "C" "G" "T")
for i in `seq 1`
do
    printf ">randomseq\n"
    for j in `seq 1000000`	 
    do
	rand=$(($RANDOM % 4))
	base=${bases[$rand]}
	printf "%s"$base
    done
done>randseq.FA



