import os
from tinydb import TinyDB
from time import sleep
from threading import Thread as td


# color
red = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
magenta = '\x1b[35m'
cyan = '\x1b[36m'

class fb_infoga:
  def __init__(self):
    pass

  def banner(self):
    os.system('clear')
    print('{cyan}************************'
    print('{cyan}*      {green}FB-INFOGA       {cyan}*'
    print('{cyan}************************'
    print('{cyan}* {green}Author : {yellow}CyberKallan {cyan}*'
    print('{cyan}* {green}Version : {yellow}0.0.1      {cyan}*'
    print('{cyan}************************'
    print("".join([i for i in "\n"*3]))
