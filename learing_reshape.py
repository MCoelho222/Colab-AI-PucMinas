import numpy as np

# Create a flat array with 96 elements
flat_array = np.arange(96)
print("Flat array:")
print(flat_array)

# Reshape the flat array into a 4D array
reshaped_array = flat_array.reshape(2, 3, 4, 4)
print("\nReshaped array (2 images, 3 channels, 4x4 resolution):")
print(reshaped_array)

# Transpose the reshaped array to the desired shape
transposed_array = reshaped_array.transpose(0, 2, 3, 1)
print("\nTransposed array (2 images, 4x4 resolution, 3 channels):")
print(transposed_array)
