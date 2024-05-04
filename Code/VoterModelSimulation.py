import os
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import imageio

random.seed(3407)  

def create_network(width, height, probability):
    """Create a 2D grid network with additional long-range edges."""
    grid = nx.grid_2d_graph(width, height, periodic=False)
    nodes = list(grid.nodes())
    for node in nodes:
        for target in nodes:
            if target != node and (node, target) not in grid.edges() and random.random() < probability:
                grid.add_edge(node, target)
    return grid

def visualize_network(grid, path):
    """Visualize the network and save the image to the specified path."""
    plt.figure()
    position = {(x, y): (y, -x) for x, y in grid.nodes()}
    color_map = ['red' if grid.nodes[node]['status'] == 1 else 'blue' for node in grid.nodes()]
    nx.draw_networkx_nodes(grid, position, node_color=color_map, node_size=5)
    plt.savefig(path)
    plt.close()

def initialize_network(grid, infected_prob):
    """Initialize the status of each node in the network."""
    positive_nodes_num = round(len(grid) * infected_prob)
    positive_nodes = random.sample(grid.nodes(), positive_nodes_num)
    nx.set_node_attributes(grid, -1, 'status')
    for node in positive_nodes:
        grid.nodes[node]['status'] = 1
    return grid

def update_network(grid):
    """Update the status of a random node based on a random neighbor's status."""
    node = random.choice(list(grid.nodes()))
    neighbors = list(grid.neighbors(node))
    if neighbors:
        selected_neighbor = random.choice(neighbors)
        grid.nodes[node]['status'] = grid.nodes[selected_neighbor]['status']
    else:
        print(f"Node {node} has no neighbors.")

def calculate_edge_diversity(grid):
    """Calculate the proportion of edges with differing statuses."""
    diverse_count = sum(1 for edge in grid.edges if grid.nodes[edge[0]]['status'] != grid.nodes[edge[1]]['status'])
    return diverse_count / len(grid.edges)

def plot_data(data_dicts, path, title, xlabel, ylabel, scale_log=False):
    """Plot multiple datasets and save to a file."""
    plt.figure(figsize=(10, 8))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if scale_log:
        plt.xscale('log')
    for data_dict in data_dicts:
        times = list(data_dict.keys())
        values = list(data_dict.values())
        plt.plot(times, values)
    plt.savefig(path)
    plt.close()

def generate_video(image_folder, output_path):
    """Generate a video from a sequence of images."""
    images = sorted([img for img in os.listdir(image_folder) if img.endswith('.jpg')],
                    key=lambda x: int(x.split('.')[0]))
    if not images:
        print("No images found.")
        return
    with imageio.get_writer(output_path, fps=30) as writer:
        for image in images:
            img_path = os.path.join(image_folder, image)
            image_data = imageio.imread(img_path)
            writer.append_data(image_data)
    print(f"Video created successfully at {output_path}")

def main():
    width, height, p = 100, 100, 0.0001
    grid = create_network(width, height, p)
    grid = initialize_network(grid, 0.5)
    visualize_network(grid, './initial_network.jpg')

    evolution_data = {}
    for time_step in range(1, 100000):
        update_network(grid)
        if time_step % 100 == 0:
            edge_diversity = calculate_edge_diversity(grid)
            evolution_data[time_step] = edge_diversity
            visualize_network(grid, f'./Images/{time_step}.jpg')
            if edge_diversity == 0:
                break

    plot_data([evolution_data], './evolution_plot.jpg', 'Network Evolution', 'Time', 'Edge Diversity', scale_log=True)
    generate_video('./Images', './network_evolution.mp4')

if __name__ == '__main__':
    main()
