import os
import fileinput
from os.path import join
import sys


args = sys.argv

WALKING_PATH = args[1] # path on for walker method to start walking
TEXT_TO_FIND = args[2] # Old text
TEXT_TO_REPLACE = args[3] # New text

def main():
	#file_walker()
	print(WALKING_PATH)
	print(TEXT_TO_FIND)
	print(TEXT_TO_REPLACE)
	file_walker()

def file_walker():
	"""
		This method walks in directories and subdirectories for the given walking path provided
		wherever a file is encountered it passes control to the replace_in_file method
	"""
	for root,dirs,files in os.walk(WALKING_PATH):
		for file in files:
			print("Changing file : ", file)
			replace_in_file(root,file)
			#newFile = file.replace("MNCW", "MNCW")
			#os.rename(join(root,file), join(root,newFile))

def replace_in_file(dir_path,file_path):
	"""
		This method accepts two arguments root directory path and file name 
		It then finds given TEXT_TO_FIND and replaces it with TEXT_TO_REPLACE
	"""
	file = fileinput.FileInput(os.path.join(dir_path,file_path), inplace = True)
	for line in file:
		print(line.replace(TEXT_TO_FIND,TEXT_TO_REPLACE), end='')
	file.close()

if __name__ == '__main__':
	main()