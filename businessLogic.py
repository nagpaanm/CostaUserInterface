'''
Created on Mar. 8, 2022

@author: Anmol Nagpal
'''
from tkinter import *

def run(e_address, root):
    address = e_address.get()
    label = Label(root, text=address)
    label.pack()