import time
from networkx.readwrite.json_graph.jit import jit_data
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

"""
The program outputs a random matrix and generates a random undirected graph each time you execute it. 
User can specify the number of friends/nodes in this network. 
In the generated matrix, the first column represents the node itself, and it cannot be repeated.
This is the number that's unique to each row; the consecutive columns represent the neighbors/friends of the node.
"""

# define the number of nodes/friends
number_of_nodes = 8  # off by 1

# for debugging purpose, output the generated matrix to a text file
generated_text_name = "generatedFile.txt"
generated_text_url = (Path(__file__).parent).joinpath(generated_text_name)


def write_to_txt_file():
    """
    Rules:
    - Undirected graph (ie. If I am friends with you, you must be friends with me; Otherwise we are not friends)
    - A node cannot connect to itself (ie. You can't be friends with yourself)
    - A node must have at least one connection (ie. You must have at least one friend. If you're not friends with anyone, you don't belong to this network.)
    - The number of neighbors of a given node is random (ie. The number of friends you have is random)
    - The neighbors of a node is random(ie. Who you're friends with is random)
    """
    with open(generated_text_name, "w") as f:
        for i in range(number_of_nodes):
            # define the initial "self" nodes or the first column
            f.write(str(i) + " ")

            # return the random "friends" of the 'self' node
            for j in range(number_of_nodes):
                start = random.randrange(1)
                surprise = random.randrange(1, 2)
                a = random.randrange(start, number_of_nodes, surprise)
                b = random.randrange(start, number_of_nodes, surprise)
                if a > b and a != i:  # a node can't be friends with itself
                    f.write(str(a) + " ")
                else:
                    f.write(" " + " ")  # indicating that the node has no friends
            f.write("\n")


def draw_graph():
    """
    draw the created matrix
    """
    G = nx.Graph()
    with open(generated_text_url, "r") as f:
        for i, row in enumerate(f):
            row = row.strip().split()
            if len(row) not in (0, 1):
                self_node = row[0]
                for neighbors in row[1:]:
                    G.add_edge(self_node, neighbors)
            elif len(row) == 1:
                if row[0] not in G:
                    nx.add_node(row[0])
            else:
                # if a row is empty, print to console
                # this is for debugging
                print(f"row {i+1} is empty")
    pos = nx.spring_layout(G, k=0.3)
    nx.draw_networkx_nodes(G, pos, alpha=0.5)
    nx.draw_networkx_edges(G, pos, edge_color="#808080")
    labels = {}
    for node in G.nodes():
        labels[node] = node

    nx.draw_networkx_labels(G, pos, labels, font_family="DejaVu Sans")
    plt.gca().margins(0.15, 0.15)
    plt.show()


if __name__ == "__main__":
    # start_time = time.time()
    write_to_txt_file()
    draw_graph()
    # print(f"\n[Finished in {(time.time() - start_time):.2f}s]")
