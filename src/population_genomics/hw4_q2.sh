
# change vcf format file to bed format to use in admixture analyses
plink2 --vcf assignment4.vcf --allow-extra-chr 0 --max-alleles 2 --make-bed --out assignment4

awk '{$1="0";print $0}' assignment4.bim > assignment4.bim.tmp
mv assignment4.bim.tmp assignment4.bim

admixture -a qn2 --cv chr16_hwe.bed 2 > log2.out
admixture -a qn2 --cv assignment4.bed 3 > log3.out
admixture -a qn2 --cv assignment4.bed 4 > log4.out
admixture -a qn2 --cv assignment4.bed 5 > log5.out
admixture -a qn2 --cv assignment4.bed 6 > log6.out
admixture -a qn2 --cv assignment4.bed 7 > log7.out
admixture -a qn2 --cv assignment4.bed 8 > log8.out
admixture -a qn2 --cv assignment4.bed 9 > log9.out
admixture -a qn2 --cv assignment4.bed 10 > log10.out
admixture -a qn2 --cv assignment4.bed 11 > log11.out
admixture -a qn2 --cv assignment4.bed 12 > log12.out


# merge all cross validation errors into one file to find out which clustering has the smallest error
grep "CV" *out | awk '{print $3,$4}' | sed -e 's/(//;s/)//;s/://;s/K=//' > assignment4.cv.error
