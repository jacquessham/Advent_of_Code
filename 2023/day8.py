import math


class Node():
	def __init__(self, node, left, right):
		self.node = node
		self.left = left
		self.right = right

	def __str__(self):
		if type(self.left) == str or type(self.right) == str:
			return f'({self.node})'
		return f'({self.node}, {self.left.node}, {self.right.node})'

with open('day8_data.txt','r') as f:
	lines = f.readlines()


# Setup
directions = list(lines[0].strip())
lines = [line.strip() for i, line in enumerate(lines) if i > 1]


node_dict = {}

for line in lines:
	curr_line = line.split(' = ')
	node_name = curr_line[0]
	left = curr_line[1].split(', ')[0][1:]
	right = curr_line[1].split(', ')[1][:-1]
	curr_node = Node(node_name, left, right)
	node_dict[node_name] = curr_node

# Part 1
## Part 1 Setup
root = None
for node in node_dict:
	if node == 'AAA':
		root = node_dict[node]

	node_dict[node].left = node_dict[node_dict[node].left]
	node_dict[node].right = node_dict[node_dict[node].right]


part1_node = root
i = 0
steps = 0

while part1_node.node != 'ZZZ':
	# print('------------------------------')
	# print(part1_node.node)
	# print(part1_node)
	# print(f"{i}, {directions[i]}")
	curr_dir = directions[i]
	if curr_dir == 'L':
		part1_node = part1_node.left
	else:
		part1_node = part1_node.right
	i += 1
	steps += 1
	if i >= len(directions):
		i = 0
print(steps)

# Part 2
## Part 2 Setup
roots = []
roots_steps = []

for node in node_dict:
	if node.endswith('A'):
		roots.append(node_dict[node])

# Loop over all node ends with A
for node in roots:
	curr_node = node
	steps = 0

	# Find the steps for every root node
	while not curr_node.node.endswith('Z'):
		curr_dir = directions[i]
		if curr_dir == 'L':
			curr_node = curr_node.left
		else:
			curr_node = curr_node.right
		i += 1
		steps += 1
		if i >= len(directions):
			i = 0
	roots_steps.append(steps)

# Print steps for each steps
for node, steps in zip(roots, roots_steps):
	print(f"{node}, {steps}")

# Then Calculate LCM, either use below link
# https://www.calculatorsoup.com/calculators/math/lcm.php

# Or use math.lcm(), but only available with Python 3.9
# math.lcm(*steps)