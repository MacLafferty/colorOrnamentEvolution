library(pavo)
library(stringr)
library(ggfortify)

#choose just one spider directory for now maybe?
#HAAM should have some interesting colors
setwd("/Users/davidmorris/Desktop/environment/")

##Importing spec data
#this doesn't grab the summary file but I don't think we care
#stop at 699 b/c we can't interpolate 700nm w/o values on the other side
flags_raw<-getspec(where=getwd(),ext="txt",lim=c(370,699),subdir = TRUE)
##Removing negative values and smoothing
flags<-procspec(flags_raw,opt="smooth",fixneg="zero",span=0.05)

##Extracting factors from variable names
#gonna skip this stuff for now
perfectPattern<-"^(\\w+)_(\\w+)_(\\w+)_(\\w+)"
factors<-str_match(names(flags),perfectPattern)
#first row shows N/As, drop them
#number of spectra is still good w/ test individual at 755
factors<-factors[-1,]
colnames(factors) <- c("full","sp","site", "number", "direction")


##Binning for PCA; for some reason this defaults to 17nm bins
#not sure why the default
spec.bin<-procspec(flags, opt="bin")

#transpose so each row is associated with a flag
spec.bin <- t(spec.bin)

wl_bins<-spec.bin[1,]

trimmed_bins<-spec.bin[-1,]

new_labels<-c(c("full","sp","site", "number", "direction"),wl_bins)

#let's go ahead and stick our factors together with bins
#helps with labeling later
data<-as.data.frame(cbind(factors,trimmed_bins))

colnames(data)<-new_labels

#at this point all our columns are storing character data so we need to rework this stuff
#make a variable to account for matrix of changing size due to bins
num_cols<-length(data[1,])

data[,1:5] <- lapply(data[,1:5],as.factor)
data[,6:num_cols] <- lapply(data[,6:num_cols],as.numeric)

##PCA
pca1 <- prcomp(data[,6:num_cols], scale = TRUE)
summary(pca1) ##PC loadings
#need to do this specifically on the prcomp output
autoplot(pca1, data=data, colour = "sp" , shape = "sp") +
  scale_shape_manual(values=c(1:19))

#we're gonna want good x axis labels corresponding to nm wavelength bins
plot_labels<-rownames(pca1$rotation)

#switch columns for different loadings
#figure out how to change the axis ticks to the WL bin sizes
plot(pca1$rotation[,1],main="PC1",xlab="WL Bins",ylab="variance")
plot(pca1$rotation[,2],main="PC2",xlab="WL Bins",ylab="variance")

