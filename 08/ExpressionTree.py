# Expression Tree

from LinkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
  """An arithmetic expression tree."""

  def __init__(self, token, left=None, right=None):
    """Crea un arbol de expresion
    """
    super().__init__()                        # LinkedBinaryTree inicializcion
    if not isinstance(token, str):
      raise TypeError('Token debe ser una cadena')
    self._add_root(token)                     # use el metodo heredado
    if left is not None:                      # forma de tres parametros
      if token not in '+-*x/':
        raise ValueError('token debe ser operador valido')
      self._attach(self.root(), left, right)  # use el metodo heredado

  def __str__(self):
    """Return representacion de cadena de la expresion."""
    pieces = []                 # sequence of piecewise strings to compose
    self._parenthesize_recur(self.root(), pieces)
    return ''.join(pieces)

  def _parenthesize_recur(self, p, result):
    """Append representacion por partes del subarbol de p."""
    if self.is_leaf(p):
      result.append(str(p.element()))                    # valor derecho como cadena
    else:
      result.append('(')                                 # parentesis abierto
      self._parenthesize_recur(self.left(p), result)     # subarbol izquierdo
      result.append(p.element())                         # operador
      self._parenthesize_recur(self.right(p), result)    # subarbol derecho
      result.append(')')                                 # parentesis cerrado

  def evaluate(self):
    """Return el resultado numerico de la expresion."""
    return self._evaluate_recur(self.root())

  def _evaluate_recur(self, p):
    """Return el resultado numerico del subarbol con raiz en p."""
    if self.is_leaf(p):
      return float(p.element())      # se asume que el elemento es numerico
    else:
      op = p.element()
      left_val = self._evaluate_recur(self.left(p))
      right_val = self._evaluate_recur(self.right(p))
      if op == '+':
        return left_val + right_val
      elif op == '-':
        return left_val - right_val
      elif op == '/':
        return left_val / right_val
      else:                          # trata 'x' or '*' como multiplicacion
        return left_val * right_val   

def tokenize(raw):
  """Produce una lista de tokens indicados por un cadena de expresion.

  Por ejemplo la cadena '(43-(3*10))' resulta en la lista
  ['(', '43', '-', '(', '3', '*', '10', ')', ')']
  """
  SYMBOLS = set('+-x*/() ')    # permite '*' or 'x' para multiplicacion

  mark = 0
  tokens = []
  n = len(raw)
  for j in range(n):
    if raw[j] in SYMBOLS:
      if mark != j:                 
        tokens.append(raw[mark:j])  # completa el token anterior
      if raw[j] != ' ':
        tokens.append(raw[j])       # incluye este token
      mark = j+1                    
  if mark != n:                 
    tokens.append(raw[mark:n])      # completa el token precedente
  return tokens

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

if __name__ == '__main__':
  big = build_expression_tree(tokenize('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))'))
  print(big, '=', big.evaluate())
