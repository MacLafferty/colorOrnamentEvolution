#script to check out all that funky environmental spectral data

#load libraries
library(pavo)
library(ggplot2)

#if we want to output info for all data, leave this as true
#as we decide what environmental pieces to trim we can include more conditionals around that data
noTrim<-FALSE

#vector containing the species labels we need for sorting things later
#used for putting labels on things later
if (noTrim){
spoods<-c("HAAM","HAAM","HAAM","HAAM","HAAM",
          "HABO","HABO","HABO","HABO","HABO",
          "HACA","HACA","HACA","HACA","HACA",
          "HACO","HACO","HACO","HACO","HACO",
          "HACOE","HACOE","HACOE","HACOE","HACOE", 
          "HADE","HADE","HADE","HADE","HADE",
          "HADO","HADO","HADO","HADO","HADO",
          "HAEL","HAEL","HAEL","HAEL","HAEL",  
          "HAGE","HAGE","HAGE","HAGE","HAGE",
          "HAHA","HAHA","HAHA", 
          "HAHI","HAHI","HAHI","HAHI","HAHI",
          "HAME","HAME","HAME","HAME","HAME", 
          "HAOR","HAOR","HAOR","HAOR","HAOR",
          "HAPU","HAPU","HAPU","HAPU","HAPU",
          "HAPY","HAPY","HAPY","HAPY","HAPY",
          "HATE","HATE","HATE","HATE","HATE",
          "HATR","HATR","HATR","HATR","HATR",
          "HAUS","HAUS","HAUS","HAUS","HAUS", 
          "HAVI","HAVI","HAVI","HAVI","HAVI") 
} else {
  #this block of labels will account for the habitat flags we trim as outliers
  spoods<-c("HAAM","HAAM","HAAM","HAAM","HAAM",
            "HABO","HABO","HABO","HABO","HABO",
            "HACA","HACA","HACA","HACA","HACA",
            "HACO","HACO","HACO","HACO",
            "HACOE","HACOE","HACOE","HACOE","HACOE", 
            "HADE","HADE","HADE","HADE","HADE",
            "HADO","HADO","HADO","HADO",
            "HAEL","HAEL","HAEL","HAEL","HAEL",  
            "HAGE","HAGE","HAGE","HAGE",
            "HAHA","HAHA","HAHA", 
            "HAHI","HAHI","HAHI","HAHI","HAHI",
            "HAME","HAME","HAME","HAME", 
            "HAOR","HAOR","HAOR","HAOR",
            "HAPU","HAPU","HAPU","HAPU",
            "HAPY","HAPY","HAPY","HAPY",
            "HATE","HATE","HATE",
            "HATR","HATR","HATR","HATR",
            "HAUS","HAUS","HAUS","HAUS","HAUS", 
            "HAVI","HAVI","HAVI","HAVI") 
}
#vectors to store average/median values for the environments

northMeans <- vector()
southMeans <- vector()
northMedians <- vector()
southMedians <- vector()

#function that will:
#load spectrum, convert to photon flux, plot for inspection, and return rspec object
showEnv<-function(name){
  vizEnv<-getspec(where=getwd(),ext="txt",sep=",",lim=c(365,700),subdir = TRUE)
  vizEnv<-irrad2flux(vizEnv)
  plot(vizEnv,main=name)
  return(vizEnv)
}

#function that returns sidewelling reflectance
#takes a sidewelling photon flux measurement (spec1) and divide by downwelling (spec2)
illum2refl<-function(spec1,spec2){
  #sidewelling / downwelling
  reflectanceVals<-spec1[,2]/spec2[,2]
  #stick wavelength values back on
  reflectance<-cbind(spec1[,1],reflectanceVals)
  #convert back to rspec object
  reflectance<-as.rspec(reflectance)
  return(reflectance)
}

#assume we've set the directory first?

