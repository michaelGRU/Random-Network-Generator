import time
from networkx.readwrite.json_graph.jit import jit_data
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

number_of_nodes = 7  # off by 1
generated_text_name = "generatedFile.txt"
generated_text_url = (Path(__file__).parent).joinpath(generated_text_name)


def write_to_txt_file():
    with open(generated_text_name, "w") as f:
        for i in range(number_of_nodes):
            f.write(str(i) + " ")
            for j in range(number_of_nodes):
                start = random.randrange(1)
                surprise = random.randrange(1, 2)
                a = random.randrange(start, number_of_nodes, surprise)
                b = random.randrange(start, number_of_nodes, surprise)
                if a > b and a != i:
                    f.write(str(a) + " ")
                else:
                    f.write(" " + " ")
            f.write("\n")


def draw_graph():
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
