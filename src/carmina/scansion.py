"""
This module contains functions for syllabification and metrical analysis of Latin text.

It includes:
- A syllabification function that splits a Latin line into syllables.
- A function to check whether a syllable is long or short based on Latin metrical rules.
"""

import re

# Define Latin vowels and diphthongs
vowels = "aeiou"
diphthongs = ['ae', 'au', 'ei', 'eu', 'oe', 'ui', 'oi']

def syllabify_word(text):
    """
    Syllabifies a single Latin word.
    
    A word is syllabified by processing each character and checking for vowels, consonants, and diphthongs. 
    The function attempts to form syllables by breaking at consonants between vowels, following Latin syllabification rules.
    
    Args:
        text (str): The Latin word to syllabify.
        
    Returns:
        list: A list of syllables formed from the word.
    """
    syllables = []  # List to store syllables
    current_syllable = ""  # Temporary syllable container
    
    i = 0
    while i < len(text):
        # If the current character is a vowel, check for diphthongs or single vowels
        if text[i] in vowels:
            if i + 1 < len(text) and text[i:i+2] in diphthongs:
                # If it's a diphthong, treat both vowels as one syllable
                current_syllable += text[i:i+2]
                i += 2  # Skip the next character as it is part of the diphthong
            else:
                # Otherwise, just add the vowel to the syllable
                current_syllable += text[i]
                i += 1
        else:
            # If it's a consonant, add it to the syllable
            current_syllable += text[i]
            i += 1

        # If the syllable is complete (contains at least one vowel), add it to the list
        if len(current_syllable) > 1 and any(c in vowels for c in current_syllable):
            syllables.append(current_syllable)
            current_syllable = ""  # Reset the syllable container

    # If anything remains in current_syllable after the loop, append it
    if current_syllable:
        syllables.append(current_syllable)

    return syllables


def syllabify_line(line):
    """
    Syllabifies a line of Latin text by splitting it into words and syllabifying each word.
    
    This function handles the entire line of text, calling `syllabify_word` for each word, 
    and then joins the syllables with dashes and separates the words with pipes.

    Args:
        line (str): The Latin line of text to syllabify.
        
    Returns:
        str: A string containing syllabified words, where syllables are separated by dashes 
             and words are separated by pipes.
    """
    words = line.split()  # Split the line into words
    syllabified_line = []

    for text in words:
        # Syllabify each word and join syllables with dashes
        syllabified_line.append("-".join(syllabify_word(text.lower())))

    # Join the words with pipes and return the result
    return " | ".join(syllabified_line)


def is_long(syllable):
    """
    Determines whether a given syllable is long according to Latin metrical rules.
    
    A syllable is considered long if:
    1. It contains a diphthong.
    2. It ends with a long vowel (assumed unless the vowel is short by position).
    3. It is followed by two or more consonants.
    
    Args:
        syllable (str): A single syllable to evaluate.
        
    Returns:
        bool: True if the syllable is long, False if the syllable is short.
    """
    vowels = "aeiouy"  # Including 'y' as it sometimes behaves as a vowel in Latin
    diphthongs = ['ae', 'au', 'ei', 'eu', 'oe', 'ui', 'oi']
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    # Check if the syllable starts with a diphthong
    if len(syllable) > 1 and syllable[:2] in diphthongs:
        return True
    
    # Check if the syllable ends with a long vowel (i.e., it's a single vowel and assumed long in position)
    if syllable[-1] in vowels and len(syllable) == 1:
        return False  # By default, assume short unless otherwise indicated by specific rules
    
    # Check for long syllables by position (vowel followed by consonants)
    for i in range(len(syllable)):
        if syllable[i] in vowels:
            remainder = syllable[i + 1:]
            # If there are two or more consonants after a vowel, the syllable is long
            if len(remainder) > 1 and all(c in consonants for c in remainder):
                return True

    # If no conditions for a long syllable are met, return False (the syllable is short)
    return False


# Example usage:
line = "Arma virumque cano Troiae qui primus ab oris"
syllabified = syllabify_line(line)
print("Syllabified line:", syllabified)

# Now split the syllabified line and check the longness of each syllable
syllables = syllabified.replace(" | ", "-").split("-")
long_status = [(syl, is_long(syl)) for syl in syllables]
print("Syllable lengths:", long_status)









def hexameter_line(line):
    """
    Single-line hexameter parsing

    Initial ideas: 
        1. Syllabify the line
        2. Exclude last two syllables and determine whether each
           syllable is long or not
        3. If long, assign "-"
        4. If short, assign "u"
        4.5 Figure out how we want to represent the final scansion
            to the user.
        5. -uu -- -- -uu -uu -- || DSSDDS
    
    Assuming line is: 
    Arma virumque cano, Troiae qui primus ab oris

    End goal is:
    "-  u u  - u   u -   -   -  -   -  u   u  - - "
    "Arma virumque cano, Troiae qui primus ab oris" <-- not this (for now)
    "arma virumque cano troiae qui primus ab oris" <-- We are doing this
    [0, 3, 5, 8, 11, 13] <-- assuming these are the syllable indices,
                             assign the -uu-- characters at each next
                             index
    """
    # TODO @Suh Young
    pass

def hexameter_text(lines):
    """
    Multi-line hexameter parsing
    """
    # TODO @Suh Young
    pass