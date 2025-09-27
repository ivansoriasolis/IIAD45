# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 12:06:12 2025

@author: soria
"""

from LinkedBinaryTree import LinkedBinaryTree
from EulerTour import EulerTour

class PreorderPrintIndentedEuler(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*' ' + str(p.element()))
        
class PreorderPrintIndentedLabeledTour(EulerTour):
  def _hook_previsit(self, p, d, path):
    label = '.'.join(str(j+1) for j in path)    # etiquetas son one-indexed
    print(2*d*' ' + label, p.element())
    
class ParenthesizeTour(EulerTour):
  def _hook_previsit(self, p, d, path):
    if path and path[-1] > 0:                  # p sigue un sibling
      print(', ', end='')                      # de forma que lo precede con coma
    print(p.element(), end='')                 # entonces imprime el elemento
    if not self.tree().is_leaf(p):             # si p tiene hijos
      print(' (', end='')                      # imprime parentesis de apertura

  def _hook_postvisit(self, p, d, path, results):
    if not self.tree().is_leaf(p):             # si p tiene hijos
      print(')', end='')                       # imprime parentesis cerrados    


def preorder_indent(T, p, d):
    """Imprime la representacion preorden del subarbol de T con raiz en p 
    y profundidad d"""
    print(2*d*' '+str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d+1)


def preorder_label(T, p, d, path):
    """Imprime la representacion etiquetada del subarbol de T con raiz en p 
    y profundidad d"""
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()

def parenthesize(T, p):
    """Imprimir la representacion parentetica del subarbol de T con raiz en p"""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')
    
if __name__ == '__main__':
    lbt = LinkedBinaryTree()
    lbt._add_root(6)
    lbt._add_right(lbt.root(),8)
    lbt._add_left(lbt.root(),4)
    lbt._add_left(lbt.left(lbt.root()),3)
    lbt._add_right(lbt.left(lbt.root()), 5)
    lbt._add_left(lbt.right(lbt.root()), 9)

    
    print("Identado")
    preorder_indent(lbt, lbt.root(), 0)

    print("Con numeración:")
    preorder_label(lbt, lbt.root(), 0, [])
    
    print("Parentizada")
    parenthesize(lbt, lbt.root())
    
    print("\n")
    print("Recorrido de Euler")    
    peuler = PreorderPrintIndentedEuler(lbt)
    peuler.execute()
    
    print("\n")
    print("Recorrido de Euler etiquetado")    
    peuler = PreorderPrintIndentedLabeledTour(lbt)
    peuler.execute()
    
    print("\n")
    print("euler parentizado")
    peuler = ParenthesizeTour(lbt)
    peuler.execute()
    