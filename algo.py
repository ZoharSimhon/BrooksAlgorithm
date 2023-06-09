import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from orderedSet import *

def createGraph(nodes,edges,colors):
    G = nx.Graph(colors = colors)
    # G.add_nodes_from(nodes, takenColors = OrderedSet(),indexColor = -1)
    for node in nodes:
        G.add_node(node, takenColors = OrderedSet(),indexColor = -1)
    G.add_edges_from(edges)
    return G

def showGraph(G):
    node_colors = []
    for node in G.nodes:
        index = G.nodes[node]['indexColor']
        if index != -1:
            node_colors.append(G.graph['colors'][index])
        else:
           node_colors.append("lightblue")

    edge_colors = ["lightblue"] * len(G.edges)
    np.random.seed(100)
    plt.clf()
    nx.draw_networkx(G, node_color=node_colors,
                    edge_color=edge_colors, with_labels=True)
    plt.ion()
    plt.show()
    plt.pause(2)
    

def greedyColor(G,order):
    for node in order:
        
        for neighbor in G.neighbors(node):
            indexColor = G.nodes[neighbor]['indexColor']
            if indexColor != -1:
                G.nodes[node]['takenColors'].add(indexColor)
                
        # check for the first free color
        color = 0
        for c in G.nodes[node]['takenColors']:
            if color != c:
                break
            color += 1
            
        # assign vertex `u` the first available color
        G.nodes[node]['indexColor'] = color

def findDelta(G):
    delta = 0
    for node in G.nodes:
        degree = len(list(G.neighbors(node)))
        if degree > delta:
            delta = degree
    return delta

def findLessDegree(G,delta):
    for node in G.nodes:
        degree = len(list(G.neighbors(node)))
        if degree < delta:
            return node
    return -1

def colorGraph(G,root):
    #find spanning tree with node as root
    spanning_tree = nx.bfs_tree(G, source=root)
    
    #show the spanning_tree using matplotlib
    spanning_tree.graph['colors']= G.graph['colors'] 
    for node in spanning_tree.nodes:
        spanning_tree.nodes[node]['indexColor'] = -1
    showGraph(spanning_tree)
    #created an order list for the greedy coloring
    order = list(spanning_tree.nodes)[-1::-1]
    greedyColor(G,order)

def findMinumColoring(G):
    # check delta(G)
    delta = findDelta(G)
    
    if delta <= 2:
        greedyColor(G, G.nodes)
        showGraph(G)
        return
    
    # two cases of G:
    root = findLessDegree(G,delta)
    #case 1:
    if root != -1:
        colorGraph(G,root)
        showGraph(G)
        return
    
    #case 2: delta-regular
    # two cases of G:
    articulation_points = list(nx.articulation_points(G))
    #case 1:
    if articulation_points:
        #split the graph into 2 graphs
        cut_vertex = articulation_points[0]
        articulation_neighbors = G.neighbors()
        G.remove_node(cut_vertex)
        subgraphs = [G.subgraph(c).copy() for c in nx.connected_components(G)]
        subgraphs[0].add_node(cut_vertex)
        for node in articulation_neighbors:
            if node in subgraphs[0].nodes:
                subgraphs[0].add_edge(node, cut_vertex)
            
        subgraphs[1].add_node(cut_vertex)
        for node in articulation_neighbors:
            if node in subgraphs[1].nodes:
                subgraphs[1].add_edge(node, cut_vertex)
        #color the first graph
        colorGraph(subgraphs[0], cut_vertex)
        showGraph(subgraphs[0])
        #color the first graph
        colorGraph(subgraphs[1], cut_vertex)
        showGraph(subgraphs[1])
        #replace the colors in subgraphs[0]
        color0 = subgraphs[0].nodes[cut_vertex]['indexColor']
        color1 = subgraphs[1].nodes[cut_vertex]['indexColor']
        if color0 !=color1:
            for node in subgraphs[0].nodes:
                if subgraphs[0].nodes[node]['indexColor'] == color0:
                    subgraphs[0].nodes[node]['indexColor'] == color1
                if subgraphs[0].nodes[node]['indexColor'] == color1:
                    subgraphs[0].nodes[node]['indexColor'] == color0
        #merge the subgraphs
        G.add_node(cut_vertex,color= color1)
        for node in articulation_neighbors:
             G.add_edge(node,cut_vertex)
        showGraph(G)
        
        return
        
        
        
    
    #case 2: kapa >= 2
    