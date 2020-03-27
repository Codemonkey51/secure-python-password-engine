from getpass import getpass
import hashlib
from termcolor import colored, cprint
from os import system as sys

def passwordEncrypt(password):
  return(hashlib.sha256(password.encode()).hexdigest())
def setPassword():
  PASSWORD = securePasswordInput("Whats your password? ")
  if (PASSWORD != securePasswordInput("Confirm password: ")):
    cprint("Passwords didnt match retry. ")
    return(setPassword())
  sys('clear')
  return(PASSWORD)
def passwordCheck(password, guess):
  if(password == guess):
    return(True)
  else:
    return(False)
def securePasswordInput(passwordPrompt):
  return(passwordEncrypt(getpass(prompt=passwordPrompt)))
