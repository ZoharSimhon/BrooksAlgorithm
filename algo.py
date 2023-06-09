import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def createGraph(nodes,edges,colors):
    G = nx.Graph(colors = colors)
    G.add_nodes_from(nodes, takenColors = [])
    G.add_edges_from(edges)
    return G

def showGraph(G):
    node_colors = ["lightblue"] * len(G.nodes)
    edge_colors = ["lightblue"] * len(G.edges)
    np.random.seed(100)
    plt.clf()
    nx.draw_networkx(G, node_color=node_colors,
                    edge_color=edge_colors, with_labels=True)
    plt.ion()
    plt.show()
    plt.pause(1.5)
    
    
    
    # np.random.seed(100)
    # plt.clf()
    # nx.draw_networkx(G, node_color=node_colors,
    #                 edge_color=edge_colors, with_labels=True)
    # plt.ion()
    # plt.show()
    # plt.pause(1.5)


# def greedyColor(G, list):
    # for node in G.nodes:
        # for neighbor in G.nodes[node].neighbors:
            

    # pass
