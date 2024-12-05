"""
Tests the functions in parser.py
"""

from carmina.parser import parse_xml, parse_txt

expected_single_mixed = ["arma virumque cano troiae qui primus ab oris"]
expected_multiline = ["arma virumque cano troiae qui primus ab oris",
                      "italiam fato profugus laviniaque venit litora",
                      "multum ille et terris iactatus et alto",
                      "vi superum saevae memorem iunonis ob iram",
                      "multa quoque et bello passus dum conderet urbem",
                      "inferretque deos latio genus unde latinum",
                      "albanique patres atque altae moenia romae"]
expected_mixed_elision = ["litora multum ille et terris iactatus et alto"]
expected_single_m_elision = ["venturum excidio libyae sic volvere parcas"]
expected_single_vowel_elision = ["turbine corripuit scopuloque infixit acuto"]


def test_parse_txt():
    """
    Tests the parse_txt() function from parser

    Inputs:
        none

    Outputs:
        none
    """
    # mixed_elision
    path_file = "CARMINA/examples/aeneid_mixed_elision.xml"
    result = parse_txt(path_file)
    assert result == expected_mixed_elision

    # multiline
    path_file = "CARMINA/examples/aeneid_multiline.xml"
    result = parse_txt(path_file)
    assert result == expected_multiline

    # single_m_elision
    path_file = "CARMINA/examples/aeneid_single_m_elision.xml"
    result = parse_txt(path_file)
    assert result == expected_single_m_elision

    # single_mixed
    path_file = "CARMINA/examples/aeneid_single_mixed.xml"
    result = parse_txt(path_file)
    assert result == expected_single_mixed

    # single_vowel_elision
    path_file = "CARMINA/examples/aeneid_single_vowel_elision.xml"
    result = parse_txt(path_file)
    assert result == expected_single_vowel_elision


def test_parse_xml():
    """
    Tests the parse_xml() function from parser

    Inputs:
        none

    Outputs:
        none
    """
    # mixed_elision
    path_file = "CARMINA/examples/aeneid_mixed_elision.xml"
    result = parse_xml(path_file)
    assert result == expected_mixed_elision

    # multiline
    path_file = "CARMINA/examples/aeneid_multiline.xml"
    result = parse_xml(path_file)
    assert result == expected_multiline

    # single_m_elision
    path_file = "CARMINA/examples/aeneid_single_m_elision.xml"
    result = parse_xml(path_file)
    assert result == expected_single_m_elision

    # single_mixed
    path_file = "CARMINA/examples/aeneid_single_mixed.xml"
    result = parse_xml(path_file)
    assert result == expected_single_mixed

    # single_vowel_elision
    path_file = "CARMINA/examples/aeneid_single_vowel_elision.xml"
    result = parse_xml(path_file)
    assert result == expected_single_vowel_elision
