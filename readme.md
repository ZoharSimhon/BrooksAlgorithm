# Brooks' Algorithm

Brooks' Algorithm is a graph coloring algorithm that aims to assign colors to the vertices of an undirected graph in such a way that no two adjacent vertices share the same color, and the numbers of colors used is not exeeding the graph's maximum degree. The algorithm is constructed from the Brook's theorem's proof.

## Overview
The Brooks algorithm is a graph algorithm used for finding node coloring in general graphs using delta(G) colors or less. The algorithm is using greedy coloring algorithm but determinating the order of the greedy coloring.

The input can be any undirected graph except a clique or an odd cycle
Here's a step-by-step explanation of the Brooks algorithm:

1. **Initialization**: Find the max degree of the graph.

1. **if the max degree is 2 or less**: Use the greedy algorithm without special order

1. **if the max degree is 3 or more**: 
    - if there is a vertex with less neighbors than the max degree, perform BFS from the said vertex and use greedy coloring on the BFS tree in reverse order
    - if the graph is k-regular:
        - if there is a cut vertex remove the vertex and perform the BFS method on the resulting two connected components
        - if there is not a cut vertex, find x,y,z such that x is connected to y,z and y,z are disconnected. remove y and z then perform the BFS method from x and finally add y,z with the same free color 

1. **Output**: The algorithm outputs the node coloring of the graph. the number of colors

## Usage

To use the Blossom-Edmond algorithm, follow these steps:

1. Install Python (version 3.6 or above) on your system if you haven't already.

1. Clone this repository to your local machine or download the source code.

1. Open a terminal or command prompt and navigate to the directory where you cloned/downloaded the repository.

1. Install the required dependencies by running the following command:
    ```
    pip install networkx
    pip install matplotlib
    ```

1. Uncomment the desired example or create your own example by creating a list of nodes and a list of tuples representing the edges

1. Run the command
    ```
    python3 main.py
    ```
1. view the algorithm in action

## References

If you are interested in learning more about the Brooks algorithm and its underlying concepts, you may find the following resources helpful:

- Elad Horev's website https://drive.google.com/file/d/11OjQv5iN9HZIrmnfyEMPrcjxh-K_EhZe/view

---