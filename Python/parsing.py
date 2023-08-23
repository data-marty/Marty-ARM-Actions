import yaml
import os


os.system('cls') # on windows

with open("C:\Repos\Marty-ARM-Actions\Python\parsing.yaml", "r") as stream:
#with open("parsing.yaml", "r") as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as e:
        print(e)