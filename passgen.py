# ███████╗░█████╗░███╗░░██╗████████╗░█████╗░░░░██████╗░███████╗██╗░░░██╗
# ╚════██║██╔══██╗████╗░██║╚══██╔══╝██╔══██╗░░░██╔══██╗██╔════╝██║░░░██║
# ░░███╔═╝██║░░██║██╔██╗██║░░░██║░░░██║░░██║░░░██║░░██║█████╗░░╚██╗░██╔╝
# ██╔══╝░░██║░░██║██║╚████║░░░██║░░░██║░░██║░░░██║░░██║██╔══╝░░░╚████╔╝░
# ███████╗╚█████╔╝██║░╚███║░░░██║░░░╚█████╔╝██╗██████╔╝███████╗░░╚██╔╝░░
# ╚══════╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░
#                                             >> https://github.com/zooont

# Импортирую библиотеки и чищу/объявляю библиотеки
import random
import os
import time
import colorama
import itertools
import threading
import sys

class style:
   GREEN = '\033[77m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   ITALIC = '\e[3m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r                               Грузимся ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

# Лжезагрузка
print(style.BOLD + style.GREEN + """
███████╗░█████╗░███╗░░██╗████████╗░█████╗░░░░██████╗░███████╗██╗░░░██╗
╚════██║██╔══██╗████╗░██║╚══██╔══╝██╔══██╗░░░██╔══██╗██╔════╝██║░░░██║
░░███╔═╝██║░░██║██╔██╗██║░░░██║░░░██║░░██║░░░██║░░██║█████╗░░╚██╗░██╔╝
██╔══╝░░██║░░██║██║╚████║░░░██║░░░██║░░██║░░░██║░░██║██╔══╝░░░╚████╔╝░
███████╗╚█████╔╝██║░╚███║░░░██║░░░╚█████╔╝██╗██████╔╝███████╗░░╚██╔╝░░
╚══════╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░""" + style.END)
print(style.ITALIC + "                                             >> https://github.com/zooont\n" + style.END)
                                                                      
t = threading.Thread(target=animate)
t.start()
time.sleep(3)
done = True

# Основная часть кода
os.system('cls')
gen=True
while gen:
  print("Генератор паролей 1.0\n")
  chars = '+-/*!&$#?=@<>AaBbcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  length = input(" » 🎉 Введите длину пароля: ")
  length = int(length)
  for n in range(1):
      password =''
      for i in range(length):
        password += random.choice(chars)
  print("🔐 Ваш пароль:", password, "\n(длина ", length, " символов)")
  gen=False
  print("\n♻ Автовозврат в меню через минуту!")
  time.sleep(5)
  gen=True