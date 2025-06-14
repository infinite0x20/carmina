"""
This module allows users to search for alliteration
within one line of poetry. 
"""
        
def proximity_score(list, a, b):
    '''
    a and b are two strings that both occur in list. This function
    returns the absolute difference in indices between these two strings.
    '''
    sublist = list[list.index(a):]
    score = sublist.index(b)
    return score

def check_proximity_allit(score, proximity=4):
    '''
    Intended to be used in conjunction with proximity_score. Returns 
    true if the score less than or equal to the proximity, meaning
    that the two words are close enough to be considered part of
    the same alliteration. Defaults to proximity=4.
    '''
    return score <= proximity

def find_letters(line):
    '''
    Given a line of poetry, returns
    two dictionaries. letter_counts has the number of words beginning
    with each letter, while word_tracker has the actual words.
    '''
    letter_counts = {}
    word_tracker = {}

    # get all the words that start with the same letter
    for word in line:
        word = word.lower()
        if word[0] in letter_counts.keys():
            letter_counts[word[0]] += 1
            word_tracker[word[0]].append(word)
        else:
            letter_counts[word[0]] = 1
            word_tracker[word[0]] = [word]

    return letter_counts, word_tracker

def find_allit(line, letter_counts, word_tracker, proximity=4):
    '''
    Uses the proximity counter to search for proper alliterations.
    We define a "proper" alliteration in this case to be one in which
    no two consecutive words are greater than the given proximity
    distance from each other
    '''
    pairs = len(line) - 1
    allit_pairs = 0

    for letter in letter_counts.keys():
        if letter_counts[letter] >= 2:
            count = letter_counts[letter]
            words = word_tracker[letter]
            for i in range(0, count - 1, 1):
                subset = line[i:]
                score = proximity_score(subset, words[i], words[i+1])

                if score <= proximity:
                    allit_pairs += 1

    return allit_pairs, pairs
