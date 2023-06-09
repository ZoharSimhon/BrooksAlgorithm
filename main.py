from algo import *
nodes = [i for i in range(6)]
edges = [(0, 1), (1, 2), (3, 2), (4, 3), (4, 5), (1, 5), (2, 4)]
colors = ["teal", "lightcoral", "limegreen", "gold", "cyan", "deeppink", "olivedrab",
          "blueviolet", "firebrick", "orange", "tomato", "maroon", "orchid", "dodgerblue", "yellow"]
G = createGraph(nodes, edges, colors)
# greedyColor(G)
showGraph(G)
