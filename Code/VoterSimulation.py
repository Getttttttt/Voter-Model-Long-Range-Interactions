import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def create_graph(N, p):
    size = int(np.sqrt(N))
    G = nx.generators.lattice.grid_2d_graph(size, size, periodic=True)
    add_long_range_edges(G, p)
    return G

def add_long_range_edges(G, p):
    nodes = list(G.nodes())
    for node in nodes:
        if random.random() < p:
            target = random.choice(nodes)
            while target == node or G.has_edge(node, target):
                target = random.choice(nodes)
            G.add_edge(node, target)

def initialize_states(G):
    states = {node: random.randint(0, 1) for node in G.nodes()}
    return states

def simulate_voter_model(G, states, num_steps):
    for _ in range(num_steps):
        node = random.choice(list(G.nodes()))
        neighbor = random.choice(list(G.neighbors(node)))
        states[node] = states[neighbor]
        # Optionally record the state for visualization/analysis
    return states

def visualize_graph(G, states):
    color_map = ['red' if states[node] else 'blue' for node in G.nodes()]
    nx.draw(G, node_color=color_map, with_labels=True)
    plt.show()

# Main simulation parameters
N = 100  # Adjust as needed
p = 0.1  # Adjust as needed
num_steps = 1000

if __name__ == '__main__':

    # Running the simulation
    G = create_graph(N, p)
    states = initialize_states(G)
    states = simulate_voter_model(G, states, num_steps)
    visualize_graph(G, states)
