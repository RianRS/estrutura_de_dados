import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(G, s):
    # Dicionário para armazenar o mapa de predecessores
    P = {} # Estrutura de dados que mapeia uma chave a um valor

    # Inicialização do algoritmo
    for v in G.nodes():
        G.nodes[v]['color'] = 'White'
        G.nodes[v]['lambda'] = float('inf')
        # Iniciar cor da raiz como cinza
        G.nodes[s]['color'] = 'gray'
        # Custo para a raiz é 0
        G.nodes[s]['lambda'] = 0
        # Iniciar fila vazia
        Q = deque()
        # Inserir nó raiz no início da fila
        Q.append(s)

        # Enquanto fila não estiver vazia
        while len(Q) > 0:
            # Obter o primeiro elemento da fila
            u = Q.popleft()

            # Para cada vértice adjacente a u
            for v in G.neighbors(u):
                # Se v é branco
                if G.nodes[v]['color'] == 'white':
                    # Atualizar o custo de V
                    G.nodes[v]['lambda'] = G.nodes[u]['lambda'] + 1
                    # Adicionar u como antecessor de v
                    P[v] = u
                    # Atualizar cor de v
                    G.nodes[v]['color'] = 'gray'
                    # Incluir v em Q
                    Q.append(v)
                    # Atualizar cor de u
                    G.nodes[u]['color'] = 'black'
                    # Retorna a lista de antecessores
                    return P

                if __name__ == '__main__':
                    # Cria um grafo exemplo
                    G = nx.grid_2d_graph(5, 5)
                    print('Plotando grafo...')
                    # Cria figura para a plotagem do grafo
                    plt.figure(1)
                    # Há vários layouts, mas spring é um dos mais estéticos
                    nx.draw_networkx(G, pos= nx.spring_layout(G), with_labels= True)
                    # Exibir figura
                    plt.show()




