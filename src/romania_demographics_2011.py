import geopandas as gdp
import matplotlib.pyplot as plt
import pandas as pd


pd.set_option('display.expand_frame_repr', False)
# Load the shape file.
map_path = "map/ro_judete_poligon.shp"
map_df = gdp.read_file(map_path)

# Set the variable to visualize.
variable = "pop2011"

# Set the range for the colorbar.
vmin, vmax = 150000, 2100000

# Create figure and axes for Matplotlib.
fig, ax = plt.subplots(1, figsize=(10, 6))

# Create map.
map_df.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')

# Add a title.
ax.set_title("Population in 2011", fontdict={'fontsize': '25', 'fontweight' : '3'})

# Add annotations.
ax.annotate('Source: Institutul National de Statistica',xy=(0.1, .08),  xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')

# Create a colorbar as legend.
sm = plt.cm.ScalarMappable(cmap='Blues',
                           norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)

# Remove the axis.
ax.axis("off")

# Show map.
plt.show()

# Save file
fig.savefig("romania_pop_2011.svg")


