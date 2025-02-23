import math

def p_of_q_overflow(reqs_count, queue_overflow_threshold, machine_count):
	sum1 = 0
	for i in range(queue_overflow_threshold, reqs_count):
		sum1 += f(reqs_count, i, machine_count, 1)
	print(str(sum1))
	return sum1 / math.pow(machine_count, reqs_count)


memo = {}

def f(reqs_count, batch_size, machine_count, depth):
	seen = (reqs_count, batch_size, machine_count, depth)
	if seen in memo:
		return memo[seen]
	##print("f(" + str(reqs_count) + "," + str(batch_size) + "," + str(machine_count) + "," + str(depth) + ")")
	factor = machine_count * math.comb(reqs_count, batch_size) / depth
	if reqs_count == batch_size:
		##print ("return " + str(factor))
		memo[seen] = factor
		return factor
	start = math.ceil((reqs_count - batch_size)/(machine_count-1))
	sum = 0
	new_batch_size = batch_size if reqs_count - batch_size > batch_size else reqs_count - batch_size
	for i in range(start, new_batch_size + 1):
		new_depth = 1 if i < batch_size else depth + 1
		sum += f(reqs_count - batch_size, i, machine_count-1, new_depth)
	##print ("return " + str(factor * sum))
	out1 = factor * sum
	memo[seen] = out1
	return out1
	
def _count(range_end_power, goal):
	_count = 0
	for i in range(0, int(math.pow(10, range_end_power))):
		stri = str(i)
		stri = stri.rjust(range_end_power, '0')
		x = {}
		max_count = 1
		for n in range(0, len(stri)):
			if stri[n] not in x:
				x[stri[n]] = 1
			else:
				x[stri[n]] = x[stri[n]] + 1
				max_count = x[stri[n]] if x[stri[n]] > max_count else max_count
		if max_count == goal:
			_count += 1
	return _count

f(15, 3, 10)
