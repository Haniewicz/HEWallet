import os
import os.path

def list_wallets():
    wallets_path = "./wallets"
    files = []
    for r, d, f in os.walk(wallets_path):
        for file in f:
            if '.txt' in file:
                files.append(file)
    x = 1
    for f in files:
        f,roz = f.split(".")
        print(str(x)+": "+f)
