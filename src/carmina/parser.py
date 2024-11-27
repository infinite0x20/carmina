"""
The module for reading in .txt and .xml files and normalizing
their text.
"""

import re

def parse_txt(file_path):
    """
    This function takes in a .txt file and returns list of strings
    that can be used later in the scansion functions.

    Inputs:
        file_path: str

    Outputs:
        normalized_lines: list[str]
    """
    with open(file_path) as f:
        lines = f.readlines()
        normalized_lines = [_normalize_line(line) for line in lines]
        return normalized_lines

def parse_xml(file_path):
    """
    This function takes in a .txt file and returns list of strings
    that can be used later in the scansion functions.

    Inputs:
        file_path: str

    Outputs:
        normalized_lines: list[str]
    """
    with open(file_path) as f:
        lines = f.readlines()
        normalized_lines = [_normalize_line(line) for line in lines if line.startswith("<l>")]
        return normalized_lines


def _normalize_line(line):
    """
    Helper function for parse_text and parse_xml
    Takes in a line and removes the <l>, </l>, and \n characters

    Question: Do we want to lowercase + remove punctuation?
    Answer: YES

    For now: implement removal of tags and \n characters. Don't worry
    about lowercasing or removing punctuation
    """
    # TODO: @Liz
    # re.sub(r'[^\w\s]', '', word.lower()) # if we want to lowercase + remove punct
    pass
