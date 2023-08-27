import os
os.system("clear")
print("Welcome to Terminal+")
while True:
    currentdir = os.getcwd()
    cmdexec = input(">")
    os.system(cmdexec)
