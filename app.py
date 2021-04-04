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
    print("{cyan}************************")
    print("{cyan}*      {green}FB-INFOGA       {cyan}*")
    print("{cyan}************************")
    print("{cyan}* {green}Author : {yellow}CyberKallan {cyan}*")
    print("{cyan}* {green}Version : {yellow}0.0.1      {cyan}*")
    print("{cyan}************************")
    print("".join([i for i in "\n"*3]))

  def animate(self,params,result):
    self.banner()
    print(f"{green}Please Wait..")
    t = td(target=self.setup,args=(params,))
    while t.is_alive():
      for i in "-\|/-\|/":
        print(f'\r{c}Please wait {a}{i} ',end="",flush=True)
        sleep(0.1)
    print(f"\nDONE !\n\n{result}")

  def paginate(self,data,n):
    n_data = round(len(data)/n) + 1
    new_data_part = []
    limit = 0
    for i in range(n_data):
      new_data = []
      for x in range(limit,n+limit):
        try:
          new_data.append(data[x])
        except:
          pass
        batas += 1
      if new_data: new_data_part.append(new_data)
    return new_data_part

