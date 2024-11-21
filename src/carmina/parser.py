"""
This is the module where we'll write the file parser
"""

# necessary imports?

def parse_txt(file_path):
    """
    This function takes in a .txt file and returns a... object?
    Usable string and/or data structure that we can do the later
    analysis on
    """
    # TODO: @Suh Young
    # Adding a fun comment for funsies
    # normalize everything anyway
    with open(file_path) as f:
        lines = f.readlines()
        # normalized_lines = [normalize_line(line) for line in lines]
        return lines

def parse_xml(file_path):
    """
    Same thing as parse_txt, but it takes in an .xml and returns
    the data in the same format as the result of parse_txt
    """
    # TODO: @Suh Young
    
#     with open(file_path) as f:
#       lines = f.readlines()
#       actual_lines = [line for line in lines if line.startswith("<l>")]
#       print(actual_lines)
#       more cleanup here
        # remove <l> and </l> tags, remove \n

    pass

def _normalize_line(line):
    """
    Helper function for parse_text and parse_xml
    Takes in a line and removes the <l>, </l>, and \n characters

    Question: Do we want to lowercase + remove punctuation?

    For now: implement removal of tags and \n characters. Don't worry
    about lowercasing or removing punctuation
    """
    # TODO: @Liz
    pass
