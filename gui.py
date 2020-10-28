"""
Visualización gráfica de árboles usando pyplot y networkx
Yael Chavoya
"""
import networkx as nx
import matplotlib.pyplot as plt
from arbol import Arbol

# mapa de colores para usar en el árbol
_colors = [
    '#55f',
    '#77f',
    '#99f',
    '#bbf',
    '#ddf',
    '#fff',
]


def visualizar_arbol(arbol: Arbol):
    """
    Abre un plot de pyplot con una representación gráfica del árbol

    :param arbol: El árbol a dibujar
    """

    # Crear un grafo de networkx con los datos de nuestro árbol
    G = nx.Graph()

    # Calcular la profundidad para establecer el mapa de colores
    nodos = arbol.order_dfs()
    depths = {n: arbol.distance_between(arbol.root, n) for n in nodos}

    # Nodos
    for nodo in reversed(nodos):
        G.add_node(nodo.content, order=-depths[nodo])

    # Mapa de colores
    colors = []
    for n in reversed(nodos):
        colors.append(_colors[depths[n] % len(_colors)])

    # Aristas (conexión padre-hijo)
    for nodo in nodos:
        for child in nodo.children:
            G.add_edge(nodo.content, child.content)

    # Crear un plot nuevo
    plt.plot()

    # Establecer el algoritmo para posicionar los nodos
    pos = nx.multipartite_layout(G, subset_key='order', align='horizontal')

    # Dibujar y mostrar el árbol
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, font_size=10)
    plt.show()
