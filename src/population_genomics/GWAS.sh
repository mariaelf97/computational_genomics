# to check loci in hardy weinberg equilibrium
vcftools --gzvcf chr16.vcf.gz --hardy
# this will create a file which has chromosome information, observed homozygosity, heterozygosity, chi square value HWE,
# p-value of HWE
# This will take out all sites not in hwe and allow not less or more than 2 alleles per site
vcftools --gzvcf chr16.vcf.gz --hwe 0.05 --min-alleles 2 --max-alleles 2 --recode --stdout | gzip -c > chr16_hwe.vcf.gz