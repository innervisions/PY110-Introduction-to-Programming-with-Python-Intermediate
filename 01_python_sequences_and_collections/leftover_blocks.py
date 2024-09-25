# Input - Number of available blocks (Integer)
# Output - Number of leftover blocks (Integer)

# - Explicit Rules:
# - The building blocks are cubes.
# - The structure is built in layers.
# - The top layer is a single block.
# - A block in an upper layer must be supported by four blocks in a lower layer.
# - A block in a lower layer can support more than one block in an upper layer.
# - You cannot leave gaps between blocks.

# Implicit
# - To produce the tallest structure we want the minimum number of blocks in each layer
# - The minimum number of blocks to support the layer above is the layer^2

# Data Structure - Integers?

# Algorithm
# - Iterate over layers beginning with top (layer 1)
# - Calculate number of blocks required to populate layer
# - If there are enough blocks to populate, subtrack blocks in layer from remaining blocks.
# - Otherwise end iteration and return remaining blocks.

def calculate_leftover_blocks(total_blocks):
    layer = 1
    layer_blocks = layer**2
    while total_blocks >= layer_blocks:
        total_blocks -= layer_blocks
        layer += 1
        layer_blocks = layer**2
    return total_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0)  # True
