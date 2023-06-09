from algo import *
from orderedSet import *

colors = ["teal", "lightcoral", "limegreen", "gold", "cyan", "deeppink", "olivedrab",
          "blueviolet", "firebrick", "orange", "tomato", "maroon", "orchid", "dodgerblue", "yellow"]

# case delta(G)<= 2 - even cycle
nodes = [i for i in range(6)]
edges = [(0, 1), (1, 2), (2, 3), (4, 3), (4, 5), (0, 5)]

# case delta(G)<= 2 - a path
# nodes = [i for i in range(6)]
# edges = [(0, 1), (1, 2), (2, 3), (4, 3), (4, 5)]


# case 1
# nodes = [i for i in range(6)]
# edges = [(0, 1), (1, 2), (3, 2), (4, 3), (4, 5), (1, 5), (2, 4)]

# case 2 - kappa = 1
# nodes = [i for i in range(10)]
# edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (3, 4),
        #  (4, 5), (5, 6), (5, 8), (6, 7), (6, 9), (7, 8), (7, 9), (8, 9)]

# case 2 - kappa >= 2
# nodes = [i for i in range(6)]
# edges = [(0, 1), (0, 2), (0, 5), (1, 3), (1, 4),
        #  (2, 3), (2, 4), (3, 5), (4, 5)]

G = createGraph(nodes, edges, colors)
showGraph(G)
findMinumColoring(G)
