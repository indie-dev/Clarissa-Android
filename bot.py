import os
import sys as sys
import bot_info as info
os.system("python /sdcard/qpython/projects/bot/bot/bot.py engage")
from bot_response import *
#Allow the user to communicate with the bot
def toBot():
	messageToBot = raw_input(info.getName()+" ")
	if(messageToBot == "--add-command"):
		writeCommand(command=raw_input("Command: "), response=raw_input("Responses: "))
		os.system("clear")
		
	elif(messageToBot == "kill-bot"):
		exit()
	elif(messageToBot == "--get-commands"):
		print "Commands: "
		print getCommands()

		print "\nResponses: "
		print getResponses()
	elif(messageToBot == "--clear-commands"):
	#	os.remove("/sdcard/qpython/projects/Bot/commands.bot")
	#	os.remove("/sdcard/qpython/projects/Bot/responses.bot")
		os.remove("/sdcard/qpython/projects/Bot/bot_response.py")
		open("/sdcard/qpython/projects/Bot/bot_response.py","w").write("#Automatically generated\ndef getResponse(messageToBot):\n\tif(messageToBot == \"Hi Clarissa\"\n\t\tprint \"Hii!!\"")
		print "Cleared commands"
	elif(messageToBot == "--set-name"):
	  info.addUser()
	getResponse(messageToBot)
	toBot()


def writeCommand(command, response):
	file = open("/sdcard/qpython/projects/bot/bot_response.py", "a")
	file.write("\n\telif(messageToBot == \""+command+"\"):")
	file.write("\n\t\tprint \"Clarissa: "+response+"\"")
	file.flush()
	file.close()

def getIf(message, command, response):
	if(message == command):
		print "Clarissa: "+response
	else:
		print "Clarissa: I do not understand "+message

def getCommands():
	return open("/sdcard/qpython/projects/bot/commands.bot", "r").read()

def getResponses():
	return open("/sdcard/qpython/projects/bot/responses.bot", "r").read()

toBot()
