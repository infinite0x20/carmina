"""
This module contains the function(s) for metrical analysis
"""

# imports?

# Vowels - FIGURE THIS OUT ABOUT THE LETTER I
VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvx"

# Arm av ir umqu e ca no
# Did that work

# Global variables for diphthongs here
DIPHTHONGS = ["ae", "ai", "oi"]

def _syllabify(line):
    """
    Breaks a single line down into syllables

    Initial ideas: Remove spaces in the line and then break up by vowels/diphthongs.

    Arma virumque cano -> armavirumquecano -> arm av ir umqu ec an o
    """
    pass

def _is_long(syllable):
    """
    Determines whether a single syllable is long or short.
    Returns true if long, false if not.

    Initial ideas: Takes in a single syllable like "arm" or "av".
    If there are multiple back-to-back consonants, return True.
    """
    pass

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
    "Arma virumque cano, Troiae qui primus ab oris"
    "arma virumque cano troiae qui primus ab oris" <-- or we could do this?
    [0, 3, 5, 8, 11, 13] <-- assuming these are the syllable indices,
                             assign the -uu-- characters at each next
                             index
    """
    pass

def hexameter_text(lines):
    """
    Multi-line hexameter parsing
    """
    pass