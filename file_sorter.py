from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#For watchdog module install watchdog using pip/pip3 install command 

from os import listdir
from os.path import isfile, join
from os import rename
import json
import time

#Add another list here for your specific files type folder
Images = ["jpeg","bmp","png","gif","raw","tiff","psd","jpg"]
Music = ["mp3","wav","mpa","cda","wma","m4a"]
Compressed = ["7z","rar","pkg","gz","z","zip","deb","iso"]
Executable = ["apk","bat","com","exe","jar"]
Videos = ["mp4","flv","avi","mpg","mpeg","wmv","m4v","3gp","mkv"]
Docs = ["rtf","txt","pdf","doc","docx","wpd","xls","xlsm","xlsx","pps","ppt","pptx","odp"]
part_file = ["crdownload","part"]

#The location at which you wanna sort the files
Base_location = "Your_folder_location_here"


class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
			file_list = [x for x in listdir(Base_location) if isfile(join(Base_location, x))]
			for file in file_list:
				typ = file.split(".")[-1]
				src =  Base_location + "/" + file

#If you wanna add more folders then just add another elif condition
	# elif typ in your_custom_extension_list:
	# 	new_destination = your_custom_destination_variable + "/" + file
	# 	rename(src,new_destination)

				if typ in part_file:
					return True
				elif typ in Images:
					new_destination = Images_location + "/" + file
					rename(src,new_destination)
				elif typ in Music:
					new_destination = Music_location + "/" + file
					rename(src,new_destination)
				elif typ in Compressed:
					new_destination = Compressed_location + "/" + file
					rename(src,new_destination)
				elif typ in Executable:
					new_destination = Executable_location + "/" + file
					rename(src,new_destination)
				elif typ in Videos:
					new_destination = Videos_location + "/" + file
					rename(src,new_destination)
				elif typ in Docs:
					new_destination = Docs_location + "/" + file
					rename(src,new_destination)
				else:
					new_destination = Misc_location + "/" + file
					rename(src,new_destination)

#Paths to your directories dedicated for specific files


Images_location = ""
Music_location = ""
Compressed_location = ""
Executable_location = ""
Videos_location = ""
Docs_location = ""
Misc_location = ""
Base_location = ""

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, Base_location, recursive=True)
observer.start()

try:
	while True:
#Change sleep time below 
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop
observer.join()