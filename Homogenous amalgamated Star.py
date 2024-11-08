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
    
    
    
    
