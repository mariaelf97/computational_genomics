velveth velvet 25 -short -fastq ERR10513377_1.fastq
velvetg velvet
time spades.py -s ERR10513377_1.fastq -o spades --sc -k 25
time unicycler -s SRR20749437_1.fastq --mode normal -o unicycler
quast velvet/contigs.fa spades/contigs.fasta unicycler/assembly.fasta ../sequence.fasta
