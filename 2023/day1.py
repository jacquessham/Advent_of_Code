with open('day1_data.txt','r') as f:
	lines = f.readlines()


## Part 1
lines = [line.strip() for line in lines]

# answer to be incrementally added each loop
ans = 0
# Save all digit in string
num_chs = [str(num) for num in range(0,10)]

for line in lines:
	# Split each character and check if it is a digit
	chs = list(line.strip())
	# If so, add to a temp list
	curr_nums = [ch for ch in chs if ch in num_chs]
	# Take the first elem and last elem, or take first elem 2 times
	if len(curr_nums) > 1:
		curr_nums = curr_nums[0] + curr_nums[-1]
	else:
		curr_nums = curr_nums[0] + curr_nums[0]
	# Incrementally add the nums
	ans += int(curr_nums)

print(ans)

## Part 2

# Spell the strings
num_strings = [
	'one','two','three','four','five',
	'six','seven','eight','nine','ten'
	]

# str2num mapping
str2num = {
	'one':1, 'two':2, 'three':3, 'four':4,'five':5,
	'six':6,'seven':7,'eight':8,'nine':9,'ten':10
}

# answer to be incrementally added each loop
ans = 0
for line in lines:
	curr_nums = []
	i = 0

	# Check the substring whether match with the num_strings
	for i in range(len(line)):
		# If is a digit, take it
		if line[i] in num_chs:
			curr_nums.append(line[i])
			continue
		if i+3 < len(line)+ 1:
			if line[i:i+3] in num_strings:
				curr_nums.append(line[i:i+3])
				continue
		if i+4 < len(line) + 1:
			if line[i:i+4] in num_strings:
				curr_nums.append(line[i:i+4])
				continue
		if i+5 < len(line) + 1:
			if line[i:i+5] in num_strings:
				print('I got this')
				curr_nums.append(line[i:i+5])
				continue
	# Take the first elem and last elem, or take first elem 2 times	
	if len(curr_nums) > 1:
		first_digit = curr_nums[0]
		second_digit = curr_nums[-1]
	else:
		first_digit = curr_nums[0]
		second_digit = curr_nums[0]

	# Convert string to digit
	if len(first_digit) > 1:
		first_digit = str(str2num[first_digit])
	if len(second_digit) > 1:
		second_digit = str(str2num[second_digit])
	curr_num = int(first_digit + second_digit)

	ans += curr_num
# Print answer
print(ans)



