'''
Created on Mar. 8, 2022

@author: Anmol Nagpal
'''
import subprocess
from tkinter import *
from tkinter import messagebox
from businessLogic import *
from subprocess import CalledProcessError

root = Tk()
root.title("Costa UI v1.0")
root.minsize(900, 600)
root.maxsize(900, 600)

frame_address = Frame(root)
frame_address.pack(pady=100)
l_address = Label(frame_address, text="Enter contract address: ").grid(row=0, column=0, padx=10)
e_address = Entry(frame_address, width=80)
e_address.grid(row=0, column=1, padx=10)
def run():
    address = e_address.get()
    try:
        output = str(subprocess.check_output(['go run main.go -a ' + address + ' -i'], shell=True))
        label = Label(root, text=output)
        label.pack()
    except CalledProcessError as e:
        messagebox.showerror(title="CMD Error", message=str(e))
b_address = Button(frame_address, text="RUN", command=run).grid(row=0, column = 2, padx=10)


root.mainloop()