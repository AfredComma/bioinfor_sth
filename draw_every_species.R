setwd("D:/BaiduNetdiskDownload/")
df <- read.csv("Species_merge_abundance.tsv",sep = '\t',row.names = 1,check.names = FALSE)

df2<-as.data.frame(t(df))
dfmap<-read.csv("merge_stages_map.tsv",sep = '\t')
dfmap$time<-sapply(dfmap$Types,FUN = function(x) strsplit(as.vector(x),'_')[[1]][1])
dfmap$cl<-sapply(dfmap$Types,FUN = function(x) strsplit(as.vector(x),'_')[[1]][2])
rownames(dfmap)<-dfmap$Sample

rr = colnames(df2)
for (i in seq(ncol(df))) {
  a = rr[i]
  b = gsub(' ','_',a)
  b = gsub('/','_',b)
  c = dfmap
  d <-cbind(c,df2[rownames(c),][,i])
  colnames(d)<-c("Sample","types","time","cl","value")
  d$time<-factor(d$time , levels=c("4", "8", "12", "16","20"))
  png(filename = paste0(b,'.png'),width = 900,height = 700)
  boxplot(value~time*cl,data = d,col=c("slateblue1" , "tomato"),
          boxwex=0.4 , ylab="Relative abundance")
  for(i in seq(0.5 , 20 , 5)){ 
    abline(v=i,lty=1, col="grey")
  }
  dev.off()
}
