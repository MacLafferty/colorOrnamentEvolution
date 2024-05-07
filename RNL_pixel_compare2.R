#script for building pixel-by-pixel comparisons of environments in DF
#other libraries needed are loaded from below
source("/Users/davidmorris/Biology/TechnicolorDreamcoat/pxp_functions.R")
library(ade4)

#here's file paths to where spider and environmental spectra are stored
#spood_path<-"/Users/davidmorris/Desktop/Habro_spectra/"
spood_path<-"/Volumes/Wario/spiders/"
#env_path<-"/Users/davidmorris/Desktop/Habro_env_trim/"
env_path<-"/Volumes/Wario/environment/"

#run grab_data to build our data frames containing the information we need
consp_front_frame<-grab_data("front","consp")
consp_back_frame<-grab_data("back","consp")

pred_front_frame<-grab_data("front","pred")
pred_back_frame<-grab_data("back","pred")

#generate output for analyses over in our comparative script
m_consp_front<-spp_avgs(consp_front_frame,"M","Male x Conspecific")
f_consp_front<-spp_avgs(consp_front_frame,"F","Female x Conspecific")

m_consp_back<-spp_avgs(consp_back_frame,"M","Male x Conspecific (back)")
f_consp_back<-spp_avgs(consp_back_frame,"F","Female x Conspecific (back)")

m_pred_front<-spp_avgs(pred_front_frame,"M","Male x pred")
f_pred_front<-spp_avgs(pred_front_frame,"F","Female x pred")

m_pred_back<-spp_avgs(pred_back_frame,"M","Male x pred (back)")
f_pred_back<-spp_avgs(pred_back_frame,"F","Female x pred (back)")


#no female HADOR,HASP,HATE,HATR


