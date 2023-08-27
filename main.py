import os
import getpass
config = open("~/terminal-plus/term.cfg", "r")
config = config.read()
exec(config)
os.system("clear")
if logintoadifferentaccount == True:
    os.system("su ", account)
print("Welcome to Terminal+")
while True:
    if safemode == True:
        username = getpass.getuser()
        if username == "root":
            exit
    currentdir = os.getcwd()
    cmdexec = input(currentdir, ">")
    if autosuperuser == True:
        os.system("sudo ", cmdexec)
    else:
        os.system(cmdexec)
