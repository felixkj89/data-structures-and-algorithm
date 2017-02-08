from random import randint

def swap_input_list(input_list):
	'''
	Swap the content of input_list randmonly.
	'''
	i = 0
	for val in input_list:
		j = randint(i,len(input_list)-1)
		temp = input_list[i]
		input_list[i] = input_list[j]
		input_list[j] = temp
		i += 1
	return input_list

def random_pick(total_pick, input_list):
	'''
	Randomly pick members of input_list for total_pick.
	'''
	num_pick = 0
	picked = []
	while (num_pick < total_pick):
		i = randint(0,len(input_list)-1)
		picked.append(input_list.pop(i))
		num_pick += 1
	return picked
		