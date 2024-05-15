import random
import json

f = open('lang.json')
data = json.load(f)

transitions = ['the', 'is', 'it', 'and', 'to']
punc = ['.', '.', '']
nouns = data['nouns']
verbs = data['verbs']
adverbs = data['adverbs']
adjectives = data['adjectives']

print(f'{random.choice(adjectives)} {random.choice(nouns)} {random.choice(transitions)} {random.choice(verbs)} {random.choice(adverbs)}{random.choice(punc)}')

for i in range(49):
    print(f'{random.choice(transitions)} {random.choice(adjectives)} {random.choice(nouns)} {random.choice(transitions)} {random.choice(verbs)} {random.choice(adverbs)}{random.choice(punc)}')
