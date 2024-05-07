#get average spider values for each group we want to use for comparative methods

library(tidyverse)

#function which will load up a dataframe for our eventual phylo ttests
#lets us specify our viewpoint, visual system, file path,
choose.your.character<-function(viewpoint,vizsystem,thepath){
  if (vizsystem =="consp"){
    pattern_string<-"north_consp_stats_v2.csv"
    output_pattern<-"^(HA\\w+)_(\\w+)_(front|back)_HA\\w+_(.+)_(.+)_(north|upwelling)_consp_stats_v2.csv"
  } else if (vizsystem =="pred"){
    pattern_string<-"north_pred_stats_v2.csv"
    output_pattern<-"^(HA\\w+)_(\\w+)_(front|back)_HA\\w+_(.+)_(.+)_(north|upwelling)_pred_stats_v2.csv"
  } else if (vizsystem =="wasp"){
    pattern_string<-"upwelling_wasp_stats_v2.csv"
    output_pattern<-"^(HA\\w+)_(\\w+)_(front|back)_HA\\w+_(.+)_(.+)_(north|upwelling)_wasp_stats_v2.csv"
  } else{
    print("you've made a terrible mistake")
  }
  super_frame<-data.frame()
  
  setwd(thepath)
  #get list of directories
  dir_names<-list.dirs(recursive=FALSE)
  #need to drop the visual system directory stored with the spider files
  dir_names<-dir_names[-1]
  num_dirs<-length(dir_names)
  #for each of our spider species directories
  for (directory in dir_names){
    print("directory name")
    print(directory)
    #move into the directory & then into the appropriate facing directory
    setwd(directory)
    setwd(viewpoint)
    spider_names <- list.files()
    #for each individual spider directory
    for (name in spider_names){
      setwd(name)
      #get files matching our parameters
      model_output_files<-list.files(path=".",pattern=pattern_string)
      #regex those dudes, add to data frame
      metadata<-str_match(model_output_files,output_pattern)
      #grab all the data from the files associated w/ the individual spider
      df = do.call(cbind, lapply(model_output_files, function(x) read.csv(x, header = FALSE,stringsAsFactors = FALSE)))
      #stick the values and metadata together
      print(name)
      file_data<-cbind(metadata,t(df))
      #add a column for sex of individual now, modify individuals later?
      file_data<-cbind(file_data,rep("M",length(file_data[,1])))
      super_frame<-rbind(super_frame,file_data)
      #go up a directory
      setwd("..")
    }
    #go up two directories, back to spider species
    setwd("../..")
  }
  #now that superframe is filled we do some cleanup and relabeling
  colnames(super_frame)<-c("full","spp","id","facing","site","flag","spec","mean_disc","med_disc","max_disc",
                           "upper_disc","mean_lum","med_lum","max_lum","upper_lum","sex")
  
  #data type everything appropriately
  #here are our factors; our sites need new levels as well
  super_frame$spp<-as.factor(super_frame$spp)
  super_frame$id<-as.factor(super_frame$id)
  super_frame$site<-as.factor(super_frame$site)
  new_labels<-c("TFP1","TFP2","BRG1","BRG2","BRG3")
  levels(super_frame$site) <- c(levels(super_frame$site), new_labels)
  #need actual numbers for discrimination values
  super_frame$mean_disc<-as.numeric(super_frame$mean_disc)
  super_frame$med_disc<-as.numeric(super_frame$med_disc)
  super_frame$max_disc<-as.numeric(super_frame$max_disc)
  super_frame$upper_disc<-as.numeric(super_frame$upper_disc)
  #luminance next
  super_frame$mean_lum<-as.numeric(super_frame$mean_lum)
  super_frame$med_lum<-as.numeric(super_frame$med_lum)
  super_frame$max_lum<-as.numeric(super_frame$max_lum)
  super_frame$upper_lum<-as.numeric(super_frame$upper_lum)
  
  #last data cleaning step
  #we need to set up the sex factor so it properly sorts out female spiders
  female_IDs<-c(2679, 2683, 2725, 2735, !2735, 5431, 2692, 2709, #HAOR, but BC population?
                2436, 2429, 2444, 2417, 2441, 2410, #HAAM
                1071, 3459, 1117, 2426, 1125, 3444, 3854, 2656, 1096, 1120, 1088, 3564, #HAVI
                3446, 1127, 1115, 3431,
                3428, "3620not", 1194, 3672, 3666, 3434, 3676, "Nancy", #HADO
                "J133", 5422, "J6", 5080, "J89", #HACA
                "J199", "J209", "J82", "J295", 5095, 4505, #double check HACOE stuff
                3675, 3425, 3421, 3416, 3438, 3647, 3667, 3432, 3423, 3422, #HADO
                3607, 3394, 3385, 3384, 3389, 3393, #HAPU
                4625, 3972, 4643, 3880, 4571, #HAPY
                3463, 3460, #HAOR, double check
                991, 3625, 3623, 1644, 3624, 3584, 3577, 1644, 1019, 3585, 3693, 3578, #HAGE
                301, 4372, 840, 4378, 923, 656, #HAHI
                4829, "Eugenia", 4825, 4319, 4827, 4820, #HAME, check 38
                4307, 4310, 4303, "D2", #HAEL, double check
                1240, #HAHA
                4164, 3970, 4165, 4171, 3969, #HABO
                952, 959, 4496, 907, 915, 3631, 912, 921, 970, 964, 920, 4149, 4162, #HACO
                4228, #HAUS
                4008 # HADE
  )
  
  #check IDs against the list of females above, and switch their sex factor to 'F'
  super_frame$sex<-as.factor(replace(super_frame$sex,is.element(super_frame$id,female_IDs),"F"))
  return(super_frame)
}

