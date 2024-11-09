#1. AdjacencyList is the best data-structure to represent / store the graph in memory. 

#2. Answer is Code

#3. The Greedy Design Strategy is well-suited for this task. By assigning labels step-by-step, beginning with the main center, then moving to the star centers, and finally to the pendants, the algorithm effectively creates unique labels that meet adjacency constraints. This method keeps computation per node low, allowing for efficient labeling without the need to continually re-check previously assigned labels.

#4. Depth-First Search (DFS) is ideal here because it explores each star subgraph completely before moving to the next, closely matching the structure of a star-centered graph and efficiently handling pendant connections.

#5. Labels: [1, [1, 3, 5, 7], [2, 7, 9, 11], [4, 11, 13, 14], [6, 14, 16, 18], [9, 16, 18, 19], [11, 18, 19, 20], [13, 19, 20, 21], [15, 20, 21, 22], [18, 20, 21, 22], [20, 21, 22, 23], [22, 22, 23, 24], [25, 22, 23, 24]]
    # Edge Weights: [2, 3, 5, 7, 10, 12, 14, 16, 19, 21, 23, 26, 4, 6, 8, 9, 11, 13, 15, 17, 18, 20, 22, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49] 48

#7. CPU can handle approximately 10,000 vertices and associated edges. Beyond this, performance may slow significantly, with memory constraints impacting computations as V and E increase.

#8. Time Complexity:

#Vertex Labeling: O(V) , as each vertex’s label is assigned without revisiting others.
#Edge Weight Assignment: O(E), each edge is assigned a weight in a straightforward pass.
#Total Complexity: O(V * E), which is efficient for large sparse graphs.

#Since each vertex and edge is processed once, the complexity remains linear, making it efficient for graph sizes within hardware capabilities.

import math

def generate_homogeneous_star_graph(num_stars, num_pendants_per_star):
    
    labels = [1, [1]]  # Initialize labels with the main center node
    edge_weights = [2]  # Initialize edge weights with the first weight


    total_vertices = num_stars * num_pendants_per_star + 1
    step_size = math.ceil(total_vertices / 2) / (num_stars - 1)
    
    
    for i in range(1, num_stars):                                       # Generate edges connecting each star center to the main center
        star_label = math.floor(step_size * i)
        labels.append([star_label])
        edge_weights.append(star_label + 1)
        
    
    
    for i, stars in enumerate(labels[1:]):                       # Generate labels for pendants connected to each star center
        pendant_label = min(edge_weights)
        
        
        for j in range(1, num_pendants_per_star):
            
            while (stars[0] + pendant_label) in edge_weights:    # checking whether the value is unique or not 
                pendant_label += 1
                
            edge_weights.append(stars[0] + pendant_label)        # append new pendent_value
            labels[i+1].append(pendant_label)
        
    return labels, edge_weights
    
    
    



num_pendants_per_star = 4
num_stars = 12

labels, edge_weights = generate_homogeneous_star_graph(num_stars, num_pendants_per_star)
print("Labels:", labels)
print("Edge Weights:", edge_weights, len(edge_weights))  




