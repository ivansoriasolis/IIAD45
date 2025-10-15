# Implementación de MultiMap utilizando un mapa subyacente para el almacenamiento.

class MultiMap:
  """
  Una clase multimap construida sobre el uso de un mapa subyacente para el almacenamiento.

  Esto usa dict como almacenamiento predeterminado.

  Las subclases pueden sobrescribir la variable de clase _MapType para cambiar el valor predeterminado.
  Esa clase de mapa debe tener un constructor por defecto que produzca un mapa vacío.
  Como ejemplo, se podría definir la siguiente subclase para usar un SortedTableMap:
 
  class SortedTableMultimap(MultiMap):
    _MapType = SortedTableMap
  """
  _MapType = dict                 # Tipo de mapa; puede ser redefinido por una subclase

  def __init__(self):
    """Crea una nueva instancia vacía de multimap."""
    self._map = self._MapType()          # crear una instancia de mapa para el almacenamiento
    self._n = 0

  def __len__(self):
    """Devuelve el número de pares (k,v) en el multimap."""
    return self._n

  def __iter__(self):
    """Itera a través de todos los pares (k,v) en el multimap."""
    for k, secondary in self._map.items():
      for v in secondary:
        yield (k, v)
    
  def add(self, k, v):
    """Agrega el par (k,v) al multimap."""
    container = self._map.setdefault(k, [])     # crea una lista vacía si es necesario
    container.append(v)
    self._n += 1

  def pop(self, k):
    """Elimina y devuelve un par (k,v) arbitrario con la clave k (o lanza KeyError)."""
    secondary = self._map[k]                    # puede lanzar KeyError
    v = secondary.pop()
    if len(secondary) == 0:
      del self._map[k]                          # no quedan pares
    self._n -= 1
    return (k, v)

  def find(self, k):
    """Devuelve un par (k,v) arbitrario con la clave dada (o lanza KeyError)."""
    secondary = self._map[k]                    # puede lanzar KeyError
    return (k, secondary[0])
    
  def find_all(self, k):
    """Genera una iteración de todos los pares (k,v) con la clave dada."""
    secondary = self._map.get(k, [])            # lista vacía por defecto
    for v in secondary:
      yield (k, v)
