library(data.table)
library(tidyverse)
library("DESeq2")
# reading files
study_data <- as.data.frame(fread("/home/mahmedi/Downloads/robertsRTCounts.csv"))
metadata <- as.data.frame(fread("/home/mahmedi/Downloads/robertsRTDesign.csv"))
rownames(study_data) <- study_data$V1
study_data <- study_data[,-1]
colnames(study_data) <- metadata$Sample

count_table <- DESeqDataSetFromMatrix(
  countData = study_data,
  colData = metadata,
  design = ~Origin+Destination
)
# subset only transplants
dds <- DESeq(count_table)
# gene expression changes when the origin is stream versus when it's lake
dds_res_ls <- as.data.frame(results(dds, contrast = c("Origin","Lake","Stream")))
dds_res_sl <- as.data.frame(results(dds, contrast = c("Origin","Stream","Lake")))
# up-regulated genes in stream-lake
resSig_sl <- dds_res_sl[ which(dds_res_sl$padj < 0.1 ), ]
down_regulated_genes_sl <- head( resSig_sl[ order( resSig_sl$log2FoldChange ), ] , 50 )
write.csv(down_regulated_genes_sl,"down_regulated_genes_stream_lake.csv")
up_regulated_genes_sl<-tail( resSig_sl[ order( resSig_sl$log2FoldChange ), ], 50 )
write.csv(up_regulated_genes_sl,"up_regulated_genes_stream_lake.csv")
# up-regulated genes in lake-stream
resSig_ls <- dds_res_ls[ which(dds_res_ls$padj < 0.1 ), ]
down_regulated_genes_ls<-head( resSig_ls[ order( resSig_ls$log2FoldChange ), ],50 )
up_regulated_genes_ls<-tail( resSig_ls[ order( resSig_ls$log2FoldChange ), ] ,50)
write.csv(down_regulated_genes_ls,"down_regulated_genes_lake_stream.csv")
write.csv(up_regulated_genes_ls,"up_regulated_genes_lake_stream.csv")
