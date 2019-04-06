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

def _main_(word, NUM_STATE_ALPHA_INIT_STATE, list_trans, alpha):
  state = NUM_STATE_ALPHA_INIT_STATE[2]
  index = len(word)-1
  lista_config = []
  while(state != "h"):
    word_old = render(word, index)
    lista_config.append( str(word_old) )
    state, act = utils._init_(state, list_trans, word, index)
    word, index = utils._accion(act, word, index, alpha)
    word = utils._check_sharp(word)
  return lista_config 