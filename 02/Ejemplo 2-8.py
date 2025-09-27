# Ejemplo 2-8: Clase Secuencia Abstracta

class Secuencia(metaclass=ABCMeta):
    
    @abstractmethod
    def __len__(self):
        
    @abstractmethod
    def __getitem__(self, j):
        
    def __iter__(self):
        """Por convención un iterador debe devolver otro"""
        return IteradorSecuencial(self)
