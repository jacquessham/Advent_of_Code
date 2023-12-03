with open('day2_data.txt','r') as f:
	lines = f.readlines()


## Part 1
rule = {'red':12, 'green':13, 'blue':14}
lines = [line.strip() for line in lines]

ans = 0

for line in lines:
	line_temp = line.split(':')
	num_game = line_temp[0].split(' ')[-1]
	games = line_temp[1].split(';')

	# To evaluate the game is possible, if not, turn to false
	game_possible = True

	# Each line has multiple games, separate by ;
	for game in games:
		elems = game.split(',')
		curr_game = {}
		for elem in elems:
			curr_elem_strs = elem.strip().split(' ')
			# Compare curr elem num with the rule dictionary
			if int(curr_elem_strs[0]) > rule[curr_elem_strs[1]]:
				# If any of the colour cube excess, break right away
				game_possible = False
				break
	# If the elem loop ever break, move on to the next loop
	if not game_possible:
		continue
	# Else, incrementally add game id
	else:
		ans += int(num_game)
print(ans)


## Part 2
lines = [line.strip() for line in lines]

ans = 0

for line in lines:
	line_temp = line.split(':')
	num_game = line_temp[0].split(' ')[-1]
	games = line_temp[1].split(';')

	curr_game = {'red':0, 'green':0, 'blue':0}

	# Each line has multiple games, separate by ;
	for game in games:
		elems = game.split(',')
		
		for elem in elems:
			curr_elem_strs = elem.strip().split(' ')
			# Replace colour-number pairs if number is greater
			if int(curr_elem_strs[0]) > curr_game[curr_elem_strs[1]]:
				curr_game[curr_elem_strs[1]] = int(curr_elem_strs[0])
	
	# Multiple curr_game
	curr_prod = 1
	for k in curr_game:
		curr_prod *= curr_game[k]

	# Incrementally add to answer
	ans += curr_prod
				
print(ans)

