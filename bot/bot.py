import sys as sys
import os
false = False
true = True


#Write a file
def write_file(file, message):
	files = open(file, "w")
	files.write(message)
	files.flush()
	files.close()

def delete_file(file):
	os.remove(file)

def getExistingFile(file):
	if(os.path.isfile(file)):
		return true
	else:
		return false

isEngaged = getExistingFile(".bot_engage")

def disengage():
	if(isEngaged == true):
		print "Disengaging..."
		delete_file(".bot_engage")
	else:
		print "You have to engage the bot in order to engage it"
def engage():
	if(isEngaged == true):
		disengageBot = raw_input("You've already engaged the bot. Do you want to disengage? ")
		if(disengageBot == "Yes"):
			disengage()
		elif(disengageBot == "yes"):
			disengage()
		else:
			 exit()
	else:
		write_file(file=".bot_engage", message="bot.engaged=true")
		print "Bot engaged"

if(os.path.isfile("/sdcard/qpython/projects/Bot/bot_response.py") == False):
	file = open("/sdcard/qpython/projects/Bot/bot_response.py", "w")
	file.write("def getResponse(messageToBot):")
	file.write("\n\tif(messageToBot == \"Hello\"):")
	file.write("\n\t\tprint \"Clarissa: Hi\"")

	
if(sys.argv[1] == "engage"):
	engage()
elif ( sys.argv[1] == "disengage" ):
	disengage()

