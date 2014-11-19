#!/usr/bin/env python3

import math
import random


def continued_fractions( real, max_elements ):
	''' 
		takes a floating point number and returns it's continued fraction
		up to max_elements in the returned list, less than max_elements if a period is detected
	'''
	rest = real
	cf = []
	rests = {}
	is_periodic = False
	while True:
		numerator = math.floor(rest)
		rest -= numerator
		if numerator not in rests.keys():
			rests[numerator] = set([rest])
		else:
			found_same_rest = False
			for r in rests[numerator]:
				if math.fabs( (r - rest)/rest ) < 0.01 :
					# found the period
					found_same_rest = True
					is_periodic = True
					print('found repeated numerator: '+str(numerator))
					break
			if found_same_rest:
				break
		rests[numerator].add(rest)
		cf += [numerator]
		rest = 1/rest
		if len(cf) == max_elements:
			break
	return (cf, is_periodic, rests)

def expand_cf( cf, periods ):
	''' given a continued fractions list, return the associated float '''
	if not cf:
		return None
	result = 0.0
	previous_inverse = 0.0
	if not periods:
		periods = 1
	for i in range(periods):
		for a in reversed(cf[1:]):
			previous_inverse = 1/(a+previous_inverse)
	previous_inverse = 1/(cf[0]+previous_inverse)
	return 1/previous_inverse
		

def prng(max_iter):
	count = 0
	while count < max_iter:
		yield random.randint(0, 256)
		count += 1


cf = continued_fractions(math.sqrt(2), 20)
print('sqrt(2)=' + str(cf[0]) )
print( expand_cf(cf[0], 10))

#random_f = 1e10/int.from_bytes(bytearray(prng(6)), 'big')
#print(random_f)
#random_f_cf =  continued_fractions(random_f, 20)[0]
#print('CF => ' + str(random_f_cf[0]))
#print('expand(CF) =>' + str(expand_cf(random_f_cf[0])))