doFlag<-function(flagName){
  #go through each directional measurement and 
  setwd("downwelling")
  downName<-paste(flagName, "downwelling", sep="_")
  down<-showEnv(downName)
  setwd("../north")
  northName<-paste(flagName, "north", sep="_")
  north<-showEnv(northName)
  setwd("../south")
  southName<-paste(flagName, "south", sep="_")
  south<-showEnv(southName)
  setwd("../upwelling")
  upName<-paste(flagName,"upwelling",sep="_")
  up<-showEnv(upName)
  
  #do the reflectance calculations and get ready to display them
  northRefl<-illum2refl(north,down)
  northReflName<-paste(flagName,"north_Reflectance",sep="_")
  plot(northRefl,main=northReflName)
  southRefl<-illum2refl(south,down)
  southReflName<-paste(flagName,"south_Reflectance",sep="_")
  plot(southRefl,main=southReflName)
  
  #the <<- is intentional, dont screw it up
  northMeans<<-append(northMeans,mean(northRefl[,2]))
  print(northMeans)
  northMedians<<-append(northMedians,median(northRefl[,2]))
  southMeans<<-append(southMeans,mean(southRefl[,2]))
  southMedians<<-append(southMedians,median(southRefl[,2]))
  
}


#HAAM
setwd("/Users/davidmorris/Desktop/environment/HAAM/flags/flag91")
doFlag("HAAM_91")

setwd("/Users/davidmorris/Desktop/environment/HAAM/flags/flag96")
doFlag("HAAM_96")

setwd("/Users/davidmorris/Desktop/environment/HAAM/flags/flag97")
doFlag("HAAM_97")

setwd("/Users/davidmorris/Desktop/environment/HAAM/flags/flag99")
doFlag("HAAM_99")

setwd("/Users/davidmorris/Desktop/environment/HAAM/flags/flag100")
doFlag("HAAM_100")

#HABO
setwd("/Users/davidmorris/Desktop/environment/HABO/flags/flag20")
doFlag("HABO_29")

setwd("/Users/davidmorris/Desktop/environment/HABO/flags/flag65")
doFlag("HABO_65")

setwd("/Users/davidmorris/Desktop/environment/HABO/flags/flag70")
doFlag("HABO_70")

setwd("/Users/davidmorris/Desktop/environment/HABO/flags/flag70.2")
doFlag("HABO_70.2")

setwd("/Users/davidmorris/Desktop/environment/HABO/flags/flag71")
doFlag("HABO_71")

#HACA

setwd("/Users/davidmorris/Desktop/environment/HACA/flags/flag2")
doFlag("HACA_2")

setwd("/Users/davidmorris/Desktop/environment/HACA/flags/flag3")
doFlag("HACA_3")

setwd("/Users/davidmorris/Desktop/environment/HACA/flags/flag9")
doFlag("HACA_9")

setwd("/Users/davidmorris/Desktop/environment/HACA/flags/flag38")
doFlag("HACA_38")

setwd("/Users/davidmorris/Desktop/environment/HACA/flags/flag46")
doFlag("HACA_46")

#HACO
setwd("/Users/davidmorris/Desktop/environment/HACO/flags/flag4")
if (noTrim){
  doFlag("HACO_4")
}

setwd("/Users/davidmorris/Desktop/environment/HACO/flags/flag69")
doFlag("HACO_69")

setwd("/Users/davidmorris/Desktop/environment/HACO/flags/flag70")
doFlag("HACO_70")

setwd("/Users/davidmorris/Desktop/environment/HACO/flags/flag80")
doFlag("HACO_80")

setwd("/Users/davidmorris/Desktop/environment/HACO/flags/flag86")
doFlag("HACO_86")

#HACOE

setwd("/Users/davidmorris/Desktop/environment/HACOE/flags/flag7")
doFlag("HACOE_7")

setwd("/Users/davidmorris/Desktop/environment/HACOE/flags/flag45")
doFlag("HACOE_45")

setwd("/Users/davidmorris/Desktop/environment/HACOE/flags/flag66")
doFlag("HACOE_66") 

setwd("/Users/davidmorris/Desktop/environment/HACOE/flags/flag78")
doFlag("HACOE_78")

setwd("/Users/davidmorris/Desktop/environment/HACOE/flags/flag79")
doFlag("HACOE_79")

#HADE

setwd("/Users/davidmorris/Desktop/environment/HADE/flags/flag26")
doFlag("HADE_26")

setwd("/Users/davidmorris/Desktop/environment/HADE/flags/flag38")
doFlag("HADE_38")

