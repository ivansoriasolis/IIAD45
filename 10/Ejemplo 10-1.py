# Conteo de palabras.

import sys
filename = sys.argv[1]

freq = {}
for piece in open(filename).read().lower().split():
  # Solo aceptamos caracteres alfabeticos
  word = ''.join(c for c in piece if c.isalpha())
  if word:                                # requiero un caracter alafabetico
    freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (w,c) in freq.items():    # (clave, valor) tuplas representan (word, count)
  if c > max_count:
    max_word = w
    max_count = c
print('La palabra mas frecuente es', max_word)
print('Su numero de ocurrencias es', max_count)