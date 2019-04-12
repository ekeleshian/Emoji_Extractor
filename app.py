# App entry

import hug
import emoji
import pandas as pd
from pdb import set_trace


df = pd.read_csv('emoji_dict.csv')

@hug.get('/emojitype/{input}')
def get_parser(input: str):
	cats = ['person', 'thing', 'place', 'time', 'activity', 'mood']
	def extract_emojis(string):
		"""
		Tool to extract emojis from string of text

		Input:  string with some (if any) emojis
		Ouput:  <list> list of the emojis. If no emojis found, returns empty list.
		"""
		emos = emoji.emoji_lis(string)
		return emos

	emojis = extract_emojis(input)
	result = dict()
	for idx, emo in enumerate(emojis):
		descr = emoji.UNICODE_EMOJI_ALIAS[emo['emoji']]
		cat = df[df.EMOJI_ALIAS_UNICODE==descr].VEC_TO_CAT.item()
		result[cat] = result.get(cat, []) + [emo['emoji']]

	return result


