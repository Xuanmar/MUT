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


def _main_(word, NUM_STATE_ALPHA_INIT_STATE, list_trans, alpha):
  state = NUM_STATE_ALPHA_INIT_STATE[2]
  index = len(word)-1
  lista_config = []
  while(state != "h"):
    word_old = config.render(word, index)
    lista_config.append( str(word_old) )
    state, act = utils._init_(state, list_trans, word, index)
    word, index = utils._accion(act, word, index, alpha)
    word = utils._check_sharp(word)
  return lista_config 
    

word_end =  _main_(word, NUM_STATE_ALPHA_INIT_STATE, list_trans, alpha)


strit = iter(word_end)
word_init = tk.Label(root, text=("Palabra Orginal: \n" + wl), font=("Helvetica", 16) )
label = tk.Label(root, text=next(strit), font=("Helvetica", 20), width=(50), height=(15), fg = "green")
word_init.pack()
label.pack()

def refresh():
    try:
        label['text'] = next(strit)
        root.after(500, refresh)
    except StopIteration:
        root.after(100000, root.destroy)

root.after(500, refresh)
root.mainloop()