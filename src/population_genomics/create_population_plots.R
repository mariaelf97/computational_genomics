library(data.table)
library(tidyverse)


pop_file <- fread("/home/mahmedi/mnt/exouser/human_pop/q2/assignment4.2.Q")
individuals <- fread("/home/mahmedi/Downloads/assignment4_indivs.txt")
meta_data<- readxl::read_excel("/home/mahmedi/Downloads/assignment4.xlsx")
# subset 523 rows to match the number of rows in the individuals file
pop_file <- pop_file[1:523,]
# create a column with individual names
pop_file$Sample_Name <- individuals$Cuniculi_A
ordered_file<-pop_file[order(pop_file$V2),]
barplot(t(as.matrix(ordered_file[,1:2])),col=rainbow(2),
        xlab="Individuals",ylab="Ancestry",border=NA,xaxt="n")
abline(v=190,col="blue",lwd=2,lty=2)
pop_file_joined <- ordered_file %>%
  merge(meta_data, by = "Sample_Name")

pop_file_cluser_info<-pop_file_joined%>%mutate(cluster_1_yes=case_when(V1 > 0.9 ~ 1, V1 <0.9 ~0))
pop_file_cluser_info%>%ggplot(aes(x=Continent,fill=as.factor(cluster_1_yes)))+geom_bar()+theme_classic()+
  guides(fill=guide_legend(title="Belongs to cluster 1"))
