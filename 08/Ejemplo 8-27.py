# Ejemplo 8-27.py

def build_expression_tree(tokens):
  """Returns un ExpressionTree en base a una expresion tokenizada.

  los tokens deben ser iterabels de cadenas representando una expresion 
  parentizada tal como ['(', '43', '-', '(', '3', '*', '10', ')', ')']
  """
  S = []                                        # usamos una lista como pila
  for t in tokens:
    if t in '+-x*/':                            # t es un simbolo de operador
      S.append(t)                               # push el operador
    elif t not in '()':                         # considera t como literal
      S.append(ExpressionTree(t))             
    elif t == ')':       # compone un nuevo arbol con las partes
      right = S.pop()                           # subarbol derecho como LIFO
      op = S.pop()                              # simbolo de operador
      left = S.pop()                            # subarbol izquierdo
      S.append(ExpressionTree(op, left, right)) # recolocar arbol
    # ignoramos el parentesis derecho
  return S.pop()