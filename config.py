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
