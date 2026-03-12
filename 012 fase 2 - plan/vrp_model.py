import json

def solve_vrptw(data, max_cars=None):
    depot = data['depot']
    locations = data['locations']
    capacity = data['capacity']
    dist_matrix = data['distance_matrix']
    time_matrix = data['time_matrix']
    
    unvisited = {loc['id']: loc for loc in locations}
    routes = []
    
    # Continue as long as there are unvisited nodes AND we haven't hit the car limit
    while unvisited:
        if max_cars is not None and len(routes) >= max_cars:
            break
            
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
                
                # Check constraints (Capacity and Time Window)
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
                
    return routes, list(unvisited.keys())

def calculate_total_cost(routes, dist_matrix):
    total_cost = 0
    for route in routes:
        if len(route) > 2: # Ignore empty routes (0 -> 0)
            for i in range(len(route) - 1):
                total_cost += dist_matrix[route[i]][route[i+1]]
    return total_cost

if __name__ == "__main__":
    with open(r'004 data\data.json', 'r') as f:
        data = json.load(f)
    
    print("=== SCENARIOANALYSE: ANTALL BILER ===\n")
    
    for n in [1, 2, 3]:
        routes, missed = solve_vrptw(data, max_cars=n)
        cost = calculate_total_cost(routes, data['distance_matrix'])
        visited_count = len(data['locations']) - len(missed)
        
        print(f"SCENARIO: {n} BIL(ER)")
        print(f"Status: {'Fullført' if not missed else 'Inkomplett'}")
        print(f"Besøkte lokasjoner: {visited_count}/{len(data['locations'])}")
        if missed:
            print(f"Manglende lokasjoner: {missed}")
        
        for i, route in enumerate(routes):
            print(f"  Bil {i+1}: {' -> '.join(map(str, route))}")
        
        print(f"Total distanse: {cost:.2f} km")
        print("-" * 30)
