import matplotlib.pyplot as pyplot



def extract_data_from_block(block):
    n = int(block[0])
    instructions = -1

    for line in block:
        if "instructions" in line:
            instructions = int(line[0:24])

    print(instructions)

file = open("inner_product.txt")

BLOCK_LEN = 25
lines = file.readlines()
blocks = []
for i in range(len(lines)):
    if "###" in lines[i]:
        blocks.append(lines[i+1:i+BLOCK_LEN])


for block in blocks:
    extract_data_from_block(block)

