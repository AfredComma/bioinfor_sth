suppressPackageStartupMessages(library(argparse))
suppressPackageStartupMessages(library(vegan))

parser <- ArgumentParser()
parser$add_argument("-i", help = "input otufile or abundance to calculate shannon")
args <- parser$parse_args()

infile <- file.path(args$i)

ddf<-read.csv(infile,sep = '\t',row.names=1)
df<-t(ddf)
#es_data<-estimateR(df)
shannon<-diversity(df,index="shannon")

simpson<-diversity(df,index="simpson")
es_data<-rbind(shannon,simpson)
outfile<-sub("gene_relative_abun","alpha",infile)
write.csv(es_data,file = outfile)

#however, I use the spceies dataframe instead to calculate the simpson value
#simpson<-diversity(t(a),index="simpson")

#In the IGC paper, we can see the evaluation of alpha diversity by chao2 index.
#So we use the same method, with fossil package in R
#library(fossil)
#df<-read.csv("gene_count.tsv", sep = '\t', row.names = 1)
#ss<-spp.est(df, rand = 10, abund = FALSE, counter = FALSE, max.est = 'all')
#the method above is still iffy, use chao1 function by species abundance instead
#apply(dat,2,chao1)
