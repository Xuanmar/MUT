import utils 
def conf(transiciones):
  transicion = []
  aux_tr = []
  num = ""
  for tr in transiciones:
    aux_tr.clear()
    num = ""
    for ch in tr:
      if ch.isnumeric():
        num = num + ch
      else:
        if num != '':
          aux_tr.append(str(num))
          num =  "" 
        aux_tr.append(str(ch))
        
    transicion.append(aux_tr.copy())
  return transicion

def render(word, index):
  word_aux = word.copy()
  word_aux.insert(index, "[")
  word_aux.insert(index + 2, "]")
  voidc = ''
  for letter in word_aux:
    voidc = voidc + ''.join(letter)
  return str(voidc)

def _step_state(state, next_state, action, read):
  if next_state != "h":
    if action == "R":
      trans = ("q"+state + "  with  " + read + "  ->  q"+ next_state +"  ") + "▶"
    elif action == "L":  
      trans = ("q"+state + "  with  " + read + "  ->  q"+ next_state +"  ") + "◀"
    else: 
      trans = ("q"+state + "  with  " + read + "  ->  q"+ next_state +"  ") + action
  else:
    if action == "R":
      trans = ("q"+state + "  with  " + read + "  ->  "+ next_state +"  ") + "▶"
    elif action == "L":  
      trans = ("q"+state + "  with  " + read + "  ->  "+ next_state +"  ") + "◀"
    else: 
      trans = ("q"+state + "  with  " + read + "  ->  "+ next_state +"  ") + action
  return str(trans) 

def _main_(word, NUM_STATE_ALPHA_INIT_STATE, list_trans, alpha):
  state = NUM_STATE_ALPHA_INIT_STATE[2]
  index = len(word)-1
  lista_config = []
  lista_step = []
  while(state != "h"):
    word_old = render(word, index)
    lista_config.append( str(word_old) )
    next_state, act, read = utils._init_(state, list_trans, word, index)
    lista_step.append(_step_state(state, next_state, act, read))
    state = next_state
    word, index = utils._accion(act, word, index, alpha)
    word = utils._check_sharp(word)

  return lista_config, lista_step 

def _dictionary_(word, step):
  lista_f = []
  index = 0
  for w in word:
    d = w + "\n\n " + step[index]
    lista_f.append(str(d))
    index = index+1
  return lista_f


