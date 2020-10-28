"""
Clases Nodo y Árbol
Yael Chavoya
"""
from typing import List

# Tipo de datos que almacena el árbol
_content_type = str


class Nodo:
    """
    Clase Nodo, representa un nodo del árbol
    """

    def __init__(self, content: _content_type):
        """
        Inicializa un nodo con su contenido

        :param content: El dato que almacena el nodo
        """
        self.content = content
        self.children: List[Nodo] = []

    def add_child(self, nodo):
        """
        Agrega un nodo hijo de este nodo

        :param nodo: Un nodo que se desee poner como hijo
        """
        if nodo not in self.children:
            self.children.append(nodo)

    def remove_child(self, nodo):
        """
        Elimina un nodo hijo de este nodo

        :param nodo: El nodo hijo a eliminar
        """
        if nodo in self.children:
            self.children.remove(nodo)

    def depth(self) -> int:
        """
        Calcula recursivamente la altura del nodo

        :return: la altura del nodo
        """
        if len(self.children) == 0:
            return 0

        # Regresar la altura máxima de sus hijos más uno
        return max([n.depth() for n in self.children]) + 1

    def es_hoja(self) -> bool:
        """
        Determina si el nodo es un nodo hoja

        :return: True si el nodo es nodo hoja
        """
        return len(self.children) == 0


