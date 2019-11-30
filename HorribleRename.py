# Name of code: AutHorribleRename
# Author of code: Alec J. Davidson
# Version of the code and the date of it’s last revision: ver 2.15 11/30/19
# Summary/Goal of the code: This script will help manage your anime library
# by renaming anime from HorribleSubs to an ideal format for Plex.
# This version will run automagically to cleanup my plex server's anime folder and all sub directories.

import os	# Imports os for use of file system
import PTN	# Allows the parsing of the raw files

animeDir = '' # PATH TO ANIME DIR ON SERVER
anime = []						# Creates a list for anime directories
anime = os.listdir(animeDir)	# Stores anime directories in the list
series_count = -1				# Keeps count of how many anime series are in the directory
for series in anime:			# For loop to iterate over each series in the directory
	series_count += 1			# Adds 1 for each series in the directory
	print(anime[series_count])	# Prints the series name
	series=[]					# Creates a list to store the series in.
	series = sorted(os.listdir(animeDir+'/'+str(anime[series_count])))	# Stores each series in a list
	season_count = -1													# Keeps count of how many seasons there are
	for season in series:												# For loop to iterate over each season in the series directory
		season_count += 1												# Adds 1 fore each season in the directory
		print('  ',series[season_count])								# Prints the season
		seasons=[]														# Creates a list for each season
		seasons = sorted(os.listdir(animeDir+'/'+str(anime[series_count])+'/'+str(series[season_count]))) # Path to seasons
		episode_count = -1						# Keeps count of how many episodes there are
		for episodes in seasons:				# Fore loop to iterate over each episode in the season directory
			print('    ',seasons[episode_count])# Prints the episode name
			episode_count += 1					# Adds 1 for each episode in the season directory
			name = seasons[episode_count]		# Episode name
			info = PTN.parse(name) 				# Parses the name of the file
			title = info['title'] 				# Title string from the parsed file
			container = info['container'] 		# File extention type from the parsed file
			title = (title+'.'+container)		# Edited title and final name for the file
			if 'HorribleSubs' in name:			# Condition to find HorribleSubs in the file name
				os.rename(episodes,title) 		# Renames target files using new_name.
			else:
				print('	','File has already been renamed')