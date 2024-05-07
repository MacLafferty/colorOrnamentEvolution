library(pavo)
library(stringr)
library(ggfortify)

#choose just one spider directory for now maybe?
#HAAM should have some interesting colors
setwd("/Users/davidmorris/Desktop/environment/HAAM/flags/")

##Importing spec data
#this doesn't grab the summary file but I don't think we care
#stop at 699 b/c we can't interpolate 700nm w/o values on the other side
newSpiders_raw<-getspec(where=getwd(),ext="txt",lim=c(370,699),subdir = TRUE)
##Removing negative values and smoothing
newSpiders<-procspec(newSpiders_raw,opt="smooth",fixneg="zero",span=0.05)

##Extracting factors from variable names
#gonna skip this stuff for now
perfectPattern<-"^(\\w+)_(\\d+)_(\\w+)_Pixel_(\\d+,\\d+)"
factors<-str_match(names(newSpiders),perfectPattern)
#first row shows N/As, drop them
#number of spectra is still good w/ test individual at 755
factors<-factors[-1,]
colnames(factors) <- c("full","sp","ind", "facing", "pixel")


##Binning for PCA; for some reason this defaults to 17nm bins
#not sure why the default
spec.bin<-procspec(newSpiders, opt="bin")

#why did we transpose here before?
spec.bin <- t(spec.bin)
#label w/ nms and drop from the main matrix
colnames(spec.bin) <- spec.bin[1, ]
spec.bin <- spec.bin[-1, ]
##PCA
pca1 <- prcomp(spec.bin, scale = TRUE)
summary(pca1) ##PC loadings
#need to do this specifically on the prcomp output
autoplot(pca1)

##EXtract PC1, PC2, PC3
PCs<-as.data.frame(pca1$x[,1:3])
colnames(PCs)<-c("PC1", "PC2", "PC3")

#indices 6-8 are the PCs
spood_data<-cbind(factors, PCs)




rep1 <- newdata[ which(newdata$repl=='t1'),]
rep2 <- newdata[ which(newdata$repl=='t2'),]
plot(rep1$PC1, rep2$PC1)






colr <- spec2rgb(aveSpiders)
wls <- as.numeric(colnames(spec.bin))
sel <- rank(pca1$x[, 1])
sel <- match(names(sort(sel)), names(aveSpiders))
par(mfrow = c(1,2), mar = c(2, 4, 2, 2), oma = c(2, 0, 0, 0))
plot(pca1$r[,1] ~ wls, type = 'l', ylab = "PC1 loading")
abline(h = 0, lty = 2)
plot(aveSpiders, select = sel, type = 's', col = spec2rgb(aveSpiders))
mtext("Wavelength (nm)", side = 1, outer = TRUE, line = 1)
