#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import utils
import config
import tkinter as tk  

root = tk.Tk() #creamos la ventana
root.title("MUT (ww^r)")
root.resizable(0,0)
root.geometry("800x200")

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()

entry = utils._read_line(args)  

NUM_STATE_ALPHA_INIT_STATE, alpha, list_trans, word = utils.transitions(entry)
wl = ''
for w in word:
  wl = wl + ''.join(w)

alpha.append("#")
list_trans = config.conf(list_trans)
word_end, lista_step =  config._main_(word, NUM_STATE_ALPHA_INIT_STATE, list_trans, alpha)
lista_final = config._dictionary_(word_end, lista_step)

strit = iter(lista_final)
_step_s = iter(lista_step)
word_init = tk.Label(root, text=("Palabra Orginal: \n" + wl), font=("Helvetica", 16), fg="gray" )
label = tk.Label(root, text=next(strit, _step_s), font=("italic", 20), width=(50), height=(15), fg = "green")
word_init.pack()
label.pack()




def refresh():
    try:
        label['text'] =  next(strit)
        root.after(400, refresh)
    except StopIteration:
        root.after(100000, root.destroy)

root.after(400, refresh)
root.mainloop()