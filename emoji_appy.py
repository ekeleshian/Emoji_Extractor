"""A simple API to enable adding two numbers together"""

import hug
import emoji
from copy import deepcopy
from pdb import set_trace
import pandas as pd
import random
import numpy as np
from pprint import pprint as pp


df = pd.read_csv('emoji_dict.csv')
failed_emojis =[]
files = ['person.txt', 'thing.txt', 'place.txt', 'time.txt', 'activity.txt', 'mood.txt']


def extract_emojis(string):
	cats = [ file[:-4] for file in files ]
	result = dict()
	for cat in cats:
		result[cat] = []

	try:
		descr = emoji.UNICODE_EMOJI_ALIAS[string]
		cat = df[df.EMOJI_ALIAS_UNICODE==descr].VEC_TO_CAT.item()
		result[cat] += [string]
	except:
		failed_emojis.append((string, idx))

	return result

test_results = []

for file in files:
	with open(file, 'r') as fp:
		distribution= dict()
		for line in fp:
			disc_emojis = emoji.emoji_lis(line)
			# set_trace()
			res = extract_emojis(line.strip('\n'))
			for key in res:
				distribution[key] = distribution.get(key, 0) + 1
		test_results.append((file, distribution))


NEEDED_THRESHOLD = .6

for file, res in test_results:
	total = sum(res.values())
	cat = file[:-4]
	perc = res[cat]/total
	print(cat, '\n', NEEDED_THRESHOLD <= perc, '\n', str(perc)+'%')

[pp(a) for a, b in test_results]
[pp(b) for a, b in test_results]
# print(len(failed_emojis))
# set_trace()

# print(failed_emojis)
# print(distribution)

# print(NEEDED_THRESHOLD == calculute_dist(results, 'person'))



# print(results)

# emojis=[]
# for i in range(100):
# 	num = random.randint(0, len(df))
# 	emojis.append(df.iloc[num].emoji)

# emojis = ''.join(emojis)
