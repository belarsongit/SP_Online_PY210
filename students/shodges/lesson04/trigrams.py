#!/usr/bin/env python3

import random
from pathlib import Path
from sys import argv

def build_trigrams(words):
    trigrams = {}
    for k, w in enumerate(words):
        if k + 2 < len(words):
            if not (w, words[k+1]) in trigrams.keys():
                trigrams[(w, words[k+1])] = []
            trigrams[(w, words[k+1])].append(words[k+2])
    return trigrams

def gutenberg_clean(guten_text):
    guten_text = guten_text.split('*** START OF THIS PROJECT GUTENBERG EBOOK') # Get rid of the first part of the header
    guten_text = guten_text[1][(guten_text[1].find('***')+3):] # Prior to the next '***' there may be arbitrary text
    guten_text = guten_text.split('*** END OF THIS PROJECT GUTENBERG EBOOK') # Cut out the footer and T's & C's
    return guten_text[0]

def add_next_word(trigrams, wip):
    next = trigrams[tuple(wip.split()[-2:])]
    if next[0] == '"':
        in_quote = True
    return ' '.join((wip, random.choice(next)))

if __name__ == '__main__':
    if not len(argv) == 2:
        print("Syntax: {} [filename]".format(argv[0]))
        quit()
    textfile = Path(argv[1])
    try:
        with textfile.open() as fileio:
            words = gutenberg_clean(fileio.read()).split()
    except FileNotFoundError:
        print("Unable to read {}".format(argv[1]))
        quit()
    trigrams = build_trigrams(words)

    literature = "It is"
    in_quote = False # sentinel value to help us finish a quote

    for i in range(0,210):
        try:
            literature = add_next_word(trigrams, literature)
        except KeyError:
            literature += '.'
            break
        else:
            if in_quote == True:
                while True:
    print(literature)
