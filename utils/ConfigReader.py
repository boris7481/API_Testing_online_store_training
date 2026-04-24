import os
import configparser
config = configparser.ConfigParser()
path = os.path.abspath(os.getcwd())

#config.read()
print(path)