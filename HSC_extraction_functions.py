#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:12:04 2022

@author: davidmorris
"""

#manage libraries, etc.
import os

from spectral import *

import spectral.io.envi as envi

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from math import sqrt

#make a list of the wavelength sensitivities of the different camera band
#the ENVI header files don't properly supply this info so we'll just do it ourselves ¯\_(ツ)_/¯
BandNMs=[365,366,367,368,369,370,371,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,405,406,407,408,409,410,411,413,414,415,416,418,419,420,421,423,424,425,427,428,430,431,432,434,435,437,438,440,442,443,445,446,448,450,451,453,455,457,459,460,462,464,466,468,470,472,474,476,478,481,483,485,487,490,492,494,497,499,502,505,507,510,513,516,518,521,524,527,531,534,537,540,544,547,551,554,558,562,566,570,574,578,583,587,592,597,601,607,612,617,623,628,634,640,646,653,660,667,674,682,690,699,707,716,726,735,746,757,768,780,793,807,822,837,854,872,892,914,938,965,996,1000]

#quick and easy function to take a matrix you want to display as a heat map
#useful for evaluating the initial images, or looking at which pixels you've extracted from a spider
#heatMatrix=matrix you want to visual via heatmap
#title=label used for graphical output
def displayHeat(HeatMatrix,Title):
    ax1 = plt.axes()
    sns.heatmap(HeatMatrix,ax=ax1)
    ax1.set_title(Title)
    plt.show()

#calculates brightness for each pixel by combining measurements across specified range of camera bands
#HSC_img = envi image object from spectral package
#returns pixel brightness in numpy matrix
def image_illumination(HSCImg,MinBand=0,MaxBand=140):
    Rows=HSCImg.nrows
    Cols=HSCImg.ncols
    HSCImgMatrix=np.zeros(shape=(Rows,Cols))
    for i in range(0,Rows):
        for j in range(0,Cols):
            #grab pixel at row and column
            Pixel = HSCImg[i,j]
            #default values include UV but exclude the infrared
            Pixel = Pixel[MinBand:MaxBand]
            #sum up the band values to get overall illumination
            Illumination = sum(Pixel)
            #save to appropriate pixel
            HSCImgMatrix[i][j] = Illumination
    return HSCImgMatrix

#calculates contrast between light and dark background subject images; can also display heatmaps of images
#lightImgName= string specifying name of image with white background, file extensions added automatically
#darkImgName= same as above, but for dark image
#outputName= name used to label graphical output for image contrast
#returns spectral image object showing contrast between backgrouns
def contrast_image(LightImgName,DarkImgName,OutputName,ScalingFactor=1.3,Graphing=True):
    #read in the images we're gonna compare
    LightImg=envi.open(LightImgName+".hdr",LightImgName+".cue")
    DarkImg=envi.open(DarkImgName+".hdr",DarkImgName+".cue")
    
    #use our image_illumination function to grab brightness for each pixel of images
    LightIllum=image_illumination(LightImg)
    DarkIllum=image_illumination(DarkImg)
    
    #subtract the dark from the light; scaling factor on light ensures we've got a nice big gap
    DiffIllum=(LightIllum*ScalingFactor)-(DarkIllum*1.0)
    
    #now that we have all our matrices we can look at them
    if Graphing:
        displayHeat(LightIllum, OutputName+"_light")
        displayHeat(DarkIllum, OutputName+"_dark")
        displayHeat(DiffIllum, OutputName+"_contrast")
    
    return DiffIllum

#Extracts a threshold value for what might be considered "subject" from a contrasted image pair
#bins brightness into a histogram and hill climbs to find where the lower mode (subject) ends
#contrastImg= spectral image file generated via contrast_image
#conservative= how picky we want to be when assigning our threshold; false selects and extra histogram bin
#returns floating point value
def contrast_threshold(ContrastImg,Conservative=True):
    #use numpy histogram function to bin our values
    #bin number needs to be high enough to see bimodal distribution (clear subject and background)
    #but also low enough we don't create too jagged a distribution
    #12 works well for our spider testing
    A=np.histogram(ContrastImg,bins=12)
    
    #next we want to iterate through the counts for each histogram bin
    #we don't want to include indeterminate values in the middle, so we look for a low point to use as a cutoff
    #values below that threshold are definitely spider (assuming we haven't accidentally photographed the stage)
    
    #estabilish an arbitrarily high value to start
    PreviousValue=1000000
    Threshold=0
    #the first few bins are always going to be subject, skip those
    #maybe make our start value scale relative to the total number of bins though?
    for BIndex in range(2,len(A[0])):
        CurrentValue=A[0][BIndex]
        if CurrentValue > PreviousValue:
            #we reached an inflection point, this bin is our threshold value
            if Conservative:
                Threshold=A[1][BIndex-1]
            else:
                #if we're feeling generous we can include some intermediate value pixels from the next bin
                Threshold=A[1][BIndex]
            return Threshold
        else:
            #at this point we should have reached a low point in the histogram
            #this will be our cutoff for spider spectra
            PreviousValue = CurrentValue
    #if we ever hit this return statement and the function gives 0 as output it's because something has gone wrong
    return Threshold

#uses a contrast image and threshold value to create a pixel map, specifying subject pixels for extraction
#contrastImage= spectral image object from contrast_image
#thresholdValue= floating point value, preferably output from contrast_threshold
#returns map of subject as specified by threshold values
def threshold_mapping(ContrastImage,ThresholdValue):
    #determine size of image
    Cols=ContrastImage[0].size
    Rows=ContrastImage.size
    #create map matrix
    MapMatrix=np.zeros(shape=(Rows,Cols))
    
    for Row in range(Rows):
        for Column in range(Cols):
            #check to see if value meets threshold
            #if so, start averaging and write info to file; store in our threshold tracker matrix
            #print(row,column)
            if ContrastImage[Row,Column] <= ThresholdValue:
                #update our thresholdTracker
                MapMatrix[Row,Column]=1
    return MapMatrix
    
#come back to this
def face_mapping():
    pass
    
#extract all spectra from a particular hyperspectral camera image
#useful for environment pics or subjects who fill the whole frame of view
#image= spectral image object, used to size map
def complete_mapping(ImageName):
    #open file with ImageName and check size
    Image=envi.open(ImageName+".hdr",ImageName+".cue")
    #get matrix size from initial image
    Cols=Image.ncols
    Rows=Image.nrows
    #create map matrix, entire thing filled with 1s
    MapMatrix=np.full((Rows, Cols), 1)
    return MapMatrix
"""
#NumSegments=integer specifying how many segments the image should be divided into
#works for 2,3,4,6,8, and 9
#Horizontal
def segmented_mapping(ImageName,NumSegments,Horizontal=True):
    #gonna stuff our eventual matrices in here
    MatrixList=[]
    
    #
    Image=envi.open(ImageName+".hdr",ImageName+".cue")
    #get matrix size from initial image
    Cols=Image.ncols
    Rows=Image.nrows
 
    #
    if NumSegments==2:
        #make 2 matrices
        if Horizontal:
            Rows/2
        else:
            Cols/2
        
    elif NumSegments==3:
        #make 3, etc.
        if Horizontal:
            pass
        else:
            pass
    elif NumSegments==4:
        pass
    elif NumSegments==6:
        if Horizontal:
            pass
        else:
            pass
    elif NumSegments==8:
        if Horizontal:
            pass
        else:
            pass
    elif NumSegments==9:
        pass
    else:
        #catch an error
        pass

    testMatrix=np.zeros((9,9))
    corner=testMatrix[:3,:3]
    corner.fill(1)
