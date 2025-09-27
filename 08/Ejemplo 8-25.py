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