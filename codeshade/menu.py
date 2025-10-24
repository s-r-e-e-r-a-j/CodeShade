# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from pathlib import Path
from .python_obf import to_base64, to_emoji
from .bash_obf import obf_bash
from .core import C

def menu() -> None:
    print(C.cyan)
    print(r"""
       _____          _       _____ _               _      
      / ____|        | |     / ____| |             | |
     | |     ___   __| | ___| (___ | |__   __ _  __| | ___ 
     | |    / _ \ / _` |/ _ \\___ \| '_ \ / _` |/ _` |/ _ \
     | |___| (_) | (_| |  __/____) | | | | (_| | (_| |  __/
      \_____\___/ \__,_|\___|_____/|_| |_|\__,_|\__,_|\___|                                                                                                    
     """)
    print(C.reset)
    while True:
        print(C.blue + "1) Python -> base64" + C.reset)
        print(C.blue + "2) Python -> emoji" + C.reset)
        print(C.blue + "3) Bash obfuscate" + C.reset)
        print(C.blue + "0) Exit" + C.reset)
        c = input(C.yellow + "> " + C.reset).strip()
        try:
            if c == "1":
                s = Path(input("src: ").strip())
                d = Path(input("dst: ").strip())
                v = input("var (payload): ").strip() or "payload"
                to_base64(s, d, v)
            elif c == "2":
                s = Path(input("src: ").strip())
                d = Path(input("dst: ").strip())
                to_emoji(s, d)
            elif c == "3":
                s = Path(input("src: ").strip())
                d = Path(input("dst: ").strip())
                a = input("auto install? (y/N): ").strip().lower() == "y"
                obf_bash(s, d, auto_install=a)
            elif c == "0":
                print(C.green + "bye" + C.reset)
                return
        except Exception as e:
            print(C.red + "error: " + str(e) + C.reset)
