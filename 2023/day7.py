from collections import Counter

with open('day7_data.txt','r') as f:
	lines = f.readlines()

lines = [line.strip() for line in lines]



## Helping functions
def strength(hand):
	cnt = Counter(hand)

	# Convert cnt to a list
	vals = [v for k,v in cnt.items()]
	vals_sorted = sorted(cnt.items(), key=lambda x: [-x[1], x[0]])
	## Five of a kind
	if 5 in vals:
		return (1,'Five of a kind')

	## Four of a kind
	elif 4 in vals:
		return (2,'Four of a kind')

	## Full House
	elif 3 in vals and 2 in vals:
		return (3,'Full House')

	## Three of a Kind
	elif 3 in vals:
		return (4,'Three of a kind')

	## Pairs
	elif 2 in vals:
		freq = Counter(vals)
		## Two Pair
		if 2 in [v for k,v in freq.items()]:
			return (5,'Two Pairs')
		## One Pair
		else:
			return (6,'One Pair')

	## High Card
	else:
		return (7,'High Card')


## To help sort string for part 1 rule
def replace_label(hand):
	# order: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
	return hand.replace('A','Z').replace('K','Y').replace('Q','X')\
		.replace('J','W').replace('T','V')

## Part 1
games = []
for line in lines:
	curr_hand = line.split(' ')

	# Each elem will have [strenght, sorting_label_hand, original_hand, bet]
	curr_hand = [strength(curr_hand[0]), replace_label(curr_hand[0]),
	 curr_hand[0], int(curr_hand[1])]
	games.append(curr_hand)

ans = 0

# Sort the games to get the mulitplier
games_sorted = sorted(games, key=lambda x: [-x[0][0], x[1]])
# Loop over to calculate the winnings
for i, elem in enumerate(games_sorted):
	print(elem)
	ans += (i+1)*elem[3]

print(ans)


## Part 2
def replace_part2label(hand):
	# order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J
	# But J becomes joker
	if hand == 'JJJJJ': return ('ZZZZZ','00000')

	cnt = Counter(hand)

	# Convert cnt to a list
	vals = [v for k,v in cnt.items()]
	vals_sorted = sorted(cnt.items(), key=lambda x: [-x[1], x[0]])
	card_mostfreq = vals_sorted[0][0]

	# In case J is the most freq
	if card_mostfreq == 'J':
		card_mostfreq = vals_sorted[1][0]

	# Replace joker cards first
	hand_label = hand.replace('J', card_mostfreq)
	# Replace all card label altogther
	hand_label = hand_label.replace('A','Z').replace('K','Y').replace('Q','X')\
		.replace('T','V')

	return (hand_label, hand)

games = []
for line in lines:
	curr_hand = line.split(' ')

	hand_label, hand = replace_part2label(curr_hand[0])
	


	card_strength = strength(hand_label)

	sorting_label_hand = replace_label(hand.replace('J','0'))

	# Each elem will have [strenght, sorting_label_hand, original_hand, bet]
	curr_hand = [card_strength, sorting_label_hand,
	 curr_hand[0], int(curr_hand[1])]
	games.append(curr_hand)

ans = 0

# Sort the games to get the mulitplier
games_sorted = sorted(games, key=lambda x: [-x[0][0], x[1]])
# Loop over to calculate the winnings
for i, elem in enumerate(games_sorted):
	print(elem)
	ans += (i+1)*elem[3]

print(ans)
