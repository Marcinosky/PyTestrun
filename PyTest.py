from datetime import datetime
import os, subprocess, colorama
from time import sleep
from pathlib import Path
from sys import argv, exit

"""
    This program executes all python scripts in a given directory and returns whether they finished succesfully or not
"""

if len(argv) != 2:
    print("Missing argument tested directory or too many arguments")
    exit()

dir = argv[1]

if not os.path.isdir(dir):
    print("Given argument not a directory")
    exit()

FAIL, PASS = colorama.Fore.LIGHTRED_EX + "FAIL" + colorama.Fore.WHITE, colorama.Fore.LIGHTGREEN_EX + "PASS" + colorama.Fore.WHITE

def flatten(directory):
    """
    Returns a list of file paths to every python script in a given directory and its sub directories
    """
    listOfFile = os.listdir(directory)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(directory, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + flatten(fullPath)
        else:
            if fullPath.endswith(".py"): allFiles.append(fullPath)          
    return allFiles

def runTest():
    directories = flatten(dir)
    Path("logs").mkdir(parents=True, exist_ok=True)
    log = open(datetime.now().strftime('logs/log%Y%m%d_%H%M.txt'), "w") 
    for test in directories:
        print("Running " + test, end=" ")
        log.write('-----------------------------\nStarting "' + test + '"...\n')
        outcome = subprocess.run(test, shell=True, check=False, capture_output=True)
        sleep(1)
        if not outcome.returncode:
            print(PASS)
        else:
            print(FAIL)
        log.write(f"Finished, returned code = {outcome.returncode}\n")
        if outcome.returncode != 0:
            log.write("An error occured:\n")
            log.write(outcome.stderr.decode("utf-8"))
    log.close

runTest()
