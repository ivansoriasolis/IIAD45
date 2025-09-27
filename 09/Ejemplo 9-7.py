#Ejemplo 9-7. Una implementación de pq_sort asumiendo una implementación apropiada de la case PriorityQueue

from HeapPriorityQueue import HeapPriorityQueue
from PositionalList import PositionalList

def pq_sort(C):
  """Ordena una colección de elementos ordenados en una lista posicional"""
  n = len(C)
  P = HeapPriorityQueue()
  for j in range(n):
    element = C.delete(C.first())
    P.add(element, element)
  for j in range(n):
    (k,v) = P.remove_min()
    C.add_last(v)

C = PositionalList()
C.add_last(5)
C.add_last(1)
C.add_last(8)
    
pq_sort(C)

    