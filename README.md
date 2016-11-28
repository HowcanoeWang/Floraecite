# Floræcite
## How to use it
Download by clicking ***release***, or click this url: https://github.com/HowcanoeWang/Floraecite/releases

After downloading,**Extract** the zip file, double click **floraecite.exe**, then in the folder-selection-dialog, select **Data** folder. 

There is only a few example pictures in the **Launch.zip** Folder. For UNB students who enrolled in the FOR/ENR2425, go to the **UNB extra pictures**, download all the Picture-zip files

## Notice
The Data(000.xlsx and pictures) are examples provided by the course of ***Autecology(FOR2425), College of Foresty and Geology，University of New Brunswick***

After opening the programme, it will create a log file called memeory.floraecite in the picture data folder, please **DO NOT** delete it! It records your mastery of species.

This programme could list your least familiar species at the first beginning due to your using process!

## Make your own database
1. The 000.xlsx is the most important file that you should not change the name of this file.
2. This program could only read sheet1 in the Excel. Please do not add information to other sheets.
3. The data structure of 000.xlsx is:


| (Picture filename) | (Latin name) | (Common name) | (Latin required) |
|------------------|------------|-------------|----------------|
| 001 | Polystichum acrostichoides | Christmas fern | 0 |
| 002 | Pteridium aquilinum | bracken fern | 1 |

PS: 
+ 0 == Latin names don't need to recite, 1 == Latin Name required. If you just want to identify plants rather than remembering their Latin names, just put zeros in that column.
+ The first row should **NOT** be put into the sheet(just tell you the meaning of each column), please start with your picture names in the first line directly.
+ Picture names in the sheet **must the same as** picture names in the Data folder. 

+ Other languages which are included in UTF-8 format are supported.
+ Recommend picture format of **.jpg**, support format of **.png** and **.gif**
+ **Please make sure all the picture files in the same format.**


## Debug
If you meet any bug, please contact the author without hesitation. You could e-mail the author or make comments on Github. Describe the problem and your operation process in detail.

--- 

## Update log
### 16.11.27
#### Beta1.7.1
+ add new version download wait string

### 16.11.26
#### Beta1.7.0
+ fix small bugs
+ change names in 000.xlsx file from ’ to '

### 16.11.23
#### Beta1.6.9
+ pack pictures into zip files
+ add new version detection function
+ fix rename picture can not change log bug

### 16.11.22
#### Beta1.6.8
+ add picture data choose function
+ display Mastery in the GUI
### 16.11.21
+ Add 13 Lichens and Bryophytes pictures
+ Moderate 000.xlsx
+ change file positions
#### Beta 1.6.7    
1. fix picture list bugs
2. change folder structure

### 16.11.20
#### Beta1.6.6
+ Improve mastary calculation

#### Beta1.6.5
+ Add icon

#### Beta1.6.4
+ Fix Next button can not rebound

### 16.11.19
#### Beta1.6.3
##### Add
+ Checking before operating the program
+ \<Enter> to 'next' instead Of clicking Button    

##### Debug 
+ Fix user delete pictures in the folder that caused program broken up    

#### Beta1.6.1

##### New: 
+ Activate Mastary rank methods 

##### Debug: 
+ Fix small screen can not show the GUI 
+ Fix log file read error 

#### Beta1.5.0
+ main functions, including veiwing and testing mode, help, and Mastery recording

### 16.11.18
+ Add version auther and official url link
+ Add single select button, excel data reading, picture list acquire

### 16.11.17
+ coding

### 16.11.15
+ github use learning

### 16.10.31
+ Program started
