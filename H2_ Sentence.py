# 07/08/25
# Homework 2: Sentence Generator
# Program By: Ricardo Duran
# File Name: H2_Sentence.py
# Function:  This program will generate a random sentence

import random

#Tuples selection
article = ("The", "A", "Each")
noun = ("Android", "Spaceship", "Planet", "Laser", "Commander")
verb = ("Scanned", "Repaired", "Launched", "Detected", "Commanded")
preposition = ("Across", "Through", "Around", "Toward", "Inside")


# Generating a Noun Phrase with a random combination of Article + Noun
noun_phrase = random.choice(article) + " " + random.choice(noun)

#Created 2 more Noun phrase due to many duplicate Nouns being displayed in the same sentence
noun_phrase2 = random.choice(article) + " " + random.choice(noun)

noun_phrase3 = random.choice(article) + " " + random.choice(noun)

# Generating a Preposition Phrase with a random combination of Preposition + Noun Phrase
preposition_phrase = random.choice(preposition) + " " + noun_phrase2

# Generating a Verb Phrase with a random combination of Verb + Noun Phrase + Preposition Phase 
verb_phrase = random.choice(verb) + " " + noun_phrase3 + " " + preposition_phrase

# Generating a sentence with a random combination of Noun Phrase + Verb Phrase
sentence_generator = noun_phrase + " " + verb_phrase 

print (sentence_generator)

test