from __future__ import print_function
import random
import time
import replit
# Made by Sevan Evans & Jimmy Lembeck
# Mr. Landfrieds 3rd Period Comp. Sci. class
# Completely hand-made, from scratch.

intro = "Welcome to Sync Labs RSA Encryption / Decryption Software"
choose = """Please choose an option:

  Encrypt
  
  Decrypt
   """
tocode = "What is the message you'd like to encrypt?: "
todecode = "What is the message you'd like to decrypt?: "
ea = "What is your E value?: "
na = "What is your N value?: "
da = "What is your D value?: "
def encode(enc):
  legnth = len(enc)
  show = []
  showindex = []
  for x in enc:
    r = chr(random.randint(130,550))
    if x == " ":
      show += " "
    else:
      show += r
  for y in range(legnth):
    showindex.append(y)
  for t in show:
    change = random.choice(showindex)
    showindex.remove(change)
    show[change] = enc[change]
    word = "".join(show)
    time.sleep(0.08)
    replit.clear()
    if enc == choose:
      print(intro)
      print(" ")
    if enc == da:
      print(intro)
      print(" ")
      print(choose)
      print(" ")
      print(todecode)
      print(" ")
    if enc == tocode:
      print(intro)
      print(" ")
      print(choose)
      print("")
      print(ea)
      print("")
      print(na)
      print(" ")
    if enc == ea:
      print(intro)
      print(" ")
      print(choose)
      print(" ")
    if enc == todecode:
      print(intro)
      print(" ")
      print(choose)
      print(" ")
    if enc == na:
      print(intro)
      print(" ")
      print(choose)
      print(" ")
      print(ea)
      print(" ")
    print(word)
too = True
while too == True:
  encode(intro)
  time.sleep(0.5)
  encode(choose)
  
  raw = input()
  
  ###ENCRYPTION###
  if raw.lower() == "encrypt" or raw.lower() == "e" or raw.lower() == "enc":
    global n
    global e
    brok = ""
    print(" ")
    print(encode(ea))
    e = input()
    print(encode(na))
    n = input()
    print(encode(tocode))
    message = input()
    for x in message:
      y = ord(x)
      enc2 = pow(y,int(e),int(n))
      den = chr(enc2)
      brok += (den)
    print(encode(brok))
    print("This screen will disappear in T-minus 10 seconds")
    time.sleep(10)
  ###DECRYPTION###
  if raw.lower() == "decrypt" or raw.lower() == "d" or raw.lower() == "dec":
    print(encode(todecode))
    brok = input()
    print(encode(da))
    d = input()
    print(encode(na))
    n = input()
    decr = ""
    for t in brok:
      numerize = ord(t)
      dec = pow(numerize, int(d), int(n))
      stu = chr(dec)
      decr += stu
    print(decr)
    print("This screen will disappear in T-minus 10 seconds")
    time.sleep(10)