#function to create subset dataframe where each species is only compared to home environment
own_env<-function(my_frame,spp_names,env_layout){
  own_data_frame<-data.frame()
  
  for (name in spp_names){
    #find appropriate site name index using sp name
    site_name<-env_layout[which(spp_names==name)]
    #subset by species name and associated site
    temp_frame=my_frame[which(my_frame$spp == name & my_frame$site == site_name),]
    #add to data frame
    own_data_frame<-as.data.frame(rbind(own_data_frame,temp_frame))
  }
  return(own_data_frame)
}

#compare species x environment model output
#sex = M, F, or B; environ = "own" or "all"
#sum_stat = a string combining (mean, med, max, or upper) + (_disc or _lum)
#e.g. "mean_disc" , "med_lum", etc.
#plot title to keep the resulting figures straight
env_compare<-function(parse_frame,sex,sum_stat,plot_title){
  #select the appropriate data frame based on sex; get species names for later
  if(sex == "M"){
    my_frame<-parse_frame[parse_frame$sex == "M",]
    spp_names<-levels(my_frame$spp)
  } else if (sex == "F"){
    my_frame<-parse_frame[parse_frame$sex == "F",]
    #we need to drop species where we don't have female representation
    spp_names<-levels(my_frame$spp)[-c(8,17,18,19)]
  } else {
    print("you've made a terrible mistake")
  }
  #we can reference an existing column using the string name of column w/ double brackets
  my_frame$value<-my_frame[[sum_stat]]

  #here's our environmental order for each species
  env_layout <- c("VIV","TFP","EOA","SNP","TFP2","PSW","WRC","BRG3","FIA","MBR","MDR","SNW","PYC","BRG",
                  "FWO","QC","GLT","BRG2","OCD","IKP","OCR")
  agg_frame<-my_frame %>% group_by(site,spp,id) %>% dplyr::summarise(value=mean(value,na.rm=TRUE))
  
  #own env
  own_agg_frame<-own_env(agg_frame,spp_names,env_layout)
  #graph
  
  own_graph<-ggplot(own_agg_frame,aes(x=spp,y=value)) + geom_boxplot() + 
    stat_boxplot(coef=1.58) + ggtitle(plot_title)
  plot(own_graph)

  return(agg_frame)
}

