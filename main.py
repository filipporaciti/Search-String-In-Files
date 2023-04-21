#!/usr/bin/env python3

from typing import Optional
import typer
import os, sys

def main(string: str, directory: str, blacklist: str = typer.Option("", help='Set directory or files that the program don\'t search string. You can put more values separated by space character (Example --> "log main.py .git")'), 
         verbose: bool = typer.Option(False, "--verbose", "-v", help="Show output in verbose mode")):
    blacklist = blacklist.split(' ')
    find = string.encode()

    for root, dirs, files in os.walk(directory.rstrip('/')):
        for file in files:
            exit = False
            for b in blacklist:
                if b in (root+'/'+file).split('/'):
                    exit = True
                    break
            if not exit:
                f = open(root + '/' + file, 'rb').read()
                if find in f:
                    lin = f.split(b'\n')
                    for i in range(len(lin)):
                        if find in lin[i]:
                            try:
                                print('\033[92m' + root + '/' + file + '\033[0m' + ' --> \033[94m(' + str(i) + ')\033[95m ' + lin[i].decode() + '\033[0m')
                            except:
                                print('\033[92m' + root + '/' + file + '\033[0m' + ' --> \033[94m(' + str(i) + ')\033[0m')
                        elif verbose:
                            print('\033[91mNot here --> ' + root + '/' + file + '\033[0m')
                            
  
  
typer.run(main)

