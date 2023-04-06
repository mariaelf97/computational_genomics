# to check loci in hardy weinberg equilibrium
vcftools --gzvcf chr16.vcf.gz --hardy
# this will create a file which has chromosoem information, observed homozygosity, heterozygosity, chi square value HWE,
# p-value of HWE