consp_front_frame<-choose.your.character("./front","consp","/Volumes/Wario/spiders/")
consp_back_frame<-choose.your.character("./back","consp","/Volumes/Wario/spiders/")
pred_front_frame<-choose.your.character("./front","pred","/Volumes/Wario/spiders/")
pred_back_frame<-choose.your.character("./back","pred","/Volumes/Wario/spiders/")

#extract the species level stuff we need
m_front_consp<-env_compare(consp_front_frame,"M","upper_disc","Male, Front, Consp.")
mfc<-m_front_consp %>% group_by(spp) %>% dplyr::summarise(value=mean(value))
mfct<-mfc[-c(8,17,18,19),]

f_front_consp<-env_compare(consp_front_frame,"F","upper_disc","Female, Front, Consp.")
ffc<- f_front_consp %>% group_by(spp) %>% dplyr::summarise(value=mean(value))

m_front_pred<-env_compare(pred_front_frame,"M","upper_disc","Male, Front, Pred.")
mfp<-m_front_pred %>% group_by(spp) %>% dplyr::summarise(value=mean(value))
mfpt<-mfp[-c(8,17,18,19),]

f_front_pred<-env_compare(pred_front_frame,"F","upper_disc","Female, Front, Pred.")
ffp<- f_front_pred %>% group_by(spp) %>% dplyr::summarise(value=mean(value))

m_back_consp<-env_compare(consp_back_frame,"M","upper_disc","Male, Back, Consp.")
mbc<- m_back_consp %>% group_by(spp) %>% dplyr::summarise(value=mean(value))
mbct<-mbc[-c(8,17,18,19),]
  
f_back_consp<-env_compare(consp_back_frame,"F","upper_disc","Female, Back, Consp.")
fbc<- f_back_consp %>% group_by(spp) %>% dplyr::summarise(value=mean(value))

m_back_pred<-env_compare(pred_back_frame,"M","upper_disc","Male, Back, Pred.")
mbp<- m_back_pred %>% group_by(spp) %>% dplyr::summarise(value=mean(value))
mbp<-mbp[-c(8,17,18,19),]

f_back_pred<-env_compare(pred_back_frame,"F","upper_disc","Female, Back, Pred.")
fbp<- f_back_pred %>% group_by(spp) %>% dplyr::summarise(value=mean(value))



m_own_upperdisc<-env_compare(consp_front_frame,"M","upper_disc","Male (mean)")
m_spp<-m_own_upperdisc %>% group_by(spp) %>% dplyr::summarise(value=mean(value))
m_spp_trim<-m_spp[-c(8,17,18,19),]

f_own_upperdisc<-env_compare(consp_front_frame,"F","upper_disc","Female (mean)")
f_spp<-f_own_upperdisc %>% group_by(spp) %>% dplyr::summarise(value=mean(value))


#flag relabel stuff we'll probably get rid of
#next we need to split up our multi-species environmental flags to prevent replication
#flag labels for each environment
trammel2_flags<-c("flag7","flag45","flag66","flag78","flag79")
bensen2_flags<-c("flag6","flag26","flag66")
bensen3_flags<-c("flag1","flag13A","flag63A","flag64A","flag89")
#check for target flags in our habitats that need splitting
tfp2<-is.element(super_frame$flag, trammel2_flags) & is.element(super_frame$site,"TFP")
brg2<-is.element(super_frame$flag,bensen2_flags) & is.element(super_frame$site,"BRG")
brg3<-is.element(super_frame$flag,bensen3_flags) & is.element(super_frame$site,"BRG")
#swap labels for each habitat
super_frame$site<-as.factor(replace(super_frame$site,tfp2,"TFP2"))
super_frame$site<-as.factor(replace(super_frame$site,brg2,"BRG2"))
super_frame$site<-as.factor(replace(super_frame$site,brg3,"BRG3"))
