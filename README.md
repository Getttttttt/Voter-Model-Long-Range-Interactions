# Voter-Model-Long-Range-Interactions

This repository contains simulation codes for studying the Voter model on a 2D lattice with long-range interactions. It includes tools to visualize opinion dynamics over time and observe the effects of varying the network size (N) and the proportion of long-range edges (p) on the duration of metastable states (plateaus).

## Question description


1. Read this week’s information
 
2. Based on existing research, try to randomly add (or randomly reconnect) long-range edges with a proportion of $p$ on the lattice network of $d=2$, and observe whether $n_a(t)$ of the Voter model changes over time. There will be a relatively flat interval (called plateau), when the system is in a metastable state. Please observe the changing pattern of the plateau length (that is, the duration of the metastable state) by changing $N$ and $p$. In addition, considering that the grid of $d=2$ is very easy to visualize (each node can be assigned plane coordinates), please conduct a random simulation ($N$ is recommended to be larger, $p$ can be changed), and observe the different $p$ When, what shape is the distribution of viewpoints in the plateau period (nodes of different viewpoints are marked with different colors, and edges do not need to be drawn)
 
3. (Additional) Save the visual images of each step of a simulation and synthesize them into videos, so that you can observe the continuous evolution process of viewpoints under the voter model.

Reference API:
 
1. https://networkx.org/documentation/latest/reference/generated/networkx.generators.lattice.grid_2d_graph.html#networkx.generators.lattice.grid_2d_graph
 
2. https://networkx.org/documentation/latest/reference/generated/networkx.drawing.nx_pylab.draw_networkx_nodes.html#networkx.drawing.nx_pylab.draw_networkx_nodes

## Steps for Simulation and Visualization

1. Set Up the Simulation Environment:
Import necessary libraries: networkx for graph manipulation, matplotlib and networkx for visualization, and numpy for numerical operations.

2. Generate the 2D Lattice:
Use networkx.generators.lattice.grid_2d_graph to create a $d=2$ lattice of size $\sqrt{N} \times \sqrt{N}$ where $N$ is the number of nodes.

3. Add Long-Range Connections:
Iterate over all nodes and add a long-range edge with probability $p$. Ensure that the added edge does not already exist.

4. Initialize Voter States:
Assign each node a random initial state (e.g., 0 or 1 representing different opinions).

5. Simulation of the Voter Model:
Perform the Voter Model dynamics: randomly select a node, then randomly select a neighbor (including long-range connections) and adopt its state.
Record the number of nodes in each state over time ($n_a(t)$).

6. Analysis of the Plateau:
Plot $n_a(t)$ over time to visually inspect for the presence of a plateau. Calculate the length of any observed plateau by determining the interval over which $n_a(t)$ remains relatively unchanged.

7. Visualization of States on the Lattice:
Use networkx.drawing.nx_pylab.draw_networkx_nodes to visualize the state of the lattice at different points in time, particularly during the plateau phase, with different colors representing different states.

8. Adjust Parameters and Repeat:
Vary $N$ and $p$ to observe changes in the plateau's characteristics.

9. Video Creation:
Store each frame of the simulation (each step or at intervals) and use a video creation library to stitch the frames into a video showing the evolution of states.

## Realization Code

