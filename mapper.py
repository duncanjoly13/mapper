import osmnx as ox
import matplotlib.pyplot as plt

city = input("Enter city name: ")
color = input("Enter matplotlib color: ")
dimension = input("Enter width/height of square image (default 10): ")

try:
    dimension = int(dimension)
except ValueError:
    if dimension == '':
        print("\nNo size specified, defaulting to 10x10")
    else:
        print("\nCould not interpret your input, defaulting to 10x10")
    dimension = 10

filename = f"{city.replace(' ', '_')}_{color}_{dimension}x{dimension}.png"
print(f"\nGenerating plot of {city} in {color} with size {dimension}x{dimension} and saving to \x1B[3m{filename}\x1B[0m" +
      "\nThis may take some time...")

admin = ox.geocode_to_gdf(city)
admin_poly = admin.geometry.values[0]

G = ox.graph_from_polygon(admin_poly)
nodes, edges = ox.graph_to_gdfs(G)

plt.style.use('dark_background')

f, ax = plt.subplots(figsize=(dimension, dimension))
edges.plot(ax=ax, edgecolor=color, linewidth=0.3)
ax.axis('off')
plt.savefig(f'plots/{filename}')

print("\nDone!")
