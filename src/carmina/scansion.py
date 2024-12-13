"""
This module contains functions for syllabification and metrical
analysis of Latin text.

It includes:
- A syllabification function that splits a Latin line into syllables.
- A function to check whether a syllable is long or short based on
  Latin metrical rules.
"""

# Define Latin vowels and diphthongs
vowels = "aeiou"
diphthongs = ["ae", "au", "ei", "eu", "oe", "ui", "oi"]
consonants = "bcdfghklmnpqrstx"
consonant_clusters = [
        "br", "bl", "cr", "cl", "dr", "fl", "fr", "gl", "gr", "qu",
        "pl", "pr", "sc", "sl", "sm", "sn", "sp", "st", "tr"
    ]


def syllabify_word(text):
    """
    Syllabifies a single Latin word.

    Args:
        text (str): The Latin word to syllabify.

    Returns:
        list: A list of syllables formed from the word.
    """
    syllables = []  # List to store syllables
    current_syllable = ""  # Temporary syllable container

    i = 0
    while i < len(text):
        # If the current character is a vowel, check for diphthongs
        # or single vowels
        if text[i] in vowels:
            if i + 1 < len(text) and text[i:i+2] in diphthongs:
                # If it's a diphthong, treat both vowels as one syllable
                current_syllable += text[i:i+2]
                i += 2  # Skip the next character as it's part of the diphthong
            else:
                # Otherwise, just add the vowel to the syllable
                current_syllable += text[i]
                i += 1
        else:
            # If it's a consonant, add it to the syllable
            current_syllable += text[i]
            i += 1

        # If the syllable is complete (contains at least one vowel),
        # add it to the list
        if len(current_syllable) > 1 and +\
                any(c in vowels for c in current_syllable):
            syllables.append(current_syllable)
            current_syllable = ""  # Reset the syllable container

    # If anything remains in current_syllable after the loop, append it
    if current_syllable:
        syllables.append(current_syllable)

    return syllables


def syllabify_line(line):
    """
    Syllabifies a line of Latin text by splitting it into words
    and syllabifying each word.

    Args:
        line (str): The Latin line of text to syllabify.

    Returns:
        syllabified_line (list[str]): A list containing
                the syllables of the line
    """
    words = line.split()  # Split the line into words
    syllabified_line = []

    for text in words:
        # Syllabify each word and join syllables with dashes
        syllabified_line.extend(syllabify_word(text.lower()))

    return syllabified_line


def print_syllabified_line(syllabified_line):
    """
    Prints a syllabified line to the console

    Inputs:
        syllabified_line (str): The syllabified line

    Outputs:
        (str): The syllabified line, with syllables
               separated by a dash (-) and words by
               a pipe (|)
    """
    return " | ".join(syllabified_line)


def is_long(syllable):
    """
    Determines whether a given syllable is long according to Latin metrical
    rules.

    A syllable is considered long if:
    1. It contains a diphthong.
    2. It ends with a long vowel (assumed unless vowel is short by position)
    3. It is followed by two or more consonants.

    Inputs:
        syllable (str): A single syllable to evaluate.

    Outputs:
        bool: True if the syllable is long, False if the syllable is short.
    """
    # Check if the syllable starts with a diphthong
    if len(syllable) > 1 and syllable[:2] in diphthongs:
        return True

    # Check if the syllable ends with a long vowel
    # (i.e., it's a single vowel and assumed long in position)
    if syllable[-1] in vowels and len(syllable) == 1:
        return False  # By default, assume short

    # Check for long syllables by position (vowel followed by consonants)
    for i in range(len(syllable)):
        if syllable[i] in vowels:
            remainder = syllable[i + 1:]
            # If there are two or more consonants after a vowel,
            #   the syllable is long
            if len(remainder) > 1 and all(c in consonants for c in remainder):
                return True

    # If no conditions for a long syllable are met,
    # return False (the syllable is short)
    return False


def hexameter_line(line):
    """
    Single-line hexameter parsing

    Assuming input is:
    "arma virumque cano troiae qui primus ab oris"

    The output is:
    "-  u u  - u   u -  -   -  -   -  u   u  - - "
    "arma virumque cano troiae qui primus ab oris"

    Inputs:
        line (str): The line to be scanned in hexameter

    Outputs:
        scanned (tuple[str]): A tuple consisting of the
                scanned syllables and the original line
    """
    syllables = syllabify_line(line)
    syl_indices = {}
    syl_lengths = {}

    for syl in syllables:
        syl_indices[line.find(syl)] = syl
        syl_lengths[syl] = is_long(syl)

    # Building up the string of - and u:
    scans = ""
    for i in range(len(line)):
        if i in syl_indices:
            if syl_lengths[syl_indices[i]]:
                scans += "-"
            else:
                scans += "u"
        else:
            scans += " "

    return scans, line


def hexameter_text(lines):
    """
    Multi-line hexameter parsing
    """
    return [hexameter_line(line) for line in lines]