class Arbol:
    """
    Clase Árbol
    """

    def __init__(self, root: Nodo = None):
        """
        Inicializa un árbol con una raíz

        :param root: El nodo raíz del árbol
        """
        self.root = root

    def insert(self, parent: Nodo, *nodos: Nodo, method='bfs'):
        """
        Inserta varios nodos al árbol, como hijos de parent

        :param parent: El nodo al que se agregarán los nodos (debe estar en el árbol)
        :param nodos: Los nodos a agregar al árbol
        :param method: Método para buscar al nodo padre (bfs o dfs)
        """
        if not self.root:
            raise ValueError('No hay raíz')

        if self.is_in_tree(parent, method):
            for nodo in nodos:
                parent.add_child(nodo)
            return

        raise ValueError('El padre no está en el árbol')

    def distance_between(self, nodo1: Nodo, nodo2: Nodo) -> int:
        """
        Calcula recursivamente la distancia de un nodo a otro. nodo1 debe ser ancestro de nodo2

        :param nodo1: El primer nodo de donde se calculará la distancia (origen)
        :param nodo2: El segundo nodo de donde se calculará la distancia (destino)
        :return: la distancia de la raíz al nodo, -1 si nodo1 no es ancestro de nodo2
        """

        # Si el nodo1 está vacío, la distancia es -1
        if not nodo1:
            return -1

        # Si el nodo es el mismo, la distancia es 0
        if nodo1 == nodo2:
            return 0

        # Buscar la distancia entre los hijos de nodo1 y nodo2
        for child in nodo1.children:
            dst = self.distance_between(child, nodo2)
            if dst >= 0:
                return dst + 1

        # En cualquier otro caso retornar -1
        return -1

    def search_bfs(self, content: _content_type) -> Nodo or None:
        """
        Buscar un nodo por su contenido, por bfs

        :param content: El dato a buscar
        :return: El nodo que contiene al dato, o None si no se encontró
        """

        # Nodos por buscar, es una cola
        pending: List[Nodo] = [self.root]
        # Nodos ya visitados
        visited: List[Nodo] = []

        # Mientras la cola tenga items
        while len(pending) > 0:
            # Procesar el primer nodo
            curr = pending.pop(0)
            visited.append(curr)

            # Si el nodo es el que se busca, retornarlo
            if curr.content == content:
                return curr

            # Agregar los hijos no visitados del nodo a la cola
            for child in curr.children:
                if child in visited:
                    continue
                pending.append(child)

        return None

    def search_dfs(self, content: _content_type) -> Nodo or None:
        """
        Buscar un nodo por su contenido, por dfs

        :param content: El dato a buscar
        :return: El nodo que contiene al dato, o None si no se encontró
        """

        # Nodos por buscar, es una pila
        pending: List[Nodo] = [self.root]
        # Nodos ya visitados
        visited: List[Nodo] = []

        # Mientras la pila tenga items
        while len(pending) > 0:
            # Procesar el primer nodo
            curr = pending.pop()
            visited.append(curr)

            # Si el nodo es el que se busca, retornarlo
            if curr.content == content:
                return curr

            # Agregar los hijos no visitados del nodo a la pila
            for child in reversed(curr.children):
                if child in visited:
                    continue
                pending.append(child)

        return None

    def is_in_tree(self, nodo: Nodo, method='bfs') -> bool:
        """
        Determina si un nodo está en el árbol

        :param nodo: El nodo a buscar
        :param method: Método de búsqueda (bfs o dfs)
        :return: True si el nodo está en el árbol
        """
        if method == 'bfs':
            return self._is_in_tree_bfs(nodo)
        return self._is_in_tree_dfs(nodo)

    def _is_in_tree_bfs(self, nodo: Nodo) -> bool:
        """
         Determina si un nodo está en el árbol usando bfs

        :param nodo: El nodo a buscar
        :return: True si el nodo está en el árbol
        """

        # Nodos por buscar, es una cola
        pending: List[Nodo] = [self.root]
        # Nodos ya visitados
        visited: List[Nodo] = []

        # Mientras la cola tenga items
        while len(pending) > 0:
            # Procesar el primer elemento
            curr = pending.pop(0)
            visited.append(curr)

            # Si el nodo es el que se busca, retornar
            if curr == nodo:
                return True

            # Agregar los hijos no visitados del nodo a la cola
            for child in curr.children:
                if child in visited:
                    continue
                pending.append(child)

        return False

    def _is_in_tree_dfs(self, nodo: Nodo) -> bool:
        """
         Determina si un nodo está en el árbol usando dfs

        :param nodo: El nodo a buscar
        :return: True si el nodo está en el árbol
        """

        # Nodos por buscar, es una pila
        pending: List[Nodo] = [self.root]
        # Nodos ya visitados
        visited: List[Nodo] = []

        # Mientras la pila tenga items
        while len(pending) > 0:
            # Procesar el primer elemento
            curr = pending.pop()
            visited.append(curr)

            # Si el nodo es el que se busca, retornar
            if curr == nodo:
                return True

            # Agregar los hijos no visitados del nodo a la pila
            for child in reversed(curr.children):
                if child in visited:
                    continue
                pending.append(child)

        return False

    def order_bfs(self) -> List[Nodo]:
        """
        Obtiene una lista con los nodos en orden por amplitud

        :return: una lista de Nodos, ordenada por bfs
        """

        # Nodos por buscar, es una cola
        pending: List[Nodo] = [self.root]
        # Nodos ya visitados
        visited: List[Nodo] = []

        # Mientras la cola tenga items
        while len(pending) > 0:
            # Procesar el primer elemento
            curr = pending.pop(0)
            visited.append(curr)

            # Agregar los hijos no visitados del nodo a la cola
            for child in curr.children:
                if child in visited:
                    continue
                pending.append(child)

        return visited

    def order_dfs(self) -> List[Nodo]:
        """
        Obtiene una lista con los nodos en orden por amplitud

        :return: una lista de Nodos, ordenada por bfs
        """
        # Nodos por buscar, es una pila
        pending: List[Nodo] = [self.root]
        # Nodos ya visitados
        visited: List[Nodo] = []

        # Mientras la pila tenga items
        while len(pending) > 0:
            # Procesar el primer elemento
            curr = pending.pop()
            visited.append(curr)

            # Agregar los hijos no visitados del nodo a la pila
            for child in reversed(curr.children):
                if child in visited:
                    continue
                pending.append(child)

        return visited
