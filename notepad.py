import os
import subprocess as sp
import time

count = 0

while count < 20:
    programName = "notepad.exe"
    fileName = "smalltext.txt"
    sp.Popen([programName, fileName])

    text_file = open("smalltext.txt", "w")
    text_file.write("Count right now: " + str(count))
    text_file.close()

    time.sleep(1.3)
    count += 1
    os.system("TASKKILL /F /IM notepad.exe")
