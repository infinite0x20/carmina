"""
Tests the functions in parser.py
"""
import os
from carmina.examples import EXAMPLE_PATH
from carmina import parser

# TODO: @Hui-Hsuan @Simon Write functions for parse_txt and parse_xml.
# TODO: Create expected outputs @Hui-Hsuan
# TODO: Write and document test_parse_txt @Simon
# TODO: Write and document test_parse_xml @Hui-Hsuan

# TODO: Create expected output from .txt files.
# Outputs should be lists of strings, where each line is a separate string
#   and all words are normalized (i.e., lowercase without punctuation)
expected_single_mixed = ["arma virumque cano troiae qui primus ab oris"]
expected_multiline = ['arma virumque cano troiae qui primus ab oris',
 'italiam fato profugus laviniaque venit litora',
 'multum ille et terris iactatus et alto vi superum saevae memorem iunonis ob iram',
 'multa quoque et bello passus dum conderet urbem',
 'inferretque deos latio genus unde latinum',
 'albanique patres atque altae moenia romae']
expected_mixed_elision = ["litora multum ille et terris iactatus et alto"]
expected_single_m_elision = ["venturum excidio libyae sic volvere parcas"]
expected_single_vowel_elision = ["turbine corripuit scopuloque infixit acuto"]
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
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_mixed_elision.xml")
    result = parser.parse_xml(path_file) 
    assert result == expected_mixed_elision

    # multiline
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_multiline.xml")
    result = parser.parse_xml(path_file) 
    assert result == expected_multiline

    # single_m_elision
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_single_m_elision.xml")
    result = parser.parse_xml(path_file) 
    assert result == expected_single_m_elision

    # single_mixed
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_single_mixed.xml")
    result = parser.parse_xml(path_file) 
    assert result == expected_single_mixed

    # single_vowel_elision
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_single_vowel_elision.xml")
    result = parser.parse_xml(path_file) 
    assert result == expected_single_vowel_elision
