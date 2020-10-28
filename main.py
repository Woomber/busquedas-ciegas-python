"""
Programa de Búsquedas ciegas
Yael Chavoya
"""
from arbol import Arbol, Nodo
from cli import main_menu


def main():
    """
    Función principal del programa
    """

    # Configurar los nodos que tendrá el árbol
    _1 = Nodo('1')
    _2 = Nodo('2')
    _3 = Nodo('3')
    _4 = Nodo('4')
    _5 = Nodo('5')
    _6 = Nodo('6')
    _7 = Nodo('7')
    _8 = Nodo('8')
    _9 = Nodo('9')
    _10 = Nodo('10')
    _11 = Nodo('11')
    _12 = Nodo('12')

    # Configurar la raíz del árbol
    arbol = Arbol(_1)

    # Configurar los hijos de cada nodo (padre, hijo1, hijo2, ...)
    arbol.insert(_1, _2, _3, _4)
    arbol.insert(_2, _5, _6)
    arbol.insert(_5, _9, _10)
    arbol.insert(_4, _7, _8)
    arbol.insert(_7, _11, _12)

    # Mostrar el menú principal
    main_menu(arbol)


if __name__ == '__main__':
    main()
