import os as os
#get bot info
def getName():
     if(os.path.isfile("/sdcard/qpython/projects/Bot/info.user")):
        return open("/sdcard/qpython/projects/Bot/info.user","r").read()
     else:
        return "User: "

def addUser():
     if(os.path.isfile("/sdcard/qpython/projects/bot/info.user")):
          print "No more than one user can be added!"
     else:
          open("/sdcard/qpython/projects/Bot/info.user","w").write(raw_input("Name: "))