"""

#Function which extracts the pixels specified in our pixel map
#imageNames = list of file name strings for all images which will be opened; automatically figures the
#fine if it only contains one image, but still needs to be in a list
#pixelMap = matrix consisting of 0 and 1s, where 1 indicates pixels to be extracted
#outputName = string specifying what you want to call output

def map_extraction(ImageNames,PixelMap,OutputName,BandCutoff=140):
    
    #maybe do some parameter verification up-front?
    
    #we need to open the envi files as images using spectral
    Images=[]
    for Name in ImageNames:
        print(Name)
        TempImg=envi.open(Name+".hdr",Name+".cue")
        Images.append(TempImg)
        
    #make a directory (for output spectra) using a relative path from our current directory
    DirectoryName="./"+OutputName
    
    #try/catch  making our directory
    try:
        os.mkdir(DirectoryName)
        #if the directory is new we'll want to move in there to make our files
        os.chdir(DirectoryName)
    #if the directory already exists we might want to do something, for now we'll just exit
    except:
        print("we've already generated output under this name")
        return
    
    #if we're still going at this point we're ready to figure which pixels we want from our map
    #grab our size from our images so we can loop across everything
    NumCols=Images[0].ncols
    NumRows=Images[0].nrows
    
    #we want to save some spectral output
    #to get an idea of what colors are in the spectra, we want to look at bins of wavelengths
    #i.e. how much light is in 300-400nn, 400-500, etc.
    #we'll keep a count of each as we go
    UVCount=0
    BlueCount=0
    GreenCount=0
    LongCount=0
    #we'll also count how many pixel we've designated for each image to look at consistency
    PixelCount=0
    
    #for each row
    for Row in range(NumRows):
        #for each column
        for Col in range(NumCols):
            #confirm pixel in pixelMap
            if PixelMap[Row,Col] == 1:
                #bump up pixelCount
                PixelCount+=1
                
                #make a file for spectral output
                FileName = OutputName+"_Pixel_"+str(Row)+","+str(Col)
                OutputFile=open(FileName+".txt","w")

                #cutoff defaults to band 140 since the following bands are infrared
                for Band in range(BandCutoff):
                    #stores band value from all images we want to average
                    BandValue=0
                    #keep track of how many images to divide by
                    ImgCount=0
                    #total up the value for each image
                    for ImgIndex in range(len(Images)):
                        ImgCount+=1
                        BandValue= BandValue + Images[ImgIndex][Row,Col][Band]
                    #now that we've totaled, we divide by the number of images to average everything out
                    BandValue= BandValue/ImgCount
                    
                    ##########################
                    ##gotta do summary stats##
                    ##########################
                    
                    #conditionals to decide what color the band belongs to
                    #switch case!
                    #rework this according to Endler stuff
                    #first is UV @ nm 365-400 (since the camera doesn't go lower), bands 0-34
                    if Band < 35:
                        UVCount=+BandValue
                    #blue bin is 401-499 nm, bands 35-95
                    elif Band < 96:
                        BlueCount=+BandValue
                    #green covers 502-597nm, bands 96-124
                    elif Band < 125:
                        GreenCount=+BandValue
                    #long wavelength colors from 601-699n, bands 125-139
                    #bands 141-160 should already have been filtered out so they won't get counted here
                    else:
                        LongCount=+BandValue    
                    
                    #write the band sensitivity and averaged band value to our file
                    OutputFile.write(str(BandNMs[Band])+"\t"+str(BandValue)+"\n")
                    
                #close file 
                OutputFile.close()
                
    ######################
    #output summary info##
    ######################

    #first up, we want to normalize our different color counts based on the number of channels
    #we get fewer measurements w/ long wavelengths so we want to account for less overall measurements
    UVCountNorm=UVCount/34
    BlueCountNorm=BlueCount/61
    GreenCountNorm=GreenCount/29
    LongCountNorm=LongCount/15
    
                
    #next we'll want the average measure per channel, so get the total and normalize
    TotalCount=UVCount+BlueCount+GreenCount+LongCount
    TotalCountNorm=TotalCount/140
    
    #once we've got normalized values we can compare the proportion of each color bin to the total
    #the resultant numbers tell us whether a particular range is over- or underrepresented
    #above 1 means overrepresentation, and under one the opposite
    UVProp=UVCountNorm/TotalCountNorm
    BlueProp=BlueCountNorm/TotalCountNorm
    GreenProp=GreenCountNorm/TotalCountNorm
    LongProp=LongCountNorm/TotalCountNorm

    #once we've gone across all pixels of interest we need to write our summary stats
    SummaryFileName=OutputName+"_summary.txt"
    SummaryFile=open(SummaryFileName,"w")
    SummaryFile.write("Pixels Extracted: " + str(PixelCount) + "\n")
    SummaryFile.write("Average: "+ str(TotalCount) +"\n")
    SummaryFile.write("UV Proportion: "+ str(UVProp) + "\n")
    SummaryFile.write("Blue: " + str(BlueProp) + "\n")
    SummaryFile.write("Green: " + str(GreenProp) + "\n")
    SummaryFile.write("Red: " + str(LongProp) + "\n")
    SummaryFile.close()
    
    #once done with everything we need to move out of our new directory and prepare for another
    os.chdir("..")
    
    #do we even need to return anything here?
    #SpecInfo is now stored in our summary file 
    return "This is a filler string"


#function used to create a list of string formatted digits for file input
#takes integers and formats with the zeros necessary for file matching
def string_list(NumOne,NumTwo):
    NumList=[]
    for Num in range(NumOne,NumTwo):
        Number=str(Num)
        if len(Number)==1:
            Number="00"+Number
        elif len(Number)==2:
            Number="0"+Number
        NumList.append(Number)
        
    return NumList

#extracts pixels of subject via white and black background contrast
#SessionNum= 3-digit string of digits showing session number (001,etc.)
#DarkNums=list of strings, formatted as previous
#OutputString=name used to ID output; ideally references specimen number or similar
#GOP=boolean used to specify how conservative the histogram threshold process is
#returns...something; set up for error checking?
def extract_subject(SessionNum,WhiteRefNum,DarkNums,OutputString,GOP=True):
    
    LightName="session_"+SessionNum+"_"+WhiteRefNum+"_snapshot_REF"
    #I suppose the number you choose for the comparisons shouldn't matter but the first is easy
    DarkName="session_"+SessionNum+"_"+DarkNums[0]+"_snapshot_REF"
    Contrast=contrast_image(LightName, DarkName, OutputString)
    Threshold=contrast_threshold(Contrast,GOP)
    ThresholdMap=threshold_mapping(Contrast, Threshold)
    Darks=[]
    for num in DarkNums:
        Darks.append("session_"+SessionNum+"_"+num+"_snapshot_REF")
    Output=map_extraction(Darks, ThresholdMap, OutputString)
    
    return Output

#extracts all pixels
#SessionNum= 3-digit string of digits showing session number (001,etc.)
#ImageNums=list of strings, formatted as previous
#GOP=boolean used to specify how conservative the histogram threshold process is
#returns...something; set up for error checking?
def extract_all(SessionNum,ImageNums,OutputString,GOP=True):
    
    ImageNames=[]
    for Num in ImageNums:
        ImageNames.append("session_"+SessionNum+"_"+Num+"_snapshot_REF")
    CompleteMap=complete_mapping(ImageNames[0])
    Output=map_extraction(ImageNames, CompleteMap, OutputString)
    
    return Output
    
        


  