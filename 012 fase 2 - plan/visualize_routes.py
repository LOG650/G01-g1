import json
import matplotlib.pyplot as plt

def visualize_routes(data, routes, title, filename):
    plt.figure(figsize=(10, 8))
    
    # Plot depot
    depot = data['depot']
    plt.scatter(depot['x'], depot['y'], c='red', marker='s', s=100, label='Slakteri (Depot)')
    plt.text(depot['x']+1, depot['y']+1, 'Depot', fontsize=12, fontweight='bold')
    
    # Plot locations
    locations = {loc['id']: loc for loc in data['locations']}
    x_coords = [loc['x'] for loc in data['locations']]
    y_coords = [loc['y'] for loc in data['locations']]
    plt.scatter(x_coords, y_coords, c='blue', marker='o', s=50, label='Oppdrettslokaliteter')
    
    for loc_id, loc in locations.items():
        plt.text(loc['x']+1, loc['y']+1, f'L{loc_id}', fontsize=10)
    
    # Plot routes
    colors = ['green', 'orange', 'purple', 'brown', 'pink', 'cyan', 'gray']
    for i, route in enumerate(routes):
        route_x = [depot['x'] if node == 0 else locations[node]['x'] for node in route]
        route_y = [depot['y'] if node == 0 else locations[node]['y'] for node in route]
        plt.plot(route_x, route_y, color=colors[i % len(colors)], label=f'Rute {i+1}', linewidth=2, alpha=0.7)
        
        # Add arrows to show direction
        for j in range(len(route_x) - 1):
            plt.annotate('', xy=(route_x[j+1], route_y[j+1]), xytext=(route_x[j], route_y[j]),
                         arrowprops=dict(arrowstyle='->', color=colors[i % len(colors)], lw=1.5))

    plt.title(title)
    plt.xlabel('X-koordinat')
    plt.ylabel('Y-koordinat')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    with open(r'004 data\data.json', 'r') as f:
        data = json.load(f)
    
    # Greedy routes from previous execution
    greedy_routes = [[0, 6, 7, 4, 0], [0, 5, 2, 0], [0, 1, 3, 0]]
    
    visualize_routes(data, greedy_routes, 'Ruteplanlegging: Heuristisk løsning (Greedy)', r'012 fase 2 - plan\rute_visualisering.png')
    
    # Baseline routes
    baseline_routes = [[0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0]]
    visualize_routes(data, baseline_routes, 'Ruteplanlegging: Referanseløsning (Baseline)', r'012 fase 2 - plan\baseline_visualisering.png')
    
    print("Visualiseringer lagret i 012 fase 2 - plan/")
