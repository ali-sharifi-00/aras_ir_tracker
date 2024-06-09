import pickle

# Path to your pickle file
pickle_file_path = 'ext_5000-0->5000-1.pckl'

# Open the pickle file in binary read mode
with open(pickle_file_path, 'rb') as file:
    data = pickle.load(file)

# Print the type of data loaded
print(data)

# Print the keys of the loaded data if it's a dictionary
if isinstance(data, dict):
    print("Data keys:", data.keys())

# # Inspect a portion of the data for further details
# # This part depends on what you expect the data to be
# # For example, if it's a dictionary with lists or nested dictionaries:
# for key in data:
#     print(f"Key: {key}, Value type: {type(data[key])}")
#     # Print the first few items of the value if it's a list
#     if isinstance(data[key], list):
#         print(f"First item under key {key}:", data[key][0])
#     elif isinstance(data[key], dict):
#         print(f"Sub-keys under key {key}:", data[key].keys())

# # If you want to examine more deeply, consider printing specific entries
# # or using additional logic to understand nested structures.
