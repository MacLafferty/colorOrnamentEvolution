#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:18:06 2022

@author: davidmorris
"""

#need this to navigate directories
import os
#make sure we're in the same directory as HSC_extraction_functions
os.chdir("/Users/morehouselab/Desktop/David_M/scripts")
#grab our magical camera extraction functions
from HSC_extraction_functions import *


#first thing we need to go to the main directory storing all output
where="/Volumes/Wario/HSC_export/habronattus"

os.chdir(where)

#next I need to go into the specific date; automating by spreadsheet would be great
where="./mar_02_2022"
os.chdir(where)


#male pyrrithrix
Front_Darks_715=string_list(20,29)
Front_Output_715=extract_subject("004","019",Front_Darks_715,"HAPY_715_front")
Back_Darks_715=string_list(31,40)
Back_Output_715=extract_subject("004","030",Back_Darks_715,"HAPY_715_back")

Front_Darks_741=string_list(46,55)
Front_Darks_741=extract_subject("004","045",Front_Darks_741,"HAPY_741_front")
Back_Darks_741=string_list(57,66)
Back_Output_741=extract_subject("004","056",Back_Darks_741,"HAPY_741_back")

Front_Darks_1821=string_list(68,77)
Front_Darks_1821=extract_subject("004","067",Front_Darks_1821,"HAPY_1821_front")
Back_Darks_1821=string_list(79,88)
Back_Output_1821=extract_subject("004","078",Back_Darks_1821,"HAPY_1821_back")

Front_Darks_Benoit=string_list(89,99)
Front_Output_Benoit=extract_subject("004","100",Front_Darks_Benoit,"HAPY_Benoit_front")

Front_Darks_3889=string_list(13,23)
Front_Darks_3889=extract_subject("007","012",Front_Darks_3889,"HAPY_3889_front")
Back_Darks_3889=string_list(49,59)
Back_Output_3889=extract_subject("007","048",Back_Darks_3889,"HAPY_3889_back")


#male calcaratus
Front_Darks_6129=string_list(25,35)
Front_Output_6129=extract_subject("007","024",Front_Darks_6129,"HACA_6129_front")
Back_Darks_6129=string_list(37,47)
Back_Output_6129=extract_subject("004","036",Back_Darks_6129,"HACA_6129_back")

Front_Darks_5311=string_list(25,35)
Front_Output_5311=extract_subject("007","024",Front_Darks_5311,"HACA_6129_front")
Back_Darks_5311=string_list(37,47)
Back_Output_5311=extract_subject("004","036",Back_Darks_5311,"HACA_6129_back")

#female calcaratus
Front_Darks_6129=string_list(25,35)
Front_Output_6129=extract_subject("007","24",Front_Darks_6129,"HACA_6129_front")



where="../mar_04_2022"
os.chdir(where)


#males 

#session 2


#this dude is new
Front_Darks_3889=string_list(6,15)
Front_Output_3889=extract_subject("002","005",Front_Darks_3889,"HACOE_3889_front")
Back_Darks_3889=string_list(17,26)
Back_Output_3889=extract_subject("002","016",Back_Darks_3889,"HACOE_3889_back")


Front_Darks_2718R=string_list(84,93)
Front_Output_2718R=extract_subject("002","083",Front_Darks_2718R,"HAOR_2718R_front")
Back_Darks_2718R=string_list(106,115)
Back_Output_2718R=extract_subject("002","105",Back_Darks_2718R,"HAOR_2718R_back")


Front_Darks_2718L=string_list(95,104)
Front_Output_2718L=extract_subject("002","094",Front_Darks_2718L,"HAOR_2718L_front")
Back_Darks_2718L=string_list(117,126)
Back_Output_2718L=extract_subject("002","116",Back_Darks_2718L,"HAOR_2718L_back")


#females

#session 1

Front_Darks_2679=string_list(8,17)
Front_Output_2679=extract_subject("001","007",Front_Darks_2679,"HAOR_2679_front")
Back_Darks_2679=string_list(19,28)
Back_Output_2679=extract_subject("001","018",Back_Darks_2679,"HAOR_2679_back")


Front_Darks_2683=string_list(30,39)
Front_Output_2683=extract_subject("001","029",Front_Darks_2683,"HAOR_2683_front")
Back_Darks_2683=string_list(41,50)
Back_Output_2683=extract_subject("001","040",Back_Darks_2683,"HAOR_2683_back")


Front_Darks_2725=string_list(52,61)
Front_Output_2725=extract_subject("001","051",Front_Darks_2725,"HAOR_2725_front")
Back_Darks_2725=string_list(63,72)
Back_Output_2725=extract_subject("001","062",Back_Darks_2725,"HAOR_2725_back")


Front_Darks_2735=string_list(74,83)
Front_Output_2735=extract_subject("001","073",Front_Darks_2735,"HAOR_2735_front")
Back_Darks_2735=string_list(85,94)
Back_Output_2735=extract_subject("001","084",Back_Darks_2735,"HAOR_2735_back")


Front_Darks_2735_other=string_list(96,105)
Front_Output_2735_other =extract_subject("001","095",Front_Darks_2735_other,"HAOR_2735!_front")
Back_Darks_2735_other=string_list(107,116)
Back_Output_2735_other=extract_subject("001","106",Back_Darks_2735_other,"HAOR_2735!_back")


Front_Darks_5431=string_list(118,129)
Front_Output_5431=extract_subject("001","117",Front_Darks_5431,"HAOR_5431_front")
Back_Darks_5431=string_list(131,140)
Back_Output_5431=extract_subject("001","130",Back_Darks_5431,"HAOR_5431_back")


#specify file path
#all of these are new
where="../mar_07_2022"
os.chdir(where)


Front_Darks_J83=string_list(28,37)
Front_Output_J83=extract_subject("000","027",Front_Darks_J83,"HACOE_J83_front")
Back_Darks_J83=string_list(39,48)
Back_Output_J83=extract_subject("000","038",Back_Darks_J83,"HACOE_J83_back")


Front_Darks_5428=string_list(6,15)
Front_Output_5428=extract_subject("001","005",Front_Darks_5428,"HAORB_5428_front")
Back_Darks_5428=string_list(18,26)
Back_Output_5428=extract_subject("001","016",Back_Darks_5428,"HAORB_5428_back")


Front_Darks_J78=string_list(28,37)
Front_Output_J78=extract_subject("001","027",Front_Darks_J78,"HACA_J78_front")
Back_Darks_J78=string_list(39,48)
Back_Output_J78=extract_subject("001","038",Back_Darks_J78,"HACA_J78_back")


Front_Darks_J199=string_list(28,37)
Front_Output_J199=extract_subject("002","027",Front_Darks_J199,"HACOE_J199_front")
Back_Darks_J199=string_list(39,48)
Back_Output_J199=extract_subject("002","038",Back_Darks_J199,"HACOE_J199_back")


Front_Darks_J133=string_list(50,61)
Front_Output_J133=extract_subject("002","049",Front_Darks_J133,"HACA_J133_front")
Back_Darks_J133=string_list(63,73)
Back_Output_J133=extract_subject("002","062",Back_Darks_J133,"HACA_J133_back")


Front_Darks_5068=string_list(75,84)
Front_Output_5068=extract_subject("002","074",Front_Darks_5068,"HACA_5068_front")
Back_Darks_5068=string_list(86,96)
Back_Output_5068=extract_subject("002","085",Back_Darks_5068,"HACA_5068_back")


#specify file path
where="../mar_09_2022"
os.chdir(where)


Front_Darks_4869=string_list(6,15)
Output_4869=extract_subject("001","005",Front_Darks_4869,"HAAM_4869_front")


Front_Darks_2621=string_list(17,26)
Front_Output_2621=extract_subject("001","016",Front_Darks_2621,"HAAM_2621_front")
Back_Darks_2621=string_list(28,37)
Back_Output_2621=extract_subject("001","027",Back_Darks_2621,"HAAM_2621_back")


Front_Darks_2629=string_list(39,48)
Front_Output_2629=extract_subject("001","038",Front_Darks_2629,"HAAM_2629_front")
Back_Darks_2629=string_list(50,60)
Back_Output_2629=extract_subject("001","049",Back_Darks_2629,"HAAM_2629_back")


Front_Darks_4863=string_list(63,72)
Front_Output_4863=extract_subject("001","062",Front_Darks_4863,"HAAM_4863_front")
Back_Darks_4863=string_list(74,83)
Back_Output_4863=extract_subject("001","073",Back_Darks_4863,"HAAM_4863_back")


Front_Darks_3203=string_list(6,15)
Front_Output_3203=extract_subject("002","005",Front_Darks_3203,"HACOE_3203_front")


Front_Darks_2692=string_list(17,26)
Front_Output_2692=extract_subject("002","016",Front_Darks_2692,"HAOR_2692_front")
Back_Darks_2692=string_list(28,38)
Back_Output_2692=extract_subject("002","027",Back_Darks_2692,"HAOR_2692_back")


Front_Darks_2709=string_list(40,49)
Front_Output_2709=extract_subject("002","039",Front_Darks_2709,"HAOR_2709_front")
Back_Darks_2709=string_list(51,61)
Back_Output_2709=extract_subject("002","050",Back_Darks_2709,"HAOR_2709_back")

Front_Darks_2740R=string_list(50,59)
Front_Output_2740R=extract_subject("003","049",Front_Darks_2740R,"HAOR_2740R_front")
Back_Darks_2740R=string_list(72,81)
Back_Output_2740R=extract_subject("003","071",Back_Darks_2740R,"HAOR_2740R_back")


Front_Darks_2740L=string_list(61,70)
Front_Output_2740L=extract_subject("003","060",Front_Darks_2740L,"HAOR_2740L_front")
Back_Darks_2740L=string_list(83,92)
Back_Output_2740L=extract_subject("003","082",Back_Darks_2740L,"HAOR_2740L_back")


Front_Darks_2713=string_list(94,104)
Front_Output_2713=extract_subject("003","093",Front_Darks_2713,"HAOR_2713_front")
Back_Darks_2713=string_list(106,115)
Back_Output_2713=extract_subject("003","105",Back_Darks_2713,"HAOR_2713_back")


Front_Darks_J177=string_list(11,20)
Front_Output_J177=extract_subject("004","010",Front_Darks_J177,"HAORB_J177_front")
Back_Darks_J177=string_list(22,31)
Back_Output_J177=extract_subject("004","021",Back_Darks_J177,"HAORB_J177_back")

Front_Darks_J75=string_list(33,42)
Front_Output_J75=extract_subject("004","032",Front_Darks_J75,"HAORB_J75_front")
Back_Darks_J75=string_list(44,53)
Back_Output_J75=extract_subject("004","043",Back_Darks_J75,"HAORB_J75_back")

Front_Darks_J106=string_list(55,64)
Front_Output_J106=extract_subject("004","054",Front_Darks_J106,"HAORB_J106_front")
Back_Darks_J106=string_list(66,75)
Back_Output_J106=extract_subject("004","065",Back_Darks_J106,"HAORB_J106_back")


Front_Darks_J209=string_list(77,86)
Front_Output_J209=extract_subject("004","076",Front_Darks_J209,"HACOE_J209_front")
Back_Darks_J209=string_list(88,97)
Back_Output_J209=extract_subject("004","087",Back_Darks_J209,"HACOE_J209_back")


#skipping a decorus male for now, need more anyway

Front_Darks_J73=string_list(6,15)
Front_Output_J73=extract_subject("005","005",Front_Darks_J73,"HAORB_J73_front")
Back_Darks_J73=string_list(17,26)
Back_Output_J73=extract_subject("005","016",Back_Darks_J73,"HAORB_J73_back")


Front_Darks_J71=string_list(28,37)
Front_Output_J71=extract_subject("005","027",Front_Darks_J71,"HAORB_J71_front")
Back_Darks_J71=string_list(55,64)
Back_Output_J71=extract_subject("005","054",Back_Darks_J71,"HAORB_J71_back")


Front_Darks_J261=string_list(6,15)
Front_Output_J261=extract_subject("006","005",Front_Darks_J261,"HAORB_J261_front")
Back_Darks_J261=string_list(17,26)
Back_Output_J261=extract_subject("006","016",Back_Darks_J261,"HAORB_J261_back")


Front_Darks_J283=string_list(28,37)
Front_Output_J283=extract_subject("006","027",Front_Darks_J283,"HACOE_J283_front")
Back_Darks_J283=string_list(29,38)
Back_Output_J283=extract_subject("006","028",Back_Darks_J283,"HACOE_J283_back")


Front_Darks_5422=string_list(50,59)
Front_Output_5422=extract_subject("006","049",Front_Darks_5422,"HACA_5422_front")
Back_Darks_5422=string_list(61,70)
Back_Output_5422=extract_subject("006","060",Back_Darks_5422,"HACA_5422_back")

Front_Darks_J6=string_list(17,26)
Front_Output_J6=extract_subject("007","016",Front_Darks_J6,"HACA_J6_front")
Back_Darks_J6=string_list(28,38)
Back_Output_J6=extract_subject("007","027",Back_Darks_J6,"HACA_J6_back")



where="../mar_11_2022"
os.chdir(where)

#malespiders


#sessiom 0!?


Front_Darks_2671R=string_list(6,15)
Front_Output_2671R=extract_subject("000","005",Front_Darks_2671R,"HAOR_2671R_front")
Back_Darks_2671R=string_list(28,37)
Back_Output_2671R=extract_subject("000","027",Back_Darks_2671R,"HAOR_2671R_back")


Front_Darks_2671L=string_list(17,26)
Front_Output_2671L=extract_subject("000","016",Front_Darks_2671L,"HAOR_2671L_front")
Back_Darks_2671L=string_list(39,48)
Back_Output_2671L=extract_subject("000","038",Back_Darks_2671L,"HAOR_2671L_back")


Front_Darks_2712=string_list(50,59)
Front_Output_2712=extract_subject("000","049",Front_Darks_2712,"HAOR_2712_front")
Back_Darks_2712=string_list(61,70)
Back_Output_2712=extract_subject("000","060",Back_Darks_2712,"HAOR_2712_back")


Front_Darks_2802=string_list(72,81)
Front_Output_2802=extract_subject("000","071",Front_Darks_2802,"HAPY_2802_front")
Back_Darks_2802=string_list(83,92)
Back_Output_2802=extract_subject("000","082",Back_Darks_2802,"HAPY_2802_back")


Front_Darks_3796=string_list(94,103)
Front_Output_3796=extract_subject("000","093",Front_Darks_3796,"HAPY_3796_front")
Back_Darks_3796=string_list(105,114)
Back_Output_3796=extract_subject("000","104",Back_Darks_3796,"HAPY_3796_back")


#session1!?

Front_Darks_2901=string_list(6, 15)
Front_Output_2901=extract_subject("001","005",Front_Darks_2901,"HAPY_2901_front")
Back_Darks_2901=string_list(17,27)
Back_Output_2901=extract_subject("001","016",Back_Darks_2901,"HAPY_2901_back")

Front_Darks_3214=string(40,49)
Front_Output_3214=extract_subject("001","039",Front_Darks_3214,"HAPY_3214_front")
Back_Darks_3214=string(51,60)
Back_Output_3214=extract_subject("001","050",Back_Darks_3214,"HAPY_3214_back")



Front_Darks_4616=string_list(51,60)
Front_Output_4616=extract_subject("001","050",Front_Darks_4616,"HAPY_4616_front")
Back_Darks_4616=string_list(62,71)
Back_Output_4616=extract_subject("001","061",Back_Darks_4616,"HAPY_4616_back")



Front_Darks_3752=string_list(73,82)
Front_Output_3752=extract_subject("001","072",Front_Darks_3752,"HAPY_3752_front")
Back_Darks_3752=string_list(84,93)
Back_Output_3752=extract_subject("001","083",Back_Darks_3752,"HAPY_3752_back")



Front_Darks_3706=string_list(95,104)
Front_Output_3706=extract_subject("001","094",Front_Darks_3706,"HAPY_3706_front")
Back_Darks_3706=string_list(106,115)
Back_Output_3706=extract_subject("001","105",Back_Darks_3706,"HAPY_3706_back")


where="../mar_15_2022"
os.chdir(where)

#males

#sessiom 0!?


Front_Darks_2700R=string_list(6,15)
Front_Output_2700R=extract_subject("000","005",Front_Darks_2700R,"HAOR_2700R_front")
Back_Darks_2700R=string_list(28,37)
Back_Output_2700R=extract_subject("000","027",Back_Darks_2700R,"HAOR_2700R_back")


Front_Darks_2700L=string_list(17,26)
Front_Output_2700L=extract_subject("000","016",Front_Darks_2700L,"HAOR_2700L_front")
Back_Darks_2700L=string_list(39,48)
Back_Output_2700L=extract_subject("000","038",Back_Darks_2700L,"HAOR_2700L_back")


Front_Darks_3500=string_list(51,60)
Front_Output_3500=extract_subject("000","050",Front_Darks_3500,"HAOR_3500_front")
Back_Darks_3500=string_list(62,71)
Back_Output_3500=extract_subject("000","061",Back_Darks_3500,"HAOR_3500_back")


Front_Darks_2413=string_list(73,82)
Front_Output_2413=extract_subject("000","072",Front_Darks_2413,"HAAM_2413_front")
Back_Darks_2413=string_list(84,93)
Back_Output_2413=extract_subject("000","083",Back_Darks_2413,"HAAM_2413_back")



#sessiom 1!/

Front_Darks_2445=string_list(6,15)
Front_Output_2445=extract_subject("001","005",Front_Darks_2445,"HAAM_2445_front")
Back_Darks_2445=string_list(17,28)
Back_Output_2445=extract_subject("001","016",Back_Darks_2445,"HAAM_2445_back")



Front_Darks_2446=string_list(30,39)
Front_Output_2446=extract_subject("001","029",Front_Darks_2446,"HAAM_2446_front")
Back_Darks_2446=string_list(41,61)
Back_Output_2446=extract_subject("001","040",Back_Darks_2446,"HAAM_2446_back")


#session 2 
Front_Darks_2439=string_list(6,15)
Front_Output_2439=extract_subject("002","005",Front_Darks_2439,"HAAM_2439_front")


where="../mar_17_2022"
os.chdir(where)


#males

#session 0!/

Front_Darks_2409=string_list(7,16)
Front_Output_2409=extract_subject("000","005",Front_Darks_2409,"HAAM_2409_front")
Back_Darks_2409=string_list(18,30)
Back_Output_2409=extract_subject("000","017",Back_Darks_2409,"HAAM_2409_back")



Front_Darks_2408=string_list(32,53)
Front_Output_2408=extract_subject("000","031",Front_Darks_2408,"HAAM_2408_front")
Back_Darks_2408=string_list(56,71)
Back_Output_2408=extract_subject("000","055",Back_Darks_2408,"HAAM_2408_back")



#session 1!?

Front_Darks_2440=string_list(7,16)
Front_Output_2440=extract_subject("001","006",Front_Darks_2440,"HAAM_2440_front")
Back_Darks_2440=string_list(18,27)
Back_Output_2440=extract_subject("001","017",Back_Darks_2440,"HAAM_2440_back")



Front_Darks_3329=string_list(29,38)
Front_Output_3329=extract_subject("001","028",Front_Darks_3329,"HAAM_3329_front")
Back_Darks_3329=string_list(40,49)
Back_Output_3329=extract_subject("001","039",Back_Darks_3329,"HAAM_3329_back")


#females

Front_Darks_2436=string_list(61,70)
Front_Output_2436=extract_subject("001","060",Front_Darks_2436,"HAAM_2436_front")
Back_Darks_2436=string_list(72,81)
Back_Output_2436=extract_subject("001","071",Back_Darks_2436,"HAAM_2436_back")

#session 2 

Front_Darks_2429=string_list(6,15)
Front_Output_2429=extract_subject("002","005",Front_Darks_2429,"HAAM_2429_front")
Back_Darks_2429=string_list(17,28)
Back_Output_2429=extract_subject("002","016",Back_Darks_2429,"HAAM_2429_back")



Front_Darks_2444=string_list(30,39)
Front_Output_2444=extract_subject("002","029",Front_Darks_2444,"HAAM_2444_front")
Back_Darks_2444=string_list(41,50)
Back_Output_2444=extract_subject("002","040",Back_Darks_2444,"HAAM_2444_back")



Front_Darks_2417=string_list(52,61)
Front_Output_2417=extract_subject("002","051",Front_Darks_2417,"HAAM_2417_front")
Back_Darks_2417=string_list(41,50)
Back_Output_2417=extract_subject("002","062",Back_Darks_2417,"HAAM_2417_back")



#session 3 

Front_Darks_2441=string_list(6,15)
Front_Output_2441=extract_subject("003","005",Front_Darks_2441,"HAAM_2441_front")
Back_Darks_2441=string_list(17,28)
Back_Output_2441=extract_subject("003","016",Back_Darks_2441,"HAAM_2441_back")



Front_Darks_2410=string_list(28,37)
Front_Output_2410=extract_subject("003","027",Front_Darks_2410,"HAAM_2410_front")
Back_Darks_2410=string_list(39,48)
Back_Output_2410=extract_subject("003","038",Back_Darks_2410,"HAAM_2410_back")

where="../mar_21_2022"
os.chdir(where)

Front_Darks_J77=string_lists(6,15)
Front_Output_J77=extract_subject("000","005",Front_Output_J77,"HACA_J77_front")
Back_Darks_J77=string_lists(17,27)
Back_Output_J77=extract_subjects("000","016",Back_Output_J77,"HACA_J77_back")

Front_Darks_J82=string_lists(40,49)
Front_Output_J82=extract_subject("000","039",Front_Darks_J82,"HACOE_J82_front")
Back_Darks_J82=string_lists(51,61)
Back_Output_J82=extract_subject("000","050",Back_Darks_J82,"HACOE_J82_back")

Front_Darks_5430=string_lists(63,72)
Front_Output_5430=extract_subject("000","062",Front_Darks_5430,"HACOR_5430_front")
Back_Darks_5430=string_lists(74,83)
Back_Output_5430=extract_subject("000","073",Back_Darks_5430,"HACOR_5430_back")

Front_Darks_5080=string_lists(6,15)
Front_Output_5080=extract_subject("001","005",Front_Darks_5080,"HACA_5080_front")
Back_Darks_5080=string_lists(17,26)
Back_Output_5080=extract_subject("001","016",Back_Darks_5080,"HACA_5080_back")

Front_Darks_J198=string_lists(28,37)
Front_Output_J198=extract_subject("001","027",Front_Darks_J198,"HACOE_J198_front")
Back_Darks_J198=string_lists(39,48)
Back_Output_J198=extract_subject("001","038",Back_Darks_J198,"HACOE_J198_back")



where="../mar_23_2022"
os.chdir(where)

#males

#session 0

Front_Darks_3475=string_list(10,19)
Front_Output_3475=extract_subject("000","009",Front_Darks_3475,"HAOR_3475_front")
Back_Darks_3475=string_list(21,30)
Back_Output_3475=extract_subject("000","020",Back_Darks_3475,"HAOR_3475_back")


Front_Darks_4121=string_list(32,41)
Front_Output_4121=extract_subject("000","031",Front_Darks_4121,"HAOR_4121_front")
Back_Darks_4121=string_list(43,52)
Back_Output_4121=extract_subject("000","042",Back_Darks_4121,"HAOR_4121_back")

#session 4

Front_Darks_3469=string_list(6,15)
Front_Output_3469=extract_subject("004","005",Front_Darks_3469,"HAOR_3469_front")
Back_Darks_3469=string_list(17,26)
Back_Output_3469=extract_subject("004","016",Back_Darks_3469,"HAOR_3469_back")


Front_Darks_3496=string_list(28,37)
Front_Output_3496=extract_subject("004","027",Front_Darks_3496,"HAOR_3496_front")
Back_Darks_3496=string_list(39,48)
Back_Output_3496=extract_subject("004","038",Back_Darks_3496,"HAOR_3496_back")


Front_Darks_3499=string_list(72,81)
Front_Output_3499=extract_subject("004","071",Front_Darks_3499,"HAOR_3499_front")
Back_Darks_3499=string_list(83,95)
Back_Output_3499=extract_subject("004","082",Back_Darks_3499,"HAOR_3499_back")


Front_Darks_3472=string_list(97,106)
Front_Output_3472=extract_subject("004","096",Front_Darks_3472,"HAOR_3472_front")
Back_Darks_3472=string_list(108,117)
Back_Output_3472=extract_subject("004","107",Back_Darks_3472,"HAOR_3472_back")


Front_Darks_3500=string_list(50,59)
Front_Output_3500=extract_subject("004","049",Front_Darks_3472,"HAOR_3500_front")
Back_Darks_3500=string_list(61,70)
Back_Output_3500=extract_subject("004","060",Back_Darks_3472,"HAOR_3500_back")

#session5

Front_Darks_3483=string_list(6,15)
Front_Output_3483=extract_subject("005","005",Front_Darks_3483,"HAOR_3483_front")
Back_Darks_3483=string_list(17,26)
Back_Output_3483=extract_subject("005","016",Back_Darks_3483,"HAOR_3483_back")


Front_Darks_3457=string_list(52,61)
Front_Output_3457=extract_subject("005","051",Front_Darks_3457,"HAOR_3457_front")
Back_Darks_3457=string_list(63,72)
Back_Output_3457=extract_subject("005","062",Back_Darks_3457,"HAOR_3457_back")

Front_Darks_J97=string_list(74,83)
Front_Output_J97=extract_subject("005","073",Front_Darks_J97,"HACA_J97,front")


#females

#sessiom 0

Front_Darks_1071=string_list(54,63)
Front_Output_1071=extract_subject("000","053",Front_Darks_1071,"HAVI_1071_front")
Back_Darks_1071=string_list(65,74)
Back_Output_1071=extract_subject("000","064",Back_Darks_1071,"HAVI_1071_back")


Front_Darks_3459=string_list(76,85)
Front_Output_3459=extract_subject("000","075",Front_Darks_3459,"HAOR_3459_front")
Back_Darks_3459=string_list(87,96)
Back_Output_3459=extract_subject("000","086",Back_Darks_3459,"HAOR_3459_back")


Front_Darks_1117=string_list(98,107)
Front_Output_1117=extract_subject("000","097",Front_Darks_1117,"HAVI_1117_front")
Back_Darks_1117=string_list(109,118)
Back_Output_1117=extract_subject("000","108",Back_Darks_1117,"HAVI_1117_back")

#session1

Front_Darks_2426=string_list(6,15)
Front_Output_2426=extract_subject("001","005",Front_Darks_2426,"HAAM_2426_front")
Back_Darks_2426=string_list(17,26)
Back_Output_2426=extract_subject("001","016",Back_Darks_2426,"HAAM_2426_back")


Front_Darks_1125=string_list(28,37)
Front_Output_1125=extract_subject("001","027",Front_Darks_1125,"HAVI_1125_front")
Back_Darks_1125=string_list(39,48)
Back_Output_1125=extract_subject("001","038",Back_Darks_1125,"HAVI_1125_back")


Front_Darks_3444=string_list(50,59)
Front_Output_3444=extract_subject("001","049",Front_Darks_3444,"HAOR_3444_front")
Back_Darks_3444=string_list(61,70)
Back_Output_3444=extract_subject("001","060",Back_Darks_3444,"HAOR_3444_back")


Front_Darks_3854=string_list(72,81)
Front_Output_3854=extract_subject("001","071",Front_Darks_3854,"HAPY_3854_front")
Back_Darks_3854=string_list(83,92)
Back_Output_3854=extract_subject("001","082",Back_Darks_3854,"HAPY_3854_back")


Front_Darks_2656=string_list(94,103)
Front_Output_2656=extract_subject("001","093",Front_Darks_2656,"HAAM_2656_front")
Back_Darks_2656=string_list(105,114)
Back_Output_2656=extract_subject("001","104",Back_Darks_2656,"HAAM_2656_back")


Front_Darks_1096=string_list(116,125)
Front_Output_1096=extract_subject("001","115",Front_Darks_1096,"HAVI_1096_front")
Back_Darks_1096=string_list(127,136)
Back_Output_1096=extract_subject("001","126",Back_Darks_1096,"HAVI_1096_back")

#session2

Front_Darks_1120=string_list(6,15)
Front_Output_1120=extract_subject("002","005",Front_Darks_1120,"HAVI_1120_front")
Back_Darks_1120=string_list(17,26)
Back_Output_1120=extract_subject("002","016",Back_Darks_1120,"HAVI_1120_back")


Front_Darks_1088=string_list(28,37)
Front_Output_1088=extract_subject("002","027",Front_Darks_1088,"HAVI_1088_front")
Back_Darks_1088=string_list(40,49)
Back_Output_1088=extract_subject("002","039",Back_Darks_1088,"HAVI_1088_back")


Front_Darks_3564=string_list(51,60)
Front_Output_3564=extract_subject("002","050",Front_Darks_3564,"HAVI_3564_front")
Back_Darks_3564=string_list(62,71)
Back_Output_3564=extract_subject("002","061",Back_Darks_3564,"HAVI_3564_back")

#session3

Front_Darks_3446=string_list(6,16)
Front_Output_3446=extract_subject("003","005",Front_Darks_3446,"HAOR_3446_front")
Back_Darks_3446=string_list(18,27)
Back_Output_3446=extract_subject("003","017",Back_Darks_3446,"HAOR_3446_back")


Front_Darks_1127=string_list(29,38)
Front_Output_1127=extract_subject("003","028",Front_Darks_1127,"HAVI_1127_front")
Back_Darks_1127=string_list(40,49)
Back_Output_1127=extract_subject("003","039",Back_Darks_1127,"HAVI_1127_back")


Front_Darks_1115=string_list(51,60)
Front_Output_1115=extract_subject("003","050",Front_Darks_1115,"HAVI_1115_front")
Back_Darks_1115=string_list(62,71)
Back_Output_1115=extract_subject("003","061",Back_Darks_1115,"HAVI_1115_back")


Front_Darks_3431=string_list(73,82)
Front_Output_3431=extract_subject("003","072",Front_Darks_3431,"HAVI_3431_front")
Back_Darks_3431=string_list(84,93)
Back_Output_3431=extract_subject("003","083",Back_Darks_3431,"HAVI_3431_back")

#session 5
#put in female 1194, figure out species


where="../mar_25_2022"
os.chdir(where)

#males

#session 0

Front_Darks_3560=string_list(6,15)
Front_Output_3560=extract_subject("000","005",Front_Darks_3560,"HAVI_3560_front")
Back_Darks_3560=string_list(17,26)
Back_Output_3560=extract_subject("000","016",Back_Darks_3560,"HAVI_3560_back")


Front_Darks_temp9=string_list(28,37)
Front_Output_temp9=extract_subject("000","027",Front_Darks_temp9,"HAVI_temp9_front")
Back_Darks_temp9=string_list(39,50)
Back_Output_temp9=extract_subject("000","038",Back_Darks_temp9,"HAVI_temp9_back")


Front_Darks_3547=string_list(52,61)
Front_Output_3547=extract_subject("000","051",Front_Darks_3547,"HAVI_3547_front")
Back_Darks_3547=string_list(63,72)
Back_Output_3547=extract_subject("000","062",Back_Darks_3547,"HAVI_3547_back")


Front_Darks_3573=string_list(74,83)
Front_Output_3573=extract_subject("000","073",Front_Darks_3573,"HAVI_3573_front")
Back_Darks_3573=string_list(85,94)
Back_Output_3573=extract_subject("000","084",Back_Darks_3573,"HAVI_3573_back")


Front_Darks_1123=string_list(96,105)
Front_Output_1123=extract_subject("000","095",Front_Darks_1123,"HAVI_1123_front")
Back_Darks_1123=string_list(107,116)
Back_Output_1123=extract_subject("000","106",Back_Darks_1123,"HAVI_1123_back")


Front_Darks_1136=string_list(118,127)
Front_Output_1136=extract_subject("000","117",Front_Darks_1136,"HAVI_1136_front")
Back_Darks_1136=string_list(129,139)
Back_Output_1136=extract_subject("000","128",Back_Darks_1136,"HAVI_1136_back")

#session 1 


Front_Darks_2637=string_list(8,17)
Front_Output_2637=extract_subject("001","007",Front_Darks_2637,"HAAM_2637_front")
Back_Darks_2637=string_list(19,28)
Back_Output_2637=extract_subject("001","018",Back_Darks_2637,"HAAM_2637_back")


Front_Darks_2628=string_list(30,39)
Front_Output_2628=extract_subject("001","029",Front_Darks_2628,"HAAM_2628_front")
Back_Darks_2628=string_list(42,51)
Back_Output_2628=extract_subject("001","041",Back_Darks_2628,"HAAM_2628_back")


Front_Darks_3499=string_list(53,63)
Front_Output_3499=extract_subject("001","052",Front_Darks_3499,"HAOR_3499_front")
Back_Darks_3499=string_list(65,74)
Back_Output_3499=extract_subject("001","064",Back_Darks_3499,"HAOR_3499_back")


Front_Darks_3182=string_list(76,85)
Front_Output_3182=extract_subject("001","075",Front_Darks_3182,"HAPY_3182_front")
Back_Darks_3182=string_list(87,96)
Back_Output_3182=extract_subject("001","086",Back_Darks_3182,"HAPY_3182_back")

Front_Darks_5315=string_list(98,107)
Front_Output_5315=extract_subject("001","097",Front_Darks_5315,"HACA_5315_front")
Back_Darks_5315=string_list(109,118)
Back_Output_5315=extract_subject("001","108",Back_Darks_5315,"HACA_5315_back")


where="../mar_30_2022"
os.chdir(where)

#males 

#session 0 

Front_Darks_3403=string_list(8,17)
Front_Output_3403=extract_subject("000","007",Front_Darks_3403,"HADO_3403_front")
Back_Darks_3403=string_list(19,28)
Back_Output_3403=extract_subject("000","018",Back_Darks_3403,"HADO_3403_back")


Front_Darks_3565=string_list(30,39)
Front_Output_3565=extract_subject("000","029",Front_Darks_3565,"HADO_3565_front")
Back_Darks_3565=string_list(41,50)
Back_Output_3565=extract_subject("000","040",Back_Darks_3565,"HADO_3565_back")


Front_Darks_3410=string_list(52,61)
Front_Output_3410=extract_subject("000","051",Front_Darks_3410,"HADO_3410_front")

#session 1 

Back_Darks_3410=string_list(6,15)
Back_Output_3410=extract_subject("001","005",Back_Darks_3410,"HADO_3410_back")


Front_Darks_4685=string_list(85,95)
Front_Output_4685=extract_subject("001","084",Front_Darks_4685,"HAFA_4685_front")
Back_Darks_4685=string_list(97,107)
Back_Output_4685=extract_subject("001","096",Back_Darks_4685,"HAFA_4685_back")

#females 


Front_Darks_3428=string_list(17,26)
Front_Output_3428=extract_subject("001","016",Front_Darks_3428,"HADO_3428_front")
Back_Darks_3428=string_list(28,37)
Back_Output_3428=extract_subject("001","027",Back_Darks_3428,"HADO_3428_back")


Front_Darks_3620other=string_list(39,48)
Front_Output_3620other=extract_subject("001","038",Front_Darks_3620other,"HADO_3620other_front")
Back_Darks_3620other=string_list(50,60)
Back_Output_3620other=extract_subject("001","049",Back_Darks_3620other,"HADO_3620other_back")


Front_Darks_1194=string_list(62,71)
Front_Output_1194=extract_subject("001","061",Front_Darks_1194,"HADO_1194_front")
Back_Darks_1194=string_list(73,83)
Back_Output_1194=extract_subject("001","072",Back_Darks_1194,"HADO_1194_back")


Front_Darks_3672=string_list(109,118)
Front_Output_3672=extract_subject("001","108",Front_Darks_3672,"HADO_3672_front")
Back_Darks_3672=string_list(120,129)
Back_Output_3672=extract_subject("001","119",Back_Darks_3672,"HADO_3672_back")


#session 2 

Front_Darks_3666=string_list(6,20)
Front_Output_3666=extract_subject("002","005",Front_Darks_3666,"HADO_3666_front")
Back_Darks_3666=string_list(22,31)
Back_Output_3666=extract_subject("002","021",Back_Darks_3666,"HADO_3666_back")


Front_Darks_3434=string_list(33,42)
Front_Output_3434=extract_subject("002","032",Front_Darks_3434,"HADO_3434_front")
Back_Darks_3434=string_list(50,61)
Back_Output_3434=extract_subject("002","043",Back_Darks_3434,"HADO_3434_back")


Front_Darks_3676=string_list(63,72)
Front_Output_3676=extract_subject("002","062",Front_Darks_3676,"HADO_3676_front")
Back_Darks_3676=string_list(74,84)
Back_Output_3676=extract_subject("002","073",Back_Darks_3676,"HADO_3676_back")


where="../apr_01_2022"
os.chdir(where)

#males

#session 0 

Front_Darks_3435=string_list(6,15)
Front_Output_3435=extract_subject("000","005",Front_Darks_3435,"HADO_3435_front")
Back_Darks_3435=string_list(18,27)
Back_Output_3435=extract_subject("000","017",Back_Darks_3435,"HADO_3435_back")


Front_Darks_3665=string_list(29,39)
Front_Output_3665=extract_subject("000","028",Front_Darks_3665,"HADO_3665_front")

#session 1 

Back_Darks_3665=string_list(6,15)
Back_Output_3665=extract_subject("001","005",Back_Darks_3665,"HADO_3665_back")

# weird sessions check image numbers!
Front_Darks_J89=string_list(17,30)
Front_Output_J89=extract_subject("001","016",Front_Darks_J89,"HAFA_J89_front")
Back_Darks_J89=string_list(18,29)
Back_Output_J89=extract_subject("002","017",Back_Darks_J89,"HAFA_J89_back")

#session 2 

Front_Darks_Dotty=string_list(31,40)
Front_Output_Dotty=extract_subject("002","030",Front_Darks_Dorotheae,"HADOR_Dotty_front")
Back_Darks_Dotty=string_list(42,51)
Back_Output_Dotty=extract_subject("002","041",Back_Darks_Dorotheae,"HADOR_Dotty_back")

Front_Darks_5317=string_list(55,66)
Front_Output_5317=extract_subject("002","054",Front_Darks_5317,"HACA_5317_front")

Front_Darks_5097=string_list(68,78)
Front_Output_5097=extract_subject("002","067",Front_Darks_5097,"HACA_5097_front")
Back_Darks_5097=string_list(80,89)
Back_Output_5097=extract_subject("002","079",Back_Darks_5097,"HACA_5097_back")


#session 3 

Front_Darks_J79=string_list(6,15)
Front_Output_J79=extract_subject("003","005",Front_Darks_J79,"HACO_J79_front")
Back_Darks_J79=string_list(17,26)
Back_Output_J79=extract_subject("003","016",Back_Darks_J79,"HACO_J79_back")


Front_Darks_3575=string_list(28,37)
Front_Output_3573=extract_subject("003","027",Front_Darks_3575,"HADO_3575_front")
Back_Darks_3575=string_list(39,49)
Back_Output_3575=extract_subject("003","038",Back_Darks_3575,"HADO_3575_back")


Front_Darks_3409=string_list(51,62)
Front_Output_3409=extract_subject("003","050",Front_Darks_3409,"HADO_3409_front")
Back_Darks_3409=string_list(64,73)
Back_Output_3409=extract_subject("003","063",Back_Darks_3409,"HADO_3409_back")

Front_Darks_J179=string_list(75,84)
Front_Output_J179=extract_subject("003","074",Front_Darks_J179,"HAORB_J179_front")
Back_Darks_J179=string_list(86,96)
Back_Output_J179=extract_subject("003","085",Back_Darks_J179,"HAORB_J179_back")

Front_Darks_5316=string_list(130,139)
Front_Output_5316=extract_subject("003","129",Front_Darks_5316,"HACA_5316_front")
Back_Darks_5316=string_list(141,150)
Back_Output_5316=extract_subject("003","140",Back_Darks_5316,"HACA_5316_back")


#females 

#sesh 2
Front_Darks_J295=string_list(91,100)
Front_Output_J295=extract_subject("002","090",Front_Darks_J295,"HACOE_J295_front")
Back_Darks_J295=string_list(102,111)
Back_Output_J295=extract_subject("002","101",Back_Darks_J295,"HACOE_J295_back")

#sesh 3
Front_Darks_Nancy=string_list(119,128)
Front_Output_Nancy=extract_subject("003","118",Front_Darks_Nancy,"HADO_Nancy_front")
Back_Darks_Nancy=string_list(108,117)
Back_Output_Nancy=extract_subject("003","107",Back_Darks_Nancy,"HADO_Nancy_back")

where="../apr_06_2022"
os.chdir(where)

Front_Darks_J89=string_list(10,20)
Front_Output_J89=extract_subject("000","009",Front_Darks_J89,"HACA_J89_front")
Back_Darks_J89=string_list(22,31)
Back_Output_J89=extract_subject("000","021",Back_Darks_J89,"HACA_J89_back")


Front_Darks_5095=string_list(33,44)
Front_Output_5095=extract_subject("000","032",Front_Darks_5095,"HACOE_5095_front")
Back_Darks_5095=string_list(46,56)
Back_Output_5095=extract_subject("000","045",Back_Darks_5095,"HACOE_5095_back")

Front_Darks_3675=string_list(6,15)
Front_Output_3675=extract_subject("001","005",Front_Darks_3675,"HADO_3675_front")
Back_Darks_3675=string_list(17,26)
Back_Output_3675=extract_subject("001","016",Back_Darks_3675,"HADO_3675_back")


# 420 blaze it
where="../apr_20_2022"
os.chdir(where)

Front_Darks_4267=string_list(6,16)
Front_Output_4267=extract_subject("000","005",Front_Darks_4267,"HATR_4267_front")
Back_Darks_4267=string_list(26,36)
Back_Output_4267=extract_subject("000","017",Back_Darks_4267,"HATR_4267_back")

Front_Darks_3936=string_list(6,16)
Front_Output_3936=extract_subject("001","005",Front_Darks_3936,"HAPU_3936_front")
Back_Darks_3936=string_list(18,26)
Back_Output_3936=extract_subject("001","017",Back_Darks_3936,"HAPU_3936_back")

#multiples here that don't have recorded image numbers, check it out

where="../jul_12_2022"
os.chdir(where)

Front_Darks_3607=string_list(6,15)
Front_Output_3607=extract_subject("000","005",Front_Darks_3607,"HAPU_3607_front")
Back_Darks_3607=string_list(17,26)
Back_Output_3607=extract_subject("000","016",Back_Darks_3607,"HAPU_3607_back")

Front_Darks_3394=string_list(28,37)
Front_Output_3394=extract_subject("000","027",Front_Darks_3394,"HAPU_3394_front")
Back_Darks_3394=string_list(39,48)
Back_Output_3394=extract_subject("000","038",Back_Darks_3394,"HAPU_3394_back")

Front_Darks_3385=string_list(50,59)
Front_Output_3385=extract_subject("000","049",Front_Darks_3385,"HAPU_3385_front")
Back_Darks_3385=string_list(61,70)
Back_Output_3385=extract_subject("000","060",Back_Darks_3385,"HAPU_3385_back")

Front_Darks_3384=string_list(72,81)
Front_Output_3384=extract_subject("000","071",Front_Darks_3384,"HAPU_3384_front")
Back_Darks_3384=string_list(83,92)
Back_Output_3384=extract_subject("000","082",Back_Darks_3384,"HAPU_3384_back")
#session 1
Front_Darks_3595=string_list(17,26)
Front_Output_3595=extract_subject("001","016",Front_Darks_3595,"HAPU_3595_front")
Back_Darks_3595=string_list(28,37)
Back_Output_3595=extract_subject("001","027",Back_Darks_3595,"HAPU_3595_back")

Front_Darks_4625=string_list(39,48)
Front_Output_4625=extract_subject("001","038",Front_Darks_4625,"HAPY_4625_front")
Back_Darks_4625=string_list(50,59)
Back_Output_4625=extract_subject("001","049",Back_Darks_4625,"HAPY_4625_back")

Front_Darks_3590=string_list(61,70)
Front_Output_3590=extract_subject("001","060",Front_Darks_3590,"HAPU_3590_front")
Back_Darks_3590=string_list(72,81)
Back_Output_3590=extract_subject("001","071",Back_Darks_3590,"HAPU_3590_back")

Front_Darks_4266=string_list(83,92)
Front_Output_4266=extract_subject("001","082",Front_Darks_4266,"HATR_4266_front")
Back_Darks_4266=string_list(94,104)
Back_Output_4266=extract_subject("001","093",Back_Darks_4266,"HATR_4266_back")

#session 2
Front_Darks_44=string_list(6,15)
Front_Output_44=extract_subject("002","005",Front_Darks_44,"HAPU_44_front")
Back_Darks_44=string_list(17,27)
Back_Output_44=extract_subject("002","016",Back_Darks_44,"HAPU_44_back")

Front_Darks_4645=string_list(29,38)
Front_Output_4645=extract_subject("002","028",Front_Darks_4645,"HADOR_4645_front")
Back_Darks_4645=string_list(40,49)
Back_Output_4645=extract_subject("002","039",Back_Darks_4645,"HADOR_4645_back")

Front_Darks_3593=string_list(51,60)
Front_Output_3593=extract_subject("002","050",Front_Darks_3593,"HAPU_3593_front")
Back_Darks_3593=string_list(62,74)
Back_Output_3593=extract_subject("002","061",Back_Darks_3593,"HAPU_3593_back")

Front_Darks_3389=string_list(76,85)
Front_Output_3389=extract_subject("002","075",Front_Darks_3389,"HAPU_3389_front")
Back_Darks_3389=string_list(87,96)
Back_Output_3389=extract_subject("002","086",Back_Darks_3389,"HAPU_3389_back")


#session 3
Front_Darks_3591=string_list(6,15)
Front_Output_3591=extract_subject("003","005",Front_Darks_3591,"HAPU_3591_front")

Front_Darks_3393=string_list(17,26)
Front_Output_3393=extract_subject("003","016",Front_Darks_3393,"HAPU_3393_front")
Back_Darks_3393=string_list(28,37)
Back_Output_3393=extract_subject("003","027",Back_Darks_3393,"HAPU_3393_back")

#july 13th
where="../jul_13_2022"
os.chdir(where)

Front_Darks_3674=string_list(8,17)
Front_Output_3674=extract_subject("000","007",Front_Darks_3674,"HAPU_3674_front")
Back_Darks_3674=string_list(20,29)
Back_Output_3674=extract_subject("000","019",Back_Darks_3674,"HAPU_3674_back")

Front_Darks_3401=string_list(31,40)
Front_Output_3401=extract_subject("000","030",Front_Darks_3401,"HAPU_3401_front")
Back_Darks_3401=string_list(42,51)
Back_Output_3401=extract_subject("000","041",Back_Darks_3401,"HAPU_3401_back")

Front_Darks_742=string_list(53,62)
Front_Output_742=extract_subject("000","052",Front_Darks_742,"HAPY_742_front")
Back_Darks_742=string_list(64,73)
Back_Output_742=extract_subject("000","063",Back_Darks_742,"HAPY_742_back")

Front_Darks_823=string_list(75,84)
Front_Output_823=extract_subject("000","074",Front_Darks_823,"HAVI_823_front")
Back_Darks_823=string_list(86,95)
Back_Output_823=extract_subject("000","085",Back_Darks_823,"HAVI_823_back")

Front_Darks_3554=string_list(97,106)
Front_Output_3554=extract_subject("000","096",Front_Darks_3554,"HAPY_3554_front")
Back_Darks_3554=string_list(108,117)
Back_Output_3554=extract_subject("000","107",Back_Darks_3554,"HAPY_3554_back")

Front_Darks_3872=string_list(6,15)
Front_Output_3872=extract_subject("001","005",Front_Darks_3872,"HAPY_3872_front")
Back_Darks_3872=string_list(18,27)
Back_Output_3872=extract_subject("001","017",Back_Darks_3872,"HAPY_3872_back")

Front_Darks_3463=string_list(29,38)
Front_Output_3463=extract_subject("001","028",Front_Darks_3463,"HAOR_3463_front")
Back_Darks_3463=string_list(40,49)
Back_Output_3463=extract_subject("001","039",Back_Darks_3463,"HAOR_3463_back")

Front_Darks_3681=string_list(51,60)
Front_Output_3681=extract_subject("001","050",Front_Darks_3681,"HADO_3681_front")
Back_Darks_3681=string_list(62,71)
Back_Output_3681=extract_subject("001","061",Back_Darks_3681,"HADO_3681_back")

Front_Darks_314=string_list(73,82)
Front_Output_314=extract_subject("001","072",Front_Darks_314,"HAVI_314_front")
Back_Darks_314=string_list(84,93)
Back_Output_314=extract_subject("001","083",Back_Darks_314,"HAVI_314_back")

Front_Darks_3540=string_list(95,104)
Front_Output_3540=extract_subject("001","094",Front_Darks_3540,"HAVI_3540_front")
Back_Darks_3540=string_list(106,115)
Back_Output_3540=extract_subject("001","105",Back_Darks_3540,"HAVI_3540_back")

Front_Darks_3553=string_list(117,126)
Front_Output_3553=extract_subject("001","116",Front_Darks_3553,"HAPY_3553_front")
Back_Darks_3553=string_list(128,137)
Back_Output_3553=extract_subject("001","127",Back_Darks_3553,"HAPY_3553_back")

Front_Darks_D1=string_list(6,15)
Front_Output_D1=extract_subject("002","005",Front_Darks_D1,"HADOR_D1_front")
Back_Darks_D1=string_list(17,26)
Back_Output_D1=extract_subject("002","016",Back_Darks_D1,"HADOR_D1_back")

Front_Darks_779=string_list(28,37)
Front_Output_779=extract_subject("002","027",Front_Darks_779,"HAPY_779_front")
Back_Darks_779=string_list(17,26)
Back_Output_779=extract_subject("002","016",Back_Darks_779,"HAPY_779_back")

Front_Darks_Dave=string_list(50,59)
Front_Output_Dave=extract_subject("002","049",Front_Darks_Dave,"HAPU_Dave_front")
Back_Darks_Dave=string_list(61,70)
Back_Output_Dave=extract_subject("002","060",Back_Darks_Dave,"HAPU_Dave_back")

Front_Darks_3544=string_list(73,82)
Front_Output_3544=extract_subject("002","072",Front_Darks_3544,"HAPY_3544_front")
Back_Darks_3544=string_list(84,93)
Back_Output_3544=extract_subject("002","083",Back_Darks_3544,"HAPY_3544_back")

#figure out 1126 here

Front_Darks_4643=string_list(6,15)
Front_Output_4643=extract_subject("003","005",Front_Darks_4643,"HAPY_4643_front")
Back_Darks_4643=string_list(17,26)
Back_Output_4643=extract_subject("003","016",Back_Darks_4643,"HAPY_4643_back")

Front_Darks_3545=string_list(28,37)
Front_Output_3545=extract_subject("003","027",Front_Darks_3545,"HAVI_3545_front")
Back_Darks_3545=string_list(39,48)
Back_Output_3545=extract_subject("003","038",Back_Darks_3545,"HAVI_3545_back")

Front_Darks_3437=string_list(50,59)
Front_Output_3437=extract_subject("003","049",Front_Darks_3437,"HADO_3437_front")
Back_Darks_3437=string_list(61,70)
Back_Output_3437=extract_subject("003","060",Back_Darks_3437,"HADO_3437_back")

Front_Darks_3551=string_list(72,81)
Front_Output_3551=extract_subject("003","071",Front_Darks_3551,"HAVI_3551_front")
Back_Darks_3551=string_list(83,92)
Back_Output_3551=extract_subject("003","082",Back_Darks_3551,"HAVI_3551_back")

Front_Darks_3542=string_list(94,103)
Front_Output_3542=extract_subject("003","093",Front_Darks_3542,"HAVI_3542_front")
Back_Darks_3542=string_list(106,116)
Back_Output_3542=extract_subject("003","105",Back_Darks_3542,"HAVI_3542_back")

Front_Darks_3880=string_list(6,15)
Front_Output_3880=extract_subject("004","005",Front_Darks_3880,"HAPY_3880_front")
Back_Darks_3880=string_list(17,26)
Back_Output_3880=extract_subject("004","016",Back_Darks_3880,"HAPY_3880_back")

Front_Darks_SR004=string_list(28,39)
Front_Output_SR004=extract_subject("004","027",Front_Darks_SR004,"HAVI_SR004_front")
Back_Darks_SR004=string_list(41,50)
Back_Output_SR004=extract_subject("004","040",Back_Darks_SR004,"HAVI_SR004_back")

Front_Darks_3730=string_list(52,63)
Front_Output_3730=extract_subject("004","051",Front_Darks_3730,"HAPY_3730_front")
Back_Darks_3730=string_list(65,74)
Back_Output_3730=extract_subject("004","064",Back_Darks_3730,"HAPY_3730_back")

Front_Darks_3563=string_list(76,85)
Front_Output_3563=extract_subject("004","075",Front_Darks_3563,"HAVI_3563_front")
Back_Darks_3563=string_list(88,97)
Back_Output_3563=extract_subject("004","087",Back_Darks_3563,"HAVI_3563_back")

Front_Darks_will=string_list(99,108)
Front_Output_will=extract_subject("004","098",Front_Darks_will,"HAPY_will_front")
#recorded only the 4 images on the sheet, double check output
Back_Darks_will=string_list(136,140)
Back_Output_will=extract_subject("004","135",Back_Darks_will,"HAPY_will_back")

#did we really take this many?
Front_Darks_4571=string_list(110,123)
Front_Output_4571=extract_subject("004","109",Front_Darks_4571,"HAVI_4571_front")
Back_Darks_4571=string_list(125,134)
Back_Output_4571=extract_subject("004","124",Back_Darks_4571,"HAVI_4571_back")

#change date
#july 14th
where="../jul_14_2022"
os.chdir(where)

#figure out 1656 sp. here
Front_Darks_3682=string_list(28,37)
Front_Output_3682=extract_subject("000","027",Front_Darks_3682,"HADO_3682_front")
Back_Darks_3682=string_list(39,48)
Back_Output_3682=extract_subject("000","038",Back_Darks_3682,"HADO_3682_back")

Front_Darks_3460=string_list(50,59)
Front_Output_3460=extract_subject("000","049",Front_Darks_3460,"HAOR_3460_front")
Back_Darks_3460=string_list(61,70)
Back_Output_3460=extract_subject("000","060",Back_Darks_3460,"HAOR_3460_back")

Front_Darks_3723=string_list(72,81)
Front_Output_3723=extract_subject("000","071",Front_Darks_3723,"HAPY_3723_front")
Back_Darks_3723=string_list(83,94)
Back_Output_3723=extract_subject("000","082",Back_Darks_3723,"HAPY_3723_back")

Front_Darks_randy=string_list(96,105)
Front_Output_randy=extract_subject("000","095",Front_Darks_randy,"HAFA_randy_front")
Back_Darks_randy=string_list(107,116)
Back_Output_randy=extract_subject("000","106",Back_Darks_randy,"HAFA_randy_back")

Front_Darks_3425=string_list(7,16)
Front_Output_3425=extract_subject("001","006",Front_Darks_3425,"HADO_3425_front")
Back_Darks_3425=string_list(18,27)
Back_Output_3425=extract_subject("001","017",Back_Darks_3425,"HADO_3425_back")

Front_Darks_4645=string_list(29,38)
Front_Output_4645=extract_subject("001","028",Front_Darks_4645,"HADOR_4645_front")
Back_Darks_4645=string_list(40,49)
Back_Output_4645=extract_subject("001","039",Back_Darks_4645,"HADOR_4645_back")

Front_Darks_chris=string_list(51,60)
Front_Output_chris=extract_subject("001","050",Front_Darks_chris,"HAPU_chris_front")
Back_Darks_chris=string_list(62,71)
Back_Output_chris=extract_subject("001","061",Back_Darks_chris,"HAPU_chris_back")

Front_Darks_3377=string_list(73,83)
Front_Output_3377=extract_subject("001","072",Front_Darks_3377,"HAPU_3377_front")
Back_Darks_3377=string_list(85,95)
Back_Output_3377=extract_subject("001","084",Back_Darks_3377,"HAPU_3377_back")

Front_Darks_dotty=string_list(97,106)
Front_Output_dotty=extract_subject("001","096",Front_Darks_dotty,"HADOR_dotty_front")
Back_Darks_dotty=string_list(108,117)
Back_Output_dotty=extract_subject("001","107",Back_Darks_dotty,"HADOR_dotty_back")

Front_Darks_3420=string_list(6,15)
Front_Output_3420=extract_subject("002","005",Front_Darks_3420,"HADOR_3420_front")
Back_Darks_3420=string_list(17,26)
Back_Output_3420=extract_subject("002","016",Back_Darks_3420,"HADOR_3420_back")

Front_Darks_3717=string_list(28,37)
Front_Output_3717=extract_subject("002","027",Front_Darks_3717,"HAPY_3717_front")
Back_Darks_3717=string_list(39,48)
Back_Output_3717=extract_subject("002","038",Back_Darks_3717,"HAPY_3717_back")

#female spider 1194

Front_Darks_3383=string_list(72,81)
Front_Output_3383=extract_subject("002","071",Front_Darks_3383,"HAPY_3383_front")
Back_Darks_3383=string_list(83,92)
Back_Output_3383=extract_subject("002","082",Back_Darks_3383,"HAPY_3383_back")

Front_Darks_3398=string_list(94,103)
Front_Output_3398=extract_subject("002","093",Front_Darks_3398,"HADO_3398_front")
Back_Darks_3398=string_list(105,114)
Back_Output_3398=extract_subject("002","104",Back_Darks_3398,"HADO_3398_back")


where="../jul_18_2022"
os.chdir(where)


Front_Darks_3405=string_list(8,17)
Front_Output_3405=extract_subject("000","007",Front_Darks_3405,"HADO_3405_front")
Back_Darks_3405=string_list(19,28)
Back_Output_3405=extract_subject("000","018",Back_Darks_3405,"HADO_3405_back")

Front_Darks_3421=string_list(3,40)
Front_Output_3421=extract_subject("000","029",Front_Darks_3421,"HADO_3421_front")
Back_Darks_3421=string_list(42,51)
Back_Output_3421=extract_subject("000","041",Back_Darks_3421,"HADO_3421_back")

Front_Darks_3416=string_list(53,62)
Front_Output_3416=extract_subject("000","052",Front_Darks_3416,"HADO_3416_front")
Back_Darks_3416=string_list(64,73)
Back_Output_3416=extract_subject("000","063",Back_Darks_3416,"HADO_3416_back")

Front_Darks_3567=string_list(75,85)
Front_Output_3567=extract_subject("000","074",Front_Darks_3567,"HADO_3567_front")
Back_Darks_3567=string_list(87,97)
Back_Output_3567=extract_subject("000","086",Back_Darks_3567,"HADO_3567_back")

Front_Darks_3685=string_list(99,108)
Front_Output_3685=extract_subject("000","098",Front_Darks_3685,"HAVI_3685_front")
Back_Darks_3685=string_list(110,119)
Back_Output_3685=extract_subject("000","109",Back_Darks_3685,"HAVI_3685_back")

Front_Darks_3438=string_list(6,16)
Front_Output_3438=extract_subject("001","005",Front_Darks_3438,"HADO_3438_front")
Back_Darks_3438=string_list(18,27)
Back_Output_3438=extract_subject("001","017",Back_Darks_3438,"HADO_3438_back")

Front_Darks_3399=string_list(29,38)
Front_Output_3399=extract_subject("001","028",Front_Darks_3399,"HADO_3399_front")
Back_Darks_3399=string_list(40,49)
Back_Output_3399=extract_subject("001","039",Back_Darks_3399,"HADO_3399_back")

Front_Darks_3647=string_list(51,60)
Front_Output_3647=extract_subject("001","050",Front_Darks_3647,"HADO_3647_front")
Back_Darks_3647=string_list(62,71)
Back_Output_3647=extract_subject("001","061",Back_Darks_3647,"HADO_3647_back")

Front_Darks_3380=string_list(73,82)
Front_Output_3380=extract_subject("001","072",Front_Darks_3380,"HADO_3380_front")
Back_Darks_3380=string_list(84,95)
Back_Output_3380=extract_subject("001","083",Back_Darks_3380,"HADO_3380_back")

Front_Darks_3561=string_list(97,106)
Front_Output_3561=extract_subject("001","096",Front_Darks_3561,"HADO_3561_front")
Back_Darks_3561=string_list(108,117)
Back_Output_3561=extract_subject("001","107",Back_Darks_3561,"HADO_3561_back")

Front_Darks_36671=string_list(6,15)
Front_Output_3667=extract_subject("002","005",Front_Darks_3667,"HADO_3667_front")
Back_Darks_3667=string_list(17,26)
Back_Output_3667=extract_subject("002","016",Back_Darks_3667,"HADO_3667_back")

Front_Darks_3432=string_list(28,37)
Front_Output_3432=extract_subject("002","027",Front_Darks_3432,"HADO_3432_front")
Back_Darks_3432=string_list(39,48)
Back_Output_3432=extract_subject("002","038",Back_Darks_3432,"HADO_3432_back")

Front_Darks_3423=string_list(50,59)
Front_Output_3423=extract_subject("002","049",Front_Darks_3423,"HADO_3423_front")
Back_Darks_3423=string_list(61,70)
Back_Output_3423=extract_subject("002","060",Back_Darks_3423,"HADO_3423_back")

Front_Darks_3422=string_list(72,81)
Front_Output_3422=extract_subject("002","071",Front_Darks_3422,"HADO_3422_front")
Back_Darks_3422=string_list(83,92)
Back_Output_3422=extract_subject("002","082",Back_Darks_3422,"HADO_3422_back")

Front_Darks_O259=string_list(94,103)
Front_Output_O259=extract_subject("002","093",Front_Darks_3422,"HADO_3422_front")
Back_Darks_3422=string_list(105,114)
Back_Output_3422=extract_subject("002","104",Back_Darks_3422,"HADO_3422_back")

where="../jul_20_2022"
os.chdir(where)

Front_Darks_991=string_list(6,15)
Front_Output_991=extract_subject("000","005",Front_Darks_991,"HAGE_991_front")
Back_Darks_991=string_list(17,26)
Back_Output_991=extract_subject("000","016",Back_Darks_991,"HAGE_991_back")

Front_Darks_3625=string_list(29,38)
Front_Output_3625=extract_subject("000","028",Front_Darks_3625,"HAGE_3625_front")
Back_Darks_3625=string_list(51,60)
Back_Output_3625=extract_subject("000","050",Back_Darks_3625,"HAGE_3625_back")

Front_Darks_3623=string_list(62,71)
Front_Output_3623=extract_subject("000","061",Front_Darks_3623,"HAGE_3623_front")
Back_Darks_3623=string_list(73,82)
Back_Output_3623=extract_subject("000","072",Back_Darks_3623,"HAGE_3623_back")

Front_Darks_3620=string_list(84,93)
Front_Output_3620=extract_subject("000","083",Front_Darks_3620,"HAGE_3623_front")
Back_Darks_3620=string_list(95,104)
Back_Output_3620=extract_subject("000","094",Back_Darks_3620,"HAGE_3623_back")

Front_Darks_1017=string_list(106,115)
Front_Output_1017=extract_subject("000","105",Front_Darks_1017,"HAGE_1017_front")
Back_Darks_1017=string_list(117,126)
Back_Output_1017=extract_subject("000","116",Back_Darks_1017,"HAGE_1017_back")

Front_Darks_1644=string_list(6,15)
Front_Output_1644=extract_subject("001","005",Front_Darks_1644,"HAGE_1644_front")
Back_Darks_1644=string_list(17,26)
Back_Output_1644=extract_subject("001","016",Back_Darks_1644,"HAGE_1644_back")

Front_Darks_3624=string_list(28,38)
Front_Output_3624=extract_subject("001","027",Front_Darks_3624,"HAGE_3624_front")
Back_Darks_3624=string_list(40,49)
Back_Output_3624=extract_subject("001","039",Back_Darks_3624,"HAGE_3624_back")

Front_Darks_3584=string_list(51,61)
Front_Output_3584=extract_subject("001","050",Front_Darks_3584,"HAGE_3584_front")
Back_Darks_3584=string_list(63,72)
Back_Output_3584=extract_subject("001","062",Back_Darks_3584,"HAGE_3584_back")

Front_Darks_301=string_list(74,83)
Front_Output_301=extract_subject("001","073",Front_Darks_301,"HAHI_301_front")
Back_Darks_301=string_list(85,94)
Back_Output_301=extract_subject("001","084",Back_Darks_301,"HAHI_301_back")

Front_Darks_3577=string_list(96,105)
Front_Output_3577=extract_subject("001","095",Front_Darks_3577,"HAGE_3577_front")
Back_Darks_3577=string_list(107,116)
Back_Output_3577=extract_subject("001","106",Back_Darks_3577,"HAGE_3577_back")

Front_Darks_1644=string_list(6,15)
Front_Output_1644=extract_subject("002","005",Front_Darks_1644,"HAGE_1644_front")
Back_Darks_1644=string_list(17,26)
Back_Output_1644=extract_subject("002","016",Back_Darks_1644,"HAGE_1644_back")

Front_Darks_4372=string_list(28,37)
Front_Output_4372=extract_subject("002","027",Front_Darks_4372,"HAHI_4372_front")
Back_Darks_4372=string_list(39,48)
Back_Output_4372=extract_subject("002","038",Back_Darks_4372,"HAHI_4372_back")

Front_Darks_840=string_list(50,59)
Front_Output_840=extract_subject("002","049",Front_Darks_840,"HAHI_840_front")
Back_Darks_840=string_list(61,70)
Back_Output_840=extract_subject("002","060",Back_Darks_840,"HAHI_840_back")

Front_Darks_1019=string_list(72,81)
Front_Output_1019=extract_subject("002","071",Front_Darks_1019,"HAGE_1019_front")
Back_Darks_1019=string_list(84,93)
Back_Output_1019=extract_subject("002","083",Back_Darks_1019,"HAGE_1019_back")

Front_Darks_4378=string_list(95,105)
Front_Output_4378=extract_subject("002","094",Front_Darks_4378,"HAHI_4378_front")
Back_Darks_4378=string_list(107,116)
Back_Output_4378=extract_subject("002","106",Back_Darks_4378,"HAHI_4378_back")

Front_Darks_3580=string_list(118,127)
Front_Output_3580=extract_subject("002","117",Front_Darks_3580,"HAGE_3580_front")
Back_Darks_3580=string_list(129,138)
Back_Output_3580=extract_subject("002","128",Back_Darks_3580,"HAGE_3580_back")

Front_Darks_3611=string_list(6,15)
Front_Output_3611=extract_subject("003","005",Front_Darks_3611,"HAGE_3611_front")
Back_Darks_3611=string_list(20,29)
Back_Output_3611=extract_subject("003","016",Back_Darks_3611,"HAGE_3611_back")

Front_Darks_3614=string_list(31,40)
Front_Output_3614=extract_subject("003","030",Front_Darks_3614,"HAGE_3614_front")
Back_Darks_3614=string_list(42,52)
Back_Output_3614=extract_subject("003","041",Back_Darks_3614,"HAGE_3614_back")

Front_Darks_3585=string_list(54,64)
Front_Output_3585=extract_subject("003","053",Front_Darks_3585,"HAGE_3585_front")
Back_Darks_3585=string_list(66,75)
Back_Output_3585=extract_subject("003","065",Back_Darks_3585,"HAGE_3585_back")

Front_Darks_3693=string_list(77,86)
Front_Output_3693=extract_subject("003","076",Front_Darks_3693,"HAGE_3693_front")
Back_Darks_3693=string_list(88,97)
Back_Output_3693=extract_subject("003","087",Back_Darks_3693,"HAGE_3693_back")

Front_Darks_3578=string_list(99,108)
Front_Output_3578=extract_subject("003","098",Front_Darks_3578,"HAGE_3578_front")
Back_Darks_3578=string_list(110,119)
Back_Output_3578=extract_subject("003","109",Back_Darks_3578,"HAGE_3578_back")

where="../jul_25_2022"
os.chdir(where)

Front_Darks_219=string_list(6,15)
Front_Output_219=extract_subject("000","005",Front_Darks_219,"HAPY_219_front")
Back_Darks_219=string_list(18,27)
Back_Output_219=extract_subject("000","017",Back_Darks_219,"HAPY_219_back")

Front_Darks_1207=string_list(29,38)
Front_Output_1207=extract_subject("000","028",Front_Darks_1207,"HAGE_1207_front")
Back_Darks_1207=string_list(40,49)
Back_Output_1207=extract_subject("000","039",Back_Darks_1207,"HAGE_1207_back")

Front_Darks_4810=string_list(51,60)
Front_Output_4810=extract_subject("000","050",Front_Darks_4810,"HAME_4810_front")
Back_Darks_4810=string_list(62,71)
Back_Output_4810=extract_subject("000","061",Back_Darks_4810,"HAME_4810_back")

Front_Darks_38special=string_list(73,82)
Front_Output_38special=extract_subject("000","072",Front_Darks_38special,"HAGE_38special_front")
Back_Darks_38special=string_list(84,93)
Back_Output_38special=extract_subject("000","083",Back_Darks_38special,"HAGE_38special_back")

Front_Darks_4829=string_list(95,104)
Front_Output_4829=extract_subject("000","094",Front_Darks_4829,"HAGE_4829_front")
Back_Darks_4829=string_list(106,115)
Back_Output_4829=extract_subject("000","105",Back_Darks_4829,"HAGE_4829_back")

Front_Darks_1578=string_list(6,15)
Front_Output_1578=extract_subject("002","005",Front_Darks_1578,"HAGE_1578_front")
Back_Darks_1578=string_list(17,26)
Back_Output_1578=extract_subject("002","016",Back_Darks_1578,"HAGE_1578_back")

Front_Darks_923=string_list(28,37)
Front_Output_923=extract_subject("002","027",Front_Darks_923,"HAHI_923_front")
Back_Darks_923=string_list(39,48)
Back_Output_923=extract_subject("002","038",Back_Darks_923,"HAHI_923_back")

Front_Darks_656=string_list(51,60)
Front_Output_656=extract_subject("002","050",Front_Darks_656,"HAHI_656_front")
Back_Darks_656=string_list(62,71)
Back_Output_656=extract_subject("002","061",Back_Darks_656,"HAHI_656_back")

where="../jul_26_2022"
os.chdir(where)

Front_Darks_3612=string_list(6,15)
Front_Output_3612=extract_subject("000","005",Front_Darks_3612,"HAGE_3612_front")
Back_Darks_3612=string_list(17,26)
Back_Output_3612=extract_subject("000","016",Back_Darks_3612,"HAGE_3612_back")

Front_Darks_4804=string_list(28,39)
Front_Output_4804=extract_subject("000","027",Front_Darks_4804,"HAME_4804_front")
Back_Darks_4804=string_list(41,50)
Back_Output_4804=extract_subject("000","040",Back_Darks_4804,"HAME_4804_back")

Front_Darks_3620=string_list(52,61)
Front_Output_3620=extract_subject("000","051",Front_Darks_3620,"HAGE_3620_front")
Back_Darks_3620=string_list(63,76)
Back_Output_3620=extract_subject("000","062",Back_Darks_3620,"HAGE_3620_back")

Front_Darks_4761=string_list(6,16)
Front_Output_4761=extract_subject("001","005",Front_Darks_4761,"HATE_4761_front")
Back_Darks_4761=string_list(18,27)
Back_Output_4761=extract_subject("001","017",Back_Darks_4761,"HATE_4761_back")

Front_Darks_Eugenia=string_list(29,39)
Front_Output_Eugenia=extract_subject("001","028",Front_Darks_Eugenia,"HAME_Eugenia_front")
Back_Darks_Eugenia=string_list(41,50)
Back_Output_Eugenia=extract_subject("001","040",Back_Darks_Eugenia,"HAME_Eugenia_back")

Front_Darks_4774=string_list(52,61)
Front_Output_4774=extract_subject("001","051",Front_Darks_4774,"HATE_4774_front")
Back_Darks_4774=string_list(63,73)
Back_Output_4774=extract_subject("001","062",Back_Darks_4774,"HATE_4774_back")

Front_Darks_4825=string_list(75,84)
Front_Output_4825=extract_subject("001","074",Front_Darks_4825,"HAME_4825_front")
Back_Darks_4825=string_list(86,95)
Back_Output_4825=extract_subject("001","085",Back_Darks_4825,"HAME_4825_back")

Front_Darks_87=string_list(97,106)
Front_Output_87=extract_subject("001","096",Front_Darks_87,"HAME_87_front")
Back_Darks_87=string_list(108,117)
Back_Output_87=extract_subject("001","107",Back_Darks_87,"HAME_87_back")


where="../jul_28_2022"
os.chdir(where)

Front_Darks_4304=string_list(6,15)
Front_Output_4304=extract_subject("000","005",Front_Darks_4304,"HAEL_4304_front")
Back_Darks_4304=string_list(17,26)
Back_Output_4304=extract_subject("001","016",Back_Darks_4304,"HAEL_4304_back")

Front_Darks_4772=string_list(28,37)
Front_Output_4772=extract_subject("000","027",Front_Darks_4772,"HATE_4772_front")
Back_Darks_4772=string_list(39,48)
Back_Output_4772=extract_subject("000","038",Back_Darks_4772,"HAGE_4772_back")

Front_Darks_4762=string_list(50,59)
Front_Output_4762=extract_subject("000","049",Front_Darks_4762,"HATE_4762_front")
Back_Darks_4762=string_list(61,71)
Back_Output_4762=extract_subject("000","060",Back_Darks_4762,"HATE_4762_back")

Front_Darks_O215=string_list(73,83)
Front_Output_O215=extract_subject("000","072",Front_Darks_O215,"HAPY_O215_front")
Back_Darks_O215=string_list(85,95)
Back_Output_O215=extract_subject("000","084",Back_Darks_O215,"HAPY_O215_back")

Front_Darks_66=string_list(97,106)
Front_Output_66=extract_subject("000","096",Front_Darks_66,"HATE_66_front")
Back_Darks_66=string_list(108,117)
Back_Output_66=extract_subject("000","107",Back_Darks_66,"HATE_66_back")

Front_Darks_D1=string_list(119,128)
Front_Output_D1=extract_subject("000","118",Front_Darks_D1,"HAGE_D1_front")
Back_Darks_D1=string_list(130,139)
Back_Output_D1=extract_subject("000","129",Back_Darks_D1,"HAGE_D1_back")

where="../jul_29_2022"
os.chdir(where)

Front_Darks_O66=string_list(6,15)
Front_Output_O66=extract_subject("000","005",Front_Darks_O66,"HAPY_O66_front")
Back_Darks_O66=string_list(17,26)
Back_Output_O66=extract_subject("000","016",Back_Darks_O66,"HAPY_O66_back")

Front_Darks_O122=string_list(28,37)
Front_Output_O122=extract_subject("000","027",Front_Darks_O122,"HAPY_O122_front")
Back_Darks_O122=string_list(39,48)
Back_Output_O122=extract_subject("000","038",Back_Darks_O122,"HAPY_O122_back")

Front_Darks_O235=string_list(50,59)
Front_Output_O235=extract_subject("000","049",Front_Darks_O235,"HAPY_O235_front")
Back_Darks_O235=string_list(61,70)
Back_Output_O235=extract_subject("000","060",Back_Darks_O235,"HAPY_O235_back")

Front_Darks_O96=string_list(72,81)
Front_Output_O96=extract_subject("000","071",Front_Darks_O96,"HAPY_O96_front")
Back_Darks_O96=string_list(83,92)
Back_Output_O96=extract_subject("000","082",Back_Darks_O96,"HAPY_O96_back")

Front_Darks_O160=string_list(94,105)
Front_Output_O160=extract_subject("000","093",Front_Darks_O160,"HAPY_O160_front")
Back_Darks_O160=string_list(107,116)
Back_Output_O160=extract_subject("000","106",Back_Darks_O160,"HAPY_O160_back")


where="../aug_02_2022"
os.chdir(where)

Front_Darks_D4=string_list(6,15)
Front_Output_D4=extract_subject("000","005",Front_Darks_D4,"HAME_D4_front")
Back_Darks_D4=string_list(17,26)
Back_Output_D4=extract_subject("000","016",Back_Darks_D4,"HAME_D4_back")

Front_Darks_4817=string_list(28,37)
Front_Output_4817=extract_subject("000","027",Front_Darks_4817,"HAME_4817_front")
Back_Darks_4817=string_list(39,48)
Back_Output_4817=extract_subject("000","038",Back_Darks_4817,"HAME_4817_back")

Front_Darks_4768=string_list(50,59)
Front_Output_4768=extract_subject("000","049",Front_Darks_4768,"HATE_4768_front")
Back_Darks_4768=string_list(61,70)
Back_Output_4768=extract_subject("000","060",Back_Darks_4768,"HATE_4768_back")

Front_Darks_4307=string_list(72,81)
Front_Output_4307=extract_subject("000","071",Front_Darks_4307,"HAEL_4307_front")
Back_Darks_4307=string_list(83,93)
Back_Output_4307=extract_subject("000","082",Back_Darks_4307,"HAEL_4307_back")

Front_Darks_4319=string_list(95,106)
Front_Output_4319=extract_subject("000","094",Front_Darks_4319,"HAME_4319_front")
Back_Darks_4319=string_list(108,117)
Back_Output_4319=extract_subject("000","107",Back_Darks_4319,"HAME_4319_back")

Front_Darks_4310=string_list(6,16)
Front_Output_4310=extract_subject("001","005",Front_Darks_4310,"HAEL_4310_front")
Back_Darks_4310=string_list(18,27)
Back_Output_4310=extract_subject("001","017",Back_Darks_4310,"HAEL_4310_back")

Front_Darks_75=string_list(29,38)
Front_Output_75=extract_subject("001","028",Front_Darks_75,"HAME_75_front")
Back_Darks_75=string_list(40,49)
Back_Output_75=extract_subject("001","039",Back_Darks_75,"HAME_75_back")

Front_Darks_4766=string_list(51,60)
Front_Output_4766=extract_subject("001","050",Front_Darks_4766,"HATE_4766_front")
Back_Darks_4766=string_list(62,71)
Back_Output_4766=extract_subject("001","061",Back_Darks_4766,"HATE_4766_back")

Front_Darks_4120not=string_list(73,82)
Front_Output_4120not=extract_subject("001","072",Front_Darks_4120not,"HAME_4120not_front")
Back_Darks_4120not=string_list(84,93)
Back_Output_4120not=extract_subject("001","083",Back_Darks_4120not,"HAME_4120not_back")

Front_Darks_4303=string_list(95,104)
Front_Output_4303=extract_subject("001","094",Front_Darks_4303,"HAEL_4303_front")
Back_Darks_4303=string_list(107,116)
Back_Output_4303=extract_subject("001","106",Back_Darks_4303,"HAEL_4303_back")

Front_Darks_4294=string_list(118,127)
Front_Output_4294=extract_subject("001","117",Front_Darks_4294,"HAEL_4294_front")
Back_Darks_4294=string_list(129,138)
Back_Output_4294=extract_subject("001","128",Back_Darks_4294,"HAEL_4294_back")

Front_Darks_4827=string_list(140,150)
Front_Output_4827=extract_subject("001","139",Front_Darks_4827,"HAME_4827_front")
Back_Darks_4827=string_list(152,165)
Back_Output_4827=extract_subject("001","151",Back_Darks_4827,"HAME_4827_back")

Front_Darks_4803=string_list(167,176)
Front_Output_4803=extract_subject("001","166",Front_Darks_4803,"HAME_4803_front")
Back_Darks_4803=string_list(178,187)
Back_Output_4803=extract_subject("001","177",Back_Darks_4803,"HAME_4803_back")

Front_Darks_4820=string_list(189,201)
Front_Output_4820=extract_subject("001","188",Front_Darks_4820,"HAME_4820_front")
Back_Darks_4820=string_list(203,213)
Back_Output_4820=extract_subject("001","202",Back_Darks_4820,"HAME_4820_back")

where="../aug_10_2022"
os.chdir(where)

Front_Darks_3583=string_list(8,18)
Front_Output_3583=extract_subject("000","007",Front_Darks_3583,"HABO_3583_front")
Back_Darks_3583=string_list(20,29)
Back_Output_3583=extract_subject("000","019",Back_Darks_3583,"HABO_3583_back")

Front_Darks_4109=string_list(31,40)
Front_Output_4109=extract_subject("000","030",Front_Darks_4109,"HABO_4109_front")
Back_Darks_4109=string_list(42,51)
Back_Output_4109=extract_subject("000","041",Back_Darks_4109,"HABO_4109_back")

Front_Darks_4112=string_list(53,62)
Front_Output_4112=extract_subject("000","052",Front_Darks_4112,"HABO_4112_front")
Back_Darks_4112=string_list(64,73)
Back_Output_4112=extract_subject("000","063",Back_Darks_4112,"HABO_4112_back")

Front_Darks_4101=string_list(75,84)
Front_Output_4101=extract_subject("000","074",Front_Darks_4101,"HABO_4101_front")
Back_Darks_4101=string_list(86,95)
Back_Output_4101=extract_subject("000","085",Back_Darks_4101,"HABO_4101_back")

Front_Darks_4110=string_list(97,106)
Front_Output_4110=extract_subject("000","096",Front_Darks_4110,"HABO_4110_front")
Back_Darks_4110=string_list(108,117)
Back_Output_4110=extract_subject("000","107",Back_Darks_4110,"HABO_4110_back")

Front_Darks_4135=string_list(6,16)
Front_Output_4135=extract_subject("001","005",Front_Darks_4135,"HABO_4135_front")
Back_Darks_4135=string_list(18,27)
Back_Output_4135=extract_subject("001","017",Back_Darks_4135,"HABO_4135_back")

Front_Darks_4111=string_list(6,16)
Front_Output_4111=extract_subject("002","005",Front_Darks_4111,"HABO_4111_front")
Back_Darks_4111=string_list(18,27)
Back_Output_4111=extract_subject("002","017",Back_Darks_4111,"HABO_4111_back")

Front_Darks_006=string_list(29,38)
Front_Output_006=extract_subject("002","028",Front_Darks_006,"HABO_006_front")
Back_Darks_006=string_list(40,49)
Back_Output_006=extract_subject("002","039",Back_Darks_006,"HABO_006_back")

where="../aug_11_2022"
os.chdir(where)

Front_Darks_1240=string_list(6,15)
Front_Output_1240=extract_subject("000","005",Front_Darks_1240,"HAHA_1240_front")
Back_Darks_1240=string_list(17,26)
Back_Output_1240=extract_subject("000","016",Back_Darks_1240,"HAHA_1240_back")

Front_Darks_953=string_list(28,37)
Front_Output_953=extract_subject("000","027",Front_Darks_953,"HAHA_953_front")
Back_Darks_953=string_list(62,71)
Back_Output_953=extract_subject("000","061",Back_Darks_953,"HAHA_953_back")

Front_Darks_1136=string_list(73,82)
Front_Output_1136=extract_subject("000","072",Front_Darks_1136,"HAHA_1136_front")
Back_Darks_1136=string_list(106,115)
Back_Output_1136=extract_subject("000","105",Back_Darks_1136,"HAHA_1136_back")

Front_Darks_3951=string_list(6,15)
Front_Output_3951=extract_subject("001","005",Front_Darks_3951,"HABO_3951_front")
Back_Darks_3951=string_list(17,26)
Back_Output_3951=extract_subject("001","016",Back_Darks_3951,"HABO_3951_back")

Front_Darks_4164=string_list(28,38)
Front_Output_4164=extract_subject("001","027",Front_Darks_4164,"HABO_4164_front")
Back_Darks_4164=string_list(40,50)
Back_Output_4164=extract_subject("001","039",Back_Darks_4164,"HABO_4164_back")

Front_Darks_3970=string_list(52,61)
Front_Output_3970=extract_subject("001","051",Front_Darks_3970,"HABO_3970_front")
Back_Darks_3970=string_list(63,72)
Back_Output_3970=extract_subject("001","062",Back_Darks_3970,"HABO_3970_back")

Front_Darks_1007=string_list(74,83)
Front_Output_1007=extract_subject("001","073",Front_Darks_1007,"HAHA_1007_front")
Back_Darks_1007=string_list(107,116)
Back_Output_1007=extract_subject("001","106",Back_Darks_1007,"HAHA_1007_back")

Front_Darks_4165=string_list(6,15)
Front_Output_4165=extract_subject("002","005",Front_Darks_4165,"HABO_4165_front")
Back_Darks_4165=string_list(17,26)
Back_Output_4165=extract_subject("002","016",Back_Darks_4165,"HABO_4165_back")

Front_Darks_1006=string_list(28,39)
Front_Output_1006=extract_subject("002","027",Front_Darks_1006,"HAHA_1006_front")
Back_Darks_1006=string_list(63,72)
Back_Output_1006=extract_subject("002","062",Back_Darks_1006,"HAHA_1006_back")

Front_Darks_4171=string_list(74,83)
Front_Output_4171=extract_subject("002","073",Front_Darks_4171,"HABO_4171_front")
Back_Darks_4171=string_list(85,94)
Back_Output_4171=extract_subject("002","084",Back_Darks_4171,"HABO_4171_back")

Front_Darks_3969=string_list(96,105)
Front_Output_3969=extract_subject("002","095",Front_Darks_3969,"HABO_3969_front")
Back_Darks_3969=string_list(107,116)
Back_Output_3969=extract_subject("002","106",Back_Darks_3969,"HABO_3969_back")

Front_Darks_4763=string_list(118,127)
Front_Output_4763=extract_subject("002","117",Front_Darks_4763,"HATE_4763_front")
Back_Darks_4763=string_list(129,139)
Back_Output_4763=extract_subject("002","128",Back_Darks_4763,"HATE_4763_back")

Front_Darks_D2=string_list(6,15)
Front_Output_D2=extract_subject("003","005",Front_Darks_D2,"HAEL_D2_front")
Back_Darks_D2=string_list(22,31)
Back_Output_D2=extract_subject("003","021",Back_Darks_D2,"HAEL_D2_back")

Front_Darks_118=string_list(33,42)
Front_Output_118=extract_subject("003","032",Front_Darks_118,"HAHA_118_front")
Back_Darks_118=string_list(66,77)
Back_Output_118=extract_subject("003","065",Back_Darks_118,"HAHA_118_back")

Front_Darks_octojeff=string_list(6,15)
Front_Output_octojeff=extract_subject("004","005",Front_Darks_octojeff,"HAHA_octojeff_front")

where="../aug_12_2022"
os.chdir(where)

Front_Darks_4132=string_list(7,17)
Front_Output_4132=extract_subject("000","006",Front_Darks_4132,"HABO_4132_front")
Back_Darks_4132=string_list(19,28)
Back_Output_4132=extract_subject("000","018",Back_Darks_4132,"HABO_4132_back")

Front_Darks_849=string_list(30,39)
Front_Output_849=extract_subject("000","029",Front_Darks_849,"HAHI_849_front")
Back_Darks_849=string_list(41,50)
Back_Output_849=extract_subject("000","040",Back_Darks_849,"HAHI_849_back")

Front_Darks_1033=string_list(52,61)
Front_Output_1033=extract_subject("000","051",Front_Darks_1033,"HAHA_1033_front")
Back_Darks_1033=string_list(88,97)
Back_Output_1033=extract_subject("000","087",Back_Darks_1033,"HAHA_1033_back")

Front_Darks_4159=string_list(6,15)
Front_Output_4159=extract_subject("001","005",Front_Darks_4159,"HAHI_4159_front")
Back_Darks_4159=string_list(17,26)
Back_Output_4159=extract_subject("001","016",Back_Darks_4159,"HAHI_4159_back")

Front_Darks_905=string_list(28,37)
Front_Output_905=extract_subject("001","027",Front_Darks_905,"HAHI_905_front")
Back_Darks_905=string_list(39,48)
Back_Output_905=extract_subject("001","038",Back_Darks_905,"HAHI_905_back")

Front_Darks_878=string_list(50,59)
Front_Output_878=extract_subject("001","049",Front_Darks_878,"HAHI_878_front")
Back_Darks_878=string_list(61,70)
Back_Output_878=extract_subject("001","060",Back_Darks_878,"HAHI_878_back")

Front_Darks_4367=string_list(72,81)
Front_Output_4367=extract_subject("001","071",Front_Darks_4367,"HAHI_4367_front")
Back_Darks_4367=string_list(83,92)
Back_Output_4367=extract_subject("001","082",Back_Darks_4367,"HAHI_4367_back")

Front_Darks_1700=string_list(94,103)
Front_Output_1700=extract_subject("001","093",Front_Darks_1700,"HAHI_1700_front")
Back_Darks_1700=string_list(105,114)
Back_Output_1700=extract_subject("001","104",Back_Darks_1700,"HAHI_1700_back")

Front_Darks_992=string_list(6,15)
Front_Output_992=extract_subject("002","005",Front_Darks_992,"HAHI_992_front")
Back_Darks_992=string_list(18,27)
Back_Output_992=extract_subject("002","017",Back_Darks_992,"HAHI_992_back")

Front_Darks_3548=string_list(29,38)
Front_Output_3548=extract_subject("002","028",Front_Darks_3548,"HABO_3548_front")
Back_Darks_3548=string_list(40,49)
Back_Output_3548=extract_subject("002","039",Back_Darks_3548,"HABO_3548_back")

Front_Darks_169=string_list(51,61)
Front_Output_169=extract_subject("002","050",Front_Darks_169,"HAHI_169_front")
Back_Darks_169=string_list(63,72)
Back_Output_169=extract_subject("002","062",Back_Darks_169,"HAHI_169_back")

Front_Darks_165=string_list(74,83)
Front_Output_165=extract_subject("002","073",Front_Darks_165,"HAHI_165_front")
Back_Darks_165=string_list(85,94)
Back_Output_165=extract_subject("002","084",Back_Darks_165,"HAHI_165_back")

Front_Darks_871=string_list(96,105)
Front_Output_871=extract_subject("002","095",Front_Darks_871,"HAHI_871_front")
Back_Darks_871=string_list(107,116)
Back_Output_871=extract_subject("002","106",Back_Darks_871,"HAHI_871_back")

Front_Darks_4349=string_list(17,26)
Front_Output_4349=extract_subject("003","016",Front_Darks_4349,"HAHI_4349_front")
Back_Darks_4349=string_list(28,38)
Back_Output_4349=extract_subject("003","027",Back_Darks_4349,"HAHI_4349_back")

Front_Darks_146=string_list(40,50)
Front_Output_146=extract_subject("003","039",Front_Darks_146,"HAHI_146_front")
Back_Darks_146=string_list(52,61)
Back_Output_146=extract_subject("003","051",Back_Darks_146,"HAHI_146_back")

Front_Darks_4136=string_list(63,72)
Front_Output_4136=extract_subject("003","062",Front_Darks_4136,"HABO_4136_front")
Back_Darks_4136=string_list(74,83)
Back_Output_4136=extract_subject("003","073",Back_Darks_4136,"HABO_4136_back")

where="../aug_14_2022"
os.chdir(where)

Front_Darks_4505=string_list(8,17)
Front_Output_4505=extract_subject("000","007",Front_Darks_4505,"HACOE_4505_front")
Back_Darks_4505=string_list(19,28)
Back_Output_4505=extract_subject("000","018",Back_Darks_4505,"HACOE_4505_back")

Front_Darks_814=string_list(30,39)
Front_Output_814=extract_subject("000","029",Front_Darks_814,"HAHI_814_front")
Back_Darks_814=string_list(41,50)
Back_Output_814=extract_subject("000","040",Back_Darks_814,"HAHI_814_back")

Front_Darks_952=string_list(52,61)
Front_Output_952=extract_subject("000","051",Front_Darks_952,"HACO_952_front")
Back_Darks_952=string_list(63,72)
Back_Output_952=extract_subject("000","062",Back_Darks_952,"HACO_952_back")

Front_Darks_959=string_list(74,83)
Front_Output_959=extract_subject("000","073",Front_Darks_959,"HACO_959_front")
Back_Darks_959=string_list(85,94)
Back_Output_959=extract_subject("000","084",Back_Darks_959,"HACO_959_back")

Front_Darks_4406=string_list(96,105)
Front_Output_4406=extract_subject("000","095",Front_Darks_4406,"HACO_4406_front")
Back_Darks_4406=string_list(107,116)
Back_Output_4406=extract_subject("000","106",Back_Darks_4406,"HACO_4406_back")

Front_Darks_4496=string_list(6,15)
Front_Output_4496=extract_subject("001","005",Front_Darks_4496,"HACO_4496_front")
Back_Darks_4496=string_list(17,26)
Back_Output_4496=extract_subject("001","016",Back_Darks_4496,"HACO_4496_back")

Front_Darks_4520=string_list(28,37)
Front_Output_4520=extract_subject("001","027",Front_Darks_4520,"HAHI_4520_front")
Back_Darks_4520=string_list(39,48)
Back_Output_4520=extract_subject("001","038",Back_Darks_4520,"HAHI_4520_back")

Front_Darks_945=string_list(50,59)
Front_Output_945=extract_subject("001","049",Front_Darks_945,"HACO_945_front")
Back_Darks_945=string_list(61,70)
Back_Output_945=extract_subject("001","060",Back_Darks_945,"HACO_945_back")

Front_Darks_4228=string_list(72,82)
Front_Output_4228=extract_subject("001","071",Front_Darks_4228,"HAUS_4228_front")
Back_Darks_4228=string_list(84,93)
Back_Output_4228=extract_subject("001","083",Back_Darks_4228,"HAUS_4228_back")

Front_Darks_1138=string_list(95,104)
Front_Output_1138=extract_subject("001","094",Front_Darks_1138,"HACO_1138_front")
Back_Darks_1138=string_list(106,115)
Back_Output_1138=extract_subject("001","105",Back_Darks_1138,"HACO_1138_back")

Front_Darks_3630=string_list(117,126)
Front_Output_3630=extract_subject("001","116",Front_Darks_3630,"HACO_3630_front")
Back_Darks_3630=string_list(128,137)
Back_Output_3630=extract_subject("001","127",Back_Darks_3630,"HACO_3630_back")

Front_Darks_898=string_list(17,26)
Front_Output_898=extract_subject("002","016",Front_Darks_898,"HACO_898_front")
Back_Darks_898=string_list(28,37)
Back_Output_898=extract_subject("002","027",Back_Darks_898,"HACO_898_back")

Front_Darks_926=string_list(39,48)
Front_Output_926=extract_subject("002","038",Front_Darks_926,"HACO_926_front")
Back_Darks_926=string_list(50,59)
Back_Output_926=extract_subject("002","049",Back_Darks_926,"HACO_926_back")

Front_Darks_1000=string_list(61,70)
Front_Output_1000=extract_subject("002","060",Front_Darks_1000,"HACO_1000_front")
Back_Darks_1000=string_list(72,81)
Back_Output_1000=extract_subject("002","071",Back_Darks_1000,"HACO_1000_back")

Front_Darks_927=string_list(83,92)
Front_Output_927=extract_subject("002","082",Front_Darks_927,"HACO_927_front")
Back_Darks_927=string_list(94,103)
Back_Output_927=extract_subject("002","093",Back_Darks_927,"HACO_927_back")

Front_Darks_184=string_list(105,114)
Front_Output_184=extract_subject("002","104",Front_Darks_184,"HACO_184_front")
Back_Darks_184=string_list(116,125)
Back_Output_184=extract_subject("002","115",Back_Darks_184,"HACO_184_back")

Front_Darks_1085=string_list(127,136)
Front_Output_1085=extract_subject("002","126",Front_Darks_1085,"HACO_1085_front")
Back_Darks_1085=string_list(138,147)
Back_Output_1085=extract_subject("002","137",Back_Darks_1085,"HACO_1085_back")

Front_Darks_907=string_list(6,16)
Front_Output_907=extract_subject("003","005",Front_Darks_907,"HACO_907_front")
Back_Darks_907=string_list(18,27)
Back_Output_907=extract_subject("003","017",Back_Darks_907,"HACO_907_back")

Front_Darks_915=string_list(29,38)
Front_Output_915=extract_subject("003","028",Front_Darks_915,"HACO_915_front")
Back_Darks_915=string_list(40,49)
Back_Output_915=extract_subject("003","039",Back_Darks_915,"HACO_915_back")

Front_Darks_3631=string_list(51,60)
Front_Output_3631=extract_subject("003","050",Front_Darks_3631,"HACO_3631_front")
Back_Darks_3631=string_list(62,73)
Back_Output_3631=extract_subject("003","061",Back_Darks_3631,"HACO_3631_back")

Front_Darks_912=string_list(75,84)
Front_Output_912=extract_subject("003","074",Front_Darks_912,"HACO_912_front")
Back_Darks_912=string_list(86,95)
Back_Output_912=extract_subject("003","085",Back_Darks_912,"HACO_912_back")

Front_Darks_921=string_list(97,107)
Front_Output_921=extract_subject("003","096",Front_Darks_921,"HACO_921_front")
Back_Darks_921=string_list(109,118)
Back_Output_921=extract_subject("003","108",Back_Darks_921,"HACO_921_back")

Front_Darks_970=string_list(120,129)
Front_Output_970=extract_subject("003","119",Front_Darks_970,"HACO_970_front")
Back_Darks_970=string_list(131,140)
Back_Output_970=extract_subject("003","130",Back_Darks_970,"HACO_970_back")

Front_Darks_964=string_list(142,151)
Front_Output_964=extract_subject("003","141",Front_Darks_964,"HACO_964_front")
Back_Darks_964=string_list(153,162)
Back_Output_964=extract_subject("003","152",Back_Darks_964,"HACO_964_back")

Front_Darks_920=string_list(6,15)
Front_Output_920=extract_subject("004","005",Front_Darks_920,"HACO_920_front")
Back_Darks_920=string_list(17,26)
Back_Output_920=extract_subject("004","016",Back_Darks_920,"HACO_920_back")

Front_Darks_4253=string_list(28,37)
Front_Output_4253=extract_subject("004","027",Front_Darks_4253,"HAUS_4253_front")
Back_Darks_4253=string_list(40,50)
Back_Output_4253=extract_subject("004","039",Back_Darks_4253,"HAUS_4253_back")

Front_Darks_4225=string_list(52,61)
Front_Output_4225=extract_subject("004","051",Front_Darks_4225,"HAUS_4225_front")
Back_Darks_4225=string_list(63,72)
Back_Output_4225=extract_subject("004","062",Back_Darks_4225,"HAUS_4225_back")

Front_Darks_4238=string_list(74,83)
Front_Output_4238=extract_subject("004","073",Front_Darks_4238,"HAUS_4238_front")
Back_Darks_4238=string_list(85,94)
Back_Output_4238=extract_subject("004","084",Back_Darks_4238,"HAUS_4238_back")

Front_Darks_4215=string_list(96,105)
Front_Output_4215=extract_subject("004","095",Front_Darks_4215,"HAUS_4215_front")
Back_Darks_4215=string_list(107,116)
Back_Output_4215=extract_subject("004","106",Back_Darks_4215,"HAUS_4215_back")

Front_Darks_4248=string_list(6,15)
Front_Output_4248=extract_subject("005","005",Front_Darks_4248,"HAUS_4248_front")
Back_Darks_4248=string_list(17,26)
Back_Output_4248=extract_subject("005","016",Back_Darks_4248,"HAUS_4248_back")

Front_Darks_4778=string_list(28,37)
Front_Output_4778=extract_subject("005","027",Front_Darks_4778,"HATE_4778_front")
Back_Darks_4778=string_list(39,48)
Back_Output_4778=extract_subject("005","038",Back_Darks_4778,"HATE_4778_back")

Front_Darks_4200=string_list(50,59)
Front_Output_4200=extract_subject("005","049",Front_Darks_4200,"HAUS_4200_front")
Back_Darks_4200=string_list(61,70)
Back_Output_4200=extract_subject("005","060",Back_Darks_4200,"HAUS_4200_back")

Front_Darks_4234=string_list(72,81)
Front_Output_4234=extract_subject("005","071",Front_Darks_4234,"HAUS_4234_front")
Back_Darks_4234=string_list(83,94)
Back_Output_4234=extract_subject("005","082",Back_Darks_4234,"HAUS_4234_back")

Front_Darks_siggy=string_list(96,105)
Front_Output_siggy=extract_subject("005","095",Front_Darks_siggy,"HASI_siggy_front")
Back_Darks_siggy=string_list(107,116)
Back_Output_siggy=extract_subject("005","106",Back_Darks_siggy,"HASI_siggy_back")

Front_Darks_4242=string_list(127,136)
Front_Output_4242=extract_subject("005","126",Front_Darks_4242,"HAUS_4242_front")
Back_Darks_4242=string_list(138,147)
Back_Output_4242=extract_subject("005","137",Back_Darks_4242,"HAUS_4242_back")

Front_Darks_848=string_list(6,15)
Front_Output_848=extract_subject("006","005",Front_Darks_848,"HAHI_848_front")
Back_Darks_848=string_list(17,26)
Back_Output_848=extract_subject("006","016",Back_Darks_848,"HAHI_848_back")

Front_Darks_995=string_list(28,37)
Front_Output_995=extract_subject("006","027",Front_Darks_995,"HACO_995_front")
Back_Darks_995=string_list(39,48)
Back_Output_995=extract_subject("006","038",Back_Darks_995,"HACO_995_back")

Front_Darks_4246=string_list(50,59)
Front_Output_4246=extract_subject("006","049",Front_Darks_4246,"HAUS_4246_front")
Back_Darks_4246=string_list(61,70)
Back_Output_4246=extract_subject("006","060",Back_Darks_4246,"HAUS_4246_back")

Front_Darks_4230=string_list(72,81)
Front_Output_4230=extract_subject("006","071",Front_Darks_4230,"HAUS_4230_front")
Back_Darks_4230=string_list(83,92)
Back_Output_4230=extract_subject("006","082",Back_Darks_4230,"HAUS_4230_back")

Front_Darks_934=string_list(94,103)
Front_Output_934=extract_subject("006","093",Front_Darks_934,"HACO_934_front")
Back_Darks_934=string_list(105,114)
Back_Output_934=extract_subject("006","104",Back_Darks_934,"HACO_934_back")

Front_Darks_976=string_list(7,16)
Front_Output_976=extract_subject("007","006",Front_Darks_976,"HACO_976_front")
Back_Darks_976=string_list(18,27)
Back_Output_976=extract_subject("007","017",Back_Darks_976,"HACO_976_back")

Front_Darks_198=string_list(29,38)
Front_Output_198=extract_subject("007","028",Front_Darks_198,"HACO_198_front")
Back_Darks_198=string_list(40,49)
Back_Output_198=extract_subject("007","039",Back_Darks_198,"HACO_198_back")

where="../aug_17_2022"
os.chdir(where)

Front_Darks_4721=string_list(6,17)
Front_Output_4721=extract_subject("000","005",Front_Darks_4721,"HADE_4721_front")
Back_Darks_4721=string_list(19,28)
Back_Output_4721=extract_subject("000","018",Back_Darks_4721,"HADE_4721_back")

Front_Darks_G1=string_list(30,40)
Front_Output_G1=extract_subject("000","029",Front_Darks_G1,"HADE_G1_front")
Back_Darks_G1=string_list(42,54)
Back_Output_G1=extract_subject("000","041",Back_Darks_G1,"HADE_G1_back")

Front_Darks_4728=string_list(56,65)
Front_Output_4728=extract_subject("000","055",Front_Darks_4728,"HADE_4728_front")
Back_Darks_4728=string_list(67,76)
Back_Output_4728=extract_subject("000","066",Back_Darks_4728,"HADE_4728_back")

Front_Darks_G6=string_list(90,99)
Front_Output_G6=extract_subject("000","089",Front_Darks_G6,"HADE_G6_front")
Back_Darks_G6=string_list(101,111)
Back_Output_G6=extract_subject("000","100",Back_Darks_G6,"HADE_G6_back")

Front_Darks_G4=string_list(6,15)
Front_Output_G4=extract_subject("001","005",Front_Darks_G4,"HADE_G4_front")
Back_Darks_G4=string_list(17,26)
Back_Output_G4=extract_subject("001","016",Back_Darks_G4,"HADE_G4_back")

Front_Darks_4726=string_list(28,40)
Front_Output_4726=extract_subject("001","027",Front_Darks_4726,"HADE_4726_front")
Back_Darks_4726=string_list(42,51)
Back_Output_4726=extract_subject("001","041",Back_Darks_4726,"HADE_4726_back")

Front_Darks_4727=string_list(53,62)
Front_Output_4727=extract_subject("001","052",Front_Darks_4727,"HADE_4727_front")
Back_Darks_4727=string_list(64,73)
Back_Output_4727=extract_subject("001","063",Back_Darks_4727,"HADE_4727_back")

Front_Darks_4723=string_list(75,87)
Front_Output_4723=extract_subject("001","074",Front_Darks_4723,"HADE_4723_front")
Back_Darks_4723=string_list(89,98)
Back_Output_4723=extract_subject("001","088",Back_Darks_4723,"HADE_4723_back")

Front_Darks_4724=string_list(100,111)
Front_Output_4724=extract_subject("001","099",Front_Darks_4724,"HADE_4724_front")
Back_Darks_4724=string_list(113,122)
Back_Output_4724=extract_subject("001","112",Back_Darks_4724,"HADE_4724_back")

Front_Darks_657=string_list(124,135)
Front_Output_657=extract_subject("001","123",Front_Darks_657,"HADE_657_front")
Back_Darks_657=string_list(137,147)
Back_Output_657=extract_subject("001","136",Back_Darks_657,"HADE_657_back")


where="../aug_19_2022"
os.chdir(where)

Front_Darks_4722=string_list(6,15)
Front_Output_4722=extract_subject("000","005",Front_Darks_4722,"HADE_4722_front")
Back_Darks_4722=string_list(17,26)
Back_Output_4722=extract_subject("000","016",Back_Darks_4722,"HADE_4722_back")

Front_Darks_G7=string_list(28,37)
Front_Output_G7=extract_subject("000","027",Front_Darks_G7,"HADE_G7_front")
Back_Darks_G7=string_list(39,48)
Back_Output_G7=extract_subject("000","038",Back_Darks_G7,"HADE_G7_back")

Front_Darks_4149=string_list(50,59)
Front_Output_4149=extract_subject("000","049",Front_Darks_4149,"HACO_4149_front")
Back_Darks_4149=string_list(61,70)
Back_Output_4149=extract_subject("000","060",Back_Darks_4149,"HACO_4149_back")

Front_Darks_4009=string_list(83,92)
Front_Output_4009=extract_subject("000","082",Front_Darks_4009,"HADE_4009_front")
Back_Darks_4009=string_list(72,81)
Back_Output_4009=extract_subject("000","071",Back_Darks_4009,"HADE_4009_back")

Front_Darks_4146=string_list(94,103)
Front_Output_4146=extract_subject("000","093",Front_Darks_4146,"HACO_4146_front")
Back_Darks_4146=string_list(105,114)
Back_Output_4146=extract_subject("000","104",Back_Darks_4146,"HACO_4146_back")

Front_Darks_4010=string_list(116,125)
Front_Output_4010=extract_subject("000","115",Front_Darks_4010,"HADE_4010_front")
Back_Darks_4010=string_list(127,136)
Back_Output_4010=extract_subject("000","126",Back_Darks_4010,"HADE_4010_back")

Front_Darks_4012=string_list(138,147)
Front_Output_4012=extract_subject("000","137",Front_Darks_4012,"HADE_4012_front")
Back_Darks_4012=string_list(149,158)
Back_Output_4012=extract_subject("000","148",Back_Darks_4012,"HADE_4012_back")

Front_Darks_G5=string_list(6,15)
Front_Output_G5=extract_subject("001","005",Front_Darks_G5,"HADE_G5_front")
Back_Darks_G5=string_list(17,27)
Back_Output_G5=extract_subject("001","016",Back_Darks_G5,"HADE_G5_back")

Front_Darks_4008=string_list(29,38)
Front_Output_4008=extract_subject("001","028",Front_Darks_4008,"HADE_4008_front")
Back_Darks_4008=string_list(40,49)
Back_Output_4008=extract_subject("001","039",Back_Darks_4008,"HADE_4008_back")

Front_Darks_G2=string_list(51,60)
Front_Output_G2=extract_subject("001","050",Front_Darks_G2,"HADE_G2_front")
Back_Darks_G2=string_list(62,71)
Back_Output_G2=extract_subject("001","061",Back_Darks_G2,"HADE_G2_back")

Front_Darks_4011=string_list(73,82)
Front_Output_4011=extract_subject("001","072",Front_Darks_4011,"HADE_4011_front")
Back_Darks_4011=string_list(84,93)
Back_Output_4011=extract_subject("001","083",Back_Darks_4011,"HADE_4011_back")

Front_Darks_4014=string_list(95,104)
Front_Output_4014=extract_subject("001","094",Front_Darks_4014,"HADE_4014_front")
Back_Darks_4014=string_list(106,115)
Back_Output_4014=extract_subject("001","105",Back_Darks_4014,"HADE_4014_back")

Front_Darks_4162=string_list(117,126)
Front_Output_4162=extract_subject("001","116",Front_Darks_4162,"HACO_4162_front")
Back_Darks_4162=string_list(128,137)
Back_Output_4162=extract_subject("001","127",Back_Darks_4162,"HACO_4162_back")

Front_Darks_G3=string_list(139,148)
Front_Output_G3=extract_subject("001","138",Front_Darks_G3,"HADE_G3_front")
Back_Darks_G3=string_list(150,159)
Back_Output_G3=extract_subject("001","149",Back_Darks_G3,"HADE_G3_back")