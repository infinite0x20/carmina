"""
Tests the functions in parser.py
"""

# TODO: @Hui-Hsuan @Simon Write functions for parse_txt and parse_xml.
# TODO: Create expected outputs @Hui-Hsuan
# TODO: Write and document test_parse_txt @Simon
# TODO: Write and document test_parse_xml @Hui-Hsuan

# TODO: Create expected output from .txt files.
# Outputs should be lists of strings, where each line is a separate string
#   and all words are normalized (i.e., lowercase without punctuation)
expected_single_mixed = ["Arma virumque cano, Troiae qui primus ab oris"]
expected_multiline = ['Arma virumque cano, Troiae qui primus ab oris', 'Italiam, fato profugus, Laviniaque venit', 'litora, multum ille et terris iactatus et alto', 'vi superum saevae memorem Iunonis ob iram;', 'multa quoque et bello passus, dum conderet urbem,\n', 'inferretque deos Latio, genus unde Latinum,', 'Albanique patres, atque altae moenia Romae.']

# pseudo-test:
# test_parse_txt <- result of this should be == expected
# test_parse_xml <- result of this should be == expected

def test_parse_txt():
    # mixed_elision

    # multiline

    # single_m_elision

    # single_mixed

    # single_vowel_elision

    pass

def test_parse_xml():
    # mixed_elision

    # multiline

    # single_m_elision

    # single_mixed

    # single_vowel_elision
    
    pass