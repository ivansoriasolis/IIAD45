# Ejemplo 8-1. La clase base abstracta Tree

class Tree:
    """Clase base abstracta que representa una arbol"""
    
    #---------------- clase Position anidada ---------------
    class Position:
        """Abstraccion que representa la localizacion de un solo elemento"""
        
        def element(self):
            """Devolver el elemento almacenado en esta Position"""
            raise NotImplementedError('Debe implementarse por subclase')
            
        def __eq__(self, otro):
            """Devuelve True si otro representa la misma localizacion"""
            raise NotImplementedError('Debe implementarse por subclase')
            
        def __ne__(self, otro):
            """Devuelve True si otro no representa la misma localizacion"""
            raise NotImplementedError('Debe implementarse por subclase')
            
    #-- metodos abstractos que las subclases concretas deben soportar ----
    def root(self):
        """Devuelve Position que es la raiz del arbol (o None si es vacio)"""
        raise NotImplementedError('Debe implementarse por subclase')
        
    def parent(self, p):
        """Devuelve Position que es el padre de p (o None si es vacia)"""
        raise NotImplementedError('Debe implementarse por subclase')

    def num_children(self, p):
        """Devuelve el numero de hijos que Position p tiene"""
        raise NotImplementedError('Debe implementarse por subclase')

    def children(self, p):
        """Genera una iteracion de Positions que representan los hijos de p"""
        raise NotImplementedError('Debe implementarse por subclase')
        
    def __len__(self):
        """Devuelve el numero total de elementos en el arbol"""
        raise NotImplementedError('Debe implementarse por subclase')
        
    #----- metodos concretos impelementados en esta clase ---------
    def is_root(self, p):
        """Devuelve True si Position p es la raiz del arbol"""
        return self.root() == p
    
    def is_leaf(self, p):
        """Devuelve True si Position p no tiene un hijo"""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Devuelve True si el arbol esta vacio"""
        return len(self) == 0
    
    def depth(self, p):
    	"""Devuelve el numero de niveles separando posiciones P desde la raiz"""
    	if self.is_root(p):
    		return 0
    	else:
    		return 1 + self.depth(self.parent(p))
        
    def _height1(self):
        """Devuelve la altura del arbol"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _height2(self, p):
        """Devuelve la altura del subarbol con raiz en la posicion p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        """Devuelve la altura del subarbol con raiz en la posicion p
        
        si p es None, devuelve la altura del arbol entero
        """
        if p is None:
            p = self.root()
        return self._height2(p)
    
    def __iter__(self):
        """Genera una iteracion de los elementos del arbol"""
        for p in self.positions():
            yield p.element()
    
    def preorder(self):
        """Genera una iteracion preorden de posiciones en el arbol"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
                
    def _subtree_preorder(self, p):
        """Genera una iteracion preorden de posiciones en el arbol con raiz en p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
                
    def positions(self):
        """Genera una iteracion de la posiciones del arbol"""
        return self.preorder()