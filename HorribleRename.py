# Name of code: HorribleRename
# Author of code: Alec J. Davidson
# Version of the code and the date of it’s last revision: ver 1.10 10/24/19
# Summary/Goal of the code: This script will help manage your anime library
# by renaming anime from HorribleSubs to an ideal format for Plex.
# This will serve as the module responsible for reformatting HorribleSubs
# content for AniName when it is complete.

import os # Imports the OS module allowing us to navigate the file system.
import PTN # Allows the parsing of the raw files.

def HoribleRename(path=''): 									# Defines default arguments for primary variables.
	path = input('Please enter the path to the target files: ') # Asks user to input the path to the video files and stores it in the path variable.
	f_list = [] 												# Creates a list that stores the target files.
	#end = len(f_list)
	f_list = sorted(os.listdir(path)) 							# Fetches all files in the given directory and stores them in files.
	#print(f_list) 												# Prints all the files in the list.
	os.chdir(path) 												# Points to the target directory stored in the path variable.
	print(os.getcwd()) 											# Prints the current working directory
	count = -1 													# Starts count at -1 so that the first index is 0 in the loop.
	for files in (f_list): 										# Loop to iterate a rename for each file in the directory.
		count = count + 1 										# Iterates for each file in the directory
		nameInput = f_list[count] 								# Iterates over how many files are in the list and uses that to keep from overwriting/deleting files.
		name = PTN.parse(nameInput) 							# Parses torrent name
		title = name['title'] 									# Title string
		titleSplit = str(title).split('-', 1) 					# Splits the title even further
		title = titleSplit[0] 									# Title text
		epNum = titleSplit[1] 									# Episode number
		container = name['container'] 							# File extention type
		newTitle = (title+'-'+epNum+'.'+container) 				# Creates Plex friendly title
		os.rename(files,newTitle) 								# Renames target files using new_name.
HoribleRename() 												# Calls function.