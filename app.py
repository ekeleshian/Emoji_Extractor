# App entry

import hug
import emoji
import pandas as pd
from pdb import set_trace


df = pd.read_csv('emoji_dict.csv')

@hug.get('/emojitype/{input}')
def get_parser(input: str):
	"""
	Returns a dictionary of found emojis (if any) with their corresponding labels, 
	given a string as input. Returns an empty dictionary if no emoji is found in string.
	"""
	cats = ['person', 'thing', 'place', 'time', 'activity', 'mood']
	def emoji_to_types(string):
		"""
		Tool to extract emojis from string of text

		Input:  string with some (if any) emojis
		Ouput:  dictionary containing discovered emojies and their corresponding label.
		"""
		emos = emoji.emoji_lis(string)

		result = dict()
		for idx, emo in enumerate(emos):
			descr = emoji.UNICODE_EMOJI_ALIAS[emo['emoji']]
			cat = df[df.EMOJI_ALIAS_UNICODE==descr].VEC_TO_CAT.item()
			result[cat] = result.get(cat, []) + [emo['emoji']]
		return result

	emoji_types = emoji_to_types(input)

	return emoji_types