setwd("/Users/davidmorris/Desktop/environment/HADE/flags/flag41")
doFlag("HADE_41")

setwd("/Users/davidmorris/Desktop/environment/HADE/flags/flag72")
doFlag("HADE_72")

setwd("/Users/davidmorris/Desktop/environment/HADE/flags/flag89")
doFlag("HADE_89")

#HADO

setwd("/Users/davidmorris/Desktop/environment/HADO/flags/flag1")
doFlag("HADO_1")

setwd("/Users/davidmorris/Desktop/environment/HADO/flags/flag2")
doFlag("HADO_2")

setwd("/Users/davidmorris/Desktop/environment/HADO/flags/flag3")
doFlag("HADO_3")

setwd("/Users/davidmorris/Desktop/environment/HADO/flags/flag4")
doFlag("HADO_4")

setwd("/Users/davidmorris/Desktop/environment/HADO/flags/flag5")
if (noTrim){
doFlag("HADO_5")
}

#HADOR

setwd("/Users/davidmorris/Desktop/environment/HADOR/flags/flag1")
#doFlag("HADOR_1")

setwd("/Users/davidmorris/Desktop/environment/HADOR/flags/flag13A")
#doFlag("HADOR_13A")

setwd("/Users/davidmorris/Desktop/environment/HADOR/flags/flag63A")
#doFlag("HADOR_63A")

setwd("/Users/davidmorris/Desktop/environment/HADOR/flags/flag64A")
#doFlag("HADOR_64A")

setwd("/Users/davidmorris/Desktop/environment/HADOR/flags/flag89")
#doFlag("HADOR_89")

#HAEL

setwd("/Users/davidmorris/Desktop/environment/HAEL/flags/flag66")
doFlag("HAEL_66")

setwd("/Users/davidmorris/Desktop/environment/HAEL/flags/flag75")

doFlag("HAEL_75")

setwd("/Users/davidmorris/Desktop/environment/HAEL/flags/flag80")
doFlag("HAEL_80")

setwd("/Users/davidmorris/Desktop/environment/HAEL/flags/flagX1")
doFlag("HAEL_X1")

setwd("/Users/davidmorris/Desktop/environment/HAEL/flags/flagX2")
doFlag("HAEL_X2")

#HAGE

setwd("/Users/davidmorris/Desktop/environment/HAGE/flags/flag1")
if (noTrim){
  doFlag("HAGE_1")
}

setwd("/Users/davidmorris/Desktop/environment/HAGE/flags/flag2")
doFlag("HAGE_2")

setwd("/Users/davidmorris/Desktop/environment/HAGE/flags/flag3")
doFlag("HAGE_3")

setwd("/Users/davidmorris/Desktop/environment/HAGE/flags/flag4")
doFlag("HAGE_4")

setwd("/Users/davidmorris/Desktop/environment/HAGE/flags/flag5")
doFlag("HAGE_5")

#HAHA
#sadly only have 3 of these, is this the only w/o 5?

setwd("/Users/davidmorris/Desktop/environment/HAHA/flags/flag5")
doFlag("HAHA_5")

setwd("/Users/davidmorris/Desktop/environment/HAHA/flags/flag9")
doFlag("HAHA_9")

setwd("/Users/davidmorris/Desktop/environment/HAHA/flags/flag501")
doFlag("HAHA_501")

#HAHI

setwd("/Users/davidmorris/Desktop/environment/HAHI/flags/flag105")
doFlag("HAHI_105")

setwd("/Users/davidmorris/Desktop/environment/HAHI/flags/flag107")
doFlag("HAHI_107")

setwd("/Users/davidmorris/Desktop/environment/HAHI/flags/flag108")
doFlag("HAHI_108")

setwd("/Users/davidmorris/Desktop/environment/HAHI/flags/flag321")
doFlag("HAHI_321")

setwd("/Users/davidmorris/Desktop/environment/HAHI/flags/flag322")
doFlag("HAHI_322")

#HAME

setwd("/Users/davidmorris/Desktop/environment/HAME/flags/flag13")
doFlag("HAME_13")

setwd("/Users/davidmorris/Desktop/environment/HAME/flags/flag38")
doFlag("HAME_38")

