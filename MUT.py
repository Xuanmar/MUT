#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import utils
import config
import tkinter as tk  

root = tk.Tk() #creamos la ventana
root.title("MUT (ww^r)")
root.resizable(0,0)
root.geometry("800x250")
mov = ["R", "L"]

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()

entry = utils._read_line(args)  
control = False
if entry != False and len(entry) == 4:
  NUM_STATE_ALPHA_INIT_STATE, alpha, list_trans, word = utils.transitions(entry)
  list_trans = config.conf(list_trans)
  alpha.append("#")
  if config._check_line_1(NUM_STATE_ALPHA_INIT_STATE):
    if config._check_ins(list_trans, NUM_STATE_ALPHA_INIT_STATE[0], alpha, mov) and config._check_word(word,alpha):
      wl = config.origin_W(word)
      word_end, lista_step, num_steps =  config._main_(word, NUM_STATE_ALPHA_INIT_STATE, list_trans, alpha)
      lista_final = config._dictionary_(word_end, lista_step, num_steps)
      strit = iter(lista_final)
      _step_s = iter(lista_step)
      word_init = tk.Label(root, text=("Palabra Orginal: \n" + wl), font=("Helvetica", 16), fg="gray" )
      label = tk.Label(root, text=next(strit, _step_s), font=("italic", 20), width=(50), height=(15), fg = "green")
      word_init.pack()
      label.pack()
      control = True
    else:
      print("Error en los parametros del archivo de entrada   error#1 (Revisa la linea 3 y 4)")
      control = False
  else:
    print("Error en los parametros del archivo de entrada     error#2  (Revisa la linea 1)")
    control = False
else:
  print("El archivo esta vacio")
  control = False


def refresh():
    try:
        label['text'] =  next(strit)
        root.after(600, refresh )
    except StopIteration:
        root.after(100000, root.destroy)
        
if control == True:
  root.after(600, refresh)
  root.mainloop()
