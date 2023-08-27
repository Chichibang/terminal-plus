#Set verbose to True to turn on verbose logging:
verbose = False
from tkinter import *
import os
print("Attempt to install git with apt-get and parmeter -y")
os.system("sudo apt-get install git -y")
def upgraderepos():
    os.system("sudo apt update -y")
    if verbose == True:
        print("apt update completed with parameter -y")
    os.system("sudo apt-get update -y")
    if verbose == True:
        print("apt-get update completed with parameter -y")
    os.system("sudo apt full-upgrade -y")
    if verbose == True:
        print("apt full-upgrade completed with parameter -y")
    os.system("sudo apt-get full-upgrade -y")
    if verbose == True:
        print("apt-get update completed with parameter -y")
    if verbose == True:
        print("Repository upgrade completed")
def consolerun():
    downloadexist = os.path.exists("~/terminal-plus")
    if downloadexist == True:
        if verbose == True:
            print("Terminal+ already downloaded, skipping")
    else:
        os.system("cd ~ && git clone https://github.com/Chichibang/terminal-plus")
        if verbose == True:
            print("Git cloned https://github.com/Chichibang/terminal-plus into directory ~")
    os.system("python3 ~/terminal-plus/main.py")
window = Tk()
window.title("PyControl v0.1")
window.geometry("640x480")
greet = Label(text="Welcome to PyControl! These are tools that control your computer.")
greet.grid(column=0, row=0)
upgradebutton = Button(text="Upgrade all repositories", command = upgraderepos)
upgradebutton.grid(column=0, row=1)
consolebutton = Button(text="Terminal+ (linux console)", command=consolerun)
consolebutton.grid(column=0, row=2)
exitbutton = Button(text="Exit PyControl", command=exit)
exitbutton.grid(column=0, row=3)
window.mainloop()