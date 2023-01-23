# SoundEffects

##In above file I have created two Scripts 
1. To convert .mp3 file to wav file 
2. To split the wav file into 10 seconds chunk 

## Libraries Used
 To convert .mp3 to .wav I have used Audio Segment technique .
 To split I have used Audio Segment techniques with pydub library 
   I have also created a function which is adding a padding layer where the duration of the file is less then 10.0.
   
## How to use 
To run this file into your system the first thing you need to do is install requirenment.txt using the command pip install -r requirements.txt
Once your Requirnment.txt is created you should go the run.py file and run it , it will return you two folders OUTPUT(wav) in which the outp of First Script Conversion of .mp3 file to .wav file is done , and Output folder where you can find the 10 second splited files in .wav formate
Hence the both the Scripts are running properly and giving output properly.

## What is done in the files 
To conver .mp3 to .wav , I have you simple Audio Segnment technique .
For splitting I divided my audio file in chunks of 10 second each and then saved it , then I checked if the duration of sound is less then 10 seconds I added an padding layer 



