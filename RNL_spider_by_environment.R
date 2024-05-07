#generate receptor noise limited values

#take 3 of hyperspectral analysis
#load libraries
library(pavo)

#move to directory where everything will be sorted
#base_path<-"/Users/davidmorris/Desktop/HSC_testing/"
base_path<-"/Volumes/Wario/spiders/"
#new path to flag info; having the two split out makes grabbing everything easier for other analyses
env_path<-"/Volumes/Wario/environment/"
setwd(base_path)

#get spider visual system sorted at the get-go
#should have 3 separate files, one for each photoreceptor absorption curve
setwd("./1_hapy_visual")
#only need to load from 365 up since that's as low as the hyperspectral camera measures
HAPY_sens_raw <- getspec(where=getwd(),ext="csv",sep=",",lim=c(365,699))
HAPY_unordered <- procspec(HAPY_sens_raw,fixneg="zero")
#have to reorder the columns; read in order but need to be short, medium, long receptors
HAPY_sens <- cbind(HAPY_unordered[1],HAPY_unordered[4],HAPY_unordered[2],HAPY_unordered[3])
HAPY_sens<- as.rspec(HAPY_sens)
names(HAPY_sens) <- c("wl","s","m","l")
#ratios in fovea from Zurek paper
HAPY_ratio <- c(1,2,4)
setwd("..")

#we should also set up other visual systems
#wasp Philanthus Triangularum
maxes=c(344,444,524)
wasp_sens=as.rspec(sensmodel(maxes))
#not smart enough to automatically leave off the wls we don't use so we'll trim ourselves
wasp_sens<-wasp_sens[66:400,]
wasp_ratio<-c(1,1,6)

#grab directories to keep track of the different species
#leave off visual system directory at the beginning
species=list.dirs(recursive = FALSE)
species=species[-1]
species2=list.dirs(recursive = FALSE)
species2=species2[-1]
species_num=length(species)

#change the indices for species to work through the list without doing the whole thing
#index 1 is americanus, 14 is oregonensis, 20 is virgilatus
for (sp in species[8]){
  setwd(sp)
  #maybe have some sort of switch b/w back and front?
  setwd("./back")
  spiders=list.dirs(recursive= FALSE)
  for (spider in spiders[1]){
    setwd(spider)
    spider_path=getwd()
    #not sure why t
    raw_spectra=getspec(where=getwd(),ext = "txt", lim=c(365,699))
    spectra=procspec(raw_spectra, opt="smooth", fixneg="zero",span=.05)
    num_spectra=length(spectra)
    #keep track of index to pair
    for (sp2 in species2){
      setwd(env_path)
      setwd(sp2)
      setwd("./flags")
      flags=list.dirs(recursive=FALSE)
      for (flag in flags){
        s_values=data.frame()
        #made it to environmental data
        setwd(flag)
        print("double check where we got a break last time")
        print(getwd())
        #now we need to grab environmental spectra
        #first grab downwelling measurement for illuminant
        setwd("./downwelling")
        #spider measures stop at 699, so we're gonna cut these off there too
        pre_flux=getspec(where=getwd(),ext="txt",lim=c(365,699))
        flux=irrad2flux(pre_flux)
        illuminant=procspec(flux,opt="smooth",fixneg="zero",span=.05)
        
        #we've decided to use north only given the statistically sign. diff. b/w the directions
        #north has less variance
        setwd("../north")
        pre_flux=getspec(where=getwd(),ext="txt",lim=c(365,699))
        flux=irrad2flux(pre_flux)
        environ=procspec(flux,opt="smooth",fixneg="zero",span=.05)
        #need to get reflectance value to compare to the spider spectra
        #divide our sidewelling measurement by the downwelling "illuminant"
        #skip wl columns, reassign
        environ[2]<-environ[2]/illuminant[2]
        
        #now that everything is loaded into memory we'll iterate over our pixels
        for (spectrum in 2:num_spectra){
          #now do the modeling
          #make a new dataset containing just wl, one spider spectrum, and the environmental spectrum
          data=cbind(spectra[1],spectra[spectrum],environ[2])
          data=as.rspec(data)
          #maybe figure out luminance stuff here using just medium (green)
          quantum_catches=vismodel(data, visual=wasp_sens,achromatic = wasp_sens[,3], illum=illuminant[,2],qcatch= "Qi",relative = FALSE,scale=1)
          
          #fetchner transform, but we won't do VK because of color constancy uncertainty
          fetchner=log(quantum_catches)
          #crunch the euclidean distances next; need to mess w/ noise later maybe
          deltaS=coldist(modeldata = fetchner,n=wasp_ratio,weber=.05,achromatic = TRUE)
          s_values=rbind(s_values,deltaS)
        }
        print("time to figure out files")
        flag_path=getwd()
        #let's go ahead and crunch the some summary stats for each
        spood_avg<-as.character(mean(s_values$dS))
        spood_median<-as.character(median(s_values$dS))
        spood_max<-as.character(max(s_values$dS))
        #this one is a little tricky; compares all dS values to the lower bound of upper quantile
        #pulls the upper quantile values and averages them to give a better idea of ornament discriminability
        spood_upper_quantile<-mean(s_values$dS[s_values$dS>quantile(s_values$dS)[4]])
        
        #do the same values but for luminance
        lum_avg<-as.character(mean(s_values$dL))
        lum_median<-as.character(median(s_values$dL))
        lum_max<-as.character(max(s_values$dL))
        lum_upper_quantile<-mean(s_values$dL[s_values$dL>quantile(s_values$dL)[4]])
        
        #work out file names
        name_base<-paste(spider,"_",s_values[1,2],sep="")
        print("file name:")
        print(name_base)
        name1<-paste(name_base,"_pred_stats_v2.csv",sep="")
        name2<-paste(name_base,"_pred_deltaS_v2.csv",sep="")
        #write summary stuff to file
        #want to drop it in with the spiders though so change paths...again
        setwd(spider_path)
        print("directory for file output")
        print(getwd())
        sink(name1)                                  
        cat(spood_avg)
        cat("\n")
        cat(spood_median)
        cat("\n")
        cat(spood_max)
        cat("\n")
        cat(spood_upper_quantile)
        cat("\n")
        cat(lum_avg)
        cat("\n")
        cat(lum_median)
        cat("\n")
        cat(lum_max)
        cat("\n")
        cat(lum_upper_quantile)
        cat("\n")
        sink()
        #write the dataframe w/ individual values as well
        write.csv(s_values,name2)
        print("file output complete")
        setwd(flag_path)
        setwd("../..")
      }
    }
    #now that we've done all the file management we need to go back to where our spoods are at
    setwd(spider_path)
    setwd("..")
  }
  setwd("../..")
}