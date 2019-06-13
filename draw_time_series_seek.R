suppressPackageStartupMessages(library(argparse))
suppressPackageStartupMessages(library(ggplot2))


parser <- ArgumentParser()
parser$add_argument("-i", help = "input otufile or abundance to draw time seek")
parser$add_argument("-o", help = "outfile of lines plot name",default="lines_time")
parser$add_argument("-s", help = "outfile of smooth name",default="smooth_name")
args <- parser$parse_args()

infile <- file.path(args$i)
outfile1<- file.path(args$o)
outfile2<- file.path(args$s)

dgs<-read.csv(infile,sep = '\t',row.names=1,check.names = FALSE)

pdf(paste(outfile1,"pdf",sep = "."),width = as.double(10), height = as.double(8))
ggplot(dgs, aes(x = period, y = value)) +
  geom_line(aes(color = person), size = 1) +
  #scale_color_manual(values = c("#00AFBB", "#E7B800")) +
  theme_minimal()
dev.off()


pdf(paste(outfile2,"pdf",sep = "."),width = as.double(10), height = as.double(8))
ggplot(dgs, aes(x = period, y = value)) + 
  geom_point( size = 1) +
  #scale_color_manual(values = c("#00AFBB", "#E7B800")) +
  geom_smooth(method=lm,  linetype="dashed",)+
  theme_minimal()
dev.off()