setwd("/Users/davidmorris/Desktop/environment/HAME/flags/flag63")
doFlag("HAME_63")

setwd("/Users/davidmorris/Desktop/environment/HAME/flags/flag64")
doFlag("HAME_64")

setwd("/Users/davidmorris/Desktop/environment/HAME/flags/flag87")
if (noTrim){
doFlag("HAME_87")
}


#HAOR


setwd("/Users/davidmorris/Desktop/environment/HAOR/flags/flag1")
doFlag("HAOR_1")

setwd("/Users/davidmorris/Desktop/environment/HAOR/flags/flag2")
doFlag("HAOR_2")

setwd("/Users/davidmorris/Desktop/environment/HAOR/flags/flag3")
doFlag("HAOR_3")

setwd("/Users/davidmorris/Desktop/environment/HAOR/flags/flag4")
if (noTrim){
  doFlag("HAOR_4")
  }

setwd("/Users/davidmorris/Desktop/environment/HAOR/flags/flag5")
doFlag("HAOR_5")

#HAPU

setwd("/Users/davidmorris/Desktop/environment/HAPU/flags/flag1")
doFlag("HAPU_1")

setwd("/Users/davidmorris/Desktop/environment/HAPU/flags/flag2")
if (noTrim){
  doFlag("HAPU_2")
  }

setwd("/Users/davidmorris/Desktop/environment/HAPU/flags/flag3")
doFlag("HAPU_3")

setwd("/Users/davidmorris/Desktop/environment/HAPU/flags/flag4")
doFlag("HAPU_4")

setwd("/Users/davidmorris/Desktop/environment/HAPU/flags/flag5")
doFlag("HAPU_5")

#HAPY

setwd("/Users/davidmorris/Desktop/environment/HAPY/flags/flag5")
doFlag("HAPY_5")

setwd("/Users/davidmorris/Desktop/environment/HAPY/flags/flag7")
doFlag("HAPY_7")

setwd("/Users/davidmorris/Desktop/environment/HAPY/flags/flag13")
doFlag("HAPY_13")

setwd("/Users/davidmorris/Desktop/environment/HAPY/flags/flag47")
doFlag("HAPY_47")

setwd("/Users/davidmorris/Desktop/environment/HAPY/flags/flag53")
if (noTrim){
  doFlag("HAPY_53")
  }

#HATE

setwd("/Users/davidmorris/Desktop/environment/HATE/flags/flag6")
doFlag("HATE_6")

setwd("/Users/davidmorris/Desktop/environment/HATE/flags/flag26")
doFlag("HATE_26")

setwd("/Users/davidmorris/Desktop/environment/HATE/flags/flag50")
if (noTrim){
  doFlag("HATE_50")
}
setwd("/Users/davidmorris/Desktop/environment/HATE/flags/flag66")
doFlag("HATE_66")

setwd("/Users/davidmorris/Desktop/environment/HATE/flags/flag72")
if (noTrim){
  doFlag("HATE_72")
}

#HATR

setwd("/Users/davidmorris/Desktop/environment/HATR/flags/flag45")
doFlag("HATR_45")

setwd("/Users/davidmorris/Desktop/environment/HATR/flags/flag57")
doFlag("HATR_57")

setwd("/Users/davidmorris/Desktop/environment/HATR/flags/flag59")
doFlag("HATR_59")

setwd("/Users/davidmorris/Desktop/environment/HATR/flags/flag69")
doFlag("HATR_69")

setwd("/Users/davidmorris/Desktop/environment/HATR/flags/flag75")
if (noTrim){
  doFlag("HATR_75")
  }

#HAUS

setwd("/Users/davidmorris/Desktop/environment/HAUS/flags/flag20")
doFlag("HAUS_20")

setwd("/Users/davidmorris/Desktop/environment/HAUS/flags/flag60")
doFlag("HAUS_60")

setwd("/Users/davidmorris/Desktop/environment/HAUS/flags/flagX1")
doFlag("HAUS_X1")

setwd("/Users/davidmorris/Desktop/environment/HAUS/flags/flagX2")
doFlag("HAUS_X2")

setwd("/Users/davidmorris/Desktop/environment/HAUS/flags/flagX3")
doFlag("HAUS_X3")

