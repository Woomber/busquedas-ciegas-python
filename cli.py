"""
Interfaz de comandos
Yael Chavoya
"""
from arbol import Arbol
import gui


def _clear_screen():
    """
    Colocar espaciado entre menú y menú
    """
    print('\n'*3)


def _wait_enter():
    """
    Esperar a que el usuario presione ENTER
    """
    input('Presione ENTER para continuar...')
    _clear_screen()


def _mostrar_arbol(arbol: Arbol):
    """
    Mostrar gráficamente el árbol

    :param arbol: El árbol a mostrar
    """
    print('Mostrando en pyplot...')
    gui.visualizar_arbol(arbol)


def _mostrar_bfs(arbol: Arbol):
    """
    Mostrar el orden del árbol por amplitud (BFS)

    :param arbol: El árbol del que se mostrará el orden
    """
    print('El orden del árbol usando búsqueda en amplitud (BFS):')
    print([n.content for n in arbol.order_bfs()])
    _wait_enter()


def _mostrar_dfs(arbol: Arbol):
    """
    Mostrar el orden del árbol por profundidad (DFS)

    :param arbol: El árbol del que se mostrará el orden
    """
    print('El orden del árbol usando búsqueda en profundidad (DFS):')
    print([n.content for n in arbol.order_dfs()])
    _wait_enter()


def main_menu(arbol: Arbol):
    """
    Menú principal
    """
    entrada: str = ''

    while entrada != '0':
        print('====== Búsquedas ciegas en Árboles ======\nAutor: Yael Chavoya\n')
        print('Nota: El árbol se configura en el código en main.py\n')
        print('Seleccione una opción:')
        print('1: Visualizar árbol')
        print('2: Ver orden de búsqueda en amplitud (BFS)')
        print('3: Ver orden de búsqueda en profundidad (DFS)')
        print('0: Salir')

        entrada = input('\n> ')
        print()

        if entrada == '0':
            break
        elif entrada == '1':
            _mostrar_arbol(arbol)
        elif entrada == '2':
            _mostrar_bfs(arbol)
        elif entrada == '3':
            _mostrar_dfs(arbol)
        else:
            print('Opción no reconocida.')
            _wait_enter()
