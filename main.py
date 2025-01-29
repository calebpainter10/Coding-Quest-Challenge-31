import pandas as pd
import math

# Import the dataframe with pandas
data_path = "data.csv"
df = pd.read_csv(data_path, sep=";")

# Quick access columns
systems = df["System"]
x_values = df["X"]
y_values = df["Y"]
z_values = df["Z"]

# Distance calculation function
def calculate_distance(One_Coordinates: tuple, Two_Coordinates: tuple):
    # Split received tuples (x, y, z) into individual variables
    (x1, y1, z1), (x2, y2, z2) = One_Coordinates, Two_Coordinates

    # Calculate distance
    distance = math.sqrt(
        (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    )

    return round(distance, 3)

# Brute force nested loop approach
minimum_distance = []

# Iterate through first reference system
for i in range(len(systems)):
    # Compare reference system i to every other system
    # Prevent comparing the same systems
    for j in range(i + 1, len(systems)):
        i_coords = (x_values[i], y_values[i], z_values[i])
        j_coords = (x_values[j], y_values[j], z_values[j])

        i_system_name = systems[i]
        j_system_name = systems[j]

        # Add distance to dictionary and give live user feedback
        distance = calculate_distance(i_coords, j_coords)
        print(f"{i_system_name} --> {j_system_name}: {distance} lightyears")

        if not minimum_distance or distance < minimum_distance[1]:
            minimum_distance = [f"{i_system_name} --> {j_system_name}", distance]


# Print results 
print("\n---------- Results ----------\n")
print(f"Minimum distance: {minimum_distance[0]} with a distance of {minimum_distance[1]} lightyears.")

