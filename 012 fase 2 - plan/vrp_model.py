import json

def solve_vrptw(data):
    depot = data['depot']
    locations = data['locations']
    capacity = data['capacity']
    dist_matrix = data['distance_matrix']
    time_matrix = data['time_matrix']
    
    unvisited = {loc['id']: loc for loc in locations}
    routes = []
    
    while unvisited:
        route = []
        current_node = 0  # Depot
        current_load = 0
        current_time = depot['time_window'][0]
        
        route.append(0)
        
        while True:
            best_next = None
            best_dist = float('inf')
            
            for loc_id, loc in unvisited.items():
                travel_time = time_matrix[current_node][loc_id]
                arrival_time = max(current_time + travel_time, loc['time_window'][0])
                
                # Check constraints
                if (current_load + loc['demand'] <= capacity and 
                    arrival_time <= loc['time_window'][1]):
                    
                    dist = dist_matrix[current_node][loc_id]
                    if dist < best_dist:
                        best_dist = dist
                        best_next = loc_id
            
            if best_next is not None:
                # Move to best_next
                travel_time = time_matrix[current_node][best_next]
                arrival_time = max(current_time + travel_time, unvisited[best_next]['time_window'][0])
                
                current_time = arrival_time + unvisited[best_next]['service_time']
                current_load += unvisited[best_next]['demand']
                current_node = best_next
                
                route.append(best_next)
                del unvisited[best_next]
            else:
                # Return to depot
                route.append(0)
                routes.append(route)
                break
                
    return routes

def calculate_total_cost(routes, dist_matrix):
    total_cost = 0
    for route in routes:
        for i in range(len(route) - 1):
            total_cost += dist_matrix[route[i]][route[i+1]]
    return total_cost

def solve_baseline(data):
    # Simple baseline: Visit each node one by one (Depot -> Node -> Depot)
    routes = []
    for loc in data['locations']:
        routes.append([0, loc['id'], 0])
    return routes

if __name__ == "__main__":
    with open(r'004 data\data.json', 'r') as f:
        data = json.load(f)
    
    # Heuristic solution
    h_routes = solve_vrptw(data)
    h_cost = calculate_total_cost(h_routes, data['distance_matrix'])
    
    # Baseline solution
    b_routes = solve_baseline(data)
    b_cost = calculate_total_cost(b_routes, data['distance_matrix'])
    
    print("--- REFERANSELØSNING (BASELINE) ---")
    print(f"Antall ruter: {len(b_routes)}")
    print(f"Total distanse: {b_cost:.2f} km")
    
    print("\n--- HEURISTISK LØSNING (GREEDY) ---")
    print(f"Antall ruter: {len(h_routes)}")
    for i, route in enumerate(h_routes):
        print(f"Rute {i+1}: {' -> '.join(map(str, route))}")
    print(f"Total distanse: {h_cost:.2f} km")
    
    improvement = (b_cost - h_cost) / b_cost * 100
    print(f"\nForbedring: {improvement:.2f}%")
