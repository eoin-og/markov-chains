import random

def build_suffix_table(full_text):
    words = full_text.split(' ')
    suffix_table = dict()
    for i in range(len(words)):
        step = random.randint(6,10)
        if words[i] in suffix_table:
            step
            suffix_table[words[i]].append(' '.join(words[i-step:i]))
        else:
            suffix_table[words[i]] = [' '.join(words[i-step:i])]

    return suffix_table

def generate_text(suffix_table, num_lines):

    capitalized_words = [w for w in suffix_table.keys() if w[0].isupper()]
    text = ''
    for _ in range(num_lines):        
        start_word = random.choice(capitalized_words)
        next_words = random.choice([suffix for suffix in suffix_table[start_word]])
        next_words.lower()
        text += str(start_word + " " + next_words +"\n")
    return text

verse_text = ' '.join([w for w in open('fob_verses.txt').read().split()])
chorus_text = ' '.join([w for w in open('fob_choruses.txt').read().split()])

verse_suffix = build_suffix_table(verse_text)
chorus_suffix = build_suffix_table(chorus_text)

first_verse = generate_text(verse_suffix, 8)
second_verse = generate_text(verse_suffix, 8)
bridge = generate_text(verse_suffix, 4)
chorus = generate_text(chorus_suffix, 4)

print("Verse 1: \n" +first_verse + "\n")
print("Chorus: \n" +chorus + "\n")
print("Verse 2: \n" +second_verse + "\n")
print("Chorus: \n" +chorus + "\n")
print("Bridge: \n" +bridge + "\n")
print("Chorus: \n" +chorus + "\n")
print(chorus + "\n")
