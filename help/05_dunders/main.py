"""This is the example module.

This module does stuff.
"""
x=11

import pacotes.modulo_a
import pacotes.subpacote.modulo_b

print(f"__name__: {__name__}")
print(f"__package__: {__package__}")
print(f"__file__: {__file__}")
print(f"__doc__: {__doc__}")
print('-'*100)

print(f"__version__: {pacotes.__version__}")
print(f"__author__: {pacotes.__author__}")
print(f"__maintainer__: {pacotes.__maintainer__}")
print(f"__status__: {pacotes.__status__}")
print(f"__credits__: {pacotes.__credits__}")
print(f"__copyright__: {pacotes.__copyright__}")
print(f"__license__: {pacotes.__license__}")
print(f"__all__: {pacotes.__all__}")
print('-'*100)

print(f"__version__: {pacotes.subpacote.__version__}")
print(f"__author__: {pacotes.subpacote.__author__}")
print(f"__maintainer__: {pacotes.subpacote.__maintainer__}")
print('-'*100)

print(f"__version__: {pacotes.modulo_a.__version__}")
print(f"__author__: {pacotes.modulo_a.__author__}")
print(f"__maintainer__: {pacotes.modulo_a.__maintainer__}")
print('-'*100)

print(f"__version__: {pacotes.subpacote.modulo_b.__version__}")
print(f"__author__: {pacotes.subpacote.modulo_b.__author__}")
print(f"__maintainer__: {pacotes.subpacote.modulo_b.__maintainer__}")
print('-'*100)
