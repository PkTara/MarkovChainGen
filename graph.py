import matplotlib.pyplot as plt 
import networkx as nx

# ==== Deal with args =====

import sys
args = sys.argv

if len(args) > 1:
    file = args[1]
else: # default file
    file = "weights.json"   # default
    # print("ERROR: must provide weights as json")
    # quit()

# ==== Import JSON ====

import json
with open(file) as f:
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
            print(key, value, weight)
            G.add_edge(key, value, weight=weight)


    drawGraph(G)


def plotGraph():
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def drawGraph(G):
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

    pos = nx.spring_layout(G, seed=7, k =40)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=200)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=3, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=4, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    # plt.tight_layout()
    plt.show()

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plotGraph()



from generateText import nextWord
def sequentialGraph(noWords: int, last: str):
    first = last
    last = nextWord(first)

    for i in range(noWords):

        limit = -1 # no limit
        local_data = dict(list(data.items())[:limit])

        print(local_data)
        for value, weight in local_data[first].items():
            print(first, value, weight)
            G.add_edge(first, value, weight=weight)

        
    drawGraph(G)

    # pos = nx.spring_layout(G, seed=7)

    # nx.draw_networkx_nodes(G, pos, node_size=200)
    # nx.draw_networkx_edges(G, pos)
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # plotGraph()

# sequentialGraph(1, "God")
wholeGraph()
