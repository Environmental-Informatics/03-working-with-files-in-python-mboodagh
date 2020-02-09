#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:19:30 2020

@author: mboodagh
"""
""" The purpose of this program is to read and write data related to the behavior of a Racoon named George based on the given instructions"""
#import required modules
import math 

##### Required functions section begin
# A function for finding the mean
def meanofrac(a):
    s=0;
    for i in range(len(a)):
        s=s+a[i]
    average=s/len(a)
    return average
# A function for finding the cumulative sum
def cumsumrac(b):
    for j in range(len(b)):
        for i in range(j):
            if j>0 :   
               b[j]=b[i]+b[j]
    return b
# A function for finding the distance traveled
def distanceofrac(X,Y):
    d=[3]*(len(X))
    for i in range(0,len(X)-1):
        d[0]=0
        d[i+1]=math.sqrt((X[i+1]-X[i])**2+(Y[i+1]-Y[i])**2)
    return d
##### Required functions section end

#####opening the file section beging
#directory of the file
file_dir="/home/mboodagh/ABE65100/using-Files-and-simple-data-structures-with-python/03-working-with-files-in-python-mboodagh/"
#name of the file you would like to open
file_to_open="2008Male00006.txt"
#open the file
fin = open( file_dir+file_to_open, "r" )
#####opening the file section end

#####Dictionary of the given data section begin
#find the header values by reading the first line
header_nonsplit=fin.readline()
# get rid of the new line character \n
header=header_nonsplit.strip().split(",")
# read lines from line2
lines = fin.readlines()
#store the last line information
last_message=lines[len(lines)-1]
#closing the file
fin.close()
#Creating a file named Data to store all the information
Data = [0]*len(lines)
for lidx in range(len(lines)):
    Data[lidx] = lines[lidx].strip().split(",")
#defining a new Dictionary    
Rac_behavior=dict()  
#determining keys by assigning initial values to them
for i in range(len(header)):
    Rac_behavior[header[i]]=Data[0][i]
# adding to the values associated with each key by the separtor','
for i in range(len(header)):
    for j in range(1,len(lines)-1):
        Rac_behavior[header[i]]+=','
        Rac_behavior[header[i]]+=(Data[j][i])
#columns having floating numbers
float_column=[4,5,8,9,10,11,12,13,14]
#columns having integers there are no integer columns in the data
integer_column=[]
#turning related strings into floating ones  
for i in float_column:
    ch=(Rac_behavior[header[i]].strip().split(","))
    for j in range(len(ch)):
        ch[j]=float(ch[j])
    Rac_behavior[header[i]]=ch
#turning related strings into integers
for i in integer_column:
    ch=(Rac_behavior[header[i]].strip().split(","))
    for j in range(len(ch)):
        ch[j]=int(ch[j])
    Rac_behavior[header[i]]=ch    
#####Dictionary section of the given data end

##### Defining a new dictionary section begin   
#finding the distance that the racoon has traveled
dis=distanceofrac(Rac_behavior[header[4]],Rac_behavior[header[5]])
#adding the distane to the dictionary
Rac_behavior['Distance']=dis
disp=dis
##### Defining a new dictionary section end

######calculating average and total values section begin
#finding the averge of X
ave_X=meanofrac(Rac_behavior[header[4]])
#finding the averge of y
ave_Y=meanofrac(Rac_behavior[header[5]])
#finding the mean energy level
ave_Energy=meanofrac(Rac_behavior['Energy Level'])
#finding the total distance geoerge has travelel through his journey
total_dis=cumsumrac(dis)[len(dis)-1]
######calculating average and total values section end

#####writing the ouput data section begin
#name of the ouput file
output_filename="Georges_life.txt"
#create the file
f=open(file_dir+output_filename,"w")
Racoon_name='George'
#create the lines you want to print
newlines="Racoon name:  {} \nAverage location: {}, {}\nDistance traveled: {}\nAverage energy level: {}\nRaccoon end state: {} ".format(Racoon_name,ave_X,ave_Y,total_dis,ave_Energy,last_message)
#write the header lines
f.writelines(newlines)
#write a black line
f.write('\n')
#defining the new headers
col_toprint=['Day', 'Time', ' X', ' Y', ' Asleep', 'Behavior Mode', 'Distance']
bibi=[0]*len(col_toprint)
#separating strings in the dictionary defining a variable bibi for storing the data
for i in range(len(col_toprint)):
    if i==2 :
       bibi[i]=Rac_behavior[col_toprint[i]]
    elif i==3 :
         bibi[i]=Rac_behavior[col_toprint[i]]
    elif i==6 :
         bibi[i]=Rac_behavior[col_toprint[i]]
    else:
         bibi[i]=Rac_behavior[col_toprint[i]].split(",")
bibi[len(bibi)-1]=distanceofrac(Rac_behavior[header[4]],Rac_behavior[header[5]])
# write the header        
for i in range(len(col_toprint)):
    f.write(col_toprint[i]+' ')
# write the rows
for j in range(len(lines)-1):
    f.write('\n')
    for i in  range(len(bibi)):
        f.write("{} ".format(bibi[i][j]))
#####writing the ouput data section end
