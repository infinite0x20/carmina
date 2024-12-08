"""
This module contains the function(s) for metrical analysis
"""

# TODO @Suh Young - imports and globals

# imports?

VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvx"
DIPHTHONGS = ["ae", "ai", "oi"]

def _is_vowel(letter):
    """Check if a letter is a vowel."""
    return letter in VOWELS

def _is_consonant(letter):
    """Check if a letter is a consonant."""
    return letter in CONSONANTS

def _syllabify_backward(line):
    """
    Breaks a single line down into syllables by checking the line backward,
    but returns the syllables in the original order.
    
    Parameters:
        line (str): A line of text to syllabify.
    
    Returns:
        list: A list of syllables from the input line in the original order.
    """
    # Remove spaces and make lowercase
    line = line.replace(" ", "").lower()
    
    syllables = []
    current = ""
    
    # Traverse the line backward
    i = len(line) - 1
    while i >= 0:
        char = line[i]
        
        if _is_vowel(char):  # If the character is a vowel
            # Check if the next two characters are consonants
            if i - 2 >= 0 and _is_consonant(line[i - 1]) and _is_consonant(line[i - 2]):
                current = char  # Put the vowel into current buffer to wait for the next vowel
            else:
                # If no two consonants follow, process the vowel normally
                if current:  # If there are accumulated consonants, add them to the syllable
                    current = char + current  # Add the vowel to the current consonant buffer
                    syllables.insert(0, current)  # Insert the consonant-vowel pair to syllables
                    current = ""  # Reset the consonant buffer
                else:
                    syllables.insert(0, char)  # Just add the vowel itself
        
        elif _is_consonant(char):  # If the character is a consonant
            current = char + current  # Accumulate the consonant
        
        i -= 1  # Move to the previous character


    # Add any remaining consonants as the final syllable
    if current:
        syllables.insert(0, current)

    # Return syllables in the original order
    return syllables

# Example usage:
line = "Arma virumque cano" 
syllables = _syllabify_backward(line)
print(syllables)  # Expected Output: ['arm', 'av', 'ir', 'umqu', 'ec', 'an', 'o'] 

# check if start from the back
# check how to deal with the diphthongs
# check how to deal with the last two syllables 

def _is_long(item):
    """
    Determines whether a single item in the list has a length greater than or equal to 3.
    Returns True if the item's length >= 3, else False.
    """
    return len(str(item)) >= 3  # Convert item to string and check length

# Example usage:
print([_is_long(syllable) for syllable in syllables])  # Output: [True, False, False, True, False, False, False]


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