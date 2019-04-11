def _read_line(args):
  entry = []
  line = args.file.readline()
  if line != "":
    while line != "":
      entry.append(line)
      line = args.file.readline()
    return entry
  else:
    return False


def transitions(entry):
  trans = entry[2]
  trans = trans.replace("\n", "")
  list_trans = trans.split(" ")
 
  NUM_STATE_ALPHA_INIT_STATE = entry[0]
  NUM_STATE_ALPHA_INIT_STATE = NUM_STATE_ALPHA_INIT_STATE.replace("\n", "")
  NUM_STATE_ALPHA_INIT_STATE = NUM_STATE_ALPHA_INIT_STATE.split(" ")
 
  alpha = entry[1]
  alpha = alpha.replace("\n", "")
  alpha = alpha.split(" ")

  word = entry[3] 
  word = word.replace("\n", "")
  word = list(word)

  return NUM_STATE_ALPHA_INIT_STATE, alpha, list_trans, word

def _move(index, mov, word):
  if mov == "R":
    if index < len(word)-1:
      index = index + 1
      return index
    else: return False
  elif mov == "L":
    if index > 0:
      index = index - 1
      return index
    else: return False
  else:
    return False 

def _write(word, simbol, index):
  if index >= 0 and index <= len(word):
    word[index] = simbol
    return word
  else: return False

def _accion(act, word, index, alpha):
  if act in alpha:
   word = _write(word, act, index)
  else:
   index = _move(index, act, word)
  return word, index

def _check_sharp(word):
  if word[-1] == "#":
    return word
  else:
    word.append("#")
    return word

def _init_(state, list_trans, word, index):
  next_state = state
  act = ""
  read = ""
  for tr in list_trans:
    if tr[0] == state:
      if tr[1] == word[index]:
        next_state = tr[-2]
        act = tr[-1]
        read = word[index]
  return next_state, act, read

