#testing out phylogenetics stuff in R from Liam and Luke's book

#here's the libraries we'll need
library(ape)
library(phangorn)
library(phytools)
library(geiger)

#example of a simple newick tree we'll read in
text.string<-"(((((Rboin,Iguana),((((Cow,Whale),Pig),Bat),
  (Lemur,Human))),Coelacanth),Goldfish),Shark);"
#build a tree
vert.tree<-read.tree(text=text.string)
#check it out
plot(vert.tree,no.margin=TRUE)

#now let's try it with data we care about
#read in wayne's stuff from nexus file
spood_trees<-read.nexus(file="Leduc-Robert&Maddison_Habronattus-Trees.nex")

#this gives us like 1k trees, how to summarize?
#if we double bracket it subsets one of the trees as a phylo object instead of multiphylo
#so let's grab our first ML tree from the whole set of trees
spood_tree<-spood_trees[[1]]

#labels are numbers, didn't interpret from the nexus I guess
#here's the labels
spood_names<-c("Evarcha_proszynskii", "Pellenes_canadensis", "conjunctus", "hirsutus", "signatus",
               "ustulatus", "geronimoi", "aestus", "tarsalis", "ophrys", "americanus", "sansoni",
               "altanus", "decorus", "chamela", "zapotecanus", "cambridgei", "icenoglei",
               "oregonensis", "hallani", "luminosus", "pugillis", "roberti",  "calcaratus_maddisoni",
               "jucundus", "aztecanus", "clypeatus", "gilaensis",  "mexicanus", "empyrus",
               "pyrrithrix", "virgulatus", "festus", "borealis", "captiosus")
spood_tree$tip.label<-spood_names
#got the indices of all the species we want, let's put them in an array
spood_spots<-c(3,4,5,6,7,11,13,14,19,20,22,24,29,31,32,34)
#grab just what we want
our_names<-spood_names[spood_spots]
#this will include just our 16 species we want
trimmed_tree<-keep.tip(spood_tree,our_names)
plotTree(trimmed_tree)

#next up we need to figure out how to summarize, organize, and store our model output
#then


