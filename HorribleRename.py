# Name of code: AutHorribleRename
# Author of code: Alec J. Davidson
# Version of the code and the date of it’s last revision: ver 2.15 01/02/19
# Summary/Goal of the code: This script will help manage your anime library
# by renaming anime from HorribleSubs to an ideal format for Plex.
# This version will run automagically to cleanup my plex server's anime folder and all sub directories.

import os
import PTN


def rename():
	info = PTN.parse(fName)
	newTitle = info['title']+'.'+info['container']
	os.rename(fName, newTitle)


for dirName, subdirList, fileList in os.walk('/home/plex'):
	for fName in fileList:
		os.chdir(dirName)
		isFile = os.path.isfile(fName)
		if isFile == True and \
				'[HorribleSubs]' in fName:
			rename()