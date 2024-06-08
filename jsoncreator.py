import json

def generate_blocks(n, m, space):
    blocks = []
    for i in range(1, (n // (m + space)) + 1):
        for j in range(1, (n // (m + space)) + 1):
            # Calculate block position
            x = (m + space) * (j - 1) + 1
            y = (m + space) * (i - 1) + 1
            # Check if placing MxM block is possible at (x, y)
            if x + m - 1 <= n and y + m - 1 <= n:
                block = {
                    "x": x,
                    "y": y,
                    "width": m,
                    "height": m,
                    "imageUrl": f"./images/{i}-{j}.jpg",
                    "linkUrl": f"{22}",
                    "title": ""
                }
                blocks.append(block)
    return blocks

def save_blocks_to_json(blocks, filename):
    with open(filename, 'w') as json_file:
        json.dump(blocks, json_file, indent=4)

# Example usage
n = 100  # Size of the board
m = 2    # Size of each block
space = 0  # Space between blocks
blocks = generate_blocks(n, m, space)
save_blocks_to_json(blocks, 'blocks.json')
