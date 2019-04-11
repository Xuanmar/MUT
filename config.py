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
  voidc = ""
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
  act = ""
  next_state = state
  read = ""
  list_steps = []
  step_number = 0
  while(state != "h"):
    word_old = render(word, index)
    lista_config.append( str(word_old) )
    next_state, act, read = utils._init_(state, list_trans, word, index)
    lista_step.append(_step_state(state, next_state, act, read))
    state = next_state
    word, index = utils._accion(act, word, index, alpha)
    word = utils._check_sharp(word)
    step_number = step_number + 1
    list_steps.append(str(step_number))

  return lista_config, lista_step, list_steps 

def _dictionary_(word, step, num_step):
  lista_f = []
  index = 0
  for w in word:
    d = "-----------------------------------------------------------------------------------\n" + w + "\n-----------------------------------------------------------------------------------\n " + step[index] + "\n Pasos: " + num_step[index]
    lista_f.append(str(d))
    index = index+1
  return lista_f

def _check_ins(Ins, num_state, alpha, Mov):
  val = True
  for _in  in Ins:
    if _in[0].isnumeric() and int(_in[0]) < (int(num_state)-1):
      val = True
    else:
      val = False
      break
    
    if ( (str(_in[1]).isalpha()  or _in[1] == "#")  and len(_in[1]) == 1) and _in[1] in alpha:
      val = True
    else:
      val = False
      break
    if (_in[2].isnumeric() and int(_in[2]) < (int(num_state)-1)) or (_in[2] == "h") :
      val = True
    else:
      val = False
      break
    if ( _in[3] in alpha or _in[3] in Mov)  and len(_in[3]) == 1:
      val = True
    else:
      val = False
      break
  return val

def _check_word(word, alpha):
  val = True
  for w in word:
    if w in alpha:
      val = True
    else:
      val = False
      break
  return val

def _check_line_1(NUM_STATE_ALPHA_INIT_STATE):
  val  = True
  if len(NUM_STATE_ALPHA_INIT_STATE) == 3:
    for num in NUM_STATE_ALPHA_INIT_STATE:
      if num.isnumeric():
        val = True
      else:
        val = False
        break
  else:
    val = False
  return val

def origin_W(word):
  wl = ''
  for w in word:
    wl = wl + ''.join(w)
  return wl
    