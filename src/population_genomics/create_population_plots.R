library(data.table)
library(tidyverse)


pop_file <- fread("/Users/maryam/Downloads/assignment4.11.Q")
individuals <- fread("/Users/maryam/Downloads/assignment4_indivs.txt")
meta_data<- readxl::read_excel("/Users/maryam/Downloads/assignment4.xlsx")
# subset 523 rows to match the number of rows in the individuals file
pop_file <- pop_file[1:523,]
# create a column with individual names
pop_file$Sample_Name <- individuals$Cuniculi_A

pop_file_reformatted <- pmax(pop_file,0.9)
pop_file_reformatted_joined <- pop_file_reformatted %>%
  merge(meta_data, by = "Sample_Name")
