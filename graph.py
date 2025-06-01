import matplotlib.pyplot as plt 
import networkx as nx
from log_config import logger

# ==== Deal with args =====

import sys
args = sys.argv

if len(args) > 1:
    file_path = args[1]
else: # default file
    file_path = "weights.json"   # default
    logger.warning("Default weights being used")
    # print("ERROR: must provide weights as json")
    # quit()


import os

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, "weights",  file_path)

# ==== Import JSON ====

import json
with open(file_path) as f:
    global data
    data = json.load(f)

# ===== Make Graph =======

G = nx.Graph()


    

# ==== Draw Graph =======

def wholeGraph():

    limit = 30
    local_data = dict(list(data.items())[:limit])
    for key, values in local_data.items():
        for value, weight in values.items():
            logger.info(f"key - {key}, value - {value}, weight - {weight}")
            G.add_edge(key, value, weight=weight)


    drawGraph(G)


def plotGraph():
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def drawGraph(G, nodeSize=800, labelFontSize=20, nodeFontSize=4, edgeWidth=1, k=None):
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

    pos = nx.spring_layout(G, seed=7, k=k)  # positions for all nodes - seed for reproducibility

    # nodes
    colors = [G.nodes[n].get("color", "lightgray") for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_size=nodeSize, node_color=colors)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=edgeWidth)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=edgeWidth, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=labelFontSize, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)


    plotGraph()

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=labelFontSize, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plotGraph()



from generateText import nextWord
def sequentialGraph(noWords: int, last: str):


    for i in range(noWords):
        first = last
        last = nextWord(first)

        limit = -1 # no limit
        local_data = dict(list(data.items())[:limit])

        for value, weight in local_data[first].items():
            G.add_edge(first, value, weight=weight)

        G.nodes[first]["color"] = "green" # so nodes we actually use are green
        G.nodes[last]["color"] = "green" # complete traversal
        
    drawGraph(G)

    # pos = nx.spring_layout(G, seed=7)

    # nx.draw_networkx_nodes(G, pos, node_size=200)
    # nx.draw_networkx_edges(G, pos)
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # plotGraph()

sequentialGraph(3, "God")
# wholeGraph()
