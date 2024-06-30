#!/usr/bin/env python3
import random

noun_list = ['cherry', 'abomination', 'wolf', 'field', 'racecar', 'propagator', 'moron', 'quark', 'language']

adjective_list = ['green', 'monstrous', 'excessive', 'delightful', 'round', 'complete', 'sharp', 'dubious']

verb_list = ['slapped', 'ran', 'wrote', 'slid', 'killed', 'painted', 'restricted', 'subdued', 'smelled', 'scratched']

noun_number_1 = random.randint(0, len(noun_list) - 1)
noun_number_2 = random.randint(0, len(noun_list) - 1)
adjective_number_1 = random.randint(0, len(adjective_list) - 1)
adjective_number_2 = random.randint(0, len(adjective_list) - 1)
verb_number = random.randint(0, len(verb_list) - 1)

noun_1 = noun_list[noun_number_1]
noun_2 = noun_list[noun_number_2]
adjective_1 = adjective_list[adjective_number_1]
adjective_2 = adjective_list[adjective_number_2]
verb = verb_list[verb_number]

print('The ' + adjective_1 + ' ' + noun_1 + ' ' + verb + ' the ' + adjective_2 + ' ' + noun_2 + '.')


