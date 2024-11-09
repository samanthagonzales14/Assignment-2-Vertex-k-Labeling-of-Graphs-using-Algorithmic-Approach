# COMP-SCI 5592
# Assignment2
# Problem3

# 1. Suggest a suitable name: Star-Centroid Graph

# 2. Devise the formulae for calculating order and size of the graph
# Sn,p where n indicates the degree of the new vertex, and 
# p represents the degree of the central vertex in each individual star.
# Let V be the order of Sn,p where (n * p) + 1 = V
# Let E be the size of Sn,p where there is n path from the center vertex and 
# pn paths that connect the outer vertices, where n + 3n = 4n = E

# 3. Data-structure to store the graph
# 4. Assign the labels using algorithm. 
# 5. Store the labels of vertices and weights of the edges as an outcome. 

def create_centroid_graph(n,p):
    # Initialize the graph with adjacency list
    graph = {}
    labels = {}
    edge_weights = {}
    
    central_vertex = 0 # Central vertex labeled as 0
    graph[central_vertex] = []
    labels[central_vertex] = "Central Vertex"
    
    current_label = 1 # Start vertex labeling from 1
    current_weight = 1 # Initialize edge weight


    
    # Loop over each branch
    for i in range(n):
        # Each branch has a center connected to the main central vertex
        branch_center = current_label
        graph[central_vertex].append(branch_center)  # connect central to branch center
        graph[branch_center] = [central_vertex]  # initialize branch center
        
        # Label the branch center vertex
        labels[branch_center] = f"Branch-{i+1} Center"
        edge_weights[(central_vertex, branch_center)] = current_weight  # set weight for edge
        current_weight += 1 # increment weight for next edge
        
        # Add the outer vertices of this branch
        outer_vertices = []
        for j in range(p):
            outer_vertex = current_label + j + 1
            outer_vertices.append(outer_vertex)
            graph[outer_vertex] = [branch_center]  # initialize outer vertex
            graph[branch_center].append(outer_vertex)  # connect branch center to outer
            
            # Label the outer vertices
            labels[outer_vertex] = f"Branch-{i+1} Vertex-{j+1}"
            edge_weights[(branch_center, outer_vertex)] = current_weight  # set weight for edge
            current_weight += 1 # increment weight for next edge
        
        # Update current_label for the next branch
        current_label += 1 + p  # 1 branch center + p outer vertices
    
    return graph, labels, edge_weights

n = 8  # Degree of the new vertex
p = 3  # Degree of the central vertex in each individual branch/star
graph, labels, edge_weights = create_centroid_graph(n,p)

# Display results
print("Graph adjacency list:")
for vertex, neighbors in graph.items():
    print(f"{vertex}: {neighbors}")

print("\nVertex labels:")
for vertex, label in labels.items():
    print(f"{vertex}: {label}")

print("\nEdge weights:")
for edge, weight in edge_weights.items():
    print(f"{edge}: {weight}")
