# Load Puzzle
with open('day4_data.txt','r') as f:
	lines = f.readlines()

lines = [line.strip() for line in lines]

## Part 1
ans = 0

for line in lines:
	curr_line = line.replace(':','|').split('|')

	# Separate winning numbers and numbers we have
	nums_winning = curr_line[1].strip().split(' ')
	# Single digit number will produce a whitespace, remove it here
	nums_winning = [num for num in nums_winning if num != '']
	nums_owning = curr_line[2].strip().split(' ')
	nums_owning = [num for num in nums_owning if num != '']

	# Compare two sets and find the intersection
	curr_result = set(nums_owning).intersection(set(nums_winning))

	# Incrementally add the winning scores
	if len(curr_result) == 1:
		ans += 1
	elif len(curr_result) > 1:
		ans += 2**(len(curr_result)-1)

print(ans)

## Part 2
results = [1 for _ in range(len(lines))]

for i, line in enumerate(lines):
	curr_line = line.replace(':','|').split('|')

	# Separate winning numbers and numbers we have
	nums_winning = curr_line[1].strip().split(' ')
	# Single digit number will produce a whitespace, remove it here
	nums_winning = [num for num in nums_winning if num != '']
	nums_owning = curr_line[2].strip().split(' ')
	nums_owning = [num for num in nums_owning if num != '']

	# Compare two sets and find the intersection
	curr_result = set(nums_owning).intersection(set(nums_winning))

	# Incrementally add copies to next cards
	copies = results[i]

	# Next cards means i+1 until sets of cards, ie, card 1 -> 2, 3, 4, 5
	for j in range(i+1, i+len(curr_result)+1):
		results[j] += copies

	print(results)

print(sum(results))





