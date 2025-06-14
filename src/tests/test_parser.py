"""
Tests the functions in parser.py
"""
import os
from carmina.examples import EXAMPLE_PATH
from carmina import parser

expected_single_mixed = ["arma virumque cano troiae qui primus ab oris"]
expected_multiline = ["arma virumque cano troiae qui primus ab oris",
                      "italiam fato profugus laviniaque venit",
                      "litora multum ille et terris iactatus et alto",
                      "vi superum saevae memorem iunonis ob iram",
                      "multa quoque et bello passus dum conderet urbem",
                      "inferretque deos latio genus unde latinum",
                      "albanique patres atque altae moenia romae"]
expected_mixed_elision = ["litora multum ille et terris iactatus et alto"]
expected_single_m_elision = ["venturum excidio libyae sic volvere parcas"]
expected_single_vowel_elision = ["turbine corripuit scopuloque infixit acuto"]

def test_parse_txt():
    # mixed_elision
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_mixed_elision.txt")
    result = parser.parse_txt(path_file) 
    assert result == expected_mixed_elision

    # multiline
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_multiline.txt")
    result = parser.parse_txt(path_file) 
    assert result == expected_multiline

    # single_m_elision
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_single_m_elision.txt")
    result = parser.parse_txt(path_file) 
    assert result == expected_single_m_elision

    # single_mixed
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_single_mixed.txt")
    result = parser.parse_txt(path_file) 
    assert result == expected_single_mixed

    # single_vowel_elision
    path_file = os.path.join(EXAMPLE_PATH, "aeneid_single_vowel_elision.txt")
    result = parser.parse_txt(path_file) 
    assert result == expected_single_vowel_elision

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
