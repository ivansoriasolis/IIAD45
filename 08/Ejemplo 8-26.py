# Ejemplo 8-26.py

# ... Continuacion del ejemplo 8-25.py
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