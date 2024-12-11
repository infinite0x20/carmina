"""
This module contains the function(s) for metrical analysis
"""

# TODO @Suh Young - imports and globals


import re
def is_diphthong(pair):
    """Check if a pair of characters is a diphthong."""
    diphthongs = {"ae", "au", "oe", "ei", "eu", "ui", "oi", "ou"}
    return pair in diphthongs

    """Check if a pair of characters is a diphthong."""
    diphthongs = {"ae", "au", "ei", "eu", "oe", "ui"}
    return pair in diphthongs

def syllabify_latin(text):
    """Syllabify a line of Latin text."""
    # Normalize text (remove non-letters and convert to lowercase)
    text = re.sub(r'[^a-zA-Z]', '', text.lower())

    syllables = []
    i = 0

    while i < len(text):
        # Handle diphthongs
        if i < len(text) - 1 and is_diphthong(text[i:i+2]):
            syllables.append(text[i:i+2])
            i += 2
        # Handle vowels (and mark syllable boundaries)
        elif text[i] in "aeiouy":
            syllables.append(text[i])
            i += 1
        # Handle consonants
        else:
            start = i
            while i < len(text) and text[i] not in "aeiouy":
                i += 1
            consonant_cluster = text[start:i]
            # Distribute consonants based on rules
            if i < len(text):
                if len(consonant_cluster) > 1 and consonant_cluster[:2] in {"pr", "tr", "pl", "cl", "fl", "bl", "gl", "cr", "br", "dr", "qu"}:
                    syllables[-1] += consonant_cluster[0]
                    syllables.append(consonant_cluster[1:])
                else:
                    split_index = -1 if len(consonant_cluster) > 1 else 0
                    syllables[-1] += consonant_cluster[:split_index]
                    syllables.append(consonant_cluster[split_index:])
            else:
                syllables[-1] += consonant_cluster

    # Ensure proper merging of syllables (avoid over-splitting)
    final_syllables = []
    for j, syl in enumerate(syllables):
        if j > 0 and syl in "aeiouy" and final_syllables[-1][-1] not in "aeiouy":
            final_syllables[-1] += syl
        else:
            final_syllables.append(syl)

    return "-".join(final_syllables)

# Example usage
line = "Arma virumque cano Troiae qui primus ab oris"
syllabified = syllabify_latin(line)
print(syllabified)



def is_long(syllable):
    """Determine if a syllable is long."""
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxyz"

    # Check if it contains a diphthong (long by nature)
    if len(syllable) > 1 and is_diphthong(syllable[:2]):
        return True

    # Check if it ends with a long vowel
    if syllable[-1] in vowels and len(syllable) == 1:
        return False  # Assume short unless we know the vowel is long

    # Check for long by position (vowel followed by multiple consonants)
    for i in range(len(syllable)):
        if syllable[i] in vowels:
            remainder = syllable[i + 1:]
            if len(remainder) > 1 and all(c in consonants for c in remainder):
                return True

    return False

# Example usage
syllables = syllabified.split("-")
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