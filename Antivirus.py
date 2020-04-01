from tkinter import *
from os import path
import os

master = Tk()

def exit():
  master.destroy()

def remove():
    f = input("What is the path of the file that you want to delete?  ")
    os.remove(f)

def scan():
  print("Scanning. . .")
  print("Wanna_Crypt:"+str(path.exists('WannaCry.exe')))
  print("MEMZ:"+str(path.exists('MEMZ-destructive.exe')))
  print("MEMZ:"+str(path.exists('MEMZ-clean.exe')))
  print("MEMZ:"+str(path.exists('MEMZ-destructive.bat')))
  print("MEMZ:"+str(path.exists('MEMZ-clean.bat')))
  print("Virus_General:"+str(path.exists('virus.sh')))
  print("Virus_General:"+str(path.exists('virus.bat')))
  print("Virus_General:"+str(path.exists('virus.zvz')))
  print("Virus_General:"+str(path.exists('virus.exe')))
  print("Keep in mind that this virus scans the most well-known viruses. e.g. WannaCry, MEMZ, or just virus.exe!")

b = Button(master, text="Delete a virus", command=remove)
b.pack()

b = Button(master, text="Scan", command=scan)
b.pack()

b = Button(master, text="Exit", command=exit)
b.pack()

mainloop()
