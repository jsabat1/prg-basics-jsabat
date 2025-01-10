# Define the anonymous function to convert m/s to km/h
ms_to_kmh = lambda ms: ms * 3.6

# Sample speeds in m/s
speeds_ms = [10, 35]

# Convert and print the results
for speed in speeds_ms:
    print(f"{speed} m/s = {ms_to_kmh(speed)} km/h")
