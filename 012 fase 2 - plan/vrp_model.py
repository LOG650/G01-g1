import json

def solve_vrptw(data, max_cars=None):
    depot = data['depot']
    locations = data['locations']
    capacity = data['capacity']
    dist_matrix = data['distance_matrix']
    time_matrix = data['time_matrix']
    
    unvisited = {loc['id']: loc for loc in locations}
    routes_data = []
    
    while unvisited:
        if max_cars is not None and len(routes_data) >= max_cars:
            break
            
        route = []
        current_node = 0
        current_load = 0
        current_time = depot['time_window'][0]
        
        route.append(0)
        
        while True:
            best_next = None
            best_dist = float('inf')
            
            for loc_id, loc in unvisited.items():
                travel_time = time_matrix[current_node][loc_id]
                arrival_time = max(current_time + travel_time, loc['time_window'][0])
                
                # Sjekk om vi kan returnere til depotet i tide etter dette besøket
                departure_time = arrival_time + loc['service_time']
                return_to_depot_time = departure_time + time_matrix[loc_id][0]
                
                if (current_load + loc['demand'] <= capacity and 
                    arrival_time <= loc['time_window'][1] and
                    return_to_depot_time <= depot['time_window'][1]):
                    
                    dist = dist_matrix[current_node][loc_id]
                    if dist < best_dist:
                        best_dist = dist
                        best_next = loc_id
            
            if best_next is not None:
                travel_time = time_matrix[current_node][best_next]
                arrival_time = max(current_time + travel_time, unvisited[best_next]['time_window'][0])
                current_time = arrival_time + unvisited[best_next]['service_time']
                current_load += unvisited[best_next]['demand']
                current_node = best_next
                route.append(best_next)
                del unvisited[best_next]
            else:
                # Return to depot
                travel_back = time_matrix[current_node][0]
                return_time = current_time + travel_back
                route.append(0)
                routes_data.append({
                    "route": route,
                    "return_time": return_time,
                    "load": current_load
                })
                break
                
    return routes_data, list(unvisited.keys())

if __name__ == "__main__":
    with open(r'004 data\data.json', 'r') as f:
        data = json.load(f)
    
    print("=== OPTIMALISERING AV ANTALL BILER ===\n")
    
    num_cars = 1
    total_locations = len(data['locations'])
    
    while True:
        print(f"Prøver med {num_cars} bil(er)...")
        routes_info, missed = solve_vrptw(data, max_cars=num_cars)
        
        visited_count = total_locations - len(missed)
        print(f"  Lokasjoner besøkt: {visited_count}/{total_locations}")
        
        if not missed:
            print(f"\nSuksess! Alle lokasjoner besøkt med {num_cars} biler.\n")
            break
        
        num_cars += 1
        if num_cars > total_locations: # Sikkerhetsmekanisme
            print("\nKunne ikke besøke alle lokasjoner selv med én bil per lokasjon.")
            break

    print("=== DETALJER FOR ENDELIG LØSNING ===\n")
    for i, info in enumerate(routes_info):
        status = "OK" if info['return_time'] <= 480 else "FOR SENT!"
        print(f"Bil {i+1}: {' -> '.join(map(str, info['route']))}")
        print(f"  Ankomst depot: {info['return_time']:.1f} min ({status})")
        print(f"  Last: {info['load']} tonn")
        print("-" * 20)
