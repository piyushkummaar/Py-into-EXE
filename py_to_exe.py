import os
import subprocess
import sys
from termcolor import colored
from colorama import init

def main(file_name):
    print(colored('[exist] PyInstaller exists...', 'green'))
    print(colored(f'[load] Py file loaded...{file_name}','yellow'))
    # print("Argument List:", str(sys.argv))
    subprocess.check_call(["pyinstaller", "--onefile", sys.argv[1]])
    print(colored('[stop] Completed successfully..Exe stored in dist folder.','green'))
    

def install(package):
    print(colored(f'[install] Installing {package}....', 'green'))
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def show_pack():
    try:
        print(colored('[check] Checking package existance...','yellow'))
        subprocess.check_call([sys.executable, "-m", "pip", "show", 'PyInstaller'])
        return True
    except Exception as e:
        return False

if __name__ == '__main__':
    try:
        init()
        print(colored("[start] Starting Converting....\tPython file into .exe", "green"))
        if show_pack() == False:
            install('pyinstaller')
            main(sys.argv[1])
        else:
            main(sys.argv[1])
    except Exception as e:
        print(colored(e,'red'))