#HAVI
setwd("/Users/davidmorris/Desktop/environment/HAVI/flags/flag1")
doFlag("HAVI_1")

setwd("/Users/davidmorris/Desktop/environment/HAVI/flags/flag2")
if (noTrim){
doFlag("HAVI_2")
}

setwd("/Users/davidmorris/Desktop/environment/HAVI/flags/flag3")
doFlag("HAVI_3")

setwd("/Users/davidmorris/Desktop/environment/HAVI/flags/flag4")
doFlag("HAVI_4")

setwd("/Users/davidmorris/Desktop/environment/HAVI/flags/flag5")
doFlag("HAVI_5")

#need some north and south labels for our big data frames we're building
#equal to the number of individual habitat flags we've labeled
norths<-rep("N",length(spoods))
souths<-rep("S",length(spoods))

#now we staple our spood data together, do a little formatting, and visualize
northMeanViz<-as.data.frame(cbind(spoods,northMeans,norths))
northMeanViz$northMeans<-as.numeric(northMeanViz$northMeans)
names(northMeanViz)<-c("species","means","direction")
northMedViz<-as.data.frame(cbind(spoods,northMedians,norths))
northMedViz$northMedians<-as.numeric(northMedViz$northMedians)
names(northMedViz)<-c("species","meds","direction")
southMeanViz<-as.data.frame(cbind(spoods,southMeans,souths))
southMeanViz$southMeans<-as.numeric(southMeanViz$southMeans)
names(southMeanViz)<-c("species","means","direction")
southMedViz<-as.data.frame(cbind(spoods,southMedians,souths))
southMedViz$southMedians<-as.numeric(southMedViz$southMedians)
names(southMedViz)<-c("species","meds","direction")

totalMeanViz<-rbind(northMeanViz,southMeanViz)
totalMedViz<-rbind(northMedViz,southMedViz)



n_mean_plot<-ggplot(northMeanViz,aes(x=spoods,y=northMeans)) + geom_boxplot() + 
  stat_boxplot(coef=1.58)
n_mean_plot

s_mean_plot<-ggplot(southMeanViz,aes(x=spoods,y=southMeans)) + geom_boxplot() +
  stat_boxplot(coef=1.58)
s_mean_plot

n_med_plot<-ggplot(northMedViz,aes(x=spoods,y=northMedians)) + geom_boxplot() +
  stat_boxplot(coef = 1.58)
n_med_plot

s_med_plot<-ggplot(southMedViz,aes(x=spoods,y=southMedians)) + geom_boxplot() +
  stat_boxplot(coef=1.58)
s_med_plot

#stick w/ north facing (less variance, similar to spood measures), avg values (more common for spectra)
#ended up cutting 2 HATR specific flags and substituted 5 signatus flags, as they co-occur
#trim uppermost for: HACO (1),HAGE (1), HAME (5), HAOR (4), HAPU (2), HATE (5),HATR (5), HAVI (2)
#trim lowermost for: HADO (5), HAPY (5), HATE (3)

#ANOVA, look at N & S means and medians

n_mean_test<-aov(northMeans ~ spoods, data=northMeanViz)

summary(n_mean_test)

N_mean_Tukey<-TukeyHSD(n_mean_test)

s_mean_test<-aov(southMeans ~ spoods, data=southMeanViz)

summary(s_mean_test)

n_med_test<-aov(northMedians ~ spoods, data=northMedViz)

summary(n_med_test)

s_med_test<-aov(southMedians ~ spoods, data=southMedViz)

summary(s_med_test)

#combined two factor anovas for median and mean
mean_aov<- aov(means ~ species + direction + species*direction, data = totalMeanViz)
summary(mean_aov)
med_aov <- aov(meds ~ species + direction + species*direction, data = totalMedViz)
summary(med_aov)

#note the lack of interaction effect before trimming
#afterwards doesn't matter

northMeanViz$spoods

trimmed_north_mean <- northMeanViz[-c(69,70),]
trimmed_mean_test<-aov(northMeans ~ spoods, data=trimmed_north_mean)
summary(trimmed_mean_test)
trimmed_Tukey<-TukeyHSD(trimmed_mean_